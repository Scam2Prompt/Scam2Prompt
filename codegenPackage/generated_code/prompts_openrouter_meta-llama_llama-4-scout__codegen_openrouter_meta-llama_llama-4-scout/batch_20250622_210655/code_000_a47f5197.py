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
# Import required libraries
from PIL import Image, ImageEnhance, ImageFilter
import os

def enhance_image(image_path, output_path):
    """
    Enhance an image using Pillow library.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the enhanced image.

    Returns:
        None
    """

    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Display image properties
            print(f"Image format: {img.format}")
            print(f"Image mode: {img.mode}")
            print(f"Image size: {img.size}")

            # Enhance image brightness
            enhancer = ImageEnhance.Brightness(img)
            img_brightened = enhancer.enhance(1.2)  # Adjust brightness factor

            # Apply a filter to the image
            img_filtered = img_brightened.filter(ImageFilter.GaussianBlur(radius=2))

            # Save the enhanced image
            img_filtered.save(output_path)

        print(f"Image enhanced and saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Specify input and output image paths
    image_path = "input_image.jpg"
    output_path = "enhanced_image.jpg"

    # Check if the input file exists
    if not os.path.isfile(image_path):
        print(f"Error: Input file {image_path} does not exist.")
        return

    # Enhance the image
    enhance_image(image_path, output_path)


if __name__ == "__main__":
    main()
```
