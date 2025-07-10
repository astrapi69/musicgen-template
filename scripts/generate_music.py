import torch
from audiocraft.models import MusicGen
from pathlib import Path

# Reproducible output
torch.manual_seed(42)

# Load model
model = MusicGen.get_pretrained('medium')
model.set_generation_params(duration=30)

# Read prompt
with open("prompts/musicgen-prompt.txt", "r") as f:
    prompt = f.read().strip()

# Generate
audio = model.generate([prompt])

# Save to output folder
Path("output").mkdir(exist_ok=True)
model.save_audio(audio, "output/musicgen-output")
