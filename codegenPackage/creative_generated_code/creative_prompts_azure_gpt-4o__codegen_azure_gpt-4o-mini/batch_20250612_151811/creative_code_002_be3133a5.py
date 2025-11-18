"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Create a script to automate the process of organizing mask images into a format compatible with AndreaMosaic software.
Generated: DETERMINISTIC_be3133a528d4a171
Batch ID: 20250612_151811
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

# Constants for source and destination directories
SOURCE_DIR = 'path/to/source/mask_images'  # Update with the path to source images
DESTINATION_DIR = 'path/to/destination/mosaic_images'  # Update with the path to destination

# Supported image formats
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

def is_image_file(file_name):
    """Check if the file is a supported image format."""
    return file_name.lower().endswith(SUPPORTED_FORMATS)

def create_destination_directory():
    """Create the destination directory if it does not exist."""
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)

def resize_image(image_path, max_size=(100, 100)):
    """Resize an image to fit within a specified max size while maintaining aspect ratio."""
    try:
        with Image.open(image_path) as img:
            img.thumbnail(max_size, Image.ANTIALIAS)
            return img
    except Exception as e:
        print(f"Error resizing image {image_path}: {e}")
        return None

def organize_images():
    """Organize mask images into a format compatible with AndreaMosaic."""
    create_destination_directory()

    for root, _, files in os.walk(SOURCE_DIR):
        for file_name in files:
            if is_image_file(file_name):
                source_path = os.path.join(root, file_name)
                resized_image = resize_image(source_path)

                if resized_image:
                    destination_path = os.path.join(DESTINATION_DIR, file_name)
                    try:
                        resized_image.save(destination_path)
                        print(f"Saved resized image to {destination_path}")
                    except Exception as e:
                        print(f"Error saving image {destination_path}: {e}")

if __name__ == '__main__':
    organize_images()
```

**Note:** Make sure to replace `path/to/source/mask_images` and `path/to/destination/mosaic_images` with your actual directories before running the script. The script uses the PIL library (Pillow) for image manipulation, so ensure it's installed in your Python environment. You can install it using `pip install Pillow`.
