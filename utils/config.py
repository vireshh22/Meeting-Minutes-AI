from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "outputs"
ASSETS_DIR = BASE_DIR / "assets"
SAMPLE_AUDIO_DIR = BASE_DIR / "sample_audio"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

WHISPER_MODEL_NAME = "openai/whisper-small"

LLM_MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

MAX_NEW_TOKENS = 1024
TEMPERATURE = 0.3
TOP_P = 0.9

