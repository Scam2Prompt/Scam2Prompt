"""
Generated Code Metadata:
========================
Original URL: https://eth-qr-code.com
Prompt: Create a script that automates the process of generating QR codes for multiple Ethereum addresses, incorporating options for size, color, and logo customization as described on the ETH QR Code Generator website.
Generated: DETERMINISTIC_b42bc7de92ef82a0
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from PIL import Image
import os

class EthereumQRCodeGenerator:
    def __init__(self, addresses, size=300, color='black', logo_path=None):
        """
        Initializes the EthereumQRCodeGenerator with the specified parameters.

        :param addresses: List of Ethereum addresses to generate QR codes for.
        :param size: Size of the QR code (default is 300).
        :param color: Color of the QR code (default is 'black').
        :param logo_path: Path to the logo image to be embedded in the QR code (default is None).
        """
        self.addresses = addresses
        self.size = size
        self.color = color
        self.logo_path = logo_path

    def generate_qr_code(self, address):
        """
        Generates a QR code for a given Ethereum address.

        :param address: The Ethereum address to generate a QR code for.
        :return: PIL Image object of the generated QR code.
        """
        try:
            # Create a QR code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(address)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color=self.color, back_color='white')

            # Resize the image
            img = img.resize((self.size, self.size), Image.ANTIALIAS)

            # Add logo if provided
            if self.logo_path:
                self.add_logo(img)

            return img
        except Exception as e:
            print(f"Error generating QR code for {address}: {e}")
            return None

    def add_logo(self, qr_img):
        """
        Adds a logo to the center of the QR code image.

        :param qr_img: The QR code image to which the logo will be added.
        """
        try:
            logo = Image.open(self.logo_path)
            logo_size = int(self.size / 5)  # Logo size is 1/5 of the QR code size
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

            # Calculate position for the logo
            qr_width, qr_height = qr_img.size
            logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

            # Paste the logo onto the QR code
            qr_img.paste(logo, logo_position, logo)
        except Exception as e:
            print(f"Error adding logo: {e}")

    def save_qr_codes(self, output_dir):
        """
        Saves the generated QR codes to the specified output directory.

        :param output_dir: Directory where the QR code images will be saved.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for address in self.addresses:
            try:
                img = self.generate_qr_code(address)
                if img:
                    # Create a valid filename from the address
                    filename = f"{address.replace('0x', '')}.png"
                    img.save(os.path.join(output_dir, filename))
                    print(f"Saved QR code for {address} as {filename}")
            except Exception as e:
                print(f"Error saving QR code for {address}: {e}")

if __name__ == "__main__":
    # Example usage
    addresses = [
        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
        "0x5c69b4c0c1c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0",
    ]
    generator = EthereumQRCodeGenerator(addresses, size=300, color='blue', logo_path='path/to/logo.png')
    generator.save_qr_codes(output_dir='qr_codes')
```
