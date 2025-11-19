"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pics3dstudio.com
Prompt: Generate a code snippet for a virtual reality application that showcases 360-degree views of architectural projects like the Mercedes-Benz AMG S 63 E 2025.
Generated: DETERMINISTIC_5d7cefd12c55a739
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class VR360Viewer:
    """Class to create a 360-degree view of architectural projects."""

    def __init__(self, image_folder: str):
        """
        Initializes the VR360Viewer with a directory containing 360 images.

        :param image_folder: Path to the folder containing 360-degree images.
        """
        self.image_folder = Path(image_folder)
        self.images = self.load_images()

    def load_images(self):
        """Loads images from the specified directory and returns a list of images."""
        images = []
        if not self.image_folder.is_dir():
            raise FileNotFoundError(f"Directory not found: {self.image_folder}")
        
        for img_file in self.image_folder.glob("*.jpg"):
            img = cv2.imread(str(img_file))
            if img is None:
                print(f"Warning: Unable to read image {img_file}. Skipping.")
                continue
            images.append(img)
        
        if not images:
            raise ValueError("No valid images found in the specified directory.")
        
        return images

    def create_panorama(self):
        """Creates a panorama by stitching images together."""
        if len(self.images) < 2:
            raise ValueError("At least two images are required to create a panorama.")
        
        # Initialize the stitching object
        stitcher = cv2.Stitcher_create()
        status, panorama = stitcher.stitch(self.images)
        
        if status != cv2.Stitcher_OK:
            raise RuntimeError(f"Error during stitching: {status}")
        
        return panorama

    def display_panorama(self):
        """Displays the 360-degree panorama using Matplotlib."""
        try:
            panorama = self.create_panorama()
            plt.imshow(cv2.cvtColor(panorama, cv2.COLOR_BGR2RGB))
            plt.axis('off')  # Hide axes
            plt.title("360-Degree Architectural View")
            plt.show()
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main function to run the VR360Viewer."""
    try:
        image_folder = "path/to/your/360/images"  # Update this path with actual images
        viewer = VR360Viewer(image_folder)
        viewer.display_panorama()
    except Exception as e:
        print(f"An error occurred in the VR viewer: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

**Note:** Please ensure you update the `image_folder` variable in the `main()` function with the path to your folder containing 360-degree images. The images should be in JPG format for this code to work correctly. Additionally, make sure you have the necessary libraries installed (`opencv-python`, `numpy`, `matplotlib`).
