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
import math
from PIL import Image, ImageDraw
import argparse
import os
import sys
from datetime import datetime

class DigitalArtGenerator:
    """
    A class to generate unique digital art pieces inspired by the 'Chum Generator 3000' concept.
    """

    def __init__(self, width=800, height=800, output_dir='output'):
        """
        Initialize the art generator with specified dimensions and output directory.
        
        Args:
            width (int): Width of the generated image in pixels. Default: 800.
            height (int): Height of the generated image in pixels. Default: 800.
            output_dir (str): Directory to save generated images. Default: 'output'.
        """
        self.width = width
        self.height = height
        self.output_dir = output_dir
        self._ensure_output_dir_exists()

    def _ensure_output_dir_exists(self):
        """Create output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            print(f"Error creating output directory: {e}", file=sys.stderr)
            raise

    def _generate_random_color(self):
        """Generate a random RGB color."""
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def _generate_art_piece(self):
        """
        Generate a unique digital art piece.
        
        Returns:
            PIL.Image: The generated image object.
        """
        # Create a blank canvas
        image = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(image)

        # Generate random shapes and patterns
        for _ in range(random.randint(5, 20)):
            shape_type = random.choice(["rectangle", "ellipse", "line", "polygon"])

            color = self._generate_random_color()
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)

            if shape_type == "rectangle":
                draw.rectangle([x1, y1, x2, y2], fill=color, outline="black")
            elif shape_type == "ellipse":
                draw.ellipse([x1, y1, x2, y2], fill=color, outline="black")
            elif shape_type == "line":
                draw.line([x1, y1, x2, y2], fill=color, width=random.randint(1, 5))
            elif shape_type == "polygon":
                points = [
                    (random.randint(0, self.width), random.randint(0, self.height))
                    for _ in range(random.randint(3, 6))
                ]
                draw.polygon(points, fill=color, outline="black")

        # Add some random noise for texture
        for _ in range(1000):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            draw.point((x, y), fill=self._generate_random_color())

        return image

    def generate_and_save(self, filename=None):
        """
        Generate an art piece and save it to a file.
        
        Args:
            filename (str): Optional custom filename. If None, a timestamp will be used.
        
        Returns:
            str: Path to the saved image file.
        """
        try:
            art = self._generate_art_piece()
            
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"art_{timestamp}.png"
            
            filepath = os.path.join(self.output_dir, filename)
            art.save(filepath)
            return filepath
        except Exception as e:
            print(f"Error generating or saving art: {e}", file=sys.stderr)
            raise

def main():
    """Command-line interface for the Digital Art Generator."""
    parser = argparse.ArgumentParser(description="Generate unique digital art pieces.")
    parser.add_argument("--width", type=int, default=800, help="Width of the image")
    parser.add_argument("--height", type=int, default=800, help="Height of the image")
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--filename", type=str, default=None, help="Custom filename (optional)")
    
    args = parser.parse_args()
    
    try:
        generator = DigitalArtGenerator(
            width=args.width,
            height=args.height,
            output_dir=args.output
        )
        saved_path = generator.generate_and_save(args.filename)
        print(f"Art piece generated and saved to: {saved_path}")
    except Exception as e:
        print(f"Failed to generate art: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
