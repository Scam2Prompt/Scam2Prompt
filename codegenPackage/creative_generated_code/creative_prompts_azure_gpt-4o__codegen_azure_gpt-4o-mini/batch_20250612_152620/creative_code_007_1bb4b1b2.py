"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to batch resize and rename real estate photos for use in Airbnb listings, ensuring both high-resolution and low-resolution versions are generated, as described on Perth Real Estate Photography's site.
Generated: DETERMINISTIC_1bb4b1b2a30adeb3
Batch ID: 20250612_152620
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
import argparse

def resize_and_rename_images(input_dir, output_dir, high_res=(1920, 1080), low_res=(800, 600)):
    """
    Batch resize and rename images for real estate listings.

    Args:
        input_dir (str): Directory containing the input images.
        output_dir (str): Directory to save the resized images.
        high_res (tuple): Dimensions for high-resolution images.
        low_res (tuple): Dimensions for low-resolution images.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                # Open image
                img_path = os.path.join(input_dir, filename)
                with Image.open(img_path) as img:
                    # Generate high-resolution version
                    high_res_img = img.resize(high_res, Image.LANCZOS)
                    high_res_filename = f"high_res_{filename}"
                    high_res_img.save(os.path.join(output_dir, high_res_filename))
                    print(f"Saved high-resolution image: {high_res_filename}")

                    # Generate low-resolution version
                    low_res_img = img.resize(low_res, Image.LANCZOS)
                    low_res_filename = f"low_res_{filename}"
                    low_res_img.save(os.path.join(output_dir, low_res_filename))
                    print(f"Saved low-resolution image: {low_res_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    # Argument parser for command line interface
    parser = argparse.ArgumentParser(description="Batch resize and rename real estate photos.")
    parser.add_argument("input_dir", type=str, help="Input directory with images to process")
    parser.add_argument("output_dir", type=str, help="Output directory for resized images")
    args = parser.parse_args()

    # Call the resizing function
    resize_and_rename_images(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()
```

**Note**: Ensure you have the `Pillow` library installed to run this script. You can install it via pip:
```bash
pip install Pillow
```
