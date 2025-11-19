"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: "Generate a Python script to stitch 360-degree photos for virtual reality experiences similar to PICS3DStudio's work."
Generated: DETERMINISTIC_02d3e2061e848fc5
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import os

class PhotoStitcher:
    def __init__(self, image_folder):
        """
        Initializes the PhotoStitcher with the path to the folder containing images.

        :param image_folder: Path to the folder containing 360-degree images.
        """
        self.image_folder = image_folder
        self.images = self.load_images()

    def load_images(self):
        """
        Loads images from the specified folder and returns a list of images.

        :return: List of loaded images.
        """
        images = []
        for filename in sorted(os.listdir(self.image_folder)):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(self.image_folder, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    images.append(img)
                else:
                    print(f"Warning: Unable to load image {img_path}")
        return images

    def stitch_images(self):
        """
        Stitches the loaded images into a single panoramic image.

        :return: The stitched image.
        """
        if len(self.images) < 2:
            raise ValueError("At least two images are required for stitching.")

        # Create a Stitcher object
        stitcher = cv2.Stitcher_create()
        status, stitched_image = stitcher.stitch(self.images)

        if status == cv2.Stitcher_OK:
            return stitched_image
        else:
            raise RuntimeError("Error during stitching: " + str(status))

    def save_stitched_image(self, output_path):
        """
        Saves the stitched image to the specified output path.

        :param output_path: Path where the stitched image will be saved.
        """
        stitched_image = self.stitch_images()
        cv2.imwrite(output_path, stitched_image)
        print(f"Stitched image saved to {output_path}")

def main():
    # Define the folder containing the images and the output path
    image_folder = 'path/to/your/images'  # Update this path
    output_path = 'path/to/output/stitched_image.jpg'  # Update this path

    try:
        # Create a PhotoStitcher instance
        stitcher = PhotoStitcher(image_folder)
        # Save the stitched image
        stitcher.save_stitched_image(output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to update the `image_folder` and `output_path` variables in the `main` function to point to your actual image directory and desired output file location.
