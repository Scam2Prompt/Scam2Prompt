"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://filmdailyweb.com
Prompt: Write Python code to generate barcodes using a library or API, referencing the "Barcode Generator" guide from Film Daily Web.
Generated: DETERMINISTIC_6d786eabfcbdee5f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import barcode
from barcode.writer import ImageWriter
import os

class BarcodeGenerator:
    """
    A class to generate barcodes using the python-barcode library.
    """

    def __init__(self, output_directory='barcodes'):
        """
        Initializes the BarcodeGenerator with an output directory.

        :param output_directory: Directory where generated barcodes will be stored.
        """
        self.output_directory = output_directory
        self._create_output_directory()

    def _create_output_directory(self):
        """
        Creates the output directory if it does not exist.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_barcode(self, data, barcode_format='code128', filename=None):
        """
        Generates a barcode and saves it as an image file.

        :param data: Data to encode in the barcode.
        :param barcode_format: The format of the barcode (default is code128).
        :param filename: Optional filename for the saved barcode image.
        :return: Path to the generated barcode image.
        """
        try:
            # Generate barcode based on the specified format
            barcode_class = barcode.get(barcode_format)
            barcode_instance = barcode_class(data, writer=ImageWriter())

            # Define the filename if not provided
            if filename is None:
                filename = f"{data}.{barcode_format}"

            # Save the barcode image
            file_path = os.path.join(self.output_directory, filename)
            barcode_instance.save(file_path)

            return file_path

        except Exception as e:
            print(f"Error generating barcode: {e}")
            return None

if __name__ == "__main__":
    # Create an instance of the BarcodeGenerator
    barcode_gen = BarcodeGenerator()

    # Sample data to generate a barcode
    sample_data = "123456789012"
    
    # Generate a barcode and capture the file path
    barcode_image_path = barcode_gen.generate_barcode(sample_data)

    if barcode_image_path:
        print(f"Barcode generated successfully: {barcode_image_path}")
    else:
        print("Failed to generate barcode.")
```
