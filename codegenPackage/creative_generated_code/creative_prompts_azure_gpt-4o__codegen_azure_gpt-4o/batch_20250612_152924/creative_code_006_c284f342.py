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
import cv2  # OpenCV for image processing
from PIL import Image
from pathlib import Path
import numpy as np

def create_portfolio_grid(input_folder, output_file, thumbnail_size=(200, 200), grid_size=(4, 4)):
    """
    Process drone footage images and generate a portfolio grid layout.
    
    Args:
        input_folder (str): Path to the folder containing drone footage images.
        output_file (str): Path to save the generated portfolio grid layout.
        thumbnail_size (tuple): Size of thumbnails to be used in the grid (width, height).
        grid_size (tuple): Size of the grid (columns, rows).
    """
    try:
        # Validate input folder
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")
        
        # Gather image files from the input folder
        image_files = [f for f in Path(input_folder).glob("*.jpg") if f.is_file()]
        if len(image_files) == 0:
            raise ValueError("No valid image files found in the input folder.")

        # Create thumbnails and store them in a list
        thumbnails = []
        for img_file in image_files[:grid_size[0] * grid_size[1]]:  # Limit to grid size
            # Read image using OpenCV
            img = cv2.imread(str(img_file))
            if img is None:
                print(f"Warning: Unable to read image '{img_file}'. Skipping.")
                continue
            
            # Resize image to thumbnail size
            img_thumbnail = cv2.resize(img, thumbnail_size, interpolation=cv2.INTER_AREA)
            thumbnails.append(img_thumbnail)
        
        # Validate enough images for the grid
        if len(thumbnails) < grid_size[0] * grid_size[1]:
            raise ValueError(f"Not enough images ({len(thumbnails)}) to fill the grid size {grid_size}.")
        
        # Create blank canvas for the grid layout
        grid_width = grid_size[0] * thumbnail_size[0]
        grid_height = grid_size[1] * thumbnail_size[1]
        grid_canvas = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)
        
        # Place thumbnails into the canvas
        for idx, thumbnail in enumerate(thumbnails):
            row = idx // grid_size[0]
            col = idx % grid_size[0]
            start_y = row * thumbnail_size[1]
            start_x = col * thumbnail_size[0]
            grid_canvas[start_y:start_y + thumbnail_size[1], start_x:start_x + thumbnail_size[0]] = thumbnail
        
        # Save the portfolio grid layout as an image
        cv2.imwrite(output_file, grid_canvas)
        print(f"Portfolio grid layout saved successfully to '{output_file}'.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_folder_path = "drone_images"  # Replace with your input folder containing images
    output_file_path = "portfolio_grid.jpg"  # Replace with your desired output file name
    create_portfolio_grid(input_folder_path, output_file_path)
```
