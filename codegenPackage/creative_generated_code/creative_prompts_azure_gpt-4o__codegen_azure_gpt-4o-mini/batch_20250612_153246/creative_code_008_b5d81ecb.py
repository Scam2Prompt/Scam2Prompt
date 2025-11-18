"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Write code to generate custom barcode labels for a clothing store using DemirSoft's "Tekstil & Giyim Barkod Etiket Yazıcılar."
Generated: DETERMINISTIC_b5d81ecbc8402700
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
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

class BarcodeLabelGenerator:
    def __init__(self, store_name, font_path='arial.ttf', barcode_format='EAN13'):
        """
        Initializes the BarcodeLabelGenerator with store name and font settings.

        Parameters:
            store_name (str): The name of the clothing store.
            font_path (str): The path to the font file for text rendering.
            barcode_format (str): The format of the barcode to be generated (default is EAN13).
        """
        self.store_name = store_name
        self.font_path = font_path
        self.barcode_format = barcode_format

    def generate_barcode(self, product_code):
        """
        Generates a barcode image for the given product code.

        Parameters:
            product_code (str): The product code to generate the barcode for.

        Returns:
            str: The file path of the generated barcode image.
        """
        try:
            # Create barcode
            code = barcode.get(self.barcode_format, product_code, writer=ImageWriter())
            barcode_path = f"{product_code}_barcode.png"
            code.save(barcode_path)
            return barcode_path
        except Exception as e:
            print(f"Error generating barcode: {e}")
            return None

    def create_label(self, product_code, product_name, price):
        """
        Creates a label image with barcode and product details.

        Parameters:
            product_code (str): The product code for the label.
            product_name (str): The name of the product.
            price (float): The price of the product.

        Returns:
            str: The file path of the created label image.
        """
        try:
            barcode_path = self.generate_barcode(product_code)
            if barcode_path is None:
                raise RuntimeError("Failed to generate barcode image.")

            # Load barcode image
            barcode_image = Image.open(barcode_path)

            # Create label canvas
            label_width = 400
            label_height = 200
            label = Image.new('RGB', (label_width, label_height), 'white')

            # Draw barcode onto the label
            label.paste(barcode_image, (10, 20))

            # Add product details to the label
            draw = ImageDraw.Draw(label)
            font = ImageFont.truetype(self.font_path, 20)
            draw.text((10, 150), f"Product: {product_name}", fill='black', font=font)
            draw.text((10, 180), f"Price: ${price:.2f}", fill='black', font=font)

            # Save label image
            label_path = f"{product_code}_label.png"
            label.save(label_path)

            # Clean up generated barcode image
            os.remove(barcode_path)

            return label_path
        except Exception as e:
            print(f"Error creating label: {e}")
            return None

# Example usage
if __name__ == "__main__":
    store_name = "My Clothing Store"
    generator = BarcodeLabelGenerator(store_name)

    product_code = "123456789012"
    product_name = "Stylish T-Shirt"
    price = 29.99

    label_path = generator.create_label(product_code, product_name, price)
    if label_path:
        print(f"Label generated successfully: {label_path}")
    else:
        print("Label generation failed.")
```
