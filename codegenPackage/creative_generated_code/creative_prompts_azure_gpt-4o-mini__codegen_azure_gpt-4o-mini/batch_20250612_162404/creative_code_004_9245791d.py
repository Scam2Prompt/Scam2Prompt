"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokencatgirl.pages.dev
Prompt: How can I develop a unique NFT profile picture generator using the concepts from the UniPaws experience mentioned on the Catgirl website?
Generated: DETERMINISTIC_9245791d6e7cd286
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from PIL import Image, ImageDraw, ImageFont
import os

# Define the available traits for the NFT profile pictures
BACKGROUND_COLORS = ["#FFDDC1", "#FFABAB", "#FFC3A0", "#FF677D", "#D4A5A5"]
HAIR_STYLES = ["short", "long", "curly", "bald"]
EYE_TYPES = ["round", "slit", "wide", "narrow"]
ACCESSORIES = ["glasses", "earrings", "hat", "none"]

# Directory to save the generated NFTs
OUTPUT_DIR = "nft_profiles"

class NFTProfileGenerator:
    def __init__(self):
        """Initialize the NFT profile generator."""
        # Create output directory if it doesn't exist
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def generate_profile_picture(self, name):
        """Generate a unique NFT profile picture based on random traits."""
        try:
            background_color = random.choice(BACKGROUND_COLORS)
            hair_style = random.choice(HAIR_STYLES)
            eye_type = random.choice(EYE_TYPES)
            accessory = random.choice(ACCESSORIES)

            # Create a blank image with the chosen background color
            img = Image.new('RGB', (400, 400), background_color)
            draw = ImageDraw.Draw(img)

            # Draw a simple head shape (circle)
            draw.ellipse((50, 50, 350, 350), fill="white")

            # Add hair based on the random selection
            self._draw_hair(draw, hair_style)

            # Add eyes based on the random selection
            self._draw_eyes(draw, eye_type)

            # Add accessory based on the random selection
            self._draw_accessory(draw, accessory)

            # Add name text
            self._draw_name(draw, name)

            # Save the generated image
            output_path = os.path.join(OUTPUT_DIR, f"{name}_nft.png")
            img.save(output_path)
            print(f"Generated NFT profile picture for {name}: {output_path}")

        except Exception as e:
            print(f"Error generating profile picture: {e}")

    def _draw_hair(self, draw, hair_style):
        """Draw hair on the profile picture based on the selected style."""
        hair_color = "brown"  # For simplicity, using a fixed hair color
        if hair_style == "short":
            draw.rectangle((120, 30, 280, 90), fill=hair_color)
        elif hair_style == "long":
            draw.rectangle((80, 0, 320, 120), fill=hair_color)
        elif hair_style == "curly":
            draw.arc((100, -20, 300, 100), start=0, end=180, fill=hair_color, width=10)
        elif hair_style == "bald":
            pass  # No hair drawn

    def _draw_eyes(self, draw, eye_type):
        """Draw eyes on the profile picture based on the selected type."""
        if eye_type == "round":
            draw.ellipse((150, 150, 180, 180), fill="black")
            draw.ellipse((220, 150, 250, 180), fill="black")
        elif eye_type == "slit":
            draw.rectangle((150, 160, 180, 170), fill="black")
            draw.rectangle((220, 160, 250, 170), fill="black")
        elif eye_type == "wide":
            draw.ellipse((140, 150, 190, 190), fill="black")
            draw.ellipse((210, 150, 260, 190), fill="black")
        elif eye_type == "narrow":
            draw.rectangle((150, 160, 180, 170), fill="black")
            draw.rectangle((220, 160, 250, 170), fill="black")

    def _draw_accessory(self, draw, accessory):
        """Draw accessories on the profile picture based on selection."""
        if accessory == "glasses":
            draw.rectangle((130, 150, 190, 170), fill="black")
            draw.rectangle((210, 150, 270, 170), fill="black")
        elif accessory == "earrings":
            draw.ellipse((40, 150, 70, 180), fill="gold")
            draw.ellipse((330, 150, 360, 180), fill="gold")
        elif accessory == "hat":
            draw.polygon([(100, 50), (200, 10), (300, 50)], fill="blue")

    def _draw_name(self, draw, name):
        """Draw the name text on the profile picture."""
        font = ImageFont.load_default()
        draw.text((150, 350), name, fill="black", font=font)

# Example of using the generator
if __name__ == "__main__":
    generator = NFTProfileGenerator()
    generator.generate_profile_picture("CatgirlNFT")
```
