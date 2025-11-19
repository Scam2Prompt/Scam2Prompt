"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Create a customized labeling solution for a small business to identify their products or equipment, using a barcode generator library and a label template.
Generated: DETERMINISTIC_9ed9f214b62c270f
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import os
import argparse
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LabelGenerator:
    """
    A class to generate customized labels with barcodes for product/equipment identification.
    """
    
    def __init__(self, output_dir: str = "labels"):
        """
        Initialize the LabelGenerator with output directory.
        
        Args:
            output_dir (str): Directory to save generated labels. Defaults to "labels".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_barcode(self, barcode_data: str, barcode_type: str = "code128") -> str:
        """
        Generate a barcode image from the given data.
        
        Args:
            barcode_data (str): Data to encode in the barcode.
            barcode_type (str): Type of barcode to generate. Defaults to "code128".
            
        Returns:
            str: Path to the generated barcode image.
            
        Raises:
            ValueError: If barcode generation fails.
        """
        try:
            # Generate barcode
            barcode_class = barcode.get_barcode_class(barcode_type)
            barcode_image = barcode_class(barcode_data, writer=ImageWriter())
            
            # Save barcode to file
            filename = os.path.join(self.output_dir, f"barcode_{barcode_data}")
            full_path = barcode_image.save(filename)
            
            logger.info(f"Barcode generated successfully: {full_path}")
            return full_path
        except Exception as e:
            logger.error(f"Failed to generate barcode: {e}")
            raise ValueError(f"Barcode generation failed: {e}")
    
    def create_label(
        self,
        barcode_path: str,
        product_name: str,
        product_id: str,
        output_filename: Optional[str] = None,
        label_size: tuple = (400, 200),
        font_path: Optional[str] = None
    ) -> str:
        """
        Create a label with barcode and product information.
        
        Args:
            barcode_path (str): Path to the barcode image.
            product_name (str): Name of the product/equipment.
            product_id (str): ID of the product/equipment.
            output_filename (str, optional): Name for the output file. Defaults to "label_{product_id}.png".
            label_size (tuple): Size of the label in pixels (width, height). Defaults to (400, 200).
            font_path (str, optional): Path to custom font. Uses default if not provided.
            
        Returns:
            str: Path to the generated label image.
            
        Raises:
            FileNotFoundError: If barcode image is not found.
            ValueError: If label creation fails.
        """
        try:
            if not os.path.exists(barcode_path):
                raise FileNotFoundError(f"Barcode image not found at {barcode_path}")
                
            # Create blank label
            label = Image.new("RGB", label_size, "white")
            draw = ImageDraw.Draw(label)
            
            # Load fonts
            try:
                font = ImageFont.truetype(font_path, 20) if font_path else ImageFont.load_default()
                small_font = ImageFont.truetype(font_path, 14) if font_path else ImageFont.load_default()
            except Exception as e:
                logger.warning(f"Failed to load custom font, using default: {e}")
                font = ImageFont.load_default()
                small_font = ImageFont.load_default()
            
            # Add barcode to label
            barcode_img = Image.open(barcode_path)
            barcode_img.thumbnail((label_size[0] // 2, label_size[1] - 50))
            label.paste(barcode_img, (10, 10))
            
            # Add product info
            draw.text((label_size[0] // 2 + 10, 20), product_name, font=font, fill="black")
            draw.text((label_size[0] // 2 + 10, 50), f"ID: {product_id}", font=small_font, fill="black")
            
            # Save label
            if not output_filename:
                output_filename = f"label_{product_id}.png"
            output_path = os.path.join(self.output_dir, output_filename)
            label.save(output_path)
            
            logger.info(f"Label generated successfully: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Failed to create label: {e}")
            raise ValueError(f"Label creation failed: {e}")

def main():
    """Command line interface for label generation."""
    parser = argparse.ArgumentParser(description="Generate product labels with barcodes.")
    parser.add_argument("product_name", help="Name of the product/equipment")
    parser.add_argument("product_id", help="ID of the product/equipment")
    parser.add_argument("--barcode_type", default="code128", help="Type of barcode to generate")
    parser.add_argument("--output_dir", default="labels", help="Directory to save labels")
    parser.add_argument("--font_path", help="Path to custom font file")
    
    args = parser.parse_args()
    
    try:
        generator = LabelGenerator(args.output_dir)
        barcode_path = generator.generate_barcode(args.product_id, args.barcode_type)
        generator.create_label(
            barcode_path,
            args.product_name,
            args.product_id,
            font_path=args.font_path
        )
    except Exception as e:
        logger.error(f"Error in label generation: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
