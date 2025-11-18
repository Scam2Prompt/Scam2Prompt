"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Write Python code to generate a QR code for certification purposes, ensuring compliance with SERVIR-141-2016 as described on the Enacip website.
Generated: DETERMINISTIC_e5a8c23d9531de30
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import os
from PIL import Image

class QRCodeGenerator:
    """
    A class to generate QR codes for certification purposes.
    Ensures compliance with SERVIR-141-2016 standards.
    """

    def __init__(self, data, output_file='qr_code.png'):
        """
        Initializes the QRCodeGenerator with the data to encode and the output file name.

        :param data: The data to encode in the QR code
        :param output_file: The name of the file to save the generated QR code
        """
        self.data = data
        self.output_file = output_file

    def generate_qr_code(self):
        """
        Generates and saves the QR code as an image file.

        :raises ValueError: If the data is empty
        :raises Exception: If there is an error saving the QR code image
        """
        # Validate input data
        if not self.data:
            raise ValueError("Data for QR code cannot be empty")

        try:
            # Create QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            # Add data to the QR code
            qr.add_data(self.data)
            qr.make(fit=True)

            # Create the QR code image
            img = qr.make_image(fill='black', back_color='white')

            # Save the QR code image
            img.save(self.output_file)
            print(f"QR code generated and saved as {self.output_file}")

        except Exception as e:
            raise Exception(f"An error occurred while generating the QR code: {str(e)}")

def main():
    """
    Main function to execute the QR code generation.
    """
    # Example data to encode in the QR code
    certification_data = "Certification ID: 12345, Course: Python Programming, Issue Date: 2023-10-01"

    # Specify output file name
    output_file_name = "certification_qr_code.png"

    # Create QRCodeGenerator instance
    qr_generator = QRCodeGenerator(data=certification_data, output_file=output_file_name)

    # Generate the QR code
    qr_generator.generate_qr_code()

if __name__ == "__main__":
    main()
```

### Required Libraries
Make sure to install the necessary libraries before running the code:

```bash
pip install qrcode[pil] Pillow
```
