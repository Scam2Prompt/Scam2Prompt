"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Suggest tools or frameworks to implement QR code generation for inspection reports, inspired by the BeSoft App Vistoria's contestation area feature.
Generated: DETERMINISTIC_2c897807752f0e72
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from PIL import Image
import os

class QRCodeGenerator:
    """A class to generate QR codes for inspection reports."""

    def __init__(self, output_dir='qr_codes'):
        """
        Initialize the QRCodeGenerator.

        Args:
            output_dir (str): The directory where QR codes will be saved.
        """
        self.output_dir = output_dir
        self._create_output_dir()

    def _create_output_dir(self):
        """Create the output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_qr_code(self, data, file_name):
        """
        Generate a QR code for the given data and save it as an image file.

        Args:
            data (str): The data to encode in the QR code.
            file_name (str): The name of the output image file (without extension).

        Returns:
            str: The path to the saved QR code image.
        """
        try:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")

            # Construct file path
            file_path = os.path.join(self.output_dir, f"{file_name}.png")

            # Save the image
            img.save(file_path)
            return file_path
        except Exception as e:
            print(f"An error occurred while generating the QR code: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    generator = QRCodeGenerator()
    report_data = "Inspection Report - Vistoria Reference 123456"
    file_name = "inspection_report_123456"
    
    qr_code_path = generator.generate_qr_code(report_data, file_name)
    
    if qr_code_path:
        print(f"QR code generated and saved at: {qr_code_path}")
    else:
        print("Failed to generate QR code.")
```
