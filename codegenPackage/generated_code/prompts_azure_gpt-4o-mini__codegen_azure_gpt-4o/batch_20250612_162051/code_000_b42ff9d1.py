"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: Generate a Python script to create custom metallic logo stickers using the specifications provided by Jttlogos, including options for Nickel Metal and Stainless Steel materials.
Generated: DETERMINISTIC_b42ff9d1cf75b158
Batch ID: 20250612_162051
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

# Constants for materials
MATERIALS = {
    "Nickel Metal": {"color": (192, 192, 192), "texture": "nickel_texture.png"},
    "Stainless Steel": {"color": (224, 224, 224), "texture": "stainless_texture.png"}
}

# Default logo specifications
DEFAULT_SPECIFICATIONS = {
    "width": 500,  # Width of the sticker in pixels
    "height": 200,  # Height of the sticker in pixels
    "font_size": 50,  # Font size for the logo text
    "font_path": "arial.ttf",  # Path to the font file
    "output_dir": "output_stickers"  # Directory to save the stickers
}

def create_logo_sticker(text, material, specifications=DEFAULT_SPECIFICATIONS):
    """
    Creates a custom metallic logo sticker.

    Args:
        text (str): The text to display on the sticker.
        material (str): The material type ("Nickel Metal" or "Stainless Steel").
        specifications (dict): Custom specifications for the sticker.

    Raises:
        ValueError: If the material is not supported.
        FileNotFoundError: If the font file or texture file is missing.
    """
    # Validate material
    if material not in MATERIALS:
        raise ValueError(f"Unsupported material: {material}. Supported materials are: {list(MATERIALS.keys())}")

    # Extract material properties
    material_properties = MATERIALS[material]
    background_color = material_properties["color"]
    texture_file = material_properties["texture"]

    # Validate texture file
    if not os.path.exists(texture_file):
        raise FileNotFoundError(f"Texture file not found: {texture_file}")

    # Validate font file
    font_path = specifications.get("font_path", DEFAULT_SPECIFICATIONS["font_path"])
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")

    # Create output directory if it doesn't exist
    output_dir = specifications.get("output_dir", DEFAULT_SPECIFICATIONS["output_dir"])
    os.makedirs(output_dir, exist_ok=True)

    # Create a blank image with the specified dimensions
    width = specifications.get("width", DEFAULT_SPECIFICATIONS["width"])
    height = specifications.get("height", DEFAULT_SPECIFICATIONS["height"])
    image = Image.new("RGB", (width, height), background_color)

    # Apply texture
    texture = Image.open(texture_file).resize((width, height))
    image.paste(texture, (0, 0), texture)

    # Draw the logo text
    draw = ImageDraw.Draw(image)
    font_size = specifications.get("font_size", DEFAULT_SPECIFICATIONS["font_size"])
    font = ImageFont.truetype(font_path, font_size)

    # Center the text
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, fill="black", font=font)

    # Save the sticker
    output_file = os.path.join(output_dir, f"{text}_{material.replace(' ', '_')}.png")
    image.save(output_file)
    print(f"Sticker saved: {output_file}")


if __name__ == "__main__":
    # Example usage
    try:
        create_logo_sticker(
            text="Jttlogos",
            material="Nickel Metal",
            specifications={
                "width": 600,
                "height": 300,
                "font_size": 60,
                "font_path": "arial.ttf",
                "output_dir": "custom_stickers"
            }
        )
    except Exception as e:
        print(f"Error: {e}")
```
