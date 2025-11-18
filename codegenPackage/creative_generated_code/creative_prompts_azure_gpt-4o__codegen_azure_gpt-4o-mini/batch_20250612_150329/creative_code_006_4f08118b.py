"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Suggest tools or libraries for generating Ethereum QR codes that can be embedded on websites, specifically referencing the functionality outlined on the Ethereum QR Code Generator page.
Generated: DETERMINISTIC_4f08118b5afca45c
Batch ID: 20250612_150329
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
    A class to generate Ethereum QR codes for wallet addresses and transactions.
    """

    def __init__(self, address: str):
        """
        Initializes the EthereumQRCodeGenerator with a wallet address.

        :param address: A valid Ethereum wallet address.
        """
        self.address = address

    def generate_qr_code(self, file_name: str, transaction_amount: float = None) -> None:
        """
        Generates a QR code for the Ethereum address with optional transaction amount.

        :param file_name: The name of the file to save the QR code image.
        :param transaction_amount: Optional amount to include in the QR code for transactions.
        """
        try:
            # Validate the Ethereum address
            self.validate_ethereum_address(self.address)
            
            # Create the payment URI
            uri = self.create_payment_uri(transaction_amount)
            
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

            # Save the image to the specified file
            img.save(file_name)
            print(f"QR code saved to {file_name}")

        except Exception as e:
            print(f"Error generating QR code: {e}")

    def create_payment_uri(self, amount: float) -> str:
        """
        Creates a payment URI for the Ethereum address.

        :param amount: The amount to be included in the URI, if any.
        :return: A formatted Ethereum payment URI.
        """
        if amount is not None:
            return f"ethereum:{self.address}?value={int(amount * 10**18)}"
        else:
            return f"ethereum:{self.address}"

    @staticmethod
    def validate_ethereum_address(address: str) -> None:
        """
        Validates the provided Ethereum address.

        :param address: The Ethereum address to validate.
        :raises ValueError: If the address is not valid.
        """
        if not isinstance(address, str) or len(address) != 42 or not address.startswith('0x'):
            raise ValueError("Invalid Ethereum address. Address must be a 42 character string starting with '0x'.")

# Example Usage
if __name__ == "__main__":
    # Define the Ethereum address
    eth_address = "0xYourEthereumAddressHere"

    # Create the QR Code generator
    qr_generator = EthereumQRCodeGenerator(eth_address)

    # Generate a QR code for the address (with optional transaction amount)
    qr_generator.generate_qr_code("ethereum_qr_code.png", transaction_amount=0.1)
```
