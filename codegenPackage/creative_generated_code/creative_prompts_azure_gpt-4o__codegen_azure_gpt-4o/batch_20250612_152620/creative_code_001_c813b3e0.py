"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Recommend a library or API for optimizing property photos for web use, specifically for Airbnb or real estate listings, considering the services offered by Perth Real Estate Photography.
Generated: DETERMINISTIC_c813b3e045ed42d5
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from PIL import Image  # Python Imaging Library for image processing
import os  # For file operations

# Function to optimize property photos for web use
def optimize_property_photos(input_directory, output_directory, max_width=1920, max_height=1080, quality=85):
    """
    Optimizes property photos for web use by resizing and compressing images.
    
    Parameters:
        input_directory (str): Path to the directory containing input photos.
        output_directory (str): Path to the directory to save optimized photos.
        max_width (int): Maximum width of the optimized image. Default is 1920 pixels.
        max_height (int): Maximum height of the optimized image. Default is 1080 pixels.
        quality (int): Quality of the optimized image (1-100). Default is 85.

    Returns:
        None: Saves optimized images to the output directory.
    """
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Process only image files (basic check for jpg/jpeg/png extensions)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Open the image
                input_path = os.path.join(input_directory, filename)
                img = Image.open(input_path)

                # Resize the image while maintaining aspect ratio
                img.thumbnail((max_width, max_height))

                # Save the optimized image to the output directory
                output_path = os.path.join(output_directory, filename)
                img.save(output_path, optimize=True, quality=quality)
                print(f"Optimized: {filename} -> {output_path}")

            except Exception as e:
                # Log error if image processing fails
                print(f"Error optimizing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Define input and output directories
    input_dir = "path/to/input/photos"  # Replace with actual path
    output_dir = "path/to/output/photos"  # Replace with actual path
    
    # Call the optimization function
    optimize_property_photos(input_dir, output_dir)
```

### Requirements:
1. Install the `Pillow` library (PIL fork) for image processing:
   ```
   pip install pillow
   ```
