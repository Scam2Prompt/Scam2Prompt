"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Write a Python script to automate the generation of business card designs using digital offset printing, considering various card sizes and layouts offered by Ram Digi Medias Pvt Ltd."
Generated: DETERMINISTIC_8fda21690c382842
Batch ID: 20250622_204729
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

# Constants for card sizes and layouts offered by Ram Digi Medias Pvt Ltd
CARD_SIZES = {
    "standard": (3.5 * 300, 2 * 300),  # 3.5x2 inches at 300 DPI
    "square": (2.5 * 300, 2.5 * 300),  # 2.5x2.5 inches at 300 DPI
    "mini": (3 * 300, 1.5 * 300)       # 3x1.5 inches at 300 DPI
}

LAYOUTS = ["simple", "modern", "creative"]

# Directory to save generated designs
OUTPUT_DIR = "business_cards"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_business_card(name, title, company, phone, email, size="standard", layout="simple"):
    """
    Generates a business card design based on the provided details.

    Args:
        name (str): Name of the individual.
        title (str): Job title of the individual.
        company (str): Company name.
        phone (str): Phone number.
        email (str): Email address.
        size (str): Card size (standard, square, mini).
        layout (str): Layout style (simple, modern, creative).

    Returns:
        str: Path to the generated business card image.
    """
    # Validate size and layout
    if size not in CARD_SIZES:
        raise ValueError(f"Invalid size '{size}'. Available sizes: {', '.join(CARD_SIZES.keys())}")
    if layout not in LAYOUTS:
        raise ValueError(f"Invalid layout '{layout}'. Available layouts: {', '.join(LAYOUTS)}")

    # Get card dimensions
    width, height = CARD_SIZES[size]

    # Create a blank image for the card
    card = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(card)

    # Load a font (ensure the font file exists in the working directory)
    try:
        font_large = ImageFont.truetype("arial.ttf", 40)
        font_medium = ImageFont.truetype("arial.ttf", 30)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        raise FileNotFoundError("Font file 'arial.ttf' not found. Please ensure it is available.")

    # Draw content based on layout
    if layout == "simple":
        # Simple layout: Centered text
        draw.text((width // 2, height // 4), name, font=font_large, fill="black", anchor="mm")
        draw.text((width // 2, height // 2), title, font=font_medium, fill="gray", anchor="mm")
        draw.text((width // 2, height * 3 // 4), f"{company}\n{phone}\n{email}", font=font_small, fill="black", anchor="mm")
    elif layout == "modern":
        # Modern layout: Left-aligned text with a colored background
        draw.rectangle([(0, 0), (width // 3, height)], fill="lightblue")
        draw.text((20, height // 4), name, font=font_large, fill="black")
        draw.text((20, height // 2), title, font=font_medium, fill="gray")
        draw.text((20, height * 3 // 4), f"{company}\n{phone}\n{email}", font=font_small, fill="black")
    elif layout == "creative":
        # Creative layout: Diagonal text with a gradient background
        for i in range(height):
            color = (255 - i // 2, 255 - i // 3, 255 - i // 4)
            draw.line([(0, i), (width, i)], fill=color)
        draw.text((width // 4, height // 4), name, font=font_large, fill="black", anchor="mm")
        draw.text((width // 4, height // 2), title, font=font_medium, fill="black", anchor="mm")
        draw.text((width // 4, height * 3 // 4), f"{company}\n{phone}\n{email}", font=font_small, fill="black", anchor="mm")

    # Save the card to the output directory
    file_name = f"{name.replace(' ', '_')}_{layout}_{size}.png"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    card.save(file_path)

    return file_path

if __name__ == "__main__":
    # Example usage
    try:
        card_path = generate_business_card(
            name="John Doe",
            title="Software Engineer",
            company="Ram Digi Medias Pvt Ltd",
            phone="+1-234-567-890",
            email="john.doe@example.com",
            size="standard",
            layout="modern"
        )
        print(f"Business card generated: {card_path}")
    except Exception as e:
        print(f"Error: {e}")
```
