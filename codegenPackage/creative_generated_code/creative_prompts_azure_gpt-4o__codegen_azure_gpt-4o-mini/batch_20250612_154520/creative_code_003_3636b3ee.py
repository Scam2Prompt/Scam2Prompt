"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pics3dstudio.com
Prompt: Provide a Python script for creating interactive 360-degree panoramic views of architectural spaces, as seen in PICS3DStudio's "Nizuc Office 2024" project.
Generated: DETERMINISTIC_3636b3eea7d0e21a
Batch ID: 20250612_154520
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
from glob import glob
from matplotlib import pyplot as plt

class PanoramicViewGenerator:
    def __init__(self, images_folder, output_file='panorama.jpg'):
        """
        Initializes the PanoramicViewGenerator with the images folder and output file name.

        Args:
            images_folder (str): Path to the folder containing images for the panorama.
            output_file (str): Name of the output file for the panoramic image.
        """
        self.images_folder = images_folder
        self.output_file = output_file
        self.images = []

    def load_images(self):
        """
        Loads images from the specified folder, ensuring they are in the correct order.

        Raises:
            RuntimeError: If no images are found in the specified folder.
        """
        image_paths = sorted(glob(os.path.join(self.images_folder, '*.jpg')))
        if not image_paths:
            raise RuntimeError("No images found in the specified folder.")
        
        self.images = [cv2.imread(img_path) for img_path in image_paths]
        if not self.images:
            raise RuntimeError("Failed to load images.")

    def stitch_images(self):
        """
        Stitches the loaded images into a single panoramic image.

        Returns:
            np.ndarray: The resulting panorama image.

        Raises:
            RuntimeError: If stitching fails.
        """
        # Create a stitcher object
        stitcher = cv2.Stitcher_create()
        status, panorama = stitcher.stitch(self.images)
        
        if status != cv2.Stitcher_OK:
            raise RuntimeError("Stitching failed with error code: {}".format(status))
        
        return panorama

    def save_panorama(self, panorama):
        """
        Saves the generated panorama image to the specified output file.

        Args:
            panorama (np.ndarray): The panorama image to save.
        """
        cv2.imwrite(self.output_file, panorama)
        print(f"Panorama saved as {self.output_file}")

    def display_panorama(self, panorama):
        """
        Displays the generated panorama using matplotlib.

        Args:
            panorama (np.ndarray): The panorama image to display.
        """
        plt.imshow(cv2.cvtColor(panorama, cv2.COLOR_BGR2RGB))
        plt.axis('off')  # Hide axes
        plt.show()

    def process(self):
        """
        Main process to load images, stitch them, save and display the result.
        """
        try:
            self.load_images()
            panorama = self.stitch_images()
            self.save_panorama(panorama)
            self.display_panorama(panorama)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Adjust the folder path and output file name as needed
    images_folder = 'path/to/your/images'  # Specify your image folder path
    output_file = 'output/panorama.jpg'  # Specify output file name and path

    # Create an instance of the panoramic view generator and process
    panoramic_view_generator = PanoramicViewGenerator(images_folder, output_file)
    panoramic_view_generator.process()
```
