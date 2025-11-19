"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Develop a script to convert markdown files into a GitBook site, leveraging the publishing tools mentioned in the Polymarket GitBook starter template.
Generated: DETERMINISTIC_c38ad39c5e3cf3c8
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
from pathlib import Path

# Define a function to convert markdown files into a GitBook site
def convert_markdown_to_gitbook(markdown_dir, gitbook_dir, gitbook_version='latest'):
    """
    Converts markdown files into a GitBook site.

    Args:
        markdown_dir (str): Directory containing markdown files.
        gitbook_dir (str): Directory to output GitBook site.
        gitbook_version (str, optional): GitBook version. Defaults to 'latest'.

    Raises:
        Exception: If GitBook installation is not found.
    """

    # Check if GitBook is installed
    try:
        subprocess.run(['gitbook', '--version'], check=True, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        print("GitBook is not installed. Please install it using 'npm install -g gitbook-cli'.")
        raise

    # Create GitBook directory if it doesn't exist
    Path(gitbook_dir).mkdir(parents=True, exist_ok=True)

    # Initialize GitBook site
    try:
        subprocess.run(['gitbook', 'init', gitbook_dir], check=True, cwd=gitbook_dir)
    except subprocess.CalledProcessError as e:
        print(f"Failed to initialize GitBook site: {e}")
        return

    # Copy markdown files to GitBook directory
    for file in Path(markdown_dir).glob('*.md'):
        file_path = Path(gitbook_dir) / file.name
        with open(file, 'r') as src, open(file_path, 'w') as dst:
            dst.write(src.read())

    # Build GitBook site
    try:
        subprocess.run(['gitbook', 'build', '.', f'--output=site/{gitbook_version}'], check=True, cwd=gitbook_dir)
    except subprocess.CalledProcessError as e:
        print(f"Failed to build GitBook site: {e}")
        return

    print("GitBook site generated successfully.")

# Define a function to serve the GitBook site
def serve_gitbook_site(gitbook_dir, port=4000):
    """
    Serves the GitBook site.

    Args:
        gitbook_dir (str): Directory containing GitBook site.
        port (int, optional): Port to serve the site on. Defaults to 4000.
    """

    try:
        subprocess.run(['gitbook', 'serve', '.', str(port)], check=True, cwd=gitbook_dir)
    except subprocess.CalledProcessError as e:
        print(f"Failed to serve GitBook site: {e}")

# Main function
if __name__ == "__main__":
    markdown_dir = 'markdown'
    gitbook_dir = 'gitbook'

    convert_markdown_to_gitbook(markdown_dir, gitbook_dir)
    serve_gitbook_site(gitbook_dir)
```

```bash
#!/bin/bash

# Install dependencies
npm install -g gitbook-cli

# Build and serve GitBook site
python convert_to_gitbook.py
```
