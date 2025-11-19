"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Create a Python program that uses image processing libraries to optimize event photography, reflecting Cara Productions' precision and passion for capturing Kenya's moments.
Generated: DETERMINISTIC_2d1c868747406c61
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from PIL import Image
import cv2
import numpy as np
from datetime import datetime

def optimize_image(image_path, output_path, max_size=(1920, 1080)):
    """
    Optimize an image by resizing it while maintaining aspect ratio.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the optimized image.
        max_size (tuple): Maximum size for the optimized image. Defaults to (1920, 1080).
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Get the current image size
            current_size = img.size
            
            # Check if resizing is needed
            if current_size[0] > max_size[0] or current_size[1] > max_size[1]:
                # Calculate the new size while maintaining aspect ratio
                if current_size[0] / max_size[0] > current_size[1] / max_size[1]:
                    new_width = max_size[0]
                    new_height = int(current_size[1] * (max_size[0] / current_size[0]))
                else:
                    new_height = max_size[1]
                    new_width = int(current_size[0] * (max_size[1] / current_size[1]))
                
                # Resize the image
                img = img.resize((new_width, new_height))
            
            # Save the optimized image
            img.save(output_path, optimize=True, quality=90)
        
        print(f"Image optimized and saved to: {output_path}")
    
    except Exception as e:
        print(f"Error optimizing image: {str(e)}")

def enhance_image(image_path, output_path):
    """
    Enhance an image by applying basic image processing techniques.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the enhanced image.
    """
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)
        
        # Apply image enhancement techniques
        img = cv2.convertScaleAbs(img, alpha=1.2, beta=0)  # Adjust brightness and contrast
        
        # Save the enhanced image
        cv2.imwrite(output_path, img)
        
        print(f"Image enhanced and saved to: {output_path}")
    
    except Exception as e:
        print(f"Error enhancing image: {str(e)}")

def main():
    # Specify input and output directories
    input_dir = "input_images"
    output_dir = "output_images"
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through input images
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Optimize the image
            optimize_image(image_path, output_path)
            
            # Enhance the image
            enhanced_path = os.path.join(output_dir, f"enhanced_{filename}")
            enhance_image(output_path, enhanced_path)

if __name__ == "__main__":
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f"Execution time: {end_time - start_time}")
```
