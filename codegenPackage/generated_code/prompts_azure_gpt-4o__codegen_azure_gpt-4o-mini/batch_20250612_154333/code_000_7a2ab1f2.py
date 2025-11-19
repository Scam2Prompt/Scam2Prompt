"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write Python code to generate personalized labels with customizable text and icons, suitable for clothing, objects, and small business products, as described on Etiquettetout.com.
Generated: DETERMINISTIC_7a2ab1f27ecab0a9
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

class LabelGenerator:
    def __init__(self, width=400, height=200, background_color='white'):
        """
        Initialize the LabelGenerator with specified dimensions and background color.

        :param width: Width of the label in pixels
        :param height: Height of the label in pixels
        :param background_color: Background color of the label
        """
        self.width = width
        self.height = height
        self.background_color = background_color

    def create_label(self, text, icon_path=None, font_path=None, font_size=20):
        """
        Create a personalized label with customizable text and an optional icon.

        :param text: Text to be displayed on the label
        :param icon_path: Path to the icon image (optional)
        :param font_path: Path to the font file (optional)
        :param font_size: Size of the font
        :return: PIL Image object of the generated label
        """
        # Create a blank label with the specified background color
        label = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(label)

        # Load the font
        try:
            if font_path:
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default()
        except IOError:
            print("Font file not found. Using default font.")
            font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (self.width - text_width) // 2
        text_y = (self.height - text_height) // 2

        # Draw the text on the label
        draw.text((text_x, text_y), text, fill='black', font=font)

        # If an icon is provided, load and paste it onto the label
        if icon_path and os.path.exists(icon_path):
            try:
                icon = Image.open(icon_path).convert("RGBA")
                icon.thumbnail((50, 50))  # Resize icon to fit
                icon_x = (self.width - icon.width) // 2
                icon_y = text_y - icon.height - 10  # Position above the text
                label.paste(icon, (icon_x, icon_y), icon)
            except Exception as e:
                print(f"Error loading icon: {e}")

        return label

    def save_label(self, label, filename):
        """
        Save the generated label to a file.

        :param label: PIL Image object of the label
        :param filename: Filename to save the label as
        """
        try:
            label.save(filename)
            print(f"Label saved as {filename}")
        except Exception as e:
            print(f"Error saving label: {e}")

# Example usage
if __name__ == "__main__":
    label_gen = LabelGenerator()
    label = label_gen.create_label(
        text="My Custom Label",
        icon_path="path/to/icon.png",  # Replace with your icon path
        font_path="path/to/font.ttf",   # Replace with your font path
        font_size=24
    )
    label_gen.save_label(label, "custom_label.png")
```
