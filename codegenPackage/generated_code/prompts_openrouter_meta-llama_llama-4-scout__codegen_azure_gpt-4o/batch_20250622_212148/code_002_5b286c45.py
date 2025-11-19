"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: "Write a Python script to categorize and organize photos into folders based on tags like 'urban', 'paradise', 'lifestyle', and 'travel'."
Generated: DETERMINISTIC_5b286c45ec7521c1
Batch ID: 20250622_212148
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
from PIL.ExifTags import TAGS

def extract_tags(image_path):
    """
    Extract tags from the image metadata.
    Returns a list of tags if found, otherwise an empty list.
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if not exif_data:
                return []
            
            tags = []
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                if tag_name == "XPKeywords":  # Common tag for keywords
                    tags = value.decode('utf-16').split(';')  # Tags are often semicolon-separated
                    break
            return tags
    except Exception as e:
        print(f"Error extracting tags from {image_path}: {e}")
        return []

def organize_photos_by_tags(source_folder, destination_folder, tag_categories):
    """
    Organize photos into folders based on tags.
    
    Parameters:
    - source_folder: Path to the folder containing photos.
    - destination_folder: Path to the folder where categorized photos will be stored.
    - tag_categories: Dictionary mapping tags to folder names.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip non-image files
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        tags = extract_tags(file_path)
        if not tags:
            print(f"No tags found for {filename}. Skipping...")
            continue
        
        # Categorize based on tags
        categorized = False
        for tag in tags:
            tag = tag.lower().strip()
            if tag in tag_categories:
                category_folder = os.path.join(destination_folder, tag_categories[tag])
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category_folder}")
                categorized = True
                break
        
        if not categorized:
            print(f"No matching category for {filename}. Skipping...")

if __name__ == "__main__":
    # Define the source folder containing photos
    source_folder = "path/to/source/folder"
    
    # Define the destination folder for organized photos
    destination_folder = "path/to/destination/folder"
    
    # Define tag categories and their corresponding folder names
    tag_categories = {
        "urban": "Urban",
        "paradise": "Paradise",
        "lifestyle": "Lifestyle",
        "travel": "Travel"
    }
    
    # Organize photos
    organize_photos_by_tags(source_folder, destination_folder, tag_categories)
```
