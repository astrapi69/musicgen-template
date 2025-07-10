"""
Initialize the directory structure and template files
for a new MusicGen-based project using this template.
"""

import os
from pathlib import Path


def create_directories(base_path: Path, directories: list[str]):
    """Create all required directories for the project."""
    for directory in directories:
        path = base_path / directory
        path.mkdir(parents=True, exist_ok=True)


def create_files(base_path: Path, files: list[str]):
    """Create all empty files that should exist."""
    for file in files:
        path = base_path / file
        path.touch(exist_ok=True)


def write_metadata_yaml(path: Path):
    """Write a basic metadata.yaml template with default values."""
    content = """title: Example Track
duration: 30
model: medium
seed: 42
prompt_file: prompts/musicgen-prompt.txt
created_with: MusicGen + Poetry
"""
    path.write_text(content, encoding="utf-8")


def write_prompt_file(path: Path):
    """Write a default text prompt to guide the user."""
    content = "Enter your music generation prompt here.\n"
    path.write_text(content, encoding="utf-8")


def main():
    """Main entry point for initializing the project."""
    project_root = Path(__file__).resolve().parent.parent
    os.chdir(project_root)

    print("🎼 Initializing MusicGen project template...\n")

    directories = ["prompts", "scripts", "output"]
    files = ["metadata.yaml", "prompts/musicgen-prompt.txt"]

    create_directories(project_root, directories)
    create_files(project_root, files)

    write_metadata_yaml(project_root / "metadata.yaml")
    write_prompt_file(project_root / "prompts/musicgen-prompt.txt")

    print("✅ Project initialized successfully.")
    print("📁 Created folders: prompts/, scripts/, output/")
    print("📄 Created and filled: metadata.yaml, prompts/musicgen-prompt.txt")
    print("🧠 Tip: Now edit your prompt and metadata to generate your first track!")


if __name__ == "__main__":
    main()
