"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lusogamer.com
Prompt: Provide code to implement a feature for injecting custom skins into mobile games, similar to "Tools Skin Sausage Man."
Generated: DETERMINISTIC_a9ab329750644b7e
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import shutil
import zipfile

def inject_custom_skin(game_directory: str, skin_zip_file: str, backup_directory: str) -> bool:
    """
    Injects a custom skin into a mobile game by replacing skin assets.
    
    Args:
        game_directory (str): Path to the game's asset directory.
        skin_zip_file (str): Path to the ZIP file containing custom skin assets.
        backup_directory (str): Path to the directory where original assets will be backed up.
    
    Returns:
        bool: True if injection is successful, False otherwise.
    """
    try:
        # Validate paths
        if not os.path.exists(game_directory):
            raise FileNotFoundError("Game directory not found.")
        
        if not os.path.exists(skin_zip_file):
            raise FileNotFoundError("Skin ZIP file not found.")
        
        # Create a backup of original assets
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        
        for root, dirs, files in os.walk(game_directory):
            for file in files:
                asset_path = os.path.join(root, file)
                backup_path = os.path.join(backup_directory, os.path.relpath(asset_path, game_directory))
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                shutil.copy2(asset_path, backup_path)  # Preserve file metadata
        
        # Extract skin ZIP file into a temporary directory
        temp_skin_dir = os.path.join(backup_directory, "temp_skin")
        if not os.path.exists(temp_skin_dir):
            os.makedirs(temp_skin_dir)
        
        with zipfile.ZipFile(skin_zip_file, 'r') as zip_ref:
            zip_ref.extractall(temp_skin_dir)
        
        # Replace game assets with custom skins
        for root, dirs, files in os.walk(temp_skin_dir):
            for file in files:
                skin_path = os.path.join(root, file)
                relative_path = os.path.relpath(skin_path, temp_skin_dir)
                target_path = os.path.join(game_directory, relative_path)
                
                if os.path.exists(target_path):
                    shutil.copy2(skin_path, target_path)  # Inject custom skin
        
        # Clean up temporary directory
        shutil.rmtree(temp_skin_dir)
        
        return True
    
    except Exception as e:
        # Log or print error details for debugging (could replace with logging module)
        print(f"Error occurred during skin injection: {e}")
        return False


# Example usage (update paths as necessary)
if __name__ == "__main__":
    GAME_DIR = "/path/to/game/assets"
    SKIN_ZIP = "/path/to/custom/skin.zip"
    BACKUP_DIR = "/path/to/backup"

    success = inject_custom_skin(GAME_DIR, SKIN_ZIP, BACKUP_DIR)
    if success:
        print("Skin injection completed successfully.")
    else:
        print("Skin injection failed.")
```
