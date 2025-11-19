"""
Generated Code Metadata:
========================
Original URL: https://npcs.pages.dev
Prompt: Provide a code example for using the NPC AI generator to create new meme images, and suggest potential applications for this technology.
Generated: DETERMINISTIC_6b6362d6846dc0e0
Batch ID: 20250622_204657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont
import random

# NPC AI Meme Generator
class MemeGenerator:
    def __init__(self, output_dir="generated_memes"):
        """
        Initialize the MemeGenerator with an output directory.
        :param output_dir: Directory where generated memes will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)  # Ensure output directory exists

    def generate_meme(self, base_image_path, text, font_path="arial.ttf", font_size=24):
        """
<<<<<<< HEAD
        Generate a meme image with the given text overlayed on a base image.
        :param base_image_path: Path to the base image file.
=======
        Generate a meme image with the given text.
        :param base_image_path: Path to the base image to use for the meme.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        :param text: Text to overlay on the image.
        :param font_path: Path to the font file to use for the text.
        :param font_size: Font size for the text.
        :return: Path to the generated meme image.
        """
        try:
            # Load the base image
<<<<<<< HEAD
            base_image = Image.open(base_image_path)
            draw = ImageDraw.Draw(base_image)
=======
            image = Image.open(base_image_path)
            draw = ImageDraw.Draw(image)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

            # Load the font
            font = ImageFont.truetype(font_path, font_size)

            # Calculate text position (centered)
            text_width, text_height = draw.textsize(text, font=font)
<<<<<<< HEAD
            image_width, image_height = base_image.size
            text_x = (image_width - text_width) // 2
            text_y = image_height - text_height - 10  # Position text near the bottom

            # Overlay the text on the image
=======
            image_width, image_height = image.size
            text_x = (image_width - text_width) // 2
            text_y = image_height - text_height - 10  # Position text near the bottom

            # Add text to the image
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
            draw.text((text_x, text_y), text, font=font, fill="white")

            # Save the generated meme
            output_path = os.path.join(self.output_dir, f"meme_{random.randint(1000, 9999)}.png")
<<<<<<< HEAD
            base_image.save(output_path)
=======
            image.save(output_path)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

            return output_path
        except Exception as e:
            print(f"Error generating meme: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the meme generator
    meme_generator = MemeGenerator()

<<<<<<< HEAD
    # Generate a meme
    base_image = "base_image.jpg"  # Replace with the path to your base image
    meme_text = "When the AI starts making memes better than humans"
=======
    # Define base image and text
    base_image = "npc_base_image.png"  # Replace with the path to your base image
    meme_text = "When the NPC AI becomes self-aware..."

    # Generate the meme
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    generated_meme_path = meme_generator.generate_meme(base_image, meme_text)

    if generated_meme_path:
        print(f"Meme generated successfully: {generated_meme_path}")
    else:
        print("Failed to generate meme.")

# Potential Applications:
<<<<<<< HEAD
# 1. Social Media Content Creation: Automate meme generation for marketing campaigns.
# 2. Entertainment Platforms: Generate memes dynamically based on trending topics.
# 3. AI-Powered Humor: Create personalized memes for users based on their preferences.
# 4. Meme Templates: Provide users with AI-generated meme templates for customization.
=======
# 1. Social Media Content Creation: Automate meme generation for trending topics.
# 2. Marketing Campaigns: Create engaging and humorous content for brand promotion.
# 3. Entertainment Platforms: Generate memes dynamically based on user interactions.
# 4. AI Research: Showcase the creative capabilities of NPC AI in visual content generation.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
