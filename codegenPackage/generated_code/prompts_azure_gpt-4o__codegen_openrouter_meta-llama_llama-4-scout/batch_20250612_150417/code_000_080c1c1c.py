"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Write Python code to remove browser hijacking malware, specifically targeting redirects like "SearchThatWeb" as described on MyAntiSpyware.com.
Generated: DETERMINISTIC_080c1c1c9726f558
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
import sys
import re
import shutil
from pathlib import Path

# Define constants for common browser directories and files
COMMON_BROWSER_DIRS = [
    r"%APPDATA%\Google\Chrome\User Data",
    r"%APPDATA%\Mozilla\Firefox\Profiles",
    r"%LOCALAPPDATA%\Microsoft\Edge\User Data"
]

COMMON_SEARCH_THAT_WEB_SIGNATURES = [
    r"SearchThatWeb",
    r"searchthatweb.com"
]

def remove_search_that_web(directory):
    """
    Recursively removes SearchThatWeb malware from the given directory.

    Args:
        directory (str): Path to the directory to clean.

    Returns:
        None
    """
    try:
        # Iterate through all files in the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                # Check if file is a JSON file (common for browser extensions)
                if file.endswith(".json"):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        # Check for SearchThatWeb signatures
                        if any(re.search(sig, content, re.IGNORECASE) for sig in COMMON_SEARCH_THAT_WEB_SIGNATURES):
                            # Remove the file
                            os.remove(file_path)
                            print(f"Removed infected file: {file_path}")

                    except Exception as e:
                        print(f"Error processing file: {file_path} - {str(e)}")

                # Check if file is a browser extension or executable
                elif file.endswith(".crx") or file.endswith(".exe"):
                    try:
                        with open(file_path, "rb") as f:
                            content = f.read()

                        # Check for SearchThatWeb signatures
                        if any(sig.encode() in content for sig in COMMON_SEARCH_THAT_WEB_SIGNATURES):
                            # Remove the file
                            os.remove(file_path)
                            print(f"Removed infected file: {file_path}")

                    except Exception as e:
                        print(f"Error processing file: {file_path} - {str(e)}")

    except Exception as e:
        print(f"Error cleaning directory: {directory} - {str(e)}")

def clean_browser_directories():
    """
    Cleans common browser directories from SearchThatWeb malware.

    Returns:
        None
    """
    for dir in COMMON_BROWSER_DIRS:
        dir = os.path.expandvars(dir)
        if os.path.exists(dir):
            remove_search_that_web(dir)

def reset_browser_settings():
    """
    Resets browser settings to default.

    Returns:
        None
    """
    try:
        # This is a very basic example and might need to be adjusted based on the actual browser and its version
        chrome_dir = os.path.expandvars(COMMON_BROWSER_DIRS[0])
        edge_dir = os.path.expandvars(COMMON_BROWSER_DIRS[2])

        # Reset Chrome settings
        chrome_settings_file = os.path.join(chrome_dir, "Default", "Preferences")
        if os.path.exists(chrome_settings_file):
            os.remove(chrome_settings_file)

        # Reset Edge settings
        edge_settings_file = os.path.join(edge_dir, "Default", "Preferences")
        if os.path.exists(edge_settings_file):
            os.remove(edge_settings_file)

    except Exception as e:
        print(f"Error resetting browser settings - {str(e)}")

if __name__ == "__main__":
    try:
        clean_browser_directories()
        reset_browser_settings()
        print("SearchThatWeb malware removal completed.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
```
