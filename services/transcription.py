import torch

from transformers import pipeline

from utils.config import WHISPER_MODEL_NAME

transcriber = None


def load_transcriber():
    global transcriber

    if transcriber is None:
        device = 0 if torch.cuda.is_available() else -1

        transcriber = pipeline(
            task="automatic-speech-recognition",
            model=WHISPER_MODEL_NAME,
            device=device,
        )

    return transcriber


def transcribe_audio(audio_path: str) -> str:
    transcriber = load_transcriber()

    result = transcriber(
        audio_path,
        return_timestamps=True,
        generate_kwargs={"task": "transcribe", "language": "english"},
    )

    return result["text"].strip()
