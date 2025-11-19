"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Write a script to batch process and optimize images for front-lit and backlit canvas printing, adhering to the high-resolution requirements mentioned on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_34d249c44473f506
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def optimize_image(input_path, output_path, size=(3000, 3000), quality=85):
    """
    Optimize an image for canvas printing.

    Parameters:
    - input_path: str, path to the input image file
    - output_path: str, path to save the optimized image
    - size: tuple, target size for the image (width, height)
    - quality: int, quality of the output image (1-100)

    Raises:
    - FileNotFoundError: if the input file does not exist
    - IOError: if there is an error during image processing
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image while maintaining aspect ratio
            img.thumbnail(size, Image.ANTIALIAS)
            # Save the optimized image
            img.save(output_path, format='JPEG', quality=quality, optimize=True)
            logging.info(f"Optimized image saved to: {output_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {input_path}")
        raise
    except IOError as e:
        logging.error(f"Error processing image {input_path}: {e}")
        raise

def batch_process_images(input_dir, output_dir, size=(3000, 3000), quality=85):
    """
    Batch process and optimize images in a directory.

    Parameters:
    - input_dir: str, directory containing input images
    - output_dir: str, directory to save optimized images
    - size: tuple, target size for the images (width, height)
    - quality: int, quality of the output images (1-100)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                optimize_image(input_path, output_path, size, quality)
            except Exception as e:
                logging.error(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_directory = 'path/to/input/images'  # Change to your input directory
    output_directory = 'path/to/output/images'  # Change to your output directory

    # Batch process images
    batch_process_images(input_directory, output_directory)
```

Make sure to replace `'path/to/input/images'` and `'path/to/output/images'` with the actual paths where your images are stored and where you want to save the optimized images.
