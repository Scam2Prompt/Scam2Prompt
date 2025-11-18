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
import uuid
import json
import datetime


class QRISPaymentSystem:
    """
    A class to simulate a QRIS-based payment system for slot deposits.
    """

    def __init__(self):
        """
        Initialize the payment system with an empty transaction history.
        """
        self.transaction_history = []

    def generate_qris_code(self, deposit_amount):
        """
        Generate a QRIS code for the deposit transaction.

        Args:
            deposit_amount (float): The amount to deposit.

        Returns:
            dict: A dictionary containing the QRIS code and transaction details.
        """
        if deposit_amount < 5000:
            raise ValueError("Minimum deposit amount is 5000.")

        transaction_id = str(uuid.uuid4())
        qris_code = f"QRIS-{transaction_id}"  # Simulated QRIS code
        transaction_details = {
            "transaction_id": transaction_id,
            "qris_code": qris_code,
            "deposit_amount": deposit_amount,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.transaction_history.append(transaction_details)
        return transaction_details

    def confirm_payment(self, transaction_id):
        """
        Confirm payment for a given transaction ID.

        Args:
            transaction_id (str): The ID of the transaction to confirm.

        Returns:
            dict: The details of the confirmed transaction.
        """
        for transaction in self.transaction_history:
            if transaction["transaction_id"] == transaction_id:
                transaction["status"] = "confirmed"
                return transaction

        # If the transaction ID is not found, raise an error
        raise ValueError("Transaction ID not found.")

    def save_transaction_history(self, filename):
        """
        Save the transaction history to a JSON file.

        Args:
            filename (str): The name of the file to save the transaction history.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.transaction_history, file, indent=4)
        except IOError as e:
            print(f"Error saving transaction history: {e}")

    def load_transaction_history(self, filename):
        """
        Load the transaction history from a JSON file.

        Args:
            filename (str): The name of the file to load the transaction history.
        """
        try:
            with open(filename, "r") as file:
                self.transaction_history = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading transaction history: {e}")


def main():
    """
    Main function to simulate the QRIS-based payment system.
    """
    payment_system = QRISPaymentSystem()

    # Simulating deposit transactions
    try:
        deposit_details = payment_system.generate_qris_code(5000)
        print("Generated QRIS Code:", deposit_details["qris_code"])
        print("Transaction Details:", deposit_details)

        # Confirm payment
        confirmed_details = payment_system.confirm_payment(deposit_details["transaction_id"])
        print("Payment Confirmed:", confirmed_details)

        # Save transaction history to a file
        payment_system.save_transaction_history("transaction_history.json")
        print("Transaction history saved.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
