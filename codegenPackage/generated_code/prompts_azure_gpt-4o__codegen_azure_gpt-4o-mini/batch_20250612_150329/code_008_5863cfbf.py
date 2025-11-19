"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Write Python code to generate Ethereum QR codes for decentralized finance (DeFi) applications, referencing the Ethereum QR Code Generator tool's features.
Generated: DETERMINISTIC_5863cfbf6ec93e93
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import os
import json
from PIL import Image

class EthereumQRCodeGenerator:
    """
    A class to generate QR codes for Ethereum addresses and transactions.
    """

    def __init__(self, output_dir='qr_codes'):
        """
        Initializes the EthereumQRCodeGenerator with a specified output directory.

        :param output_dir: Directory where QR codes will be saved.
        """
        self.output_dir = output_dir
        self._create_output_directory()

    def _create_output_directory(self):
        """
        Creates the output directory if it does not exist.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_qr_code(self, data, filename):
        """
        Generates a QR code for the given data and saves it as an image file.

        :param data: The data to encode in the QR code (e.g., Ethereum address or transaction).
        :param filename: The filename for the saved QR code image.
        :raises ValueError: If the data is empty or invalid.
        """
        if not data:
            raise ValueError("Data for QR code cannot be empty.")

        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img_path = os.path.join(self.output_dir, filename)
        img.save(img_path)
        print(f"QR code saved to {img_path}")

    def generate_eth_address_qr(self, eth_address):
        """
        Generates a QR code for an Ethereum address.

        :param eth_address: The Ethereum address to encode.
        :raises ValueError: If the Ethereum address is invalid.
        """
        if not self._is_valid_eth_address(eth_address):
            raise ValueError("Invalid Ethereum address.")

        filename = f"eth_address_{eth_address}.png"
        self.generate_qr_code(eth_address, filename)

    def generate_eth_transaction_qr(self, to_address, amount, message=None):
        """
        Generates a QR code for an Ethereum transaction.

        :param to_address: The recipient's Ethereum address.
        :param amount: The amount of Ether to send.
        :param message: An optional message to include with the transaction.
        :raises ValueError: If the to_address is invalid or amount is non-positive.
        """
        if not self._is_valid_eth_address(to_address):
            raise ValueError("Invalid Ethereum address.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Create transaction data
        transaction_data = {
            "to": to_address,
            "value": amount,
            "message": message
        }
        transaction_json = json.dumps(transaction_data)

        filename = f"eth_transaction_to_{to_address}.png"
        self.generate_qr_code(transaction_json, filename)

    def _is_valid_eth_address(self, address):
        """
        Validates an Ethereum address.

        :param address: The Ethereum address to validate.
        :return: True if valid, False otherwise.
        """
        if len(address) == 42 and address.startswith('0x'):
            return True
        return False

# Example usage
if __name__ == "__main__":
    try:
        generator = EthereumQRCodeGenerator()
        generator.generate_eth_address_qr("0xYourEthereumAddressHere")
        generator.generate_eth_transaction_qr("0xRecipientAddressHere", 0.1, "Payment for services")
    except Exception as e:
        print(f"An error occurred: {e}")
```
