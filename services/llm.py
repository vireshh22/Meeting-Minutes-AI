import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
)

from utils.config import (
    LLM_MODEL_NAME,
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P,
)

from prompts.prompts import MEETING_MINUTES_SYSTEM_PROMPT

tokenizer = None
model = None

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)


def load_llm():

    global tokenizer, model

    if tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
        
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

    if model is None:
        model = AutoModelForCausalLM.from_pretrained(
            LLM_MODEL_NAME, device_map="auto", quantization_config=bnb_config
        )

        model.eval()

    return tokenizer, model


def generate_meeting_minutes(transcript: str, language: str, output_style: str) -> str:

    tokenizer, model = load_llm()

    messages = [
        {
            "role": "system",
            "content": MEETING_MINUTES_SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": f"""
Generate meeting minutes using the following requirements.

Language:
{language}

Output Style:
{output_style}

Style Instructions:

- Professional:
Write formal corporate meeting minutes.

- Executive Summary:
Focus on high-level decisions and business outcomes.

- Bullet Points:
Keep everything short and use bullet points.

- Agile Sprint Notes:
Format the output like Scrum meeting notes including blockers, sprint progress, and next sprint tasks.

Meeting Transcript:

{transcript}
""",
        },
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
        add_generation_prompt=True,
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1] :]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    )

    return response
