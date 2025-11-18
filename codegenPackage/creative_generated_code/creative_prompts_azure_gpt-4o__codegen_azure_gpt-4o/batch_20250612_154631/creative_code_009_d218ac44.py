"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Write a script to automate the creation of Doge-themed collectibles using the IP licensed by Atsuko Sato, as described in the "Own The Doge" initiative.
Generated: DETERMINISTIC_d218ac44b4554083
Batch ID: 20250612_154631
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
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Constants
COLLECTIBLE_FOLDER = "doge_collectibles"
METADATA_FOLDER = os.path.join(COLLECTIBLE_FOLDER, "metadata")
IMAGE_FOLDER = os.path.join(COLLECTIBLE_FOLDER, "images")
BASE_IMAGE_PATH = "doge_base_image.jpg"  # Base Doge image for collectibles
FONT_PATH = "arial.ttf"  # Path to the font file
LICENSE_OWNER = "Atsuko Sato"
INITIATIVE_NAME = "Own The Doge"

# Ensure directories exist for storing collectibles
os.makedirs(METADATA_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def generate_collectible(name: str, tagline: str, color: tuple, unique_id: int):
    """
    Generate a Doge-themed collectible with metadata and an image.
    
    :param name: Name of the collectible.
    :param tagline: Tagline or caption for the collectible.
    :param color: RGB tuple for text color.
    :param unique_id: Unique identifier for the collectible.
    :return: None
    """
    try:
        # Load base image
        base_image = Image.open(BASE_IMAGE_PATH)
        draw = ImageDraw.Draw(base_image)
        
        # Prepare font
        try:
            font = ImageFont.truetype(FONT_PATH, size=50)
        except OSError:
            raise FileNotFoundError("Font file not found. Please check the FONT_PATH variable.")
        
        # Add text to image
        draw.text((50, 50), tagline, fill=color, font=font)
        
        # Save image
        image_filename = f"{name}_{unique_id}.png"
        image_path = os.path.join(IMAGE_FOLDER, image_filename)
        base_image.save(image_path)
        
        # Create metadata
        metadata = {
            "name": name,
            "tagline": tagline,
            "color": color,
            "unique_id": unique_id,
            "image_path": image_path,
            "license_owner": LICENSE_OWNER,
            "initiative_name": INITIATIVE_NAME,
            "created_at": datetime.now().isoformat()
        }
        
        # Save metadata
        metadata_filename = f"{name}_{unique_id}.json"
        metadata_path = os.path.join(METADATA_FOLDER, metadata_filename)
        with open(metadata_path, "w") as metadata_file:
            json.dump(metadata, metadata_file, indent=4)
        
        print(f"Collectible '{name}' successfully created!")
    except Exception as e:
        print(f"Error generating collectible: {e}")

def main():
    """
    Main function to automate the creation of Doge-themed collectibles.
    """
    # Example collectibles to generate
    collectibles = [
        {"name": "DogeMoon", "tagline": "To the moon!", "color": (255, 223, 0), "unique_id": 1},
        {"name": "DogeSun", "tagline": "Shine bright!", "color": (255, 69, 0), "unique_id": 2},
        {"name": "DogeStar", "tagline": "Twinkle twinkle!", "color": (0, 191, 255), "unique_id": 3}
    ]
    
    for collectible in collectibles:
        generate_collectible(**collectible)

if __name__ == "__main__":
    main()
```
