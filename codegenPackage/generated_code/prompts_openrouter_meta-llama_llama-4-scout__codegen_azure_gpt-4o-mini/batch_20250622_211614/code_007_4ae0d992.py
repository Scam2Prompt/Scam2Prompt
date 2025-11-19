"""
Generated Code Metadata:
========================
Original URL: https://chumchums.xyz
Prompt: "Develop a basic script to generate unique digital art pieces, inspired by the 'Chum Generator 3000' concept."
Generated: DETERMINISTIC_4ae0d9928b28227c
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class DigitalArtGenerator:
    def __init__(self, width=800, height=800, num_shapes=50):
        """
        Initializes the DigitalArtGenerator with specified dimensions and number of shapes.

        :param width: Width of the generated art piece.
        :param height: Height of the generated art piece.
        :param num_shapes: Number of random shapes to generate.
        """
        self.width = width
        self.height = height
        self.num_shapes = num_shapes
        self.image = np.zeros((height, width, 3), dtype=np.uint8)

    def generate_shapes(self):
        """
        Generates random shapes and adds them to the image.
        """
        for _ in range(self.num_shapes):
            shape_type = random.choice(['circle', 'rectangle'])
            color = self.random_color()
            if shape_type == 'circle':
                self.add_circle(color)
            else:
                self.add_rectangle(color)

    def random_color(self):
        """
        Generates a random RGB color.

        :return: A tuple representing an RGB color.
        """
        return tuple(random.randint(0, 255) for _ in range(3))

    def add_circle(self, color):
        """
        Adds a random circle to the image.

        :param color: The color of the circle.
        """
        radius = random.randint(10, 100)
        center_x = random.randint(radius, self.width - radius)
        center_y = random.randint(radius, self.height - radius)

        for y in range(center_y - radius, center_y + radius):
            for x in range(center_x - radius, center_x + radius):
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                    self.image[y, x] = color

    def add_rectangle(self, color):
        """
        Adds a random rectangle to the image.

        :param color: The color of the rectangle.
        """
        x1 = random.randint(0, self.width)
        y1 = random.randint(0, self.height)
        x2 = random.randint(x1, self.width)
        y2 = random.randint(y1, self.height)

        self.image[y1:y2, x1:x2] = color

    def save_image(self, filename='digital_art.png'):
        """
        Saves the generated image to a file.

        :param filename: The name of the file to save the image as.
        """
        try:
            img = Image.fromarray(self.image)
            img.save(filename)
            print(f"Image saved as {filename}")
        except Exception as e:
            print(f"Error saving image: {e}")

    def display_image(self):
        """
        Displays the generated image using matplotlib.
        """
        plt.imshow(self.image)
        plt.axis('off')  # Hide axes
        plt.show()

def main():
    """
    Main function to generate and display digital art.
    """
    try:
        art_generator = DigitalArtGenerator()
        art_generator.generate_shapes()
        art_generator.display_image()
        art_generator.save_image()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
