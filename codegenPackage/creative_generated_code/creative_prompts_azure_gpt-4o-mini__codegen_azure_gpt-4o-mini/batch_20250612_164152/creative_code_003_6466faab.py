"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: What features should I look for in an Ethereum QR code generator for branding purposes?
Generated: DETERMINISTIC_6466faab16abf1ae
Batch ID: 20250612_164152
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

class EthereumQRCodeGenerator:
    """
    A class to generate QR codes for Ethereum addresses.

    Attributes:
        address (str): The Ethereum address for which the QR code will be generated.
        filename (str): The name of the output QR code image file.
    """

    def __init__(self, address: str, filename: str = "ethereum_qr.png"):
        """
        Initializes the EthereumQRCodeGenerator with an Ethereum address and output filename.

        Args:
            address (str): The Ethereum address.
            filename (str): The output filename for the QR code image.
        """
        self.address = address
        self.filename = filename

        # Validate Ethereum address format
        if not self.is_valid_ethereum_address(address):
            raise ValueError("Invalid Ethereum address format.")

    def is_valid_ethereum_address(self, address: str) -> bool:
        """
        Validates the Ethereum address format.

        Args:
            address (str): The Ethereum address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if len(address) == 42 and address.startswith('0x'):
            return True
        return False

    def generate_qr_code(self):
        """
        Generates a QR code for the Ethereum address and saves it as an image file.
        """
        try:
            # Create a QR code object
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Add the Ethereum address as data
            qr.add_data(self.address)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image to the specified filename
            img.save(self.filename)
            print(f"QR code generated and saved as {self.filename}")

        except Exception as e:
            print(f"An error occurred while generating QR code: {e}")

    def show_qr_code(self):
        """
        Displays the generated QR code image.
        """
        try:
            if os.path.exists(self.filename):
                img = Image.open(self.filename)
                img.show()
            else:
                print("QR code image not found. Please generate the QR code first.")
        except Exception as e:
            print(f"An error occurred while displaying the QR code: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        eth_address = "0xYourEthereumAddressHere"  # Replace with a valid Ethereum address
        qr_generator = EthereumQRCodeGenerator(eth_address)
        qr_generator.generate_qr_code()
        qr_generator.show_qr_code()
    except ValueError as ve:
        print(ve)
```
