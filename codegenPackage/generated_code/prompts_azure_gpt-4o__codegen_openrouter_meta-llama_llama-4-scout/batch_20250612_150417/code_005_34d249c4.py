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
# image_optimizer.py

import os
from PIL import Image, ImageEnhance
import argparse

def optimize_image(image_path, output_path, brightness=1.5, contrast=1.2):
    """
    Optimizes an image for printing on canvas.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to the output image.
        brightness (float, optional): Brightness adjustment. Defaults to 1.5.
        contrast (float, optional): Contrast adjustment. Defaults to 1.2.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Ensure the image is in RGB mode
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Apply brightness and contrast adjustments
            enhancer_brightness = ImageEnhance.Brightness(img)
            img = enhancer_brightness.enhance(brightness)

            enhancer_contrast = ImageEnhance.Contrast(img)
            img = enhancer_contrast.enhance(contrast)

            # Save the optimized image
            img.save(output_path, quality=95)
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def batch_process_images(input_dir, output_dir_frontlit, output_dir_backlit):
    """
    Batch processes images for front-lit and backlit canvas printing.

    Args:
        input_dir (str): Directory containing input images.
        output_dir_frontlit (str): Directory for front-lit optimized images.
        output_dir_backlit (str): Directory for back-lit optimized images.
    """
    # Create output directories if they don't exist
    os.makedirs(output_dir_frontlit, exist_ok=True)
    os.makedirs(output_dir_backlit, exist_ok=True)

    # Iterate through input images
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            output_path_frontlit = os.path.join(output_dir_frontlit, filename)
            output_path_backlit = os.path.join(output_dir_backlit, filename)

            # Optimize for front-lit printing
            optimize_image(image_path, output_path_frontlit, brightness=1.5, contrast=1.2)

            # Optimize for back-lit printing
            optimize_image(image_path, output_path_backlit, brightness=0.8, contrast=1.5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch process and optimize images for canvas printing.")
    parser.add_argument("-i", "--input_dir", required=True, help="Directory containing input images.")
    parser.add_argument("-o_frontlit", required=True, help="Directory for front-lit optimized images.")
    parser.add_argument("-o_backlit", required=True, help="Directory for back-lit optimized images.")

    args = parser.parse_args()

    batch_process_images(args.input_dir, args.o_frontlit, args.o_backlit)
```
