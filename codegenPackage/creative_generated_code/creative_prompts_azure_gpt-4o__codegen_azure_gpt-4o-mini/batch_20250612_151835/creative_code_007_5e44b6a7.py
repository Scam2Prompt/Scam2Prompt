"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Recommend APIs or libraries for creating retina-ready images and text for web applications, inspired by Ansh Soft Tech's focus on vibrant and crisp visuals.
Generated: DETERMINISTIC_5e44b6a788075606
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

class ImageProcessor:
    """
    A class to create retina-ready images and text for web applications.
    """

    def __init__(self, output_directory: str):
        """
        Initializes the ImageProcessor with an output directory.

        :param output_directory: Directory where processed images will be saved.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def create_retina_image(self, input_image_path: str, scale_factor: float = 2.0) -> str:
        """
        Creates a retina-ready image by scaling the original image.

        :param input_image_path: Path to the input image file.
        :param scale_factor: Factor by which to scale the image. Default is 2.0 for retina display.
        :return: Path to the newly created retina-ready image.
        """
        try:
            # Open the original image
            with Image.open(input_image_path) as img:
                # Calculate new dimensions
                new_dimensions = (int(img.width * scale_factor), int(img.height * scale_factor))
                
                # Resize the image
                retina_image = img.resize(new_dimensions, Image.LANCZOS)
                
                # Construct output path
                base_name = os.path.basename(input_image_path)
                output_path = os.path.join(self.output_directory, f"retina_{base_name}")
                
                # Save the retina-ready image
                retina_image.save(output_path)
                return output_path
        except Exception as e:
            print(f"Error creating retina image: {e}")
            return ""

    def create_retina_text_image(self, text: str, font_path: str, font_size: int = 40, scale_factor: float = 2.0) -> str:
        """
        Creates an image with text rendered in a retina-ready format.

        :param text: Text to be rendered.
        :param font_path: Path to the TTF font file to be used.
        :param font_size: Base font size. Default is 40.
        :param scale_factor: Factor by which to scale the text image. Default is 2.0.
        :return: Path to the newly created text image.
        """
        try:
            # Load the font with the specified size
            font = ImageFont.truetype(font_path, int(font_size * scale_factor))
            
            # Calculate text size and create an image
            text_width, text_height = font.getsize(text)
            img = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Render the text onto the image
            draw.text((0, 0), text, font=font, fill="black")

            # Construct output path
            output_path = os.path.join(self.output_directory, f"text_image_{text.replace(' ', '_')}.png")
            
            # Save the text image
            img.save(output_path)
            return output_path
        except Exception as e:
            print(f"Error creating text image: {e}")
            return ""

# Usage example
if __name__ == "__main__":
    # Specify an output directory for processed images
    output_dir = 'output_images'
    
    # Create an instance of the ImageProcessor
    processor = ImageProcessor(output_directory=output_dir)
    
    # Create a retina-ready image
    retina_image_path = processor.create_retina_image('input_image.jpg')
    print(f"Retina image saved at: {retina_image_path}")
    
    # Create a retina text image
    text_image_path = processor.create_retina_text_image('Hello, World!', 'path/to/font.ttf')
    print(f"Text image saved at: {text_image_path}")
```
