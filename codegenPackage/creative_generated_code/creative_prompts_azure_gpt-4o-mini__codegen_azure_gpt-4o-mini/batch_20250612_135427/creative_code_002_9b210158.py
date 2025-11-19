"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: What are the security features of the Bitcoin QR Code Generator on btc-qr.to when creating QR codes for cryptocurrency payments?
Generated: DETERMINISTIC_9b210158d3c3675b
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BitcoinQRCodeGenerator:
    def __init__(self, address: str, amount: float = 0.0, label: str = '', message: str = ''):
        """
        Initializes the BitcoinQRCodeGenerator with the necessary parameters.

        :param address: Bitcoin address for the payment.
        :param amount: Amount of Bitcoin to be sent (optional).
        :param label: Label for the QR code (optional).
        :param message: Message associated with the transaction (optional).
        """
        self.address = address
        self.amount = amount
        self.label = label
        self.message = message
        self.qr_code = None

        # Validate Bitcoin address
        self.validate_address()

    def validate_address(self):
        """Validates the Bitcoin address."""
        if not self.address.startswith('1') and not self.address.startswith('3'):
            logging.error("Invalid Bitcoin address.")
            raise ValueError("Invalid Bitcoin address provided.")

    def create_qr_code(self):
        """
        Creates a QR code for the Bitcoin payment.

        The QR code URI format is: 
        bitcoin:<address>?amount=<amount>&label=<label>&message=<message>
        """
        try:
            uri = f"bitcoin:{self.address}"
            if self.amount > 0:
                uri += f"?amount={self.amount}"
            if self.label:
                uri += f"&label={self.label}"
            if self.message:
                uri += f"&message={self.message}"

            logging.info("Generating QR code...")
            self.qr_code = qrcode.make(uri)
            logging.info("QR code generated successfully.")

        except Exception as e:
            logging.error("Error occurred while generating QR code: %s", e)
            raise

    def save_qr_code(self, file_path: str):
        """
        Saves the QR code to a file.

        :param file_path: The path where the QR code image will be saved.
        """
        if self.qr_code is None:
            logging.error("QR code has not been generated yet.")
            raise RuntimeError("QR code is not generated. Call create_qr_code() before saving.")

        try:
            self.qr_code.save(file_path)
            logging.info(f"QR code saved to {file_path}")

        except Exception as e:
            logging.error("Error occurred while saving QR code: %s", e)
            raise

if __name__ == "__main__":
    try:
        # Example usage
        address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        amount = 0.001
        label = "Payment for services"
        message = "Thank you for your support"

        generator = BitcoinQRCodeGenerator(address, amount, label, message)
        generator.create_qr_code()
        generator.save_qr_code(os.path.join(os.getcwd(), "bitcoin_payment_qr.png"))

    except Exception as e:
        logging.error("Application error: %s", e)
```
