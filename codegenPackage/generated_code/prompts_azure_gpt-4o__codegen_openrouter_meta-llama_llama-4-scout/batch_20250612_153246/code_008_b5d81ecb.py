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
# barcode_label_generator.py

import os
from PIL import Image, ImageDraw, ImageFont

class BarcodeLabelGenerator:
    """
    Generates custom barcode labels for a clothing store using DemirSoft's 
    "Tekstil & Giyim Barkod Etiket Yazıcılar."
    """

    def __init__(self, 
                 barcode_data: str, 
                 product_name: str, 
                 product_code: str, 
                 size: str, 
                 color: str, 
                 label_width: int = 101, 
                 label_height: int = 30):
        """
        Initializes the BarcodeLabelGenerator.

        Args:
        - barcode_data (str): The barcode data to be encoded.
        - product_name (str): The name of the product.
        - product_code (str): The code of the product.
        - size (str): The size of the product.
        - color (str): The color of the product.
        - label_width (int): The width of the label in mm. Defaults to 101.
        - label_height (int): The height of the label in mm. Defaults to 30.
        """

        self.barcode_data = barcode_data
        self.product_name = product_name
        self.product_code = product_code
        self.size = size
        self.color = color
        self.label_width = label_width
        self.label_height = label_height

    def generate_barcode(self) -> Image:
        """
        Generates a barcode image using the provided barcode data.

        Returns:
        - Image: The generated barcode image.
        """

        # Using Code128 barcode font for encoding barcode data
        from barcode import Code128
        from barcode.writer import ImageWriter

        barcode = Code128(self.barcode_data, writer=ImageWriter())
        barcode_image = barcode.image

        return barcode_image

    def generate_label(self) -> Image:
        """
        Generates a custom barcode label.

        Returns:
        - Image: The generated label image.
        """

        # Create a new label image
        label_image = Image.new('RGB', (self.label_width * 5, self.label_height * 5), color = (73, 109, 137))
        d = ImageDraw.Draw(label_image)

        # Generate barcode image
        barcode_image = self.generate_barcode()
        barcode_image = barcode_image.resize((80, 20))
        label_image.paste(barcode_image, (10, 10))

        # Add product information
        font = ImageFont.load_default()
        d.text((10, 40), f"Product: {self.product_name}", fill=(255, 255, 0), font=font)
        d.text((10, 60), f"Code: {self.product_code}", fill=(255, 255, 0), font=font)
        d.text((10, 80), f"Size: {self.size}", fill=(255, 255, 0), font=font)
        d.text((10, 100), f"Color: {self.color}", fill=(255, 255, 0), font=font)

        return label_image

    def save_label(self, filename: str):
        """
        Saves the generated label to a file.

        Args:
        - filename (str): The filename to save the label.
        """

        try:
            label_image = self.generate_label()
            label_image.save(filename, 'png')
            print(f"Label saved to {filename}")
        except Exception as e:
            print(f"Error saving label: {str(e)}")


if __name__ == "__main__":
    generator = BarcodeLabelGenerator(
        barcode_data="1234567890123",
        product_name="T-Shirt",
        product_code="TS001",
        size="L",
        color="Blue"
    )

    generator.save_label("label.png")
```
