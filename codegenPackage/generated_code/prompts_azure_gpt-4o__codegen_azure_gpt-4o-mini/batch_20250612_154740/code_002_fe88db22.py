"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Generate code to organize and categorize portrait photos into creative and classic styles, reflecting the personalized approach described in Officine dell’Immagine's portrait services.
Generated: DETERMINISTIC_fe88db2250da88a9
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
from PIL import Image

class PhotoOrganizer:
    """
    A class to organize and categorize portrait photos into creative and classic styles.
    """

    def __init__(self, source_directory, destination_directory):
        """
        Initializes the PhotoOrganizer with source and destination directories.

        :param source_directory: Directory containing the portrait photos.
        :param destination_directory: Directory where organized photos will be saved.
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.creative_directory = os.path.join(destination_directory, 'Creative')
        self.classic_directory = os.path.join(destination_directory, 'Classic')

        # Create destination directories if they do not exist
        os.makedirs(self.creative_directory, exist_ok=True)
        os.makedirs(self.classic_directory, exist_ok=True)

    def categorize_photos(self):
        """
        Categorizes photos into creative and classic styles based on their filenames.
        """
        try:
            for filename in os.listdir(self.source_directory):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self._categorize_photo(filename)
                else:
                    print(f"Skipping non-image file: {filename}")
        except Exception as e:
            print(f"Error while categorizing photos: {e}")

    def _categorize_photo(self, filename):
        """
        Categorizes a single photo based on its filename.

        :param filename: The name of the photo file to categorize.
        """
        source_path = os.path.join(self.source_directory, filename)

        # Simple categorization logic based on filename keywords
        if 'creative' in filename.lower():
            destination_path = os.path.join(self.creative_directory, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Copied to Creative: {filename}")
        elif 'classic' in filename.lower():
            destination_path = os.path.join(self.classic_directory, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Copied to Classic: {filename}")
        else:
            print(f"No category found for: {filename}")

    def resize_photos(self, max_size=(800, 800)):
        """
        Resizes photos in the destination directories to a maximum size.

        :param max_size: A tuple representing the maximum width and height.
        """
        try:
            for category in [self.creative_directory, self.classic_directory]:
                for filename in os.listdir(category):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                        self._resize_photo(os.path.join(category, filename), max_size)
        except Exception as e:
            print(f"Error while resizing photos: {e}")

    def _resize_photo(self, photo_path, max_size):
        """
        Resizes a single photo to fit within the specified maximum size.

        :param photo_path: The path to the photo file to resize.
        :param max_size: A tuple representing the maximum width and height.
        """
        with Image.open(photo_path) as img:
            img.thumbnail(max_size)
            img.save(photo_path)
            print(f"Resized photo: {photo_path}")

if __name__ == "__main__":
    # Example usage
    source_dir = 'path/to/source/photos'
    destination_dir = 'path/to/destination/photos'

    organizer = PhotoOrganizer(source_dir, destination_dir)
    organizer.categorize_photos()
    organizer.resize_photos()
```
