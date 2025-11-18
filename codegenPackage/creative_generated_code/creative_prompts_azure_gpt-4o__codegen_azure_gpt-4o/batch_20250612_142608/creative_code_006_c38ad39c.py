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
import shutil
import subprocess
from pathlib import Path

def convert_markdown_to_gitbook(markdown_dir: str, output_dir: str):
    """
    Converts a directory of markdown files into a GitBook site.

    Args:
        markdown_dir (str): Path to the directory containing markdown files.
        output_dir (str): Path to the output directory for the GitBook site.

    Raises:
        FileNotFoundError: If the markdown directory does not exist.
        Exception: If GitBook installation or commands fail.
    """
    # Ensure markdown directory exists
    if not os.path.exists(markdown_dir):
        raise FileNotFoundError(f"Markdown directory '{markdown_dir}' does not exist.")

    # Ensure the output directory exists, create if it doesn't
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        # Check if GitBook CLI is installed
        subprocess.run(["gitbook", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        # GitBook CLI not installed
        raise Exception("GitBook CLI is not installed. Please install it globally using 'npm install -g gitbook-cli'.")

    try:
        # Initialize the GitBook structure in the output directory
        subprocess.run(["gitbook", "init", "."], cwd=output_dir, check=True)

        # Copy markdown files to the GitBook directory
        for file_name in os.listdir(markdown_dir):
            if file_name.endswith(".md"):
                shutil.copy(os.path.join(markdown_dir, file_name), output_dir)

        # Build the GitBook
        subprocess.run(["gitbook", "build"], cwd=output_dir, check=True)

    except subprocess.CalledProcessError as e:
        raise Exception(f"An error occurred while running GitBook commands: {str(e)}")

    print(f"GitBook site successfully generated at: {output_dir}")

if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert markdown files into a GitBook site.")
    parser.add_argument("markdown_dir", type=str, help="Path to the directory containing markdown files.")
    parser.add_argument("output_dir", type=str, help="Path to the output directory for the GitBook site.")
    args = parser.parse_args()

    try:
        convert_markdown_to_gitbook(args.markdown_dir, args.output_dir)
    except Exception as e:
        print(f"Error: {str(e)}")
```
