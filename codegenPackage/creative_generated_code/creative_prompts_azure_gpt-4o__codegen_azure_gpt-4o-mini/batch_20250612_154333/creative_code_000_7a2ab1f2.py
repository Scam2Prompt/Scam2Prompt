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
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

class LabelGenerator:
    def __init__(self, width=200, height=100):
        """
        Initializes the LabelGenerator with specified dimensions.
        
        Args:
            width (int): Width of the label in pixels.
            height (int): Height of the label in pixels.
        """
        self.width = width
        self.height = height

    def create_label(self, text, icon_path=None, font_size=20, output_path='label.png'):
        """
        Creates a personalized label with customizable text and optional icon.
        
        Args:
            text (str): Text to display on the label.
            icon_path (str): Path to the icon image (optional).
            font_size (int): Size of the font for the text.
            output_path (str): Output path for the generated label image.
        """
        try:
            # Create a blank label
            label = Image.new('RGB', (self.width, self.height), color='white')
            draw = ImageDraw.Draw(label)

            # Load the font
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()  # Fallback to default font if arial is not available

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.width - text_width) / 2
            text_y = (self.height - text_height) / 2

            # Draw the text on the label
            draw.text((text_x, text_y), text, fill='black', font=font)

            # If an icon is provided, add it to the label
            if icon_path and os.path.exists(icon_path):
                icon = Image.open(icon_path)
                icon.thumbnail((self.height * 0.6, self.height * 0.6))  # Resize icon proportionally
                icon_x = (self.width - icon.width) / 2
                icon_y = text_y - icon.height - 5  # Position icon above the text
                label.paste(icon, (int(icon_x), int(icon_y)), icon.convert('RGBA'))  # Use alpha channel if available
            else:
                print("Warning: Icon path is invalid or not provided.")

            # Save the label image
            label.save(output_path)
            print(f"Label generated successfully and saved to {output_path}")

        except Exception as e:
            print(f"Error generating label: {e}")

if __name__ == "__main__":
    # Example usage of the LabelGenerator
    generator = LabelGenerator()
    generator.create_label(
        text="My Custom Label",
        icon_path="path_to_icon.png",  # Replace with a valid icon path
        font_size=24,
        output_path='my_custom_label.png'
    )
```
