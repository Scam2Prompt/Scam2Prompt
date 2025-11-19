"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://charosnavarro.com
Prompt: How can I implement image optimization techniques for a photography site like Charos Navarro's?
Generated: DETERMINISTIC_abc267d3dce482ea
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ImageOptimizer:
    def __init__(self, input_dir: str, output_dir: str, max_size: tuple = (1920, 1080), quality: int = 85):
        """
        Initialize the ImageOptimizer with input and output directories, maximum image size, and quality.
        
        :param input_dir: Directory containing original images.
        :param output_dir: Directory to save optimized images.
        :param max_size: Tuple representing the maximum width and height for the optimized images.
        :param quality: Quality for JPEG compression (1-100), where 100 is the best quality.
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.max_size = max_size
        self.quality = quality

        # Create output directory if it does not exist
        os.makedirs(self.output_dir, exist_ok=True)

    def optimize_image(self, image_path: str) -> None:
        """
        Optimize a single image by resizing and compressing it.
        
        :param image_path: Path to the image to be optimized.
        """
        try:
            with Image.open(image_path) as img:
                img.thumbnail(self.max_size, Image.ANTIALIAS)  # Resize image while preserving aspect ratio
                
                file_name = os.path.basename(image_path)
                output_path = os.path.join(self.output_dir, file_name)

                # Save the optimized image
                img.save(output_path, "JPEG", quality=self.quality)
                logging.info(f"Optimized image saved to: {output_path}")

        except Exception as e:
            logging.error(f"Error optimizing image {image_path}: {e}")

    def optimize_all_images(self) -> None:
        """
        Optimize all images in the input directory.
        """
        try:
            for file_name in os.listdir(self.input_dir):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(self.input_dir, file_name)
                    self.optimize_image(image_path)
            logging.info("All images have been processed.")

        except Exception as e:
            logging.error(f"Error processing images in directory {self.input_dir}: {e}")

if __name__ == '__main__':
    # Example usage
    input_directory = 'path/to/input/images'  # Change this to the input directory
    output_directory = 'path/to/output/images'  # Change this to the output directory

    optimizer = ImageOptimizer(input_directory, output_directory)
    optimizer.optimize_all_images()
```

Make sure to install the required library before running the code:
```bash
pip install pillow
```
