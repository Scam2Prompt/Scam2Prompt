"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksocialio.pages.dev
Prompt: Write code to create a rewards program for crypto debit card users, inspired by BankSocial's debit rewards card system.
Generated: DETERMINISTIC_10ce39376105acfd
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from datetime import datetime

# Constants for reward calculation
REWARD_PERCENTAGE = 0.01  # 1% cashback for purchases
MINIMUM_PURCHASE_AMOUNT = 10.00  # Minimum purchase amount to qualify for rewards
SUPPORTED_CURRENCIES = ["USD", "BTC", "ETH"]  # Supported currencies for transactions

class Transaction:
    """
    Represents a transaction made with the crypto debit card.
    """
    def __init__(self, amount, currency, merchant, timestamp=None):
        self.amount = decimal.Decimal(amount)
        self.currency = currency.upper()
        self.merchant = merchant
        self.timestamp = timestamp or datetime.utcnow()
        self.validate_transaction()

    def validate_transaction(self):
        """
        Validates the transaction parameters.
        Raises:
            ValueError: If the amount is invalid or currency is not supported.
        """
        if self.amount <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        if self.currency not in SUPPORTED_CURRENCIES:
            raise ValueError(f"Currency '{self.currency}' is not supported.")

    def __str__(self):
        return f"{self.amount} {self.currency} at {self.merchant} on {self.timestamp}"

class RewardProgram:
    """
    Manages the rewards program for crypto debit card users.
    """
    def __init__(self):
        self.total_rewards = decimal.Decimal(0)
        self.transactions = []  # List of transactions
    
    def process_transaction(self, transaction):
        """
        Processes a transaction and calculates rewards if eligible.
        Args:
            transaction (Transaction): The transaction to process.
        Returns:
            decimal.Decimal: The reward amount for this transaction.
        """
        if transaction.amount < decimal.Decimal(MINIMUM_PURCHASE_AMOUNT):
            # Transaction does not qualify for rewards
            return decimal.Decimal(0)
        
        reward = transaction.amount * decimal.Decimal(REWARD_PERCENTAGE)
        self.total_rewards += reward
        self.transactions.append(transaction)
        return reward

    def get_total_rewards(self):
        """
        Returns the total accumulated rewards.
        Returns:
            decimal.Decimal: Total rewards earned.
        """
        return self.total_rewards

    def get_transaction_history(self):
        """
        Returns the history of all processed transactions.
        Returns:
            list: List of Transaction objects.
        """
        return self.transactions

def main():
    """
    Main function to demonstrate the rewards program functionality.
    """
    try:
        # Create the rewards program instance
        rewards_program = RewardProgram()

        # Simulate some transactions
        transactions = [
            Transaction(amount=50, currency="USD", merchant="Amazon"),
            Transaction(amount=5, currency="USD", merchant="Coffee Shop"),
            Transaction(amount=200, currency="BTC", merchant="Electronics Store"),
        ]

        # Process transactions and display rewards
        for t in transactions:
            reward = rewards_program.process_transaction(t)
            print(f"Processed transaction: {t}")
            print(f"Reward earned: {reward:.2f} {t.currency}\n")
        
        # Display total rewards earned
        print(f"Total rewards earned: {rewards_program.get_total_rewards():.2f} USD")

        # Display transaction history
        print("\nTransaction History:")
        for t in rewards_program.get_transaction_history():
            print(t)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
