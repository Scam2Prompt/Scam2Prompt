"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Design a basic TMS/client app integration with a fuel card program, focusing on seamless funding and payment processing for trucking companies.
Generated: DETERMINISTIC_9b3c851f65558f19
Batch ID: 20250622_205459
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

# Define a basic Trucking Management System (TMS) class
class TMS:
    def __init__(self):
        # Initialize trucking company accounts
        self.accounts = {}

    def create_account(self, company_name):
        """
        Create a new account for a trucking company.
        :param company_name: Name of the trucking company
        :return: Account ID
        """
        account_id = str(uuid.uuid4())
        self.accounts[account_id] = {
            "company_name": company_name,
            "balance": 0.0,
            "transactions": []
        }
        return account_id

    def get_account_balance(self, account_id):
        """
        Retrieve the balance of a trucking company account.
        :param account_id: Account ID
        :return: Account balance
        """
        if account_id not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_id]["balance"]

    def record_transaction(self, account_id, amount, description):
        """
        Record a transaction for a trucking company account.
        :param account_id: Account ID
        :param amount: Transaction amount (positive for funding, negative for payment)
        :param description: Description of the transaction
        """
        if account_id not in self.accounts:
            raise ValueError("Account not found.")
        self.accounts[account_id]["balance"] += amount
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "amount": amount,
            "description": description,
            "timestamp": datetime.now().isoformat()
        }
        self.accounts[account_id]["transactions"].append(transaction)

    def get_transaction_history(self, account_id):
        """
        Retrieve the transaction history for a trucking company account.
        :param account_id: Account ID
        :return: List of transactions
        """
        if account_id not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_id]["transactions"]


# Define a Fuel Card Program class
class FuelCardProgram:
    def __init__(self, tms):
        """
        Initialize the Fuel Card Program with a reference to the TMS.
        :param tms: Instance of the TMS class
        """
        self.tms = tms

    def fund_account(self, account_id, amount):
        """
        Fund a trucking company account.
        :param account_id: Account ID
        :param amount: Amount to fund
        """
        if amount <= 0:
            raise ValueError("Funding amount must be positive.")
        self.tms.record_transaction(account_id, amount, "Funding")

    def process_payment(self, account_id, amount):
        """
        Process a payment from a trucking company account.
        :param account_id: Account ID
        :param amount: Payment amount
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        current_balance = self.tms.get_account_balance(account_id)
        if current_balance < amount:
            raise ValueError("Insufficient balance for payment.")
        self.tms.record_transaction(account_id, -amount, "Payment")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize TMS and Fuel Card Program
        tms = TMS()
        fuel_card_program = FuelCardProgram(tms)

        # Create a trucking company account
        account_id = tms.create_account("Trucking Co. A")
        print(f"Account created with ID: {account_id}")

        # Fund the account
        fuel_card_program.fund_account(account_id, 500.0)
        print(f"Account balance after funding: ${tms.get_account_balance(account_id):.2f}")

        # Process a payment
        fuel_card_program.process_payment(account_id, 200.0)
        print(f"Account balance after payment: ${tms.get_account_balance(account_id):.2f}")

        # Retrieve transaction history
        transactions = tms.get_transaction_history(account_id)
        print("Transaction history:")
        for transaction in transactions:
            print(transaction)

    except Exception as e:
        print(f"Error: {e}")
```
