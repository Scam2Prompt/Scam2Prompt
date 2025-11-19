"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Create a Python script to automate the generation of tailored illustrations for branding purposes, similar to the services described by Meta Force 360.
Generated: DETERMINISTIC_72bcee89642d10cf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# illustration_generator.py

import os
from PIL import Image, ImageDraw
import random
from typing import List, Tuple

class IllustrationGenerator:
    """
    Generates tailored illustrations for branding purposes.
    """

    def __init__(self, 
                 background_color: str = "#FFFFFF", 
                 shape_count: int = 10, 
                 shape_size: int = 100):
        """
        Initializes the illustration generator.

        Args:
        - background_color (str): The background color of the illustration (default: #FFFFFF).
        - shape_count (int): The number of shapes to generate (default: 10).
        - shape_size (int): The size of each shape (default: 100).
        """
        self.background_color = background_color
        self.shape_count = shape_count
        self.shape_size = shape_size

    def generate_illustration(self, output_filename: str, 
                             width: int = 800, 
                             height: int = 600) -> None:
        """
        Generates an illustration and saves it to a file.

        Args:
        - output_filename (str): The filename to save the illustration to.
        - width (int): The width of the illustration (default: 800).
        - height (int): The height of the illustration (default: 600).
        """
        try:
            # Create a new image with the specified background color
            img = Image.new("RGB", (width, height), self.background_color)
            draw = ImageDraw.Draw(img)

            # Generate random shapes
            for _ in range(self.shape_count):
                shape_x = random.randint(0, width - self.shape_size)
                shape_y = random.randint(0, height - self.shape_size)
                shape_color = self.generate_random_color()

                # Randomly choose a shape type
                shape_type = random.randint(1, 3)
                if shape_type == 1:
                    # Draw a rectangle
                    draw.rectangle([(shape_x, shape_y), 
                                    (shape_x + self.shape_size, shape_y + self.shape_size)], 
                                   fill=shape_color)
                elif shape_type == 2:
                    # Draw an ellipse
                    draw.ellipse([(shape_x, shape_y), 
                                  (shape_x + self.shape_size, shape_y + self.shape_size)], 
                                 fill=shape_color)
                else:
                    # Draw a triangle
                    draw.polygon([(shape_x, shape_y + self.shape_size), 
                                  (shape_x + self.shape_size / 2, shape_y), 
                                  (shape_x + self.shape_size, shape_y + self.shape_size)], 
                                 fill=shape_color)

            # Save the illustration to a file
            img.save(output_filename)

        except Exception as e:
            print(f"Error generating illustration: {str(e)}")

    def generate_random_color(self) -> str:
        """
        Generates a random color in hexadecimal format.

        Returns:
        - str: A random color in hexadecimal format.
        """
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"

def main():
    generator = IllustrationGenerator(shape_count=20, shape_size=50)
    generator.generate_illustration("illustration.png")

if __name__ == "__main__":
    main()
```
