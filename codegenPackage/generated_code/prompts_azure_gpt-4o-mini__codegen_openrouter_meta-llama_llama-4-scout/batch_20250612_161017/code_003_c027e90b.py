"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: Create a script that organizes and filters images by location, such as "Golden Paradise" and "Island Dream," reflecting the unique features of the élán-life image galleries.
Generated: DETERMINISTIC_c027e90be0b51e08
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# image_organizer.py

import os
import shutil
from pathlib import Path
from typing import Dict, List

class ImageOrganizer:
    """
    Organizes and filters images by location.

    Attributes:
        image_dir (str): The directory containing the images.
        destination_dir (str): The directory where the organized images will be moved.
    """

    def __init__(self, image_dir: str, destination_dir: str):
        """
        Initializes the ImageOrganizer.

        Args:
            image_dir (str): The directory containing the images.
            destination_dir (str): The directory where the organized images will be moved.
        """
        self.image_dir = image_dir
        self.destination_dir = destination_dir

    def organize_images(self, location_features: Dict[str, List[str]]):
        """
        Organizes images by location.

        Args:
            location_features (Dict[str, List[str]]): A dictionary where the keys are location names and the values are lists of features.

        Returns:
            None
        """
        # Create the destination directory if it doesn't exist
        Path(self.destination_dir).mkdir(parents=True, exist_ok=True)

        # Iterate over each location and its features
        for location, features in location_features.items():
            # Create the location directory if it doesn't exist
            location_dir = os.path.join(self.destination_dir, location)
            Path(location_dir).mkdir(parents=True, exist_ok=True)

            # Iterate over each image in the image directory
            for filename in os.listdir(self.image_dir):
                # Check if the file is an image
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    # Iterate over each feature of the location
                    for feature in features:
                        # Check if the feature is in the filename
                        if feature.lower() in filename.lower():
                            # Move the image to the location directory
                            try:
                                shutil.move(os.path.join(self.image_dir, filename), location_dir)
                                print(f"Moved {filename} to {location_dir}")
                            except Exception as e:
                                print(f"Error moving {filename}: {str(e)}")

def main():
    image_dir = "path/to/images"
    destination_dir = "path/to/organized/images"

    location_features = {
        "Golden Paradise": ["golden", "paradise", "beach"],
        "Island Dream": ["island", "dream", "sea"]
    }

    organizer = ImageOrganizer(image_dir, destination_dir)
    organizer.organize_images(location_features)

if __name__ == "__main__":
    main()
```
