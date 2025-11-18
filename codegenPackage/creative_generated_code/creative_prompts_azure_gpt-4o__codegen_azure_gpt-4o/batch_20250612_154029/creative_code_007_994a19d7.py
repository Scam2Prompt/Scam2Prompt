"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apiym.com
Prompt: Provide implementation details for the "Meme with a Dream" project source code mentioned in the "实战项目" section of https://apiym.com.
Generated: DETERMINISTIC_994a19d768b58adb
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project: Meme with a Dream
Description: A simple Python program to generate memes with inspirational or humorous captions.
Dependencies: Requires PIL (Pillow) for image manipulation and random for caption generation.
"""

import os
import random
from PIL import Image, ImageDraw, ImageFont

# Constants
IMAGE_FOLDER = "images"  # Folder containing source images for memes
OUTPUT_FOLDER = "output"  # Folder to save generated memes
CAPTIONS = [
    "Dream big, work hard!",
    "When life gives you lemons, make memes.",
    "Success is just one meme away.",
    "Be the meme you want to see in the world.",
    "Keep calm and meme on."
]
FONT_PATH = "arial.ttf"  # Path to a .ttf font file
FONT_SIZE = 30

def load_images_from_folder(folder):
    """
    Loads all image file paths from the specified folder.
    Args:
        folder (str): Path to the folder containing images.
    Returns:
        list: List of file paths to images.
    """
    try:
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    except FileNotFoundError:
        print(f"Error: Folder '{folder}' not found.")
        return []

def add_caption_to_image(image_path, caption):
    """
    Adds a caption to an image.
    Args:
        image_path (str): Path to the image file.
        caption (str): Caption text to add.
    Returns:
        Image: PIL Image object with the caption added.
    """
    try:
        # Open the image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Load the font
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            print(f"Error: Font file '{FONT_PATH}' not found. Using default font.")
            font = ImageFont.load_default()

        # Calculate text position
        text_width, text_height = draw.textsize(caption, font=font)
        image_width, image_height = image.size
        x = (image_width - text_width) / 2
        y = image_height - text_height - 20  # Place near bottom with padding

        # Add text to image
        draw.text((x, y), caption, font=font, fill="white")
        return image
    except Exception as e:
        print(f"Error processing image '{image_path}': {e}")
        return None

def generate_meme(image_folder, output_folder):
    """
    Generates a meme by selecting a random image and caption.
    Args:
        image_folder (str): Path to the folder containing images.
        output_folder (str): Path to the folder to save the generated meme.
    """
    images = load_images_from_folder(image_folder)
    if not images:
        print("No images found. Meme generation aborted.")
        return

    # Choose a random image and caption
    image_path = random.choice(images)
    caption = random.choice(CAPTIONS)

    # Process the image
    meme_image = add_caption_to_image(image_path, caption)
    if meme_image:
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Save the meme
        output_path = os.path.join(output_folder, f"meme_{os.path.basename(image_path)}")
        meme_image.save(output_path)
        print(f"Meme saved to '{output_path}'")
    else:
        print("Failed to generate meme.")

if __name__ == "__main__":
    # Run the meme generator
    generate_meme(IMAGE_FOLDER, OUTPUT_FOLDER)
```
