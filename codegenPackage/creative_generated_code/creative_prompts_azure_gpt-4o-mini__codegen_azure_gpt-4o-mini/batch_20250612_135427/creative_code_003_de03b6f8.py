"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: What features does the Bitcoin QR Code Generator offer for creating QR codes for Bitcoin, Ethereum, and other cryptocurrencies?
Generated: DETERMINISTIC_de03b6f889117bac
Batch ID: 20250612_135427
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
from typing import Optional

class CryptoQRCodeGenerator:
    """
    A class to generate QR codes for various cryptocurrencies such as Bitcoin and Ethereum.
    """

    def __init__(self):
        """
        Initializes the QR code generator.
        """
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate_qr_code(self, crypto_address: str, crypto_type: str, amount: Optional[float] = None) -> str:
        """
        Generates a QR code for the given cryptocurrency address and optionally an amount.

        :param crypto_address: The cryptocurrency address to encode in the QR code.
        :param crypto_type: The type of cryptocurrency (e.g., 'bitcoin', 'ethereum').
        :param amount: The amount of cryptocurrency to include (optional).
        :return: The filename of the generated QR code image.
        :raises ValueError: If the address is invalid or if the cryptocurrency type is unsupported.
        """

        # Validate cryptocurrency type
        supported_types = ['bitcoin', 'ethereum']
        if crypto_type.lower() not in supported_types:
            raise ValueError(f"Unsupported cryptocurrency type: {crypto_type}. Supported types are: {supported_types}")

        # Validate address
        if not self.is_valid_address(crypto_address, crypto_type):
            raise ValueError(f"Invalid address for {crypto_type}: {crypto_address}")

        # Prepare the QR code data
        qr_data = self.prepare_qr_data(crypto_address, crypto_type, amount)

        # Generate the QR code
        self.qr.add_data(qr_data)
        self.qr.make(fit=True)

        # Create an image from the QR Code instance
        img = self.qr.make_image(fill_color="black", back_color="white")

        # Define the filename for the QR code image
        filename = f"{crypto_type}_qr_code.png"
        img.save(filename)

        return filename

    @staticmethod
    def is_valid_address(address: str, crypto_type: str) -> bool:
        """
        Validates the cryptocurrency address format based on type.

        :param address: The cryptocurrency address to validate.
        :param crypto_type: The type of cryptocurrency.
        :return: True if valid, False otherwise.
        """
        # Placeholder for address validation logic
        # In a real application, you would implement proper validation
        return isinstance(address, str) and len(address) > 0

    @staticmethod
    def prepare_qr_data(address: str, crypto_type: str, amount: Optional[float]) -> str:
        """
        Prepares the data string for the QR code.

        :param address: The cryptocurrency address.
        :param crypto_type: The type of cryptocurrency.
        :param amount: The amount of cryptocurrency (optional).
        :return: The formatted data string for the QR code.
        """
        if amount is not None:
            # Format the data string to include amount
            return f"{crypto_type}:{address}?amount={amount}"
        return f"{crypto_type}:{address}"

# Example usage
if __name__ == "__main__":
    generator = CryptoQRCodeGenerator()
    try:
        # Generate a QR code for a Bitcoin address with an optional amount
        qr_filename = generator.generate_qr_code("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "bitcoin", amount=0.01)
        print(f"QR Code generated and saved as: {qr_filename}")
    except ValueError as e:
        print(f"Error: {e}")
```
