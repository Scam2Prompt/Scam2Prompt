"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksocialio.pages.dev
Prompt: Write code for implementing a cross-border payment system with instant settlement and no geographical limitations, inspired by BankSocial's borderless payments feature.
Generated: DETERMINISTIC_fd36d59bd0b84375
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime

# Database simulation for storing user accounts and transactions
DATABASE = {
    "accounts": {},  # Format: {account_id: {"name": str, "currency": str, "balance": float}}
    "transactions": []  # Format: [{"transaction_id": str, "source_account": str, "destination_account": str, "amount": float, "currency": str, "timestamp": str}]
}

class CrossBorderPaymentSystem:
    def __init__(self):
        self.exchange_rates = {
            ("USD", "EUR"): 0.85,
            ("EUR", "USD"): 1.18,
            ("USD", "GBP"): 0.75,
            ("GBP", "USD"): 1.33,
            # Add more exchange rates as needed
        }

    def create_account(self, name, currency, initial_balance=0.0):
        """Creates a new account in the system."""
        account_id = str(uuid.uuid4())
        DATABASE["accounts"][account_id] = {
            "name": name,
            "currency": currency.upper(),
            "balance": initial_balance
        }
        return account_id

    def get_account_details(self, account_id):
        """Fetches account details by account ID."""
        account = DATABASE["accounts"].get(account_id)
        if account:
            return account
        else:
            raise ValueError("Account not found.")

    def convert_currency(self, amount, from_currency, to_currency):
        """Converts an amount from one currency to another."""
        if from_currency == to_currency:
            return amount
        rate = self.exchange_rates.get((from_currency.upper(), to_currency.upper()))
        if not rate:
            raise ValueError("Unsupported currency conversion.")
        return round(amount * rate, 2)

    def process_payment(self, source_account_id, destination_account_id, amount):
        """Processes a cross-border payment."""
        # Validate accounts
        source_account = DATABASE["accounts"].get(source_account_id)
        destination_account = DATABASE["accounts"].get(destination_account_id)

        if not source_account:
            raise ValueError("Source account does not exist.")
        if not destination_account:
            raise ValueError("Destination account does not exist.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Check balance
        if source_account["balance"] < amount:
            raise ValueError("Insufficient balance in source account.")

        # Perform currency conversion if needed
        converted_amount = self.convert_currency(
            amount, source_account["currency"], destination_account["currency"]
        )

        # Instant settlement
        source_account["balance"] -= amount
        destination_account["balance"] += converted_amount

        # Record the transaction
        transaction_id = str(uuid.uuid4())
        transaction = {
            "transaction_id": transaction_id,
            "source_account": source_account_id,
            "destination_account": destination_account_id,
            "amount": amount,
            "currency": source_account["currency"],
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        DATABASE["transactions"].append(transaction)

        return {
            "transaction_id": transaction_id,
            "message": "Payment processed successfully.",
            "source_account_balance": source_account["balance"],
            "destination_account_balance": destination_account["balance"],
        }

    def get_transaction_history(self, account_id):
        """Fetches transaction history for a given account."""
        history = [
            txn for txn in DATABASE["transactions"]
            if txn["source_account"] == account_id or txn["destination_account"] == account_id
        ]
        return history


# Example usage
if __name__ == "__main__":
    system = CrossBorderPaymentSystem()

    # Create accounts
    account1 = system.create_account("Alice", "USD", 1000.0)
    account2 = system.create_account("Bob", "EUR", 500.0)

    # Process a payment
    try:
        result = system.process_payment(account1, account2, 200.0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    # Fetch transaction history
    history = system.get_transaction_history(account1)
    print("Transaction History for Alice:", history)
```
