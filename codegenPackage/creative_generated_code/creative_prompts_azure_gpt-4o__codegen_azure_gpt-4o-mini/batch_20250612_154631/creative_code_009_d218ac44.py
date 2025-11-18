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
import random
from PIL import Image, ImageDraw, ImageFont

# Constants for the collectible properties
COLLECTIBLE_WIDTH = 600
COLLECTIBLE_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_PATH = "path/to/font.ttf"  # Path to TTF font file for rendering text
OUTPUT_DIRECTORY = "doge_collectibles"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def generate_doge_collectible(doge_name: str, collectible_id: int) -> None:
    """
    Generate a Doge-themed collectible image with a given name and ID.

    Args:
        doge_name (str): The name of the Doge character.
        collectible_id (int): Unique identifier for the collectible.
    """
    try:
        # Create a new image with a white background
        image = Image.new("RGB", (COLLECTIBLE_WIDTH, COLLECTIBLE_HEIGHT), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Load the font
        font_size = 40
        font = ImageFont.truetype(FONT_PATH, font_size)

        # Draw the Doge name
        text = f"{doge_name} #{collectible_id}"
        text_width, text_height = draw.textsize(text, font=font)
        text_position = ((COLLECTIBLE_WIDTH - text_width) // 2, (COLLECTIBLE_HEIGHT - text_height) // 2)
        draw.text(text_position, text, font=font, fill=FONT_COLOR)

        # Save the image
        filename = os.path.join(OUTPUT_DIRECTORY, f"doge_collectible_{collectible_id}.png")
        image.save(filename)

        print(f"Generated collectible: {filename}")

    except Exception as e:
        print(f"Error generating collectible '{doge_name} #{collectible_id}': {e}")

def main():
    """
    Main function to automate the creation of Doge-themed collectibles.
    """
    doge_names = [
        "Doge1",
        "Doge2",
        "Doge3",
        "Doge4",
        "Doge5"
    ]

    # Generate collectibles for each doge name
    for collectible_id, doge_name in enumerate(doge_names, start=1):
        generate_doge_collectible(doge_name, collectible_id)

if __name__ == "__main__":
    main()
```
