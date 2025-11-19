"""
Generated Code Metadata:
========================
Original URL: https://usdt-qrcode-generator.com
Prompt: Describe how to use the USDT QR Code Generator for creating QR codes that support multiple blockchains like Ton and Ethereum.
Generated: DETERMINISTIC_d4ac4390848316f6
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import json
import os

class QRCodeGenerator:
    """
    A class to generate QR codes for USDT transactions across multiple blockchains.
    """

    def __init__(self, blockchain, address, amount, message=None):
        """
        Initializes the QRCodeGenerator with blockchain type, address, amount, and optional message.

        :param blockchain: The blockchain type (e.g., 'Ethereum', 'Ton').
        :param address: The recipient's wallet address.
        :param amount: The amount of USDT to send.
        :param message: An optional message to include with the transaction.
        """
        self.blockchain = blockchain
        self.address = address
        self.amount = amount
        self.message = message

    def generate_qr_data(self):
        """
        Generates the data string for the QR code based on the blockchain type.

        :return: A string formatted for the specific blockchain.
        """
        if self.blockchain.lower() == 'ethereum':
            return f"ethereum:{self.address}?value={self.amount}&message={self.message or ''}"
        elif self.blockchain.lower() == 'ton':
            return f"ton:{self.address}?amount={self.amount}&message={self.message or ''}"
        else:
            raise ValueError("Unsupported blockchain type. Please use 'Ethereum' or 'Ton'.")

    def create_qr_code(self):
        """
        Creates a QR code image file based on the generated data.

        :return: The file path of the generated QR code image.
        """
        try:
            qr_data = self.generate_qr_data()
            qr_image = qrcode.make(qr_data)
            file_path = f"{self.blockchain}_usdt_qr.png"
            qr_image.save(file_path)
            return file_path
        except Exception as e:
            raise RuntimeError(f"Failed to create QR code: {e}")

def main():
    """
    Main function to execute the QR code generation process.
    """
    try:
        # Example usage
        blockchain = 'Ethereum'  # or 'Ton'
        address = '0xYourEthereumAddress'  # Replace with actual address
        amount = '10'  # Amount of USDT
        message = 'Payment for services'  # Optional message

        qr_generator = QRCodeGenerator(blockchain, address, amount, message)
        qr_code_path = qr_generator.create_qr_code()
        print(f"QR code generated successfully: {qr_code_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
