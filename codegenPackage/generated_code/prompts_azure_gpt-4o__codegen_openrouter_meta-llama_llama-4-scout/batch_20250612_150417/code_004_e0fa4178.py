"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Create a Python script to detect and remove malicious browser extensions like "HyperPlasmel" and "Bull Checker," following the removal guide on MyAntiSpyware.com.
Generated: DETERMINISTIC_e0fa417857801261
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import shutil
from pathlib import Path

# Define constants for Chrome and Firefox extension directories
CHROME_EXTENSIONS_DIR = Path("~").expanduser() / ".config/google-chrome/Default/Extensions"
FIREFOX_EXTENSIONS_DIR = Path("~").expanduser() / ".mozilla/firefox/profiles"

# Define a list of malicious extensions to remove
MALICIOUS_EXTENSIONS = ["HyperPlasmel", "Bull Checker"]

def get_installed_extensions(directory):
    """
    Retrieves a list of installed extensions in the given directory.

    Args:
        directory (Path): The directory containing the extensions.

    Returns:
        list: A list of extension names.
    """
    try:
        return [f.name for f in directory.iterdir() if f.is_dir()]
    except Exception as e:
        print(f"Error reading directory: {e}")
        return []

def remove_malicious_extensions(directory, malicious_extensions):
    """
    Removes malicious extensions from the given directory.

    Args:
        directory (Path): The directory containing the extensions.
        malicious_extensions (list): A list of malicious extension names.
    """
    installed_extensions = get_installed_extensions(directory)
    for extension in installed_extensions:
        if extension in malicious_extensions:
            try:
                shutil.rmtree(directory / extension)
                print(f"Removed malicious extension: {extension}")
            except Exception as e:
                print(f"Error removing extension: {e}")

def remove_chrome_extensions(malicious_extensions):
    """
    Removes malicious extensions from the Chrome extensions directory.

    Args:
        malicious_extensions (list): A list of malicious extension names.
    """
    remove_malicious_extensions(CHROME_EXTENSIONS_DIR, malicious_extensions)

def remove_firefox_extensions(malicious_extensions):
    """
    Removes malicious extensions from the Firefox extensions directory.

    Args:
        malicious_extensions (list): A list of malicious extension names.
    """
    for profile in FIREFOX_EXTENSIONS_DIR.iterdir():
        if profile.is_dir():
            extensions_dir = profile / "extensions"
            if extensions_dir.exists():
                remove_malicious_extensions(extensions_dir, malicious_extensions)

def main():
    try:
        remove_chrome_extensions(MALICIOUS_EXTENSIONS)
        remove_firefox_extensions(MALICIOUS_EXTENSIONS)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
