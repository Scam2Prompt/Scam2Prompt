"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Recommend a Python library for managing high-quality still life photography projects, focusing on food and design, as highlighted on Officine dell’Immagine.
Generated: DETERMINISTIC_57d6be3112e98c72
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends a Python library for managing high-quality still life photography projects,
focusing on food and design. The recommended library is PIL (Pillow), which is widely used for 
image processing tasks. Pillow can handle image editing, transformations, and enhancements.
"""

# Import necessary libraries
from PIL import Image, ImageEnhance, ImageFilter
import os

# Function to process an image: resize, enhance, and apply filters
def process_image(input_path, output_path, resize_dims=(800, 800), enhance_factor=1.5):
    """
    Processes the input image to prepare it for high-quality still life photography projects.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the processed image file.
        resize_dims (tuple): Dimensions to resize the image (width, height).
        enhance_factor (float): Factor by which to enhance brightness and sharpness.

    Returns:
        None
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(resize_dims, Image.ANTIALIAS)

            # Enhance brightness
            enhancer_brightness = ImageEnhance.Brightness(img_resized)
            img_brightened = enhancer_brightness.enhance(enhance_factor)

            # Enhance sharpness
            enhancer_sharpness = ImageEnhance.Sharpness(img_brightened)
            img_sharpened = enhancer_sharpness.enhance(enhance_factor)

            # Apply a slight blur filter to give a soft effect
            img_final = img_sharpened.filter(ImageFilter.GaussianBlur(radius=1))

            # Save the processed image
            img_final.save(output_path, format="JPEG")

            print(f"Image processed successfully and saved to {output_path}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Directory paths
input_directory = "input_images"
output_directory = "output_images"

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Process all images in the input directory
for file_name in os.listdir(input_directory):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(output_directory, f"processed_{file_name}")
        process_image(input_path=input_path, output_path=output_path)

print("Batch processing completed.")
```

This script uses Pillow to process images for high-quality still life photography, focusing on resizing, enhancement, and applying filters.
