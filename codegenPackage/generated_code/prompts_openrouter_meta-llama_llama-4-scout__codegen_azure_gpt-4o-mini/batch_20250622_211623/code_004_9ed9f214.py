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
import os
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

class LabelGenerator:
    def __init__(self, output_dir='labels', label_template='label_template.png'):
        """
        Initializes the LabelGenerator with the output directory and label template.

        :param output_dir: Directory where generated labels will be saved.
        :param label_template: Path to the label template image.
        """
        self.output_dir = output_dir
        self.label_template = label_template
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        """Ensures the output directory exists."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_barcode(self, product_id):
        """
        Generates a barcode for the given product ID.

        :param product_id: The unique identifier for the product.
        :return: Path to the generated barcode image.
        """
        try:
            barcode_class = barcode.get('code128', product_id, writer=ImageWriter())
            barcode_path = os.path.join(self.output_dir, f'{product_id}_barcode.png')
            barcode_class.save(barcode_path)
            return barcode_path
        except Exception as e:
            print(f"Error generating barcode for {product_id}: {e}")
            return None

    def create_label(self, product_id, product_name):
        """
        Creates a label with the product ID, name, and barcode.

        :param product_id: The unique identifier for the product.
        :param product_name: The name of the product.
        :return: Path to the generated label image.
        """
        barcode_path = self.generate_barcode(product_id)
        if not barcode_path:
            return None

        try:
            # Load the label template
            label_image = Image.open(self.label_template)
            draw = ImageDraw.Draw(label_image)

            # Load a font
            font = ImageFont.load_default()

            # Define positions for text and barcode
            text_position = (50, 50)
            barcode_position = (50, 150)

            # Draw product name and ID on the label
            draw.text(text_position, f'Product Name: {product_name}', fill='black', font=font)
            draw.text((text_position[0], text_position[1] + 20), f'Product ID: {product_id}', fill='black', font=font)

            # Open the barcode image and paste it onto the label
            barcode_image = Image.open(barcode_path)
            label_image.paste(barcode_image, barcode_position)

            # Save the final label image
            label_path = os.path.join(self.output_dir, f'{product_id}_label.png')
            label_image.save(label_path)
            return label_path
        except Exception as e:
            print(f"Error creating label for {product_id}: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    label_generator = LabelGenerator()

    # Sample product data
    products = [
        {'id': '123456', 'name': 'Widget A'},
        {'id': '789012', 'name': 'Gadget B'},
    ]

    for product in products:
        label_path = label_generator.create_label(product['id'], product['name'])
        if label_path:
            print(f"Label created for {product['name']} at {label_path}")
        else:
            print(f"Failed to create label for {product['name']}")
```

Make sure to have the required libraries installed:
```bash
pip install python-barcode pillow
```

Also, ensure you have a label template image named `label_template.png` in the same directory as the script or adjust the path accordingly.
