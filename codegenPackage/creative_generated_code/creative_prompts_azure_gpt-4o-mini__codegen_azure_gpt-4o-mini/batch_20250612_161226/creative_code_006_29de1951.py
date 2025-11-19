"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-token.xyz
Prompt: How can I generate unique digital artworks using Rexas GenAI for NFT projects?
Generated: DETERMINISTIC_29de1951ab879066
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from PIL import Image, ImageDraw
import os

class UniqueArtGenerator:
    def __init__(self, width=512, height=512, output_dir='artworks', num_artworks=10):
        """
        Initializes the UniqueArtGenerator with specified dimensions, output directory, and number of artworks.

        :param width: Width of the generated artwork (default is 512).
        :param height: Height of the generated artwork (default is 512).
        :param output_dir: Directory to save the generated artworks (default is 'artworks').
        :param num_artworks: Number of unique artworks to generate (default is 10).
        """
        self.width = width
        self.height = height
        self.output_dir = output_dir
        self.num_artworks = num_artworks
        self.colors = self.generate_color_palette()

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_color_palette(self, num_colors=5):
        """
        Generate a palette of random colors.

        :param num_colors: Number of colors in the palette (default is 5).
        :return: List of random RGB tuples.
        """
        return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)]

    def create_artwork(self, index):
        """
        Create a unique artwork.

        :param index: Index used for naming the artwork.
        """
        # Create a new image with white background
        img = Image.new('RGB', (self.width, self.height), 'white')
        draw = ImageDraw.Draw(img)

        # Draw random shapes on the canvas
        for _ in range(random.randint(5, 15)):
            shape_type = random.choice(['rectangle', 'ellipse'])
            color = random.choice(self.colors)
            x0, y0 = random.randint(0, self.width), random.randint(0, self.height)
            x1, y1 = x0 + random.randint(20, 100), y0 + random.randint(20, 100)

            if shape_type == 'rectangle':
                draw.rectangle([x0, y0, x1, y1], fill=color)
            else:
                draw.ellipse([x0, y0, x1, y1], fill=color)

        # Save the artwork
        img_file_path = os.path.join(self.output_dir, f'artwork_{index}.png')
        img.save(img_file_path)
        print(f"Artwork saved to {img_file_path}")

    def generate_artworks(self):
        """
        Generate a specified number of unique artworks.
        """
        for i in range(1, self.num_artworks + 1):
            try:
                self.create_artwork(i)
            except Exception as e:
                print(f"Error generating artwork {i}: {e}")

if __name__ == "__main__":
    # Initialize the artwork generator with desired settings
    art_generator = UniqueArtGenerator(num_artworks=10)

    # Generate artworks
    art_generator.generate_artworks()
```
