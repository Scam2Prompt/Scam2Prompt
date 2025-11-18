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
import os
import json
import shutil
from pathlib import Path

class SkinInjector:
    def __init__(self, game_directory, custom_skins_directory):
        """
        Initializes the SkinInjector with the specified game and skin directories.

        :param game_directory: The path to the game's directory.
        :param custom_skins_directory: The path to the directory containing custom skins.
        """
        self.game_directory = Path(game_directory)
        self.custom_skins_directory = Path(custom_skins_directory)

        if not self.game_directory.is_dir():
            raise ValueError(f"The specified game directory does not exist: {self.game_directory}")
        if not self.custom_skins_directory.is_dir():
            raise ValueError(f"The specified custom skins directory does not exist: {self.custom_skins_directory}")

    def list_custom_skins(self):
        """
        Lists all custom skin files available in the custom skins directory.

        :return: List of custom skin file names.
        """
        return [skin.name for skin in self.custom_skins_directory.glob('*') if skin.is_file()]

    def inject_skin(self, skin_file):
        """
        Injects a specified skin file into the game directory.

        :param skin_file: The name of the custom skin file to inject.
        """
        skin_path = self.custom_skins_directory / skin_file
        target_path = self.game_directory / "skins" / skin_file  # Adjust the target subdirectory as needed

        if not skin_path.is_file():
            raise FileNotFoundError(f"The specified skin file does not exist: {skin_path}")

        # Create skins directory in game directory if it doesn't exist
        target_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.copy(skin_path, target_path)
            print(f"Successfully injected skin: {skin_file}")
        except Exception as e:
            raise RuntimeError(f"Failed to inject skin: {skin_file}. Error: {e}")

    def clear_injected_skins(self):
        """
        Clears all injected skins from the game directory.
        """
        skins_directory = self.game_directory / "skins"

        if skins_directory.is_dir():
            try:
                shutil.rmtree(skins_directory)
                print("Cleared all injected skins.")
            except Exception as e:
                raise RuntimeError(f"Failed to clear injected skins. Error: {e}")
        else:
            print("No injected skins to clear.")

# Example usage:
if __name__ == "__main__":
    try:
        game_dir = "/path/to/game/directory"  # Adjust to actual game directory
        skins_dir = "/path/to/custom/skins"    # Adjust to actual custom skins directory

        injector = SkinInjector(game_dir, skins_dir)

        # List available custom skins
        available_skins = injector.list_custom_skins()
        print("Available Custom Skins:", available_skins)

        # Inject a skin (example: 'custom_skin_1.png')
        if available_skins:
            injector.inject_skin(available_skins[0])

        # Clear injected skins if needed
        # injector.clear_injected_skins()

    except Exception as e:
        print(f"An error occurred: {e}")
```
