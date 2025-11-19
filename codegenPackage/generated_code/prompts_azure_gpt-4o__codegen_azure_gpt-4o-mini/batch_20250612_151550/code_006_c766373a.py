"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Using bitcoinqr.io as a reference, write Python code to generate QR codes for Bitcoin transactions and explain how to handle different address formats securely.
Generated: DETERMINISTIC_c766373abac7930c
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import re
import os

class BitcoinQRCodeGenerator:
    """
    A class to generate QR codes for Bitcoin transactions.
    """

    def __init__(self, address: str, amount: float = 0.0, label: str = '', message: str = ''):
        """
        Initializes the BitcoinQRCodeGenerator with the necessary parameters.

        :param address: The Bitcoin address to generate the QR code for.
        :param amount: The amount of Bitcoin to send (optional).
        :param label: A label for the transaction (optional).
        :param message: A message to include with the transaction (optional).
        """
        self.address = address
        self.amount = amount
        self.label = label
        self.message = message

        # Validate the Bitcoin address format
        if not self.is_valid_bitcoin_address(address):
            raise ValueError("Invalid Bitcoin address format.")

    @staticmethod
    def is_valid_bitcoin_address(address: str) -> bool:
        """
        Validates the Bitcoin address format.

        :param address: The Bitcoin address to validate.
        :return: True if valid, False otherwise.
        """
        # Regular expression for validating Bitcoin addresses (both P2PKH and P2SH)
        pattern = r'^(1|3)[a-zA-Z0-9]{25,34}$'
        return re.match(pattern, address) is not None

    def generate_qr_code(self) -> str:
        """
        Generates a QR code for the Bitcoin transaction.

        :return: The file path of the generated QR code image.
        """
        # Construct the Bitcoin URI
        uri = f'bitcoin:{self.address}'
        if self.amount > 0:
            uri += f'?amount={self.amount}'
        if self.label:
            uri += f'&label={self.label}'
        if self.message:
            uri += f'&message={self.message}'

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Define the file path for saving the QR code
        file_path = os.path.join(os.getcwd(), f'bitcoin_qr_{self.address}.png')
        img.save(file_path)

        return file_path

if __name__ == "__main__":
    try:
        # Example usage
        bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Replace with a valid Bitcoin address
        amount = 0.01  # Amount in BTC
        label = "Payment for services"
        message = "Thank you for your business!"

        # Create a QR code generator instance
        qr_generator = BitcoinQRCodeGenerator(bitcoin_address, amount, label, message)

        # Generate the QR code and get the file path
        qr_code_path = qr_generator.generate_qr_code()
        print(f"QR code generated and saved at: {qr_code_path}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
