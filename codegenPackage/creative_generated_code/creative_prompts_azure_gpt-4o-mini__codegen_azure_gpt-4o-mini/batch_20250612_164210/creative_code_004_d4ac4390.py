"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Describe how to use the USDT QR Code Generator for creating QR codes that support multiple blockchains like Ton and Ethereum.
Generated: DETERMINISTIC_d4ac4390848316f6
Batch ID: 20250612_164210
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

class QRCodeGenerator:
    """
    A class to create QR codes for cryptocurrency transactions, supporting multiple blockchains.
    """

    def __init__(self, blockchain, address, amount=None, message=None):
        """
        Initializes the QRCodeGenerator with blockchain details.

        Parameters:
            blockchain (str): The blockchain to generate the QR code for (e.g., "Ethereum", "Ton").
            address (str): The wallet address to encode in the QR code.
            amount (float, optional): The amount of cryptocurrency (if applicable).
            message (str, optional): A message to include in the QR code.
        """
        self.blockchain = blockchain
        self.address = address
        self.amount = amount
        self.message = message

    def generate_qr_code(self):
        """
        Generates a QR code based on the provided details.

        Returns:
            Image: The generated QR code as an image.
        """
        try:
            # Construct the URI based on the blockchain type
            if self.blockchain.lower() == "ethereum":
                uri = f"ethereum:{self.address}"
                if self.amount:
                    uri += f"?value={self.amount}"
                if self.message:
                    uri += f"&message={self.message}"
            elif self.blockchain.lower() == "ton":
                uri = f"ton:{self.address}"
                if self.amount:
                    uri += f"?amount={self.amount}"
                if self.message:
                    uri += f"&text={self.message}"
            else:
                raise ValueError("Unsupported blockchain type. Use 'Ethereum' or 'Ton'.")

            # Generate the QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(uri)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")
            return img

        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None

    def save_qr_code(self, file_path):
        """
        Saves the generated QR code to a file.

        Parameters:
            file_path (str): The path where the QR code image will be saved.
        """
        try:
            img = self.generate_qr_code()
            if img is not None:
                img.save(file_path)
                print(f"QR code saved to {file_path}")
            else:
                print("QR code generation failed. No file saved.")

        except IOError as e:
            print(f"Error saving QR code: {e}")

# Example usage
if __name__ == "__main__":
    # Create a QR code for an Ethereum address
    eth_qr_generator = QRCodeGenerator(blockchain="Ethereum", address="0xYourEthereumAddress", amount=0.01, message="Payment for services")
    eth_qr_generator.save_qr_code("ethereum_qr.png")

    # Create a QR code for a TON address
    ton_qr_generator = QRCodeGenerator(blockchain="Ton", address="YourTonAddress", amount=100, message="Payment for services")
    ton_qr_generator.save_qr_code("ton_qr.png")
```
