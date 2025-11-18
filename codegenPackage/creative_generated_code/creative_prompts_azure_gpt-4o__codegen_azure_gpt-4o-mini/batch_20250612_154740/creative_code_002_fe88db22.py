"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Generate code to organize and categorize portrait photos into creative and classic styles, reflecting the personalized approach described in Officine dell’Immagine's portrait services.
Generated: DETERMINISTIC_fe88db2250da88a9
Batch ID: 20250612_154740
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

class PortraitOrganizer:
    def __init__(self, source_directory: str, dest_directory: str):
        """
        Initialize the PortraitOrganizer with source and destination directories.
        
        Parameters:
        source_directory (str): The directory containing the portrait photos.
        dest_directory (str): The destination directory to organize photos.
        """
        self.source_directory = source_directory
        self.dest_directory = dest_directory
        self.creative_dir = os.path.join(dest_directory, 'Creative')
        self.classic_dir = os.path.join(dest_directory, 'Classic')

        # Create destination directories if they don't exist
        os.makedirs(self.creative_dir, exist_ok=True)
        os.makedirs(self.classic_dir, exist_ok=True)

    def categorize_photos(self):
        """
        Iterate through photos in the source directory and categorize them
        into creative and classic styles based on some criteria.
        """
        for filename in os.listdir(self.source_directory):
            file_path = os.path.join(self.source_directory, filename)
            if os.path.isfile(file_path):
                try:
                    self._categorize_photo(file_path, filename)
                except Exception as e:
                    print(f"Error processing '{filename}': {e}")

    def _categorize_photo(self, file_path: str, filename: str):
        """
        Categorize a single photo based on its characteristics.
        
        Parameters:
        file_path (str): The full path of the photo file.
        filename (str): The name of the photo file.
        """
        # Open the image to determine its style
        with Image.open(file_path) as img:
            # Simplified condition to categorize images
            if self._is_creative_photo(img):
                self._move_photo(file_path, self.creative_dir, filename)
            else:
                self._move_photo(file_path, self.classic_dir, filename)

    def _is_creative_photo(self, img: Image.Image) -> bool:
        """
        Determine if the photo is of creative style.
        
        Parameters:
        img (Image.Image): The image to analyze.

        Returns:
        bool: True if the photo is creative, False otherwise.
        """
        # Implement custom logic for categorization based on image properties
        # For example, check the image mode or dimensions
        return img.size[0] > img.size[1]  # Simple example: landscape is creative

    def _move_photo(self, src: str, dest_dir: str, filename: str):
        """
        Move the photo to the appropriate directory.
        
        Parameters:
        src (str): Source file path.
        dest_dir (str): Destination directory.
        filename (str): Name of the photo file.
        """
        dest_path = os.path.join(dest_dir, filename)
        shutil.move(src, dest_path)
        print(f"Moved '{filename}' to '{dest_dir}'")

def main():
    source_dir = 'path/to/source_directory'  # Specify the source directory
    dest_dir = 'path/to/destination_directory'  # Specify the destination directory

    organizer = PortraitOrganizer(source_dir, dest_dir)
    organizer.categorize_photos()

if __name__ == "__main__":
    main()
```

### Note:
- Ensure to replace `'path/to/source_directory'` and `'path/to/destination_directory'` with actual paths before running the code.
- The categorization logic in `_is_creative_photo` is simplified and should be tailored to your specific requirements for distinguishing between creative and classic styles.
