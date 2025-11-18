"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Generate a Python script to analyze and organize the file archive for Half-Life mods, ensuring compatibility with the Source engine as described on SteamCommunity.ru.
Generated: DETERMINISTIC_6cd61457c1dad2ae
Batch ID: 20250612_154412
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("mod_organizer.log"),
        logging.StreamHandler()
    ]
)

# Define constants
SOURCE_ENGINE_DIRECTORIES = ["maps", "materials", "models", "sound", "scripts"]
MOD_ARCHIVE_PATH = "path/to/your/mods_archive"  # Replace with the actual path to your mod archive
ORGANIZED_MODS_PATH = "path/to/organized_mods"  # Replace with the actual path to the output directory

# Ensure output directory exists
os.makedirs(ORGANIZED_MODS_PATH, exist_ok=True)

def is_source_engine_compatible(directory):
    """
    Check if the mod directory contains folders required for Source engine compatibility.
    :param directory: Path to the mod directory
    :return: True if compatible, False otherwise
    """
    for required_dir in SOURCE_ENGINE_DIRECTORIES:
        if not os.path.exists(os.path.join(directory, required_dir)):
            logging.warning(f"Missing required folder '{required_dir}' in {directory}")
            return False
    return True

def organize_mods(archive_path, output_path):
    """
    Organize Half-Life mods for Source engine compatibility.
    :param archive_path: Path to the mods archive directory
    :param output_path: Path to the organized mods directory
    """
    try:
        for mod_name in os.listdir(archive_path):
            mod_path = os.path.join(archive_path, mod_name)
            
            # Skip non-directory files
            if not os.path.isdir(mod_path):
                logging.info(f"Skipping non-directory: {mod_name}")
                continue

            logging.info(f"Analyzing mod: {mod_name}")

            # Check compatibility
            if is_source_engine_compatible(mod_path):
                destination_path = os.path.join(output_path, mod_name)
                
                # Move compatible mod to organized folder
                shutil.copytree(mod_path, destination_path)
                logging.info(f"Mod '{mod_name}' has been organized successfully.")
            else:
                logging.warning(f"Mod '{mod_name}' is not compatible with the Source engine.")
    except Exception as e:
        logging.error(f"An error occurred during organization: {e}", exc_info=True)

if __name__ == "__main__":
    logging.info("Starting mod archive analysis and organization...")
    organize_mods(MOD_ARCHIVE_PATH, ORGANIZED_MODS_PATH)
    logging.info("Mod archive organization completed.")
```
