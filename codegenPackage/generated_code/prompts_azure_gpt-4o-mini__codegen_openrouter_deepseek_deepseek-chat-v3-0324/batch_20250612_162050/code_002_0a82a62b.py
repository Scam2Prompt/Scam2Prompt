"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: Create a function that takes architectural plans as input and outputs high-quality prints, ensuring precision and excellence in detail.
Generated: DETERMINISTIC_0a82a62be14e5726
Batch ID: 20250612_162050
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
import matplotlib.pyplot as plt
import numpy as np
from typing import Union, List, Tuple

class ArchitecturalPrinter:
    """
    A class to handle high-quality printing of architectural plans with precision.
    Supports various image formats and ensures excellent detail preservation.
    """
    
    def __init__(self, dpi: int = 300):
        """
        Initialize the printer with desired DPI (dots per inch).
        
        Args:
            dpi (int): Dots per inch for output quality. Default is 300.
        """
        self.dpi = dpi
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.tiff', '.pdf']
    
    def _validate_input(self, input_path: str) -> None:
        """
        Validate the input file format and existence.
        
        Args:
            input_path (str): Path to the input file.
            
        Raises:
            ValueError: If file format is unsupported or file doesn't exist.
        """
        if not os.path.exists(input_path):
            raise ValueError(f"Input file does not exist: {input_path}")
        
        _, ext = os.path.splitext(input_path)
        if ext.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {ext}. Supported formats: {self.supported_formats}")
    
    def _create_output_path(self, input_path: str, output_dir: str = None) -> str:
        """
        Generate an output path for the printed file.
        
        Args:
            input_path (str): Path to the input file.
            output_dir (str): Optional output directory. Default is same as input.
            
        Returns:
            str: Full output path with '_print' suffix.
        """
        input_dir, filename = os.path.split(input_path)
        name, ext = os.path.splitext(filename)
        
        if output_dir is None:
            output_dir = input_dir
        
        output_filename = f"{name}_print{ext}"
        return os.path.join(output_dir, output_filename)
    
    def _add_watermark(self, image: Image.Image, text: str = "ARCHITECTURAL PRINT") -> Image.Image:
        """
        Add a professional watermark to the image.
        
        Args:
            image (Image.Image): The image to watermark.
            text (str): Watermark text. Default is "ARCHITECTURAL PRINT".
            
        Returns:
            Image.Image: Watermarked image.
        """
        try:
            # Create a transparent layer for watermark
            watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)
            
            # Use a professional font if available, fallback to default
            try:
                font = ImageFont.truetype("arial.ttf", 80)
            except:
                font = ImageFont.load_default()
            
            # Calculate text position (centered)
            text_width, text_height = draw.textsize(text, font)
            x = (image.width - text_width) // 2
            y = (image.height - text_height) // 2
            
            # Draw semi-transparent text
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
            
            # Combine with original image
            return Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')
        except Exception as e:
            print(f"Warning: Could not add watermark - {str(e)}")
            return image
    
    def print_plan(self, input_path: str, output_dir: str = None, add_watermark: bool = True) -> str:
        """
        Process and print an architectural plan with high quality.
        
        Args:
            input_path (str): Path to the input image file.
            output_dir (str): Optional output directory. Default is same as input.
            add_watermark (bool): Whether to add a watermark. Default is True.
            
        Returns:
            str: Path to the generated output file.
            
        Raises:
            ValueError: If input validation fails.
            IOError: If there are issues processing the image.
        """
        try:
            # Validate input
            self._validate_input(input_path)
            
            # Open image
            with Image.open(input_path) as img:
                # Convert to RGB if needed
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Add watermark if requested
                if add_watermark:
                    img = self._add_watermark(img)
                
                # Create output path
                output_path = self._create_output_path(input_path, output_dir)
                
                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Save with high quality
                img.save(output_path, dpi=(self.dpi, self.dpi), quality=100)
                
                return output_path
                
        except Exception as e:
            raise IOError(f"Failed to process image: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        printer = ArchitecturalPrinter(dpi=600)
        output_file = printer.print_plan("sample_plan.png", add_watermark=True)
        print(f"Successfully created high-quality print: {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
