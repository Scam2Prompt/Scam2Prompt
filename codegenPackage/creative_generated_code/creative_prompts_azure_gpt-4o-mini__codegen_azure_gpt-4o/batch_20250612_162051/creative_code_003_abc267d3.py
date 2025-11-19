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

Here is a Python script that utilizes the Pillow library for image optimization. This code compresses images and resizes them for web optimization.

```python
from PIL import Image
import os

def optimize_images(input_folder, output_folder, max_width=1920, max_height=1080, quality=85):
    """
    Optimize images by resizing and compressing them.
    
    Args:
    - input_folder (str): Path to the folder containing the original images.
    - output_folder (str): Path to the folder where optimized images will be saved.
    - max_width (int): Maximum width of the resized image.
    - max_height (int): Maximum height of the resized image.
    - quality (int): Compression quality (1-100, higher is better quality but less compression).
    
    Raises:
    - FileNotFoundError: If the input folder does not exist.
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # Open the image
            with Image.open(input_path) as img:
                # Convert image to RGB (to avoid issues with formats like PNG with transparency)
                img = img.convert("RGB")
                
                # Resize the image while maintaining aspect ratio
                img.thumbnail((max_width, max_height), Image.ANTIALIAS)
                
                # Save the optimized image to the output folder
                img.save(output_path, format="JPEG", quality=quality, optimize=True)
                print(f"Optimized: {file_name}")
        
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    # Example usage
    input_folder = "path/to/your/input/images"
    output_folder = "path/to/your/output/images"
    
    # Optimize images with a maximum size of 1920x1080 and 85% quality
    optimize_images(input_folder, output_folder)
```

### Requirements:
1. Install Pillow via pip:
   ```
   pip install pillow
   ```

### Key Points:
- Ensure the `input_folder` contains the original images to optimize.
- The `output_folder` will store the optimized images.
- The script handles resizing, compression, and format conversion (all images saved as JPEG for consistency).
- Proper error handling is included to capture issues like unsupported file formats or corrupted files.
