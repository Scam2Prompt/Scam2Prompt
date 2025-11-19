"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Write Python code to simulate a QRIS-based deposit system for an online slot platform like Satria4D, including QR code generation and validation.
Generated: DETERMINISTIC_61be383b250ca10a
Batch ID: 20250612_152739
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
import hashlib
import hmac
import time
import json
import os

class QRISDepositSystem:
    def __init__(self, merchant_id, secret_key):
        """
        Initialize the QRIS deposit system.

        Args:
            merchant_id (str): The merchant ID.
            secret_key (str): The secret key for HMAC verification.
        """
        self.merchant_id = merchant_id
        self.secret_key = secret_key.encode('utf-8')

    def generate_qr_code(self, amount, transaction_id):
        """
        Generate a QR code for deposit.

        Args:
            amount (int): The deposit amount.
            transaction_id (str): The unique transaction ID.

        Returns:
            str: The QR code data in JSON format.
        """
        # Create a dictionary to store the QR code data
        qr_data = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "transaction_id": transaction_id,
            "timestamp": int(time.time())
        }

        # Convert the dictionary to JSON
        qr_data_json = json.dumps(qr_data)

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(qr_data_json)
        qr.make(fit=True)

        # Save the QR code to an image file
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        return qr_data_json

    def validate_qr_code(self, qr_data_json):
        """
        Validate the QR code data.

        Args:
            qr_data_json (str): The QR code data in JSON format.

        Returns:
            bool: True if the QR code is valid, False otherwise.
        """
        try:
            # Load the QR code data from JSON
            qr_data = json.loads(qr_data_json)

            # Verify the HMAC signature
            signature = hmac.new(self.secret_key, qr_data_json.encode('utf-8'), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(signature, qr_data.get("signature", "")):
                return False

            # Verify the timestamp
            timestamp = qr_data.get("timestamp")
            if timestamp is None or int(time.time()) - timestamp > 300:  # 5 minutes
                return False

            return True
        except json.JSONDecodeError:
            return False

    def verify_transaction(self, transaction_id, amount):
        """
        Verify a transaction.

        Args:
            transaction_id (str): The unique transaction ID.
            amount (int): The deposit amount.

        Returns:
            bool: True if the transaction is valid, False otherwise.
        """
        # Simulate a database query to verify the transaction
        # Replace this with your actual database query
        transactions = {
            "transaction_123": 10000
        }

        if transaction_id in transactions and transactions[transaction_id] == amount:
            return True
        return False


def main():
    merchant_id = "satria4d"
    secret_key = "your_secret_key_here"

    qris_system = QRISDepositSystem(merchant_id, secret_key)

    amount = 10000
    transaction_id = "transaction_123"

    qr_data_json = qris_system.generate_qr_code(amount, transaction_id)
    print("QR Code Data:", qr_data_json)

    # Simulate HMAC signature generation
    signature = hmac.new(qris_system.secret_key, qr_data_json.encode('utf-8'), hashlib.sha256).hexdigest()
    qr_data_with_signature = json.loads(qr_data_json)
    qr_data_with_signature["signature"] = signature
    qr_data_json_with_signature = json.dumps(qr_data_with_signature)

    is_valid = qris_system.validate_qr_code(qr_data_json_with_signature)
    print("Is QR Code Valid?", is_valid)

    is_transaction_valid = qris_system.verify_transaction(transaction_id, amount)
    print("Is Transaction Valid?", is_transaction_valid)


if __name__ == "__main__":
    main()
```
