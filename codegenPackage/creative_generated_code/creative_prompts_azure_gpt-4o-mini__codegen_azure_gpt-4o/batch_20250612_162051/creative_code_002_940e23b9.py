"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwakeelacademy.com
Prompt: Write a Python script that utilizes financial accounting principles and includes features for searching solutions, inspired by alwakeelacademy.com.
Generated: DETERMINISTIC_940e23b99e8e5ed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture important events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialAccounting:
    """
    A class to represent financial accounting principles and operations.
    Inspired by alwakeelacademy.com.
    """

    def __init__(self):
        """
        Initialize the financial accounting system with empty records.
        """
        self.records = []
        logging.info("FinancialAccounting system initialized.")

    def add_transaction(self, description, amount, transaction_type):
        """
        Add a financial transaction to the records.

        Args:
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
            transaction_type (str): Type of the transaction ('Debit' or 'Credit').

        Raises:
            ValueError: If transaction_type is not 'Debit' or 'Credit'.
        """
        if transaction_type not in ['Debit', 'Credit']:
            raise ValueError("Transaction type must be 'Debit' or 'Credit'.")
        
        transaction = {
            'description': description,
            'amount': amount,
            'type': transaction_type
        }
        self.records.append(transaction)
        logging.info(f"Transaction added: {transaction}")

    def search_transactions(self, query):
        """
        Search for transactions containing the query string in their description.

        Args:
            query (str): The search query.

        Returns:
            list: A list of transactions that match the search query.
        """
        results = [record for record in self.records if query.lower() in record['description'].lower()]
        logging.info(f"Search executed with query: '{query}'. {len(results)} result(s) found.")
        return results

    def calculate_balance(self):
        """
        Calculate the overall balance from all transactions.

        Returns:
            float: The calculated balance.
        """
        balance = 0
        for record in self.records:
            if record['type'] == 'Credit':
                balance += record['amount']
            elif record['type'] == 'Debit':
                balance -= record['amount']
        logging.info(f"Balance calculated: {balance}")
        return balance


def main():
    """
    Main function to demonstrate the functionality of the FinancialAccounting system.
    """
    try:
        # Create an instance of the FinancialAccounting system
        accounting_system = FinancialAccounting()

        # Add sample transactions
        accounting_system.add_transaction("Office Supplies", 200.50, "Debit")
        accounting_system.add_transaction("Client Payment", 1500.00, "Credit")
        accounting_system.add_transaction("Utility Bill", 100.00, "Debit")
        
        # Search transactions
        search_results = accounting_system.search_transactions("office")
        print("Search Results:", search_results)

        # Calculate balance
        balance = accounting_system.calculate_balance()
        print(f"Final Balance: {balance:.2f}")

    except Exception as e:
        # Handle any exceptions gracefully
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
