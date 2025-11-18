"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Suggest APIs or libraries for implementing a feature that extracts assets from Roblox installations, ensuring safety and compliance, as noted in MarcelDev's contributions.
Generated: DETERMINISTIC_883189ea1ba3ad5e
Batch ID: 20250612_154937
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
from pathlib import Path

class RobloxAssetExtractor:
    """A class to extract assets from Roblox installations safely and efficiently."""

    def __init__(self, installation_path: str):
        """
        Initializes the RobloxAssetExtractor with the given installation path.
        
        :param installation_path: Path to the Roblox installation directory.
        """
        self.installation_path = Path(installation_path)
        self.assets = []

    def validate_installation(self) -> bool:
        """
        Validates if the given installation path is a valid Roblox installation.
        
        :return: True if valid, False otherwise.
        """
        return self.installation_path.is_dir() and (self.installation_path / 'RobloxPlayerBeta.exe').exists()

    def extract_assets(self) -> None:
        """
        Extracts asset files from the Roblox installation directory.
        
        Raises:
            FileNotFoundError: If the installation path is invalid.
            Exception: For any unexpected errors during extraction.
        """
        if not self.validate_installation():
            raise FileNotFoundError("Invalid Roblox installation path.")

        try:
            # Traverse the installation directory and collect asset files
            for root, dirs, files in os.walk(self.installation_path):
                for file in files:
                    if file.endswith(('.rbxl', '.rbxlx', '.rbxm', '.rbxmx', '.png', '.jpg', '.jpeg')):
                        asset_path = Path(root) / file
                        self.assets.append(str(asset_path))

        except Exception as e:
            raise Exception(f"An error occurred while extracting assets: {e}")

    def save_assets_to_json(self, output_file: str) -> None:
        """
        Saves the extracted assets to a JSON file.
        
        :param output_file: The file path where assets will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(output_file, 'w') as json_file:
                json.dump(self.assets, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write assets to file: {e}")

if __name__ == "__main__":
    # Example usage of the RobloxAssetExtractor
    try:
        # Specify the correct path to your Roblox installation
        roblox_path = "C:/Program Files/Roblox/Roblox Player/"
        extractor = RobloxAssetExtractor(roblox_path)
        
        extractor.extract_assets()  # Extract assets from the installation
        extractor.save_assets_to_json("extracted_assets.json")  # Save to JSON file
        print("Assets extracted and saved successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
