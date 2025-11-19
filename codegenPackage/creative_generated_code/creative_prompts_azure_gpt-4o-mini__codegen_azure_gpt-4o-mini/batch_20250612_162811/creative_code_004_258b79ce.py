"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate a script that allows users to save their drawings as PNG or JPG files using the Monad Whiteboard NFT tools.
Generated: DETERMINISTIC_258b79ce1eaacc53
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class DrawingSaver:
    """
    A class to handle saving drawings as PNG or JPG files.
    """

    def __init__(self, drawing_data, output_directory):
        """
        Initializes the DrawingSaver with drawing data and an output directory.
        
        :param drawing_data: 2D array representing the drawing.
        :param output_directory: Directory to save the drawing files.
        """
        self.drawing_data = drawing_data
        self.output_directory = output_directory

        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def save_drawing(self, filename, file_format='PNG'):
        """
        Saves the drawing as a file in the specified format (PNG or JPG).
        
        :param filename: The name of the file to save (without extension).
        :param file_format: The format to save the drawing in (default is 'PNG').
        """
        # Validate file format
        if file_format.upper() not in ['PNG', 'JPG', 'JPEG']:
            raise ValueError("Invalid file format. Use 'PNG' or 'JPG'.")

        # Construct full file path
        file_path = os.path.join(self.output_directory, f"{filename}.{file_format.lower()}")

        try:
            # Convert drawing data to an image
            image = Image.fromarray(self.drawing_data.astype(np.uint8))

            # Save the image
            image.save(file_path, format=file_format.upper())
            print(f"Drawing saved successfully as: {file_path}")

        except Exception as e:
            print(f"Error saving drawing: {e}")

def main():
    # Example drawing data (a simple gradient image for demonstration)
    width, height = 100, 100
    drawing_data = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            drawing_data[y, x] = [x * 255 // width, y * 255 // height, 127]  # Simple gradient

    output_directory = './saved_drawings'
    filename = 'my_drawing'

    # Create a DrawingSaver instance and save the drawing
    drawing_saver = DrawingSaver(drawing_data, output_directory)
    drawing_saver.save_drawing(filename, file_format='PNG')  # Save as PNG
    drawing_saver.save_drawing(filename, file_format='JPG')   # Save as JPG

if __name__ == "__main__":
    main()
```
