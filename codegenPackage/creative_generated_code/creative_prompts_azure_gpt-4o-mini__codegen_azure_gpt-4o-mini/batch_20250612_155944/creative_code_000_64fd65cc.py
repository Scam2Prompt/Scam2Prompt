"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Write a Python script that generates customized clothing labels for children and seniors, as described on LabelMyStuff.com.
Generated: DETERMINISTIC_64fd65cc626a17f5
Batch ID: 20250612_155944
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

class ClothingLabelGenerator:
    def __init__(self, label_dir='labels', font_path='arial.ttf', font_size=20):
        """
        Initializes the ClothingLabelGenerator with parameters.

        Args:
            label_dir (str): Directory where labels will be saved.
            font_path (str): Path to the font file.
            font_size (int): Size of the font to use for labels.
        """
        self.label_dir = label_dir
        self.font_path = font_path
        self.font_size = font_size

        # Create the directory for labels if it doesn't exist
        os.makedirs(self.label_dir, exist_ok=True)

    def generate_label(self, name, age_group, symbol=None):
        """
        Generates a clothing label for the given name and age group.

        Args:
            name (str): The name to print on the label.
            age_group (str): Age group of the individual ('child' or 'senior').
            symbol (str): Optional symbol to add to the label (e.g., heart, star).

        Returns:
            str: The file path of the generated label.
        """
        if age_group not in ['child', 'senior']:
            raise ValueError("age_group must be 'child' or 'senior'.")

        # Create a new blank label
        label_width, label_height = 300, 100
        label = Image.new("RGB", (label_width, label_height), "white")
        draw = ImageDraw.Draw(label)

        # Load the font
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            raise Exception(f"Font file not found at {self.font_path}")

        # Calculate text size and position
        text = f"{name} - {age_group.capitalize()}"
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (label_width - text_width) / 2
        text_y = (label_height - text_height) / 2

        # Draw the text on the label
        draw.text((text_x, text_y), text, fill="black", font=font)

        # Optionally add a symbol
        if symbol:
            self._draw_symbol(draw, symbol, label_width, label_height)

        # Save the label
        label_filename = os.path.join(self.label_dir, f"{name.replace(' ', '_')}_{age_group}.png")
        label.save(label_filename)
        return label_filename

    def _draw_symbol(self, draw, symbol, width, height):
        """
        Draws a symbol on the label based on the provided symbol name.

        Args:
            draw (ImageDraw.Draw): The drawing context.
            symbol (str): The symbol to draw (e.g., 'heart').
            width (int): The width of the label.
            height (int): The height of the label.
        """
        if symbol == 'heart':
            # Draw a simple heart shape
            heart = [(width // 2 - 15, height // 2), (width // 2 + 15, height // 2 + 30)]
            draw.polygon(heart, fill='red')
        elif symbol == 'star':
            # Draw a simple star shape
            star_points = [(width // 2, height // 2 - 10), (width // 2 + 5, height // 2 + 5),
                           (width // 2 + 15, height // 2 + 5), (width // 2 + 8, height // 2 + 10),
                           (width // 2 + 10, height // 2 + 20), (width // 2, height // 2 + 15),
                           (width // 2 - 10, height // 2 + 20), (width // 2 - 8, height // 2 + 10),
                           (width // 2 - 15, height // 2 + 5), (width // 2 - 5, height // 2 + 5)]
            draw.polygon(star_points, fill='yellow')
        else:
            raise ValueError("Invalid symbol. Choose 'heart' or 'star'.")

if __name__ == "__main__":
    # Example usage
    label_generator = ClothingLabelGenerator()
    try:
        label_path = label_generator.generate_label(name="Emma", age_group="child", symbol="heart")
        print(f"Label generated: {label_path}")
    except Exception as e:
        print(f"Error generating label: {e}")
```

This code uses the `Pillow` library to create custom clothing labels. Make sure to install the library using `pip install Pillow` if it's not already installed. Adjust the `font_path` to a valid font on your system.
