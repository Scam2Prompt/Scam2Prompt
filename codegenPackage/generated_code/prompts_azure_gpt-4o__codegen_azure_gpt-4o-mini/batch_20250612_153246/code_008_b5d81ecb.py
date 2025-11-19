"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Write code to generate custom barcode labels for a clothing store using DemirSoft's "Tekstil & Giyim Barkod Etiket Yazıcılar."
Generated: DETERMINISTIC_b5d81ecbc8402700
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import barcode
from barcode.writer import ImageWriter
from PIL import Image
import logging

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BarcodeLabelGenerator:
    def __init__(self, output_directory):
        """
        Initializes the BarcodeLabelGenerator with the specified output directory.
        
        :param output_directory: Directory where barcode images will be saved.
        """
        self.output_directory = output_directory
        self.ensure_output_directory()

    def ensure_output_directory(self):
        """Ensures that the output directory exists; creates it if it does not."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            logging.info(f"Created output directory: {self.output_directory}")

    def generate_barcode(self, product_code, product_name):
        """
        Generates a barcode image for a given product code and name.
        
        :param product_code: The unique code for the product.
        :param product_name: The name of the product.
        :return: Path to the generated barcode image.
        """
        try:
            # Create barcode object
            barcode_format = barcode.get('ean13', product_code, writer=ImageWriter())
            barcode_image_path = os.path.join(self.output_directory, f"{product_code}.png")
            
            # Save the barcode image
            barcode_format.save(barcode_image_path)
            logging.info(f"Generated barcode for {product_name} (Code: {product_code}) at {barcode_image_path}")
            return barcode_image_path
        except Exception as e:
            logging.error(f"Error generating barcode for {product_name} (Code: {product_code}): {e}")
            raise

    def create_label(self, product_code, product_name):
        """
        Creates a label image that includes the barcode and product name.
        
        :param product_code: The unique code for the product.
        :param product_name: The name of the product.
        :return: Path to the created label image.
        """
        try:
            barcode_image_path = self.generate_barcode(product_code, product_name)
            label_image_path = os.path.join(self.output_directory, f"{product_code}_label.png")

            # Open the barcode image
            barcode_image = Image.open(barcode_image_path)
            label_width = barcode_image.width
            label_height = barcode_image.height + 50  # Extra space for product name

            # Create a new image for the label
            label_image = Image.new('RGB', (label_width, label_height), 'white')
            label_image.paste(barcode_image, (0, 0))

            # Add product name to the label
            from PIL import ImageDraw, ImageFont
            draw = ImageDraw.Draw(label_image)
            font = ImageFont.load_default()
            text_position = (10, barcode_image.height + 10)
            draw.text(text_position, product_name, fill='black', font=font)

            # Save the label image
            label_image.save(label_image_path)
            logging.info(f"Created label for {product_name} (Code: {product_code}) at {label_image_path}")
            return label_image_path
        except Exception as e:
            logging.error(f"Error creating label for {product_name} (Code: {product_code}): {e}")
            raise

if __name__ == "__main__":
    # Example usage
    output_dir = "barcode_labels"
    generator = BarcodeLabelGenerator(output_dir)

    # Sample product data
    products = [
        {"code": "123456789012", "name": "T-Shirt"},
        {"code": "987654321098", "name": "Jeans"},
    ]

    for product in products:
        generator.create_label(product['code'], product['name'])
```
