"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Develop a script to convert markdown files into a GitBook site, leveraging the publishing tools mentioned in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_c38ad39c5e3cf3c8
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import shutil
from pathlib import Path

# Define constants for source and target directories
SOURCE_DIR = 'markdown_files'
TARGET_DIR = 'gitbook_site'
GITBOOK_TEMPLATE = 'polymarket-gitbook-template'

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        exit(1)

def create_gitbook_site():
    """Create a GitBook site structure from markdown files."""
    # Check if the source directory exists
    if not Path(SOURCE_DIR).exists():
        print(f"Source directory '{SOURCE_DIR}' does not exist.")
        exit(1)

    # Remove existing target directory if it exists
    if Path(TARGET_DIR).exists():
        shutil.rmtree(TARGET_DIR)

    # Create a new target directory
    os.makedirs(TARGET_DIR)

    # Copy GitBook template files to the target directory
    shutil.copytree(GITBOOK_TEMPLATE, TARGET_DIR, dirs_exist_ok=True)

    # Move markdown files to the target directory
    for md_file in Path(SOURCE_DIR).rglob('*.md'):
        target_path = Path(TARGET_DIR) / md_file.name
        shutil.copy(md_file, target_path)

    print(f"Markdown files have been copied to '{TARGET_DIR}'.")

def build_gitbook():
    """Build the GitBook site."""
    os.chdir(TARGET_DIR)

    # Install GitBook if not installed
    print("Checking for GitBook installation...")
    run_command(['npm', 'install', 'gitbook-cli', '-g'])

    # Build the GitBook site
    print("Building the GitBook site...")
    run_command(['gitbook', 'build'])

    print("GitBook site has been built successfully.")

def main():
    """Main function to execute the Markdown to GitBook conversion."""
    create_gitbook_site()
    build_gitbook()

if __name__ == '__main__':
    main()
```
