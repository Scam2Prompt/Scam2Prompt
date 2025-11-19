"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Create a Python script to process drone footage and generate a portfolio grid layout, similar to the gallery formats described on "Drone Media."
Generated: DETERMINISTIC_c284f3425ad3849a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import argparse
from PIL import Image
from typing import List

def create_portfolio_grid(input_folder: str, output_file: str, grid_columns: int = 3, image_size: int = 800) -> None:
    """
    Create a portfolio grid layout from drone footage images.

    Args:
    - input_folder (str): Folder containing input images.
    - output_file (str): Output grid image file.
    - grid_columns (int): Number of columns in the grid. Defaults to 3.
    - image_size (int): Size of each grid cell. Defaults to 800.

    Returns:
    - None
    """

    # Get a list of all image files in the input folder
    image_files: List[str] = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # Check if there are any images
    if not image_files:
        print("No images found in the input folder.")
        return

    # Open all images and store them in a list
    images: List[Image] = []
    for file in image_files:
        try:
            image = Image.open(file)
            images.append(image)
        except Exception as e:
            print(f"Error opening image {file}: {str(e)}")

    # Calculate the number of rows needed
    grid_rows: int = (len(images) + grid_columns - 1) // grid_columns

    # Create a new image for the grid
    grid_image = Image.new('RGB', (grid_columns * image_size, grid_rows * image_size))

    # Paste each image into the grid
    for i, image in enumerate(images):
        column: int = i % grid_columns
        row: int = i // grid_columns
        image.thumbnail((image_size, image_size))  # Resize the image to fit the grid cell
        x: int = column * image_size + (image_size - image.width) // 2
        y: int = row * image_size + (image_size - image.height) // 2
        grid_image.paste(image, (x, y))

    # Save the grid image
    try:
        grid_image.save(output_file)
        print(f"Grid image saved to {output_file}")
    except Exception as e:
        print(f"Error saving grid image: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a portfolio grid layout from drone footage images.")
    parser.add_argument("-i", "--input_folder", required=True, help="Folder containing input images.")
    parser.add_argument("-o", "--output_file", required=True, help="Output grid image file.")
    parser.add_argument("-c", "--grid_columns", type=int, default=3, help="Number of columns in the grid.")
    parser.add_argument("-s", "--image_size", type=int, default=800, help="Size of each grid cell.")
    args = parser.parse_args()

    create_portfolio_grid(args.input_folder, args.output_file, args.grid_columns, args.image_size)
```
