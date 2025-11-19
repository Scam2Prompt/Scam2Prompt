"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elan-life.com
Prompt: Create a script that organizes and filters images by location, such as "Golden Paradise" and "Island Dream," reflecting the unique features of the élán-life image galleries.
Generated: DETERMINISTIC_c027e90be0b51e08
Batch ID: 20250612_161017
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
from PIL import Image
from pathlib import Path
from typing import List, Dict

class ImageOrganizer:
    def __init__(self, source_directory: str, destination_directory: str):
        """
        Initializes the ImageOrganizer instance.

        :param source_directory: Directory containing the images to organize.
        :param destination_directory: Directory where organized images will be stored.
        """
        self.source_directory = Path(source_directory)
        self.destination_directory = Path(destination_directory)

        # Ensure destination directory exists
        self.destination_directory.mkdir(parents=True, exist_ok=True)

    def get_image_location(self, image_path: Path) -> str:
        """
        Extracts the location from the image file's name.

        :param image_path: The path of the image file.
        :return: The location as a string.
        """
        # Assuming the location is in the file name, formatted as "location_image.jpg"
        return image_path.stem.split('_')[0]  # Get the part before the first underscore

    def organize_images(self) -> None:
        """
        Organizes images into folders based on their location.
        """
        try:
            # Iterate through all image files in the source directory
            for image_file in self.source_directory.glob('*.*'):
                if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                    location = self.get_image_location(image_file)

                    # Create a directory for the location if it doesn't exist
                    location_directory = self.destination_directory / location
                    location_directory.mkdir(exist_ok=True)

                    # Copy the image to the respective location folder
                    shutil.copy(image_file, location_directory / image_file.name)
                    print(f"Copied {image_file.name} to {location_directory}")

        except Exception as e:
            print(f"An error occurred while organizing images: {e}")

    def filter_images_by_location(self, location: str) -> List[Path]:
        """
        Retrieves images from the specified location.

        :param location: The location to filter images by.
        :return: List of image paths from the specified location.
        """
        location_directory = self.destination_directory / location

        # Check if location directory exists and return images if it does
        if location_directory.exists() and location_directory.is_dir():
            return list(location_directory.glob('*.*'))
        else:
            print(f"No images found for location: {location}")
            return []

# Example usage
if __name__ == "__main__":
    SOURCE_DIR = "path/to/source/images"  # Update with the actual source directory path
    DESTINATION_DIR = "path/to/destination/images"  # Update with the actual destination directory path

    organizer = ImageOrganizer(SOURCE_DIR, DESTINATION_DIR)
    organizer.organize_images()

    # Example of filtering images from a specific location
    filtered_images = organizer.filter_images_by_location("Golden Paradise")
    for img in filtered_images:
        print(f"Found image: {img.name}")

```
