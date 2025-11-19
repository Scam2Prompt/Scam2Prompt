"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a Python script to generate a customized plaque design with a company's logo and name using laser engraving on aluminum.
Generated: DETERMINISTIC_b5709f8aebc73c79
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from typing import Tuple, Optional

class PlaqueDesigner:
    """
    A class to generate customized plaque designs for laser engraving on aluminum.
    """
    
    def __init__(self, width: int = 600, height: int = 400, bg_color: Tuple[int, int, int] = (255, 255, 255)):
        """
        Initialize the plaque designer with dimensions and background color.
        
        Args:
            width: Width of the plaque in pixels
            height: Height of the plaque in pixels
            bg_color: Background color as RGB tuple
        """
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.image = Image.new('RGB', (width, height), bg_color)
        self.draw = ImageDraw.Draw(self.image)
        
    def add_logo(self, logo_path: str, position: Tuple[int, int], size: Tuple[int, int]) -> None:
        """
        Add a company logo to the plaque.
        
        Args:
            logo_path: Path to the logo image file
            position: (x, y) coordinates for top-left corner of logo
            size: (width, height) dimensions for the logo
        """
        try:
            logo = Image.open(logo_path)
            logo = logo.resize(size)
            self.image.paste(logo, position)
        except FileNotFoundError:
            raise FileNotFoundError(f"Logo file not found at {logo_path}")
        except Exception as e:
            raise Exception(f"Error processing logo: {str(e)}")
            
    def add_text(self, text: str, position: Tuple[int, int], font_path: str, 
                 font_size: int, color: Tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Add text to the plaque.
        
        Args:
            text: Text to display
            position: (x, y) coordinates for the text
            font_path: Path to the font file
            font_size: Size of the font in points
            color: Text color as RGB tuple
        """
        try:
            font = ImageFont.truetype(font_path, font_size)
            self.draw.text(position, text, fill=color, font=font)
        except IOError:
            raise IOError(f"Font file not found at {font_path}")
        except Exception as e:
            raise Exception(f"Error adding text: {str(e)}")
            
    def add_border(self, thickness: int = 5, color: Tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Add a border around the plaque.
        
        Args:
            thickness: Thickness of the border in pixels
            color: Border color as RGB tuple
        """
        self.draw.rectangle([(0, 0), (self.width-1, self.height-1)], outline=color, width=thickness)
        
    def save_design(self, output_path: str, format: str = 'PNG') -> None:
        """
        Save the plaque design to a file.
        
        Args:
            output_path: Path to save the design
            format: Image format (e.g., 'PNG', 'JPEG')
        """
        try:
            self.image.save(output_path, format)
        except Exception as e:
            raise Exception(f"Error saving design: {str(e)}")
            
    def generate_laser_instructions(self, output_path: str, power: int = 80, speed: int = 100) -> None:
        """
        Generate a simple text file with laser engraving instructions.
        
        Args:
            output_path: Path to save the instructions
            power: Laser power percentage (0-100)
            speed: Laser speed percentage (0-100)
        """
        try:
            with open(output_path, 'w') as f:
                f.write(f"Laser Engraving Instructions:\n")
                f.write(f"Material: Aluminum\n")
                f.write(f"Power: {power}%\n")
                f.write(f"Speed: {speed}%\n")
                f.write(f"Passes: 1\n")
        except Exception as e:
            raise Exception(f"Error generating laser instructions: {str(e)}")

def main():
    try:
        # Example usage
        designer = PlaqueDesigner(width=800, height=600)
        
        # Add logo (replace with actual path)
        designer.add_logo("company_logo.png", position=(50, 50), size=(200, 200))
        
        # Add company name
        designer.add_text("ACME Corporation", position=(300, 100), 
                         font_path="arial.ttf", font_size=48)
        
        # Add border
        designer.add_border(thickness=10, color=(50, 50, 50))
        
        # Save design
        designer.save_design("plaque_design.png")
        
        # Generate laser instructions
        designer.generate_laser_instructions("laser_instructions.txt")
        
        print("Plaque design generated successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
