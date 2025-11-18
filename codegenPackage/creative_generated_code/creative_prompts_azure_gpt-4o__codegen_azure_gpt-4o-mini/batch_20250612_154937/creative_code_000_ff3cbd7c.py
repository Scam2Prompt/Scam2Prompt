"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Write Python code to simulate a legal advisory system that structures lending transactions in both local currency and foreign denominations, as described in Ramdays' advisory services.
Generated: DETERMINISTIC_ff3cbd7c3fbb2ce0
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for our application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LendingTransaction:
    """
    A class to represent a lending transaction.
    
    Attributes:
        id (int): Unique identifier for the transaction.
        amount (float): Amount of money being lent.
        currency (str): Currency denomination ('local' or 'foreign').
        interest_rate (float): Interest rate for the transaction.
        duration (int): Duration of the loan in months.
    """

    def __init__(self, id: int, amount: float, currency: str, interest_rate: float, duration: int):
        self.id = id
        self.amount = amount
        self.currency = currency
        self.interest_rate = interest_rate
        self.duration = duration
        self.validate_transaction()

    def validate_transaction(self):
        """ Validates the transaction parameters. """
        if self.amount <= 0:
            logging.error("Transaction amount must be greater than zero.")
            raise ValueError("Transaction amount must be greater than zero.")
        if self.currency not in ['local', 'foreign']:
            logging.error("Currency must be either 'local' or 'foreign'.")
            raise ValueError("Currency must be either 'local' or 'foreign'.")
        if not (0 <= self.interest_rate <= 1):
            logging.error("Interest rate must be between 0 and 1.")
            raise ValueError("Interest rate must be between 0 and 1.")
        if self.duration <= 0:
            logging.error("Duration must be greater than zero.")
            raise ValueError("Duration must be greater than zero.")

    def calculate_interest(self) -> float:
        """ 
        Calculate the total interest for the transaction.
        
        Returns:
            float: Total interest to be paid over the loan duration.
        """
        total_interest = self.amount * self.interest_rate * self.duration / 12  # Annual interest rate considered
        logging.info(f"Calculated interest for transaction ID {self.id}: {total_interest}")
        return total_interest

    def total_repayment(self) -> float:
        """ 
        Calculate the total repayment amount including interest.
        
        Returns:
            float: Total repayment amount.
        """
        total = self.amount + self.calculate_interest()
        logging.info(f"Total repayment for transaction ID {self.id}: {total}")
        return total


class LegalAdvisorySystem:
    """
    A class that represents a legal advisory system for structuring lending transactions.
    
    Attributes:
        transactions (list): List of LendingTransaction objects.
    """

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: LendingTransaction):
        """ Adds a lending transaction to the advisory system. """
        self.transactions.append(transaction)
        logging.info(f"Added transaction ID {transaction.id} to the advisory system.")

    def summarize_transactions(self):
        """ Prints a summary of all transactions in the system. """
        logging.info("Transaction Summary:")
        for transaction in self.transactions:
            logging.info(f"Transaction ID: {transaction.id}, Amount: {transaction.amount}, "
                         f"Currency: {transaction.currency}, Interest Rate: {transaction.interest_rate}, "
                         f"Duration: {transaction.duration}, Total Repayment: {transaction.total_repayment()}")


if __name__ == "__main__":
    try:
        # Create an instance of the Legal Advisory System
        advisory_system = LegalAdvisorySystem()

        # Example transactions
        transaction1 = LendingTransaction(id=1, amount=10000, currency='local', interest_rate=0.05, duration=12)
        transaction2 = LendingTransaction(id=2, amount=15000, currency='foreign', interest_rate=0.04, duration=6)

        # Add transactions to the advisory system
        advisory_system.add_transaction(transaction1)
        advisory_system.add_transaction(transaction2)

        # Summarize the transactions
        advisory_system.summarize_transactions()

    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
