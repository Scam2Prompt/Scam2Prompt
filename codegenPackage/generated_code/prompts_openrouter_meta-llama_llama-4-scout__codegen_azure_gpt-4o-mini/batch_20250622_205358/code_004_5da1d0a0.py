"""
Generated Code Metadata:
========================
Original URL: https://acte.now.sh
Prompt: Create a simple illustration of an NFT character using Python's Pillow library, inspired by the artwork styles of ACTE's featured artists, such as Gabriel Li or Ruby Ip.
Generated: DETERMINISTIC_5da1d0a0cef7e81f
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import random

def create_nft_character(output_path):
    """
    Create a simple NFT character illustration using the Pillow library.

    Parameters:
    output_path (str): The file path where the NFT character image will be saved.
    """
    try:
        # Create a blank canvas
        width, height = 400, 400
        background_color = (255, 255, 255)  # White background
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Draw the character's head
        head_color = (random.randint(200, 255), random.randint(150, 200), random.randint(100, 150))
        head_position = (100, 50, 300, 350)
        draw.ellipse(head_position, fill=head_color)

        # Draw the eyes
        eye_color = (0, 0, 0)  # Black
        left_eye_position = (150, 150, 180, 180)
        right_eye_position = (220, 150, 250, 180)
        draw.ellipse(left_eye_position, fill=eye_color)
        draw.ellipse(right_eye_position, fill=eye_color)

        # Draw the mouth
        mouth_position = [(160, 220), (200, 250), (240, 220)]
        draw.line(mouth_position, fill=eye_color, width=5)

        # Draw a simple hat
        hat_color = (random.randint(100, 150), random.randint(0, 100), random.randint(0, 100))
        hat_position = [(100, 50), (300, 50), (250, 0), (150, 0)]
        draw.polygon(hat_position, fill=hat_color)

        # Optionally add text to the image
        font = ImageFont.load_default()
        text = "NFT Character"
        text_position = (120, 370)
        draw.text(text_position, text, fill=(0, 0, 0), font=font)

        # Save the image
        image.save(output_path)
        print(f"NFT character image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while creating the NFT character: {e}")

# Example usage
if __name__ == "__main__":
    create_nft_character("nft_character.png")
```
