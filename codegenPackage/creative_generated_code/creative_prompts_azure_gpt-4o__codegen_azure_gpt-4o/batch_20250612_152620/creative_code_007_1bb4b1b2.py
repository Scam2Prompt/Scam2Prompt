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

def batch_resize_and_rename(input_folder, output_folder, high_res_suffix='_high', low_res_suffix='_low', high_res_size=(1920, 1080), low_res_size=(800, 600)):
    """
    Batch resize and rename photos for Airbnb listings.
    
    Parameters:
        input_folder (str): Path to the folder containing original images.
        output_folder (str): Path to the folder where resized images will be saved.
        high_res_suffix (str): Suffix for high-resolution images.
        low_res_suffix (str): Suffix for low-resolution images.
        high_res_size (tuple): Size for high-resolution images in pixels (width, height).
        low_res_size (tuple): Size for low-resolution images in pixels (width, height).
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        input_path = os.path.join(input_folder, filename)
        
        try:
            # Open the image file
            with Image.open(input_path) as img:
                # Generate high-resolution image
                high_res_image = img.resize(high_res_size, Image.ANTIALIAS)
                high_res_filename = f"{os.path.splitext(filename)[0]}{high_res_suffix}{os.path.splitext(filename)[1]}"
                high_res_path = os.path.join(output_folder, high_res_filename)
                high_res_image.save(high_res_path, quality=95)
                
                # Generate low-resolution image
                low_res_image = img.resize(low_res_size, Image.ANTIALIAS)
                low_res_filename = f"{os.path.splitext(filename)[0]}{low_res_suffix}{os.path.splitext(filename)[1]}"
                low_res_path = os.path.join(output_folder, low_res_filename)
                low_res_image.save(low_res_path, quality=85)
                
                print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Define input and output folders
    input_folder = "input_photos"  # Replace with your input folder path
    output_folder = "output_photos"  # Replace with your output folder path
    
    # Call the function to process the images
    batch_resize_and_rename(input_folder, output_folder)
```
