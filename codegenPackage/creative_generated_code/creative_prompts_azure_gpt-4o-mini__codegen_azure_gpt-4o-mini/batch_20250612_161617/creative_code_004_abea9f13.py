"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: How do I use a library to manage color calibration for packaging designs to ensure consistency, as emphasized by the services provided on the Metis site?
Generated: DETERMINISTIC_abea9f13dd7e0585
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
import os

class ColorCalibration:
    """
    A class to perform color calibration for packaging designs.
    This class uses a reference color profile to adjust colors in images
    for consistent packaging designs.
    """

    def __init__(self, reference_color):
        """
        Initialize the ColorCalibration with a reference color.

        :param reference_color: A tuple representing the reference RGB color.
        """
        self.reference_color = np.array(reference_color)

    def load_image(self, image_path):
        """
        Load an image from a specified path.

        :param image_path: The file path to the image.
        :return: The loaded image as an array.
        """
        try:
            image = io.imread(image_path)
            return image
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found: {image_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading the image: {str(e)}")

    def calibrate_color(self, image):
        """
        Calibrate the colors in the image to the reference color.

        :param image: The image to be calibrated.
        :return: The color-calibrated image.
        """
        # Convert image to LAB color space for better color manipulation
        image_lab = color.rgb2lab(image)
        reference_lab = color.rgb2lab(np.reshape(self.reference_color, (1, 1, 3)))

        # Compute the scaling factors for each channel
        scaling_factors = reference_lab / np.mean(image_lab, axis=(0, 1))

        # Apply scaling to each channel in the LAB color space
        calibrated_image_lab = image_lab * scaling_factors

        # Convert back to RGB color space
        calibrated_image_rgb = color.lab2rgb(calibrated_image_lab)

        return np.clip(calibrated_image_rgb, 0, 1)  # Ensure values are within valid range

    def save_image(self, image, output_path):
        """
        Save the calibrated image to a specified path.

        :param image: The calibrated image to save.
        :param output_path: The file path where the image will be saved.
        """
        try:
            io.imsave(output_path, (image * 255).astype(np.uint8))  # Convert to 8-bit image
        except Exception as e:
            raise Exception(f"An error occurred while saving the image: {str(e)}")

    def process_image(self, input_path, output_path):
        """
        Load, calibrate, and save the image.

        :param input_path: The file path of the input image.
        :param output_path: The file path for the output calibrated image.
        """
        image = self.load_image(input_path)
        calibrated_image = self.calibrate_color(image)
        self.save_image(calibrated_image, output_path)

# Example usage
if __name__ == "__main__":
    # Define a reference RGB color (white in this case)
    reference_color = (1.0, 1.0, 1.0)

    # Create a ColorCalibration instance
    color_calibrator = ColorCalibration(reference_color)

    # Define input and output file paths
    input_file_path = "input_image.jpg"  # Replace with your actual input file
    output_file_path = "calibrated_image.jpg"  # Desired output file name

    # Process the image to apply color calibration
    color_calibrator.process_image(input_file_path, output_file_path)
```
