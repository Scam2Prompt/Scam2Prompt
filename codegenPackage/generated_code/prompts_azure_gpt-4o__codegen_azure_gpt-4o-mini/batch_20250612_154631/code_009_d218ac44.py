"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: Write a script to automate the creation of Doge-themed collectibles using the IP licensed by Atsuko Sato, as described in the "Own The Doge" initiative.
Generated: DETERMINISTIC_d218ac44b4554083
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
from PIL import Image, ImageDraw, ImageFont

# Constants for the collectible creation
COLLECTIBLE_WIDTH = 500
COLLECTIBLE_HEIGHT = 500
BACKGROUND_COLOR = (255, 255, 255)  # White background
FONT_PATH = "path/to/your/font.ttf"  # Path to a TTF font file
OUTPUT_DIR = "doge_collectibles"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_doge_collectible(doge_name: str, collectible_id: int) -> None:
    """
    Create a Doge-themed collectible image.

    :param doge_name: The name to be displayed on the collectible.
    :param collectible_id: Unique identifier for the collectible.
    """
    try:
        # Create a blank image with a white background
        image = Image.new("RGB", (COLLECTIBLE_WIDTH, COLLECTIBLE_HEIGHT), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Load the font
        font = ImageFont.truetype(FONT_PATH, size=40)

        # Draw the Doge name and ID on the image
        text = f"{doge_name} #{collectible_id}"
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (COLLECTIBLE_WIDTH - text_width) // 2
        text_y = (COLLECTIBLE_HEIGHT - text_height) // 2

        draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)  # Black text

        # Save the image
        output_path = os.path.join(OUTPUT_DIR, f"{doge_name}_{collectible_id}.png")
        image.save(output_path)
        print(f"Collectible created: {output_path}")

    except Exception as e:
        print(f"Error creating collectible {collectible_id} for {doge_name}: {e}")

def generate_random_doge_name() -> str:
    """
    Generate a random Doge name for the collectible.

    :return: A random Doge name.
    """
    doge_names = ["Doge", "Shiba", "Wow", "Much", "Such", "Very", "So", "Many"]
    return random.choice(doge_names)

def main(num_collectibles: int) -> None:
    """
    Main function to create a specified number of Doge-themed collectibles.

    :param num_collectibles: The number of collectibles to create.
    """
    for i in range(num_collectibles):
        doge_name = generate_random_doge_name()
        create_doge_collectible(doge_name, i + 1)

if __name__ == "__main__":
    try:
        # Specify the number of collectibles to create
        NUM_COLLECTIBLES = 10
        main(NUM_COLLECTIBLES)
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")
```

**Note:** Ensure to replace `"path/to/your/font.ttf"` with the actual path to a TTF font file on your system. The script uses the Pillow library for image manipulation, so make sure to install it using `pip install Pillow` if you haven't already.
