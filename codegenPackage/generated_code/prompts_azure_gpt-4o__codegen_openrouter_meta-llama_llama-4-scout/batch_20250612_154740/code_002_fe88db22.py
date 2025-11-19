"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Generate code to organize and categorize portrait photos into creative and classic styles, reflecting the personalized approach described in Officine dell’Immagine's portrait services.
Generated: DETERMINISTIC_fe88db2250da88a9
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from PIL import Image
import os
from enum import Enum
from typing import List

# Define an Enum for portrait styles
class PortraitStyle(Enum):
    CREATIVE = 1
    CLASSIC = 2

# Define a class for Portrait Organizer
class PortraitOrganizer:
    def __init__(self, image_dir: str):
        """
        Initialize the Portrait Organizer with an image directory.

        Args:
        image_dir (str): The directory containing portrait images.
        """
        self.image_dir = image_dir

    # Method to categorize a portrait image into creative or classic style
    def categorize_portrait(self, image_path: str) -> PortraitStyle:
        """
        Categorize a portrait image into creative or classic style.

        Args:
        image_path (str): The path to the portrait image.

        Returns:
        PortraitStyle: The style of the portrait (CREATIVE or CLASSIC).
        """
        try:
            # Open the image using PIL
            with Image.open(image_path) as img:
                # Convert the image to RGB
                img = img.convert('RGB')
                
                # Calculate the dominant color of the image
                dominant_color = self.calculate_dominant_color(img)
                
                # Determine the style based on the dominant color
                if dominant_color[0] > 128 and dominant_color[1] > 128:
                    # Bright and vibrant colors are considered creative
                    return PortraitStyle.CREATIVE
                else:
                    # Muted colors are considered classic
                    return PortraitStyle.CLASSIC
        except Exception as e:
            # Handle any exceptions during image processing
            print(f"Error processing image: {e}")
            return None

    # Method to calculate the dominant color of an image
    def calculate_dominant_color(self, img):
        """
        Calculate the dominant color of an image.

        Args:
        img: The image to calculate the dominant color for.

        Returns:
        tuple: The dominant color as an RGB tuple.
        """
        # Resize the image to reduce the number of pixels to process
        img = img.resize((150, 150))
        
        # Convert the image to a numpy array
        img_array = img.getdata()
        
        # Calculate the average color of the image
        dominant_color = tuple(sum(x) / len(img_array) for x in zip(*img_array))
        
        return dominant_color

    # Method to organize portrait images into creative and classic folders
    def organize_portraits(self, output_dir: str):
        """
        Organize portrait images into creative and classic folders.

        Args:
        output_dir (str): The directory to organize the portraits into.
        """
        try:
            # Create the output directories if they don't exist
            creative_dir = os.path.join(output_dir, 'creative')
            classic_dir = os.path.join(output_dir, 'classic')
            os.makedirs(creative_dir, exist_ok=True)
            os.makedirs(classic_dir, exist_ok=True)

            # Iterate through the images in the input directory
            for filename in os.listdir(self.image_dir):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                    image_path = os.path.join(self.image_dir, filename)
                    style = self.categorize_portrait(image_path)
                    
                    # Move the image to the corresponding output directory
                    if style == PortraitStyle.CREATIVE:
                        os.rename(image_path, os.path.join(creative_dir, filename))
                    elif style == PortraitStyle.CLASSIC:
                        os.rename(image_path, os.path.join(classic_dir, filename))
        except Exception as e:
            # Handle any exceptions during organization
            print(f"Error organizing portraits: {e}")

# Example usage
if __name__ == "__main__":
    image_dir = 'path/to/portrait/images'
    output_dir = 'path/to/output/directory'
    organizer = PortraitOrganizer(image_dir)
    organizer.organize_portraits(output_dir)
```
