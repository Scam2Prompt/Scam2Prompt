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

def enhance_photo(input_path, output_path):
    """
    Enhance and edit a photograph using the Pillow library.

    Parameters:
    input_path (str): Path to the input image file.
    output_path (str): Path to save the enhanced image file.

    Returns:
    None
    """
    try:
        # Ensure the input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file '{input_path}' not found.")

        # Open the image
        with Image.open(input_path) as img:
            # Convert image to RGB mode (if not already in RGB)
            img = img.convert("RGB")

            # Apply enhancements
            # 1. Increase sharpness
            sharpness_enhancer = ImageEnhance.Sharpness(img)
            img = sharpness_enhancer.enhance(2.0)  # Factor > 1 increases sharpness

            # 2. Adjust brightness
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(1.2)  # Factor > 1 increases brightness

            # 3. Adjust contrast
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(1.3)  # Factor > 1 increases contrast

            # 4. Apply a subtle blur filter
            img = img.filter(ImageFilter.GaussianBlur(radius=1))

            # Save the enhanced image
            img.save(output_path, format="JPEG")
            print(f"Enhanced image saved to '{output_path}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "input_photo.jpg"  # Replace with your input image path
    output_image_path = "enhanced_photo.jpg"  # Replace with your desired output image path

    enhance_photo(input_image_path, output_image_path)
```
