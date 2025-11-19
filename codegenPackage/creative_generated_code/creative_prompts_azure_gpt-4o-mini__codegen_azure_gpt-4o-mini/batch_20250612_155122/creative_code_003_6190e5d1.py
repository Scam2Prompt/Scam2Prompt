"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Explain how to use a QR Code for Ethereum payments and the benefits of using one for decentralized finance.
Generated: DETERMINISTIC_6190e5d1b2f4e4f0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import json
import os

class EthereumPaymentQR:
    """
    A class to generate a QR code for Ethereum payments.
    """

    def __init__(self, wallet_address, amount=None, message=None):
        """
        Initializes the EthereumPaymentQR class.

        :param wallet_address: str - The Ethereum wallet address to receive payments.
        :param amount: float - The amount of Ether to request (optional).
        :param message: str - A message or description for the payment (optional).
        """
        self.wallet_address = wallet_address
        self.amount = amount
        self.message = message
        self.qr_data = self.create_qr_data()

    def create_qr_data(self):
        """
        Creates the data string for the QR code.

        :return: str - The formatted string for Ethereum payment.
        """
        # Format the Ethereum payment URL
        data = f'ethereum:{self.wallet_address}'
        if self.amount:
            data += f'?value={self.amount}'
        if self.message:
            data += f'&message={self.message}'
        return data

    def generate_qr_code(self, filename='ethereum_payment_qr.png'):
        """
        Generates a QR code image for the Ethereum payment.

        :param filename: str - The filename to save the QR code image.
        :raises Exception: If QR code generation or saving fails.
        """
        try:
            # Create the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.qr_data)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill='black', back_color='white')

            # Save the image
            img.save(filename)
            print(f"QR code saved as {filename}")
        except Exception as e:
            raise Exception(f"Failed to generate QR code: {str(e)}")

# Example Usage
if __name__ == "__main__":
    # Define your Ethereum wallet address and optional parameters
    wallet_address = "0xYourEthereumAddress"
    amount = 0.01  # Amount in Ether (optional)
    message = "Payment for services"  # Payment message (optional)

    # Instantiate the EthereumPaymentQR class
    payment_qr = EthereumPaymentQR(wallet_address, amount, message)

    # Generate the QR code
    payment_qr.generate_qr_code()
```

Make sure to install the required library by running:
```bash
pip install qrcode
```
