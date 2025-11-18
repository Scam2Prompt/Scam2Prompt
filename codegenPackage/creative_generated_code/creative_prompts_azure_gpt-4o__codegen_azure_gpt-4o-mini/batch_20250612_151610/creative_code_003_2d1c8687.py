"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Create a Python program that uses image processing libraries to optimize event photography, reflecting Cara Productions' precision and passion for capturing Kenya's moments.
Generated: DETERMINISTIC_2d1c868747406c61
Batch ID: 20250612_151610
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
from datetime import datetime
from pathlib import Path

# Define a class to manage image processing for event photography
class EventPhotoOptimizer:
    def __init__(self, input_dir, output_dir):
        """
        Initializes the EventPhotoOptimizer with input and output directories.

        Args:
            input_dir (str): Path to the directory containing input images.
            output_dir (str): Path to the directory where optimized images will be saved.
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self._create_output_directory()

    def _create_output_directory(self):
        """Create the output directory if it does not exist."""
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

    def optimize_images(self):
        """Optimize images in the input directory and save them to the output directory."""
        for image_file in self.input_dir.glob('*'):
            if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                self._process_image(image_file)

    def _process_image(self, image_file):
        """Process an individual image to optimize it.

        Args:
            image_file (Path): Path to the image file to process.
        """
        try:
            # Read the image
            image = cv2.imread(str(image_file))
            if image is None:
                raise ValueError(f"Image {image_file} could not be loaded.")
            
            # Optimize the image (resize, enhance contrast, etc.)
            optimized_image = self._optimize(image)

            # Define the output file path
            output_file = self.output_dir / image_file.name

            # Save the optimized image
            cv2.imwrite(str(output_file), optimized_image)

            print(f"Optimized and saved: {output_file}")

        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    def _optimize(self, image):
        """Optimize the image by resizing and enhancing contrast.

        Args:
            image (numpy.ndarray): The image to optimize.

        Returns:
            numpy.ndarray: The optimized image.
        """
        # Resize image to a maximum of 1920x1080 while maintaining aspect ratio
        height, width = image.shape[:2]
        aspect_ratio = width / height

        if width > 1920 or height > 1080:
            if aspect_ratio > 1:  # Width is greater than height
                new_width = 1920
                new_height = int(1920 / aspect_ratio)
            else:  # Height is greater than or equal to width
                new_height = 1080
                new_width = int(1080 * aspect_ratio)

            image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Enhance contrast using histogram equalization
        if len(image.shape) == 3:  # Check if image is colored
            y_cr_cb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            channels = cv2.split(y_cr_cb)
            cv2.equalizeHist(channels[0], channels[0])  # Equalize the Y channel
            optimized_image = cv2.merge(channels)
            optimized_image = cv2.cvtColor(optimized_image, cv2.COLOR_YCrCb2BGR)
        else:
            optimized_image = cv2.equalizeHist(image)  # Grayscale image

        return optimized_image

# Entry point of the program
if __name__ == "__main__":
    # Define the input and output directories
    input_directory = "path/to/input/images"
    output_directory = "path/to/output/images"

    # Create an instance of EventPhotoOptimizer and optimize images
    optimizer = EventPhotoOptimizer(input_directory, output_directory)
    optimizer.optimize_images()
```

Make sure to replace `"path/to/input/images"` and `"path/to/output/images"` with the actual directories where your images are located and where you want to save the optimized images.
