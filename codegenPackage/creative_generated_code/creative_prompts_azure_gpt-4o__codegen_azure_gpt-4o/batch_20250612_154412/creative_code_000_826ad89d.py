"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.steamcommunity.ru
Prompt: Write a Python script to create a custom Half-Life 2 mod using the Source engine, incorporating specific textures and materials as described in the Source Inside section of the SteamCommunity.ru website.
Generated: DETERMINISTIC_826ad89d75a378fb
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

# --- Configuration Section ---

# Define paths for the Source SDK and mod directories
SOURCE_SDK_PATH = "C:/Program Files (x86)/Steam/steamapps/common/SourceSDK"
MOD_DIRECTORY = "C:/Program Files (x86)/Steam/steamapps/sourcemods/my_custom_mod"

# Define custom textures and materials to be included
CUSTOM_TEXTURES = [
    "custom_texture_1.vtf",
    "custom_texture_2.vtf",
]
CUSTOM_MATERIALS = [
    "custom_material_1.vmt",
    "custom_material_2.vmt",
]

# Paths for custom files (assumes files are stored in a local directory)
LOCAL_TEXTURES_PATH = "./textures"
LOCAL_MATERIALS_PATH = "./materials"

# --- Utility Functions ---

def create_mod_directory(mod_dir):
    """
    Creates the base directory structure for the mod.
    """
    try:
        os.makedirs(mod_dir, exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "materials"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "maps"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "models"), exist_ok=True)
        print(f"Mod directory structure created at: {mod_dir}")
    except OSError as e:
        print(f"Error creating mod directory: {e}")
        raise

def copy_files(src_dir, dest_dir, files):
    """
    Copies specified files from the source directory to the destination.
    """
    try:
        for file_name in files:
            src_path = os.path.join(src_dir, file_name)
            dest_path = os.path.join(dest_dir, file_name)
            if os.path.exists(src_path):
                shutil.copy(src_path, dest_path)
                print(f"Copied {file_name} to {dest_path}")
            else:
                print(f"File not found: {src_path}")
    except Exception as e:
        print(f"Error copying files: {e}")
        raise

def create_mod_manifest(mod_dir):
    """
    Creates a basic `gameinfo.txt` file required by Source engine mods.
    """
    manifest_path = os.path.join(mod_dir, "gameinfo.txt")
    gameinfo_content = """\
"GameInfo"
{
    game "Custom Half-Life 2 Mod"
    title "Custom Half-Life 2 Mod"
    type "singleplayer_only"
    FileSystem
    {
        SteamAppId 220
        ToolsAppId 211
        SearchPaths
        {
            Game |gameinfo_path|.
            Game hl2
        }
    }
}
"""
    try:
        with open(manifest_path, "w") as manifest_file:
            manifest_file.write(gameinfo_content)
        print(f"Created gameinfo.txt at: {manifest_path}")
    except IOError as e:
        print(f"Error writing gameinfo.txt: {e}")
        raise

# --- Main Script ---

def main():
    print("Starting custom Half-Life 2 mod creation...")

    # Step 1: Create mod directory structure
    create_mod_directory(MOD_DIRECTORY)

    # Step 2: Copy custom textures and materials
    print("Copying custom textures...")
    copy_files(LOCAL_TEXTURES_PATH, os.path.join(MOD_DIRECTORY, "materials"), CUSTOM_TEXTURES)

    print("Copying custom materials...")
    copy_files(LOCAL_MATERIALS_PATH, os.path.join(MOD_DIRECTORY, "materials"), CUSTOM_MATERIALS)

    # Step 3: Create mod manifest file
    print("Creating mod manifest...")
    create_mod_manifest(MOD_DIRECTORY)

    print("Mod creation completed successfully!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred during mod creation: {e}")
```
