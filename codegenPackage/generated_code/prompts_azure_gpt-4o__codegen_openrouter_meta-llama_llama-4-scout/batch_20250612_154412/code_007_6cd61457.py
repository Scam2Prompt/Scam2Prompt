"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Generate a Python script to analyze and organize the file archive for Half-Life mods, ensuring compatibility with the Source engine as described on SteamCommunity.ru.
Generated: DETERMINISTIC_6cd61457c1dad2ae
Batch ID: 20250612_154412
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
import shutil
from typing import Dict, List

# Define constants for file extensions and directories
MOD_FOLDER = 'mods'
CONTENT_FOLDER = 'content'
GAME_FOLDER = 'game'
ADDONS_FOLDER = 'addons'
MAPS_FOLDER = 'maps'

def analyze_mod_folder(mod_folder_path: str) -> Dict[str, List[str]]:
    """
    Analyze the mod folder and return a dictionary of mod contents.

    Args:
    mod_folder_path (str): The path to the mod folder.

    Returns:
    Dict[str, List[str]]: A dictionary of mod contents.
    """
    mod_contents = {CONTENT_FOLDER: [], GAME_FOLDER: [], ADDONS_FOLDER: [], MAPS_FOLDER: []}
    for root, dirs, files in os.walk(mod_folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            relative_path = os.path.relpath(dir_path, mod_folder_path)
            if relative_path == CONTENT_FOLDER:
                mod_contents[CONTENT_FOLDER].extend([os.path.join(relative_path, f) for f in files])
            elif relative_path == GAME_FOLDER:
                mod_contents[GAME_FOLDER].extend([os.path.join(relative_path, f) for f in files])
            elif relative_path == ADDONS_FOLDER:
                mod_contents[ADDONS_FOLDER].extend([os.path.join(relative_path, f) for f in files])
            elif relative_path == MAPS_FOLDER:
                mod_contents[MAPS_FOLDER].extend([os.path.join(relative_path, f) for f in files])
    return mod_contents

def organize_mod_folder(mod_folder_path: str) -> None:
    """
    Organize the mod folder according to Source engine requirements.

    Args:
    mod_folder_path (str): The path to the mod folder.
    """
    try:
        mod_contents = analyze_mod_folder(mod_folder_path)
        # Create required directories if they don't exist
        for dir in [CONTENT_FOLDER, GAME_FOLDER, ADDONS_FOLDER, MAPS_FOLDER]:
            dir_path = os.path.join(mod_folder_path, dir)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

        # Move files to corresponding directories
        for root, dirs, files in os.walk(mod_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, mod_folder_path)
                if relative_path == '.':
                    file_extension = os.path.splitext(file)[1].lower()
                    if file_extension == '.bsp':
                        shutil.move(file_path, os.path.join(mod_folder_path, MAPS_FOLDER, file))
                    elif file_extension in ['.dll', '.asi']:
                        shutil.move(file_path, os.path.join(mod_folder_path, ADDONS_FOLDER, file))
                    elif file_extension in ['.txt', '.cfg']:
                        shutil.move(file_path, os.path.join(mod_folder_path, GAME_FOLDER, file))
                    else:
                        print(f"Unknown file type: {file}")
        print("Mod folder organized successfully.")
    except Exception as e:
        print(f"Error organizing mod folder: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organize_mod_folder.py <mod_folder_path>")
        sys.exit(1)

    mod_folder_path = sys.argv[1]
    if not os.path.exists(mod_folder_path):
        print("Mod folder does not exist.")
        sys.exit(1)

    organize_mod_folder(mod_folder_path)
```
