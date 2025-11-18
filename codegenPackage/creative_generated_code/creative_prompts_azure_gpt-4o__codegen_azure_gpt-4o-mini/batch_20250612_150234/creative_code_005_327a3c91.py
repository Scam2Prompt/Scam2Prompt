"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemebot.com
Prompt: Develop a script to manage and organize the online history of screenshots saved in Joxi's storage.
Generated: DETERMINISTIC_327a3c91aaa9182c
Batch ID: 20250612_150234
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
from datetime import datetime

class JoxiScreenshotManager:
    """Class to manage and organize Joxi screenshot storage."""

    def __init__(self, storage_path):
        """
        Initialize the screenshot manager with the storage path.

        Args:
            storage_path (str): Path to the Joxi screenshot storage.
        """
        self.storage_path = storage_path
        self.screenshots = []

    def load_screenshots(self):
        """Load screenshots from the storage path."""
        try:
            self.screenshots = [
                os.path.join(self.storage_path, f)
                for f in os.listdir(self.storage_path)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            ]
        except FileNotFoundError:
            print(f"Error: The path '{self.storage_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred while loading screenshots: {e}")

    def organize_by_date(self):
        """Organize screenshots into folders by their creation date."""
        for screenshot in self.screenshots:
            try:
                # Get the creation time and format it
                creation_time = os.path.getctime(screenshot)
                date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

                # Create a directory for the date if it doesn't exist
                date_dir = os.path.join(self.storage_path, date_folder)
                os.makedirs(date_dir, exist_ok=True)

                # Move the screenshot to the corresponding date directory
                shutil.move(screenshot, os.path.join(date_dir, os.path.basename(screenshot)))
            except Exception as e:
                print(f"Failed to process '{screenshot}': {e}")

    def save_screenshot_metadata(self, output_file):
        """
        Save metadata of screenshots to a JSON file.

        Args:
            output_file (str): File path where metadata will be saved.
        """
        metadata = []
        for screenshot in self.screenshots:
            try:
                creation_time = os.path.getctime(screenshot)
                metadata.append({
                    'filename': os.path.basename(screenshot),
                    'path': screenshot,
                    'creation_time': datetime.fromtimestamp(creation_time).isoformat()
                })
            except Exception as e:
                print(f"Failed to gather metadata for '{screenshot}': {e}")

        try:
            with open(output_file, 'w') as f:
                json.dump(metadata, f, indent=4)
        except Exception as e:
            print(f"Failed to save metadata to '{output_file}': {e}")

def main():
    # Example usage of JoxiScreenshotManager
    storage_path = '/path/to/joxi/screenshots'  # Update this to your actual Joxi storage path
    output_metadata_file = '/path/to/output/screenshots_metadata.json'  # Update this path

    manager = JoxiScreenshotManager(storage_path)
    manager.load_screenshots()
    manager.organize_by_date()
    manager.save_screenshot_metadata(output_metadata_file)

if __name__ == "__main__":
    main()
```
