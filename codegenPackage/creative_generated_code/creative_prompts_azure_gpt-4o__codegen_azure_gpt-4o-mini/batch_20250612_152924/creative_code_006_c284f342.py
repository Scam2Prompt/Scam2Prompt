"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Create a Python script to process drone footage and generate a portfolio grid layout, similar to the gallery formats described on "Drone Media."
Generated: DETERMINISTIC_c284f3425ad3849a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

class DronePortfolio:
    def __init__(self, input_folder, output_image, grid_size=(3, 3), thumbnail_size=(150, 150)):
        """
        Initialize the DronePortfolio with input parameters.

        :param input_folder: Path to the folder containing drone footage images.
        :param output_image: Path where the portfolio grid image will be saved.
        :param grid_size: Tuple representing the grid layout (rows, columns).
        :param thumbnail_size: Tuple representing the size of each thumbnail in the grid.
        """
        self.input_folder = Path(input_folder)
        self.output_image = output_image
        self.grid_size = grid_size
        self.thumbnail_size = thumbnail_size
        self.images = []

        # Validate input folder
        if not self.input_folder.is_dir():
            raise ValueError(f"Input folder '{self.input_folder}' is not a valid directory.")
        
        # Load images from the input folder
        self.load_images()

    def load_images(self):
        """Load images from the input directory and store them in the images list."""
        for image_file in self.input_folder.glob('*.jpg'):
            try:
                img = Image.open(image_file)
                img.thumbnail(self.thumbnail_size)
                self.images.append(img)
            except Exception as e:
                print(f"Error loading image {image_file}: {e}")

    def create_grid(self):
        """Create a grid layout image from the loaded images."""
        if not self.images:
            raise ValueError("No images loaded. Please check the input folder.")

        rows, cols = self.grid_size
        grid_image = Image.new('RGB', (cols * self.thumbnail_size[0], rows * self.thumbnail_size[1]))

        for idx, img in enumerate(self.images[:rows * cols]):
            x = (idx % cols) * self.thumbnail_size[0]
            y = (idx // cols) * self.thumbnail_size[1]
            grid_image.paste(img, (x, y))

        return grid_image

    def save_grid(self):
        """Save the portfolio grid image to the specified output path."""
        grid_image = self.create_grid()
        try:
            grid_image.save(self.output_image)
            print(f"Portfolio grid saved to '{self.output_image}'.")
        except Exception as e:
            print(f"Error saving the grid image: {e}")

if __name__ == "__main__":
    # Define input folder, output file and grid layout
    input_folder = "path/to/drone/images"  # Change this to your input folder
    output_image = "portfolio_grid.jpg"     # Output file name
    
    try:
        # Create a DronePortfolio instance and save the grid
        portfolio = DronePortfolio(input_folder, output_image)
        portfolio.save_grid()
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Make sure to replace `"path/to/drone/images"` with the actual path where your drone images are stored. The script expects the images to be in JPEG format. Adjust the `input_folder` and `output_image` variables as needed before running the code.
