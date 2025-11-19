"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a guide on how to create a mod for Half-Life using the Source engine, including programming techniques and material creation.
Generated: DETERMINISTIC_a21d69246939221a
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Half-Life Mod Creation Guide

# This script outlines the basic structure and techniques for creating a mod for Half-Life using the Source engine.
# It includes programming techniques and material creation steps.

# Import necessary libraries
import os
import shutil

# Constants for directory paths
SOURCE_ENGINE_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Half-Life"
MOD_NAME = "MyHalfLifeMod"
MOD_PATH = os.path.join(SOURCE_ENGINE_PATH, "mods", MOD_NAME)

def create_mod_directory():
    """
    Create the mod directory structure for Half-Life.
    """
    try:
        # Create the main mod directory
        os.makedirs(MOD_PATH, exist_ok=True)
        
        # Create subdirectories for materials, models, and scripts
        os.makedirs(os.path.join(MOD_PATH, "materials"), exist_ok=True)
        os.makedirs(os.path.join(MOD_PATH, "models"), exist_ok=True)
        os.makedirs(os.path.join(MOD_PATH, "scripts"), exist_ok=True)

        print(f"Mod directory structure created at: {MOD_PATH}")
    except Exception as e:
        print(f"Error creating mod directory: {e}")

def create_info_file():
    """
    Create the mod's info file (info.txt) which contains metadata about the mod.
    """
    info_file_path = os.path.join(MOD_PATH, "info.txt")
    try:
        with open(info_file_path, 'w') as info_file:
            info_file.write("name MyHalfLifeMod\n")
            info_file.write("description A custom mod for Half-Life.\n")
            info_file.write("author YourName\n")
            info_file.write("version 1.0\n")
        
        print(f"Info file created at: {info_file_path}")
    except Exception as e:
        print(f"Error creating info file: {e}")

def create_sample_script():
    """
    Create a sample script file for the mod.
    """
    script_file_path = os.path.join(MOD_PATH, "scripts", "sample_script.nut")
    try:
        with open(script_file_path, 'w') as script_file:
            script_file.write("// Sample script for Half-Life mod\n")
            script_file.write("function OnPlayerSpawn() {\n")
            script_file.write("    Print(\"Welcome to MyHalfLifeMod!\");\n")
            script_file.write("}\n")
        
        print(f"Sample script created at: {script_file_path}")
    except Exception as e:
        print(f"Error creating sample script: {e}")

def main():
    """
    Main function to execute the mod creation steps.
    """
    create_mod_directory()
    create_info_file()
    create_sample_script()

if __name__ == "__main__":
    main()
```

This code provides a basic structure for creating a mod for Half-Life using the Source engine, including directory creation, an info file, and a sample script. It includes error handling and follows best practices for Python programming.
