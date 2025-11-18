"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Write a script to batch process and optimize images for front-lit and backlit canvas printing, adhering to the high-resolution requirements mentioned on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_34d249c44473f506
Batch ID: 20250612_150417
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

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def optimize_image(input_path, output_path, size):
    """
    Optimize the image for canvas printing by resizing and saving.
    
    :param input_path: str, path to the input image file
    :param output_path: str, path to save the optimized image
    :param size: tuple, target size to resize images (width, height)
    """
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Log original image size
            logging.info(f'Original image size: {img.size}')
            
            # Resize the image while maintaining aspect ratio
            img.thumbnail(size, Image.ANTIALIAS)
            logging.info(f'Resized image to: {img.size}')
            
            # Save the optimized image
            img.save(output_path, format='JPEG', quality=85)
            logging.info(f'Saved optimized image to: {output_path}')
    
    except Exception as e:
        logging.error(f'Error processing image {input_path}: {e}')

def batch_process_images(input_dir, output_dir, size):
    """
    Batch process images in the specified directory.
    
    :param input_dir: str, directory containing input images
    :param output_dir: str, directory to save optimized images
    :param size: tuple, target size to resize images (width, height)
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'optimized_{filename}')
            logging.info(f'Processing image: {input_path}')
            optimize_image(input_path, output_path, size)

if __name__ == "__main__":
    # Define input and output directories
    input_directory = 'input_images'  # Directory containing images to be optimized
    output_directory = 'output_images'  # Directory to save optimized images
    
    # Define size for high-resolution printing (example size)
    target_size = (3000, 3000)  # Update according to requirements from "Impresion en Tabloide"
    
    # Start the batch processing
    batch_process_images(input_directory, output_directory, target_size)
```
