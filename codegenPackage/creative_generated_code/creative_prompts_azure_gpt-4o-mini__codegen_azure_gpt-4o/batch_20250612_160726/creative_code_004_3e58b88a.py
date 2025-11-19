"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddysbearprc20.com
Prompt: Explain how to create and share memes for the Teddy Bear PRC20 community, including the relevant hashtags and social media tags to use.
Generated: DETERMINISTIC_3e58b88a54c9ca3c
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script helps users create and share memes for the Teddy Bear PRC20 community.
It allows users to input meme text and an image, adds relevant hashtags and tags,
and prepares the meme for sharing on social media.
"""

import os
from PIL import Image, ImageDraw, ImageFont


def create_meme(image_path: str, meme_text: str, output_path: str = "output_meme.png") -> str:
    """
    Creates a meme by overlaying text on an image.

    Args:
        image_path (str): Path to the input image file.
        meme_text (str): Text to overlay on the image.
        output_path (str): Path where the output meme image will be saved.

    Returns:
        str: Path to the saved meme image.
    """
    try:
        # Load the image
        img = Image.open(image_path)

        # Prepare to draw on the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()  # Fallback to default font

        # Determine text position and size
        image_width, image_height = img.size
        text_width, text_height = draw.textsize(meme_text, font=font)
        text_x = (image_width - text_width) // 2
        text_y = image_height - text_height - 20  # Position at the bottom with some padding

        # Draw the text on the image
        draw.text((text_x, text_y), meme_text, font=font, fill="white")

        # Save the meme
        img.save(output_path)
        return output_path

    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while creating the meme: {e}")


def share_meme(meme_path: str) -> None:
    """
    Provides sharing instructions for the meme on social media.

    Args:
        meme_path (str): Path to the meme image file.
    """
    try:
        if not os.path.exists(meme_path):
            raise FileNotFoundError(f"Meme file not found: {meme_path}")

        # Relevant hashtags and social media tags
        hashtags = "#TeddyBear #PRC20 #CryptoMemes #BlockchainCommunity"
        tags = "Tag: @TeddyBearOfficial"

        # Display sharing instructions
        print(f"Your meme is ready at {meme_path}!")
        print("\nShare your meme with the following hashtags and tags:")
        print(hashtags)
        print(tags)

    except Exception as e:
        raise RuntimeError(f"An error occurred while preparing the sharing instructions: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to the Teddy Bear PRC20 Meme Generator!")
        image_path = input("Enter the path to your image file: ").strip()
        meme_text = input("Enter the text for your meme: ").strip()

        # Create the meme
        output_meme = create_meme(image_path, meme_text)
        print(f"Meme created successfully: {output_meme}")

        # Provide sharing instructions
        share_meme(output_meme)

    except Exception as e:
        print(f"An error occurred: {e}")
```
