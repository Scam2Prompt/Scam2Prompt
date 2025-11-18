"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Write a Python script to simulate a QRIS-based payment system for slot deposits, referencing the "Link Slot Deposit 5k Tanpa Potongan Via QRIS" feature described on the website.
Generated: DETERMINISTIC_4e71bebb6f301573
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import qrcode
from datetime import datetime

class PaymentError(Exception):
    """Custom exception class for payment errors."""
    pass

class SlotDeposit:
    def __init__(self, user_id, deposit_amount=5000):
        """
        Initializes a new SlotDeposit instance.

        :param user_id: str, user's unique identifier
        :param deposit_amount: int, amount to deposit (default is 5000)
        """
        self.user_id = user_id
        self.deposit_amount = deposit_amount
        self.transaction_id = None
        self.timestamp = None

    def generate_qr_code(self):
        """
        Generates a QR code for the payment.
        
        :return: str, file path to the generated QR code image
        """
        self.transaction_id = self.generate_transaction_id()
        self.timestamp = datetime.now().isoformat()
        
        # Prepare payment data
        payment_data = {
            "user_id": self.user_id,
            "amount": self.deposit_amount,
            "transaction_id": self.transaction_id,
            "timestamp": self.timestamp
        }
        
        # Convert payment data to JSON format
        payment_json = json.dumps(payment_data)

        # Generate QR code
        qr_file = f"{self.transaction_id}.png"
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(payment_json)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(qr_file)
            return qr_file
        except Exception as e:
            raise PaymentError(f"Error generating QR code: {str(e)}")

    def generate_transaction_id(self):
        """
        Generates a unique transaction ID.

        :return: str, unique transaction ID
        """
        return f"TX-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"

    def process_payment(self):
        """
        Simulates processing the payment using the QR code.

        :return: str, transaction status
        """
        try:
            qr_code_file = self.generate_qr_code()
            print(f"QR Code generated: {qr_code_file}")
            # Simulate payment processing (e.g., await payment confirmation)
            print(f"Processing payment of {self.deposit_amount} for user {self.user_id}...")
            # In real application, here would be the logic to confirm the payment
            return f"Payment of {self.deposit_amount} processed successfully for transaction ID {self.transaction_id}."
        except PaymentError as e:
            return str(e)

# Example of how to use the SlotDeposit class
if __name__ == "__main__":
    user_id_input = input("Enter your user ID: ")
    slot_deposit = SlotDeposit(user_id=user_id_input)
    
    # Initiate the payment process
    payment_status = slot_deposit.process_payment()
    print(payment_status)
```

Ensure you have the `qrcode` library installed by running:
```bash
pip install qrcode[pil]
``` 

This script provides a simple simulation of a QRIS-based payment system specifically for slot deposits, generating a unique QR code for a fixed deposit amount and simulating the payment process.
