"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: How can Rexas GenAI assist artists in generating digital artworks for NFTs?
Generated: DETERMINISTIC_def056e730111ef6
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
from PIL import Image, ImageDraw, ImageFont

class ArtGenerator:
    """
    A class to generate digital artworks for NFTs using random shapes and colors.
    """
    
    def __init__(self, output_directory):
        """
        Initializes the ArtGenerator with the given output directory.
        
        Parameters:
            output_directory (str): The directory where generated artworks will be saved.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def generate_artwork(self, width=800, height=800, num_shapes=10):
        """
        Generates an artwork consisting of random shapes and colors.

        Parameters:
            width (int): Width of the artwork.
            height (int): Height of the artwork.
            num_shapes (int): Number of shapes to draw on the artwork.

        Returns:
            str: File path of the saved artwork.
        """
        try:
            # Create a blank image with a white background
            artwork = Image.new("RGB", (width, height), "white")
            draw = ImageDraw.Draw(artwork)

            # Draw random shapes
            for _ in range(num_shapes):
                shape_type = random.choice(['rectangle', 'circle'])
                color = self._random_color()
                coordinates = self._random_coordinates(width, height)

                if shape_type == 'rectangle':
                    draw.rectangle(coordinates, fill=color)
                else:
                    draw.ellipse(coordinates, fill=color)

            # Save the artwork to the specified directory
            file_path = os.path.join(self.output_directory, f'artwork_{random.randint(1000, 9999)}.png')
            artwork.save(file_path)
            return file_path

        except Exception as e:
            print(f"An error occurred while generating artwork: {e}")
            return None

    def _random_color(self):
        """
        Generates a random color.

        Returns:
            tuple: A tuple representing an RGB color.
        """
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def _random_coordinates(self, width, height):
        """
        Generates random coordinates for drawing shapes.

        Parameters:
            width (int): Width of the artwork.
            height (int): Height of the artwork.

        Returns:
            tuple: A tuple containing the coordinates for the shape.
        """
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))


if __name__ == "__main__":
    # Example of how to use the ArtGenerator class
    output_dir = "generated_artworks"
    art_generator = ArtGenerator(output_directory=output_dir)
    
    # Generate an artwork
    artwork_path = art_generator.generate_artwork(num_shapes=15)
    
    if artwork_path:
        print(f"Artwork generated and saved at: {artwork_path}")
    else:
        print("Failed to generate artwork.")
```
