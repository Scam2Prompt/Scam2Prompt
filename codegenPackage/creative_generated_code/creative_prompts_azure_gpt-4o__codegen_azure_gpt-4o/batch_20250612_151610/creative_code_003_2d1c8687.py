"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Create a Python program that uses image processing libraries to optimize event photography, reflecting Cara Productions' precision and passion for capturing Kenya's moments.
Generated: DETERMINISTIC_2d1c868747406c61
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cv2
import numpy as np
from PIL import Image

def optimize_photographs(input_dir, output_dir):
    """
    Optimizes images in the input directory and saves optimized versions in the output directory.
    
    This function performs image resizing, sharpening, noise reduction, and saves
    the optimized images in JPEG format for event photography purposes.
    
    Args:
        input_dir (str): Directory containing the input images.
        output_dir (str): Directory where optimized images will be saved.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Loop through all files in the input directory
        for file_name in os.listdir(input_dir):
            # Only process image files
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(input_dir, file_name)
                
                # Read the image using OpenCV
                image = cv2.imread(input_path)

                # Resize the image to a standard resolution (e.g., 1920x1080)
                optimized_resolution = (1920, 1080)
                resized_image = cv2.resize(image, optimized_resolution, interpolation=cv2.INTER_AREA)

                # Apply sharpening kernel
                sharpening_kernel = np.array([
                    [-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]
                ])
                sharpened_image = cv2.filter2D(resized_image, -1, sharpening_kernel)

                # Apply noise reduction using GaussianBlur
                denoised_image = cv2.GaussianBlur(sharpened_image, (5, 5), 0)

                # Convert the image to RGB format for saving as JPEG
                final_image = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB)

                # Save the optimized image using PIL for better control over compression
                output_path = os.path.join(output_dir, f"optimized_{file_name}")
                pil_image = Image.fromarray(final_image)
                pil_image.save(output_path, format='JPEG', quality=90)

                print(f"Optimized and saved: {file_name}")
    
    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e}")

# Main function to invoke the image optimization process
if __name__ == "__main__":
    # Input and output directories
    input_directory = "./input_images"  # Replace with the actual input directory path
    output_directory = "./output_images"  # Replace with the actual output directory path

    # Run the optimization process
    optimize_photographs(input_directory, output_directory)
```
