"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Develop a Python script to create templates for engraved plaques for machine tools, including material selection and text formatting, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_19312084ffd61d41
Batch ID: 20250612_153246
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

class PlaqueTemplate:
    """Class to create templates for engraved plaques."""
    
    def __init__(self, material: str, text: str, font_size: int = 24):
        """
        Initializes the plaque template with material type and text.
        
        Args:
            material (str): Type of material for the plaque.
            text (str): Text to be engraved on the plaque.
            font_size (int): Size of the font for the text.
        """
        self.material = material
        self.text = text
        self.font_size = font_size
        self.font_path = self._get_font_path()
        
    def _get_font_path(self) -> str:
        """Determines font path based on system OS."""
        if os.name == 'nt':  # Windows
            return "C:\\Windows\\Fonts\\Arial.ttf"
        elif os.name == 'posix':  # Unix/Linux
            return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        else:
            raise EnvironmentError("Unsupported OS for font path.")
        
    def create_template(self, width: int, height: int) -> Image:
        """
        Creates a plaque template image.
        
        Args:
            width (int): Width of the plaque in pixels.
            height (int): Height of the plaque in pixels.
        
        Returns:
            Image: A PIL Image object representing the plaque template.
        """
        # Create an image with a white background
        plaque_image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(plaque_image)
        
        # Load font
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            raise RuntimeError("Font file not found. Please check the font path.")
        
        # Add text to the center of the plaque
        text_width, text_height = draw.textsize(self.text, font)
        text_x = (width - text_width) / 2
        text_y = (height - text_height) / 2
        draw.text((text_x, text_y), self.text, fill='black', font=font)
        
        return plaque_image

def save_template(image: Image, filename: str) -> None:
    """
    Saves the plaque image to a file.
    
    Args:
        image (Image): The image object to save.
        filename (str): The filepath where the image will be saved.
    """
    try:
        image.save(filename)
        print(f"Template saved successfully as '{filename}'.")
    except Exception as e:
        print(f"Error saving the image: {e}")

def main():
    """Main function to create and save a plaque template."""
    # User-defined specifications
    material = "Aluminum"  # Example material
    text = "Engraved Plaque Example"
    width = 400
    height = 200
    
    # Create plaque template
    template = PlaqueTemplate(material, text)
    plaque_image = template.create_template(width, height)
    
    # Save the created template
    save_template(plaque_image, "plaque_template.png")

if __name__ == "__main__":
    main()
```
