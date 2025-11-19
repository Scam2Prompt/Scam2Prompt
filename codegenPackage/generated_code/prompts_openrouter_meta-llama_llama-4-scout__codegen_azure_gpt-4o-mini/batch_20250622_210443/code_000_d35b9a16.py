"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write a Python code snippet to process and generate products cartográficos using Georreferenciadas images acquired from RPA sensores remotos.
Generated: DETERMINISTIC_d35b9a16dd4f24d7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import geopandas as gpd
from rasterio import open as rio_open
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import numpy as np

class CartographicProductGenerator:
    """
    A class to process and generate cartographic products from georeferenced images
    acquired from remote sensing RPA sensors.
    """

    def __init__(self, input_directory, output_directory):
        """
        Initializes the CartographicProductGenerator with input and output directories.

        :param input_directory: Directory containing georeferenced images.
        :param output_directory: Directory to save processed cartographic products.
        """
        self.input_directory = input_directory
        self.output_directory = output_directory
        self._validate_directories()

    def _validate_directories(self):
        """Validates the existence of input and output directories."""
        if not os.path.exists(self.input_directory):
            raise FileNotFoundError(f"Input directory '{self.input_directory}' does not exist.")
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def process_images(self):
        """Processes all georeferenced images in the input directory."""
        for filename in os.listdir(self.input_directory):
            if filename.endswith('.tif'):
                self._process_image(os.path.join(self.input_directory, filename))

    def _process_image(self, image_path):
        """
        Processes a single georeferenced image and generates a cartographic product.

        :param image_path: Path to the georeferenced image.
        """
        try:
            with rio_open(image_path) as src:
                # Read the image data
                image_data = src.read()
                transform = src.transform

                # Example processing: Resampling the image to half its original size
                resampled_data = self._resample_image(image_data, src.meta)

                # Save the processed image
                output_path = os.path.join(self.output_directory, os.path.basename(image_path))
                self._save_image(resampled_data, transform, output_path, src.meta)

        except Exception as e:
            print(f"Error processing image '{image_path}': {e}")

    def _resample_image(self, image_data, meta):
        """
        Resamples the image data to half its original size.

        :param image_data: The original image data.
        :param meta: Metadata of the original image.
        :return: Resampled image data.
        """
        # Calculate new dimensions
        new_height = image_data.shape[1] // 2
        new_width = image_data.shape[2] // 2

        # Resample the image
        resampled_data = np.empty((image_data.shape[0], new_height, new_width), dtype=image_data.dtype)
        for i in range(image_data.shape[0]):
            resampled_data[i] = image_data[i].reshape((new_height, new_width))

        return resampled_data

    def _save_image(self, image_data, transform, output_path, meta):
        """
        Saves the processed image to the specified output path.

        :param image_data: The processed image data.
        :param transform: The transform for the image.
        :param output_path: Path to save the processed image.
        :param meta: Metadata of the original image.
        """
        meta.update({
            'height': image_data.shape[1],
            'width': image_data.shape[2],
            'transform': transform
        })

        with rio_open(output_path, 'w', **meta) as dst:
            dst.write(image_data)

if __name__ == "__main__":
    # Example usage
    input_dir = "path/to/georeferenced/images"
    output_dir = "path/to/save/cartographic/products"

    generator = CartographicProductGenerator(input_dir, output_dir)
    generator.process_images()
```
