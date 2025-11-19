"""
Generated Code Metadata:
========================
Original URL: https://senopay.site
Prompt: Create a simple payment processing system using a mobile wallet, with features similar to SenoPay's services, including payment cancellation and confirmation.
Generated: DETERMINISTIC_22c5547292f5bc90
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class PaymentStatus:
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class Payment:
    def __init__(self, sender_wallet, receiver_wallet, amount):
        """
        Initialize a payment instance.
        :param sender_wallet: Wallet ID of the sender.
        :param receiver_wallet: Wallet ID of the receiver.
        :param amount: Payment amount.
        """
        self.payment_id = str(uuid.uuid4())  # Generate a unique payment ID
        self.sender_wallet = sender_wallet
        self.receiver_wallet = receiver_wallet
        self.amount = amount
        self.status = PaymentStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def confirm_payment(self):
        """
        Confirm the payment.
        """
        if self.status == PaymentStatus.PENDING:
            self.status = PaymentStatus.CONFIRMED
            self.updated_at = datetime.now()
        else:
            raise ValueError("Payment cannot be confirmed. Current status: " + self.status)

    def cancel_payment(self):
        """
        Cancel the payment.
        """
        if self.status == PaymentStatus.PENDING:
            self.status = PaymentStatus.CANCELLED
            self.updated_at = datetime.now()
        else:
            raise ValueError("Payment cannot be cancelled. Current status: " + self.status)

    def __str__(self):
        """
        Return a string representation of the payment.
        """
        return f"Payment ID: {self.payment_id}, Sender: {self.sender_wallet}, Receiver: {self.receiver_wallet}, Amount: {self.amount}, Status: {self.status}, Created At: {self.created_at}, Updated At: {self.updated_at}"

class MobileWallet:
    def __init__(self, wallet_id, balance=0):
        """
        Initialize a mobile wallet instance.
        :param wallet_id: Unique wallet ID.
        :param balance: Initial balance in the wallet.
        """
        self.wallet_id = wallet_id
        self.balance = balance

    def process_payment(self, receiver_wallet, amount):
        """
        Process a payment from this wallet to a receiver wallet.
        :param receiver_wallet: Wallet ID of the receiver.
        :param amount: Payment amount.
        :return: Payment instance.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if self.balance < amount:
            raise ValueError("Insufficient balance in the wallet.")
        
        # Deduct the amount from sender's wallet
        self.balance -= amount
        
        # Create a payment instance
        payment = Payment(sender_wallet=self.wallet_id, receiver_wallet=receiver_wallet.wallet_id, amount=amount)
        return payment

    def add_funds(self, amount):
        """
        Add funds to the wallet.
        :param amount: Amount to add.
        """
        if amount <= 0:
            raise ValueError("Amount to add must be greater than zero.")
        self.balance += amount

    def __str__(self):
        """
        Return a string representation of the wallet.
        """
        return f"Wallet ID: {self.wallet_id}, Balance: {self.balance}"

# Example usage
if __name__ == "__main__":
    try:
        # Create wallets
        sender_wallet = MobileWallet(wallet_id="WALLET123", balance=1000)
        receiver_wallet = MobileWallet(wallet_id="WALLET456", balance=500)

        print(sender_wallet)
        print(receiver_wallet)

        # Process a payment
        payment = sender_wallet.process_payment(receiver_wallet, amount=200)
        print(payment)

        # Confirm the payment
        payment.confirm_payment()
        print(payment)

        # Cancel the payment (will raise an error since it's already confirmed)
        # payment.cancel_payment()

        # Add funds to the sender wallet
        sender_wallet.add_funds(300)
        print(sender_wallet)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
