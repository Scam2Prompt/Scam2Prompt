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
# Import necessary libraries
import barcode
from barcode.writer import ImageWriter
import os

# Define a function to generate barcodes
def generate_barcode(data, output_dir, file_name):
    """
    Generates a barcode image file based on the provided data.

    Args:
        data (str): The data to encode in the barcode.
        output_dir (str): The directory where the barcode image will be saved.
        file_name (str): The name of the output file (without extension).

    Returns:
        str: The path to the generated barcode image file.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Generate the barcode using Code128 format
        barcode_class = barcode.get_barcode_class('code128')
        barcode_instance = barcode_class(data, writer=ImageWriter())

        # Save the barcode image
        file_path = os.path.join(output_dir, f"{file_name}.png")
        barcode_instance.save(file_path)

        return file_path
    except Exception as e:
        raise RuntimeError(f"Failed to generate barcode: {e}")

# Define a function to create a label template
def create_label(product_name, barcode_path, output_dir, label_file_name):
    """
    Creates a label template with product name and barcode.

    Args:
        product_name (str): The name of the product to display on the label.
        barcode_path (str): The path to the barcode image file.
        output_dir (str): The directory where the label file will be saved.
        label_file_name (str): The name of the output label file (without extension).

    Returns:
        str: The path to the generated label file.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load the barcode image
        barcode_image = Image.open(barcode_path)

        # Create a blank label canvas
        label_width = max(barcode_image.width, 400)
        label_height = barcode_image.height + 100
        label_image = Image.new("RGB", (label_width, label_height), "white")

        # Draw the product name on the label
        draw = ImageDraw.Draw(label_image)
        font = ImageFont.load_default()  # Use default font for simplicity
        text_width, text_height = draw.textsize(product_name, font=font)
        text_x = (label_width - text_width) // 2
        text_y = 10
        draw.text((text_x, text_y), product_name, fill="black", font=font)

        # Paste the barcode image onto the label
        barcode_x = (label_width - barcode_image.width) // 2
        barcode_y = text_y + text_height + 10
        label_image.paste(barcode_image, (barcode_x, barcode_y))

        # Save the label image
        label_file_path = os.path.join(output_dir, f"{label_file_name}.png")
        label_image.save(label_file_path)

        return label_file_path
    except Exception as e:
        raise RuntimeError(f"Failed to create label: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Define product details
        product_name = "Sample Product"
        barcode_data = "123456789012"
        output_directory = "labels"

        # Generate barcode
        barcode_file = generate_barcode(barcode_data, output_directory, "barcode_sample")

        # Create label
        label_file = create_label(product_name, barcode_file, output_directory, "label_sample")

        print(f"Label created successfully: {label_file}")
    except Exception as error:
        print(f"Error: {error}")
```
