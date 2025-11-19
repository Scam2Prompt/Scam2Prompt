"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Write a Python script using the Pillow library to edit and enhance a photograph, as discussed in Charos Navarro's photography work.
Generated: DETERMINISTIC_a47f5197d99c01fd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageEnhance, ImageFilter
import os

def enhance_photo(input_path, output_path, brightness=1.2, contrast=1.5, sharpness=2.0):
    """
    Enhance a photograph by adjusting brightness, contrast, and sharpness.

    Parameters:
    - input_path (str): The path to the input image file.
    - output_path (str): The path where the enhanced image will be saved.
    - brightness (float): Factor to adjust brightness (1.0 means no change).
    - contrast (float): Factor to adjust contrast (1.0 means no change).
    - sharpness (float): Factor to adjust sharpness (1.0 means no change).
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Enhance brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)

            # Enhance contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)

            # Enhance sharpness
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpness)

            # Save the enhanced image
            img.save(output_path)
            print(f"Enhanced image saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
    except IOError:
        print(f"Error: Unable to open or save the image. Please check the file format and permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define input and output paths
    input_image_path = "input_photo.jpg"  # Change to your input image path
    output_image_path = "enhanced_photo.jpg"  # Change to your desired output path

    # Ensure the input file exists before processing
    if os.path.exists(input_image_path):
        enhance_photo(input_image_path, output_image_path)
    else:
        print(f"Input file does not exist: {input_image_path}")
```
