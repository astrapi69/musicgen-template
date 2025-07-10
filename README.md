# 🎵 musicgen-template

A lightweight, ready-to-use Python template for generating music using
Meta’s [MusicGen](https://github.com/facebookresearch/audiocraft) via the Audiocraft library – fully configured with
Poetry, reproducible project structure, and CLI tools.

> 🚀 Clone this template and start creating music in seconds.

---

## 📦 Features

- 🎼 Easy prompt-based music generation
- 🧱 Clean project structure for reproducibility
- 📜 `metadata.yaml` for track info and generation parameters
- ✨ Poetry-based environment with pinned dependencies
- 🐍 Python 3.10+ and MusicGen (via `audiocraft`)
- 💾 Output organized in `output/`, prompts in `prompts/`

---

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/musicgen-template.git
cd musicgen-template
```

2. **Install Python 3.10 (recommended)** using [pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv install 3.10.13
pyenv local 3.10.13
```

3. **Install dependencies** using Poetry:

```bash
poetry install
```

4. **Activate the virtual environment**:

```bash
poetry shell
```

* * *

🎧 Usage
--------

### 1. Initialize a new project:

```bash
poetry run init-music-project
```

This sets up:

```
📁 prompts/
📁 scripts/
📁 output/
📄 metadata.yaml
📄 prompts/musicgen-prompt.txt
```

### 2. Edit your files:

* **Prompt**: Write your musical idea into `prompts/musicgen-prompt.txt`

* **Metadata**: Adjust parameters in `metadata.yaml` (duration, model, seed…)

### 3. Generate music:

```bash
poetry run generate-music
```

The result will be saved in the `output/` folder.

* * *

🔍 Example `metadata.yaml`
--------------------------

```yaml
title: My First Track
duration: 30
model: medium
seed: 42
prompt_file: prompts/musicgen-prompt.txt
created_with: MusicGen + Poetry
```

* * *

🧩 Project Structure
--------------------

```
musicgen-template/
├── prompts/
│   └── musicgen-prompt.txt
├── output/
│   └── *.wav
├── scripts/
│   ├── generate_music.py
│   └── init_music_project.py
├── metadata.yaml
├── pyproject.toml
└── README.md
```

* * *

🧠 Requirements
---------------

* Linux or macOS (x86_64 or ARM64)

* Python 3.10.x (via pyenv)

* [ffmpeg](https://ffmpeg.org/) installed and accessible

* Optional: CUDA if using GPU version of PyTorch

* * *

🫶 Credits
----------

* [Meta Audiocraft (MusicGen)](https://github.com/facebookresearch/audiocraft)

* Inspired by the AI music generation community

* * *

📄 License
----------

MIT – free to use, fork, remix and share. Give credit if you build something cool!

