"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: "Generate a social media post design for a business in Ethiopia, using a style similar to the examples provided on Alpha Digital Solutions' website."
Generated: DETERMINISTIC_ced0da3152e60e50
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from PIL import Image, ImageDraw, ImageFont
import os

def create_social_media_post(image_path, business_name, post_text, font_path):
    """
    Generate a social media post design for a business.

    Args:
        image_path (str): Path to the background image.
        business_name (str): Name of the business.
        post_text (str): Text to be displayed on the post.
        font_path (str): Path to the font file.

    Returns:
        str: Path to the generated image.
    """

    try:
        # Open the background image
        with Image.open(image_path) as img:
            # Create a drawing context
            draw = ImageDraw.Draw(img)

            # Load the font
            font = ImageFont.truetype(font_path, 40)

            # Draw the business name
            draw.text((20, 20), business_name, font=font, fill=(255, 255, 255))

            # Draw the post text
            lines = post_text.splitlines()
            for i, line in enumerate(lines):
                draw.text((20, 80 + (i * 50)), line, font=font, fill=(255, 255, 255))

            # Save the generated image
            generated_image_path = "generated_post.png"
            img.save(generated_image_path)

            return generated_image_path

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Define the background image path
    image_path = "background.jpg"

    # Define the business name and post text
    business_name = "Ethiopian Business"
    post_text = "We are open for business!\nCome and experience the best services in town."

    # Define the font path
    font_path = "arial.ttf"

    # Check if files exist
    if not os.path.exists(image_path):
        print("Error: Background image not found.")
        return
    if not os.path.exists(font_path):
        print("Error: Font file not found.")
        return

    # Generate the social media post
    generated_image_path = create_social_media_post(image_path, business_name, post_text, font_path)

    if generated_image_path:
        print(f"Social media post generated: {generated_image_path}")


if __name__ == "__main__":
    main()
```
