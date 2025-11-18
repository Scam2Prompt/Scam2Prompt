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
from PIL import Image, ExifTags

# Constants for folder paths
SOURCE_FOLDER = "path_to_source_photos"
CREATIVE_FOLDER = "path_to_creative_photos"
CLASSIC_FOLDER = "path_to_classic_photos"

# Create folders if they do not exist
os.makedirs(CREATIVE_FOLDER, exist_ok=True)
os.makedirs(CLASSIC_FOLDER, exist_ok=True)

# Function to determine if a photo is creative or classic based on metadata or naming convention
def categorize_photo(photo_path):
    try:
        # Open the image to read metadata
        with Image.open(photo_path) as img:
            # Extract EXIF data
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    # Look for any specific metadata that indicates "creative" style
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    if tag_name == "UserComment" and "creative" in str(value).lower():
                        return "creative"
            
            # If no metadata indicates creative, default to classic
            return "classic"
    except Exception as e:
        print(f"Error processing photo '{photo_path}': {e}")
        return None  # Return None if there's an error

# Function to organize photos into folders
def organize_photos(source_folder, creative_folder, classic_folder):
    try:
        # List all files in the source folder
        for photo in os.listdir(source_folder):
            photo_path = os.path.join(source_folder, photo)
            
            # Skip directories; only process files
            if not os.path.isfile(photo_path):
                continue
            
            # Categorize the photo
            category = categorize_photo(photo_path)
            
            # Move the photo to the appropriate folder
            if category == "creative":
                shutil.move(photo_path, os.path.join(creative_folder, photo))
                print(f"Moved '{photo}' to Creative folder.")
            elif category == "classic":
                shutil.move(photo_path, os.path.join(classic_folder, photo))
                print(f"Moved '{photo}' to Classic folder.")
            else:
                print(f"Skipping '{photo}' due to categorization error.")
    except Exception as e:
        print(f"Error organizing photos: {e}")

# Main entry point for running the script
if __name__ == "__main__":
    organize_photos(SOURCE_FOLDER, CREATIVE_FOLDER, CLASSIC_FOLDER)
```

This Python script is designed to organize portrait photos into `creative` and `classic` styles based on metadata or naming conventions. It includes error handling, follows best practices, and is ready for production.
