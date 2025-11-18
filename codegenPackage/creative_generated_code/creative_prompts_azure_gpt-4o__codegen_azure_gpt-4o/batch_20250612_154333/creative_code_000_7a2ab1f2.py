"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Write Python code to generate personalized labels with customizable text and icons, suitable for clothing, objects, and small business products, as described on Etiquettetout.com.
Generated: DETERMINISTIC_7a2ab1f27ecab0a9
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

def create_personalized_label(text, icon_path, output_path, label_size=(300, 100), font_path=None, font_size=24):
    """
    Generate personalized labels with customizable text and icons.

    Args:
        text (str): The text to be displayed on the label.
        icon_path (str): Path to the icon image to include on the label.
        output_path (str): Path to save the generated label image.
        label_size (tuple): Dimensions of the label (width, height). Default is (300, 100).
        font_path (str): Path to the font file. If None, a default PIL font will be used.
        font_size (int): Size of the font for the label text. Default is 24.
    
    Returns:
        None: Saves the label as an image at the specified output path.
    """
    try:
        # Create a blank label
        label = Image.new("RGBA", label_size, "white")
        draw = ImageDraw.Draw(label)

        # Load and position the icon
        if icon_path and os.path.exists(icon_path):
            icon = Image.open(icon_path).convert("RGBA")
            icon_size = (int(label_size[1] * 0.8), int(label_size[1] * 0.8))  # Scale icon to fit label height
            icon = icon.resize(icon_size, Image.ANTIALIAS)
            icon_position = (10, (label_size[1] - icon_size[1]) // 2)  # Align left with padding
            label.paste(icon, icon_position, icon)
        else:
            raise FileNotFoundError(f"Icon file not found: {icon_path}")

        # Load the font
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()  # Use default font if no custom font is provided

        # Calculate text position
        text_position = (icon_position[0] + icon_size[0] + 10, (label_size[1] - font_size) // 2)  # Next to the icon
        draw.text(text_position, text, fill="black", font=font)

        # Save the label
        label.save(output_path, "PNG")
        print(f"Label saved to {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage of the function
if __name__ == "__main__":
    create_personalized_label(
        text="Custom Label",
        icon_path="icon.png",  # Replace with the path to your icon file
        output_path="label.png",  # Replace with the desired output file path
        label_size=(300, 100),
        font_path=None,  # Replace with the path to your font file
        font_size=24
    )
```
