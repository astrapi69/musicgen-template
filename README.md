# 🎵 musicgen-template

A ready-to-use template for generating AI music with Meta's MusicGen and Poetry.

## 🚀 Quick Start

1. Clone this template:
```bash
   gh repo create my-new-track --template=astrapi69/musicgen-template
```

2. Install dependencies:
    
 ```bash
 poetry install
 ```
    
3. Run the generation:
    
 ```bash
 poetry run python scripts/generate_music.py
 ```
    
4. Find your generated `.wav` file in the `output/` folder.
    

📁 Structure
------------

* `prompts/` – your text prompt for the music
    
* `scripts/` – Python scripts to run generation
    
* `output/` – generated `.wav` files
    
* `metadata.yaml` – optional metadata (title, seed, model, etc.)
    

✅ Features
----------

* Reproducible via `torch.manual_seed`
    
* Based on open-source [audiocraft/MusicGen](https://github.com/facebookresearch/audiocraft)
    
* Fully offline
    

📜 License
----------

MIT – free to use and remix



---

### 6. 🪪 Lizenz

**`LICENSE`** (MIT empfohlen für maximale Offenheit)

---

### 7. 📤 Repo auf GitHub hochladen

```bash
git init
git add .
git commit -m "init: MusicGen template for reproducible AI music"
gh repo create astrapi69/musicgen-template --public --template --source=. --remote=origin
git push -u origin main
```

> Optional: Füge `template: true` im GitHub Repository Settings hinzu (wird automatisch gesetzt bei `--template` mit CLI)

* * *

🎁 Ergebnis
-----------

Du bekommst ein **perfektes GitHub-Template-Repository**, mit dem du oder andere mit einem Klick neue Projekte starten können:

* Kein Setup-Overhead
    
* Prompt einfach anpassen
    
* Musik generieren
    
* WAV-Datei verwenden, veröffentlichen, speichern
    

* * *