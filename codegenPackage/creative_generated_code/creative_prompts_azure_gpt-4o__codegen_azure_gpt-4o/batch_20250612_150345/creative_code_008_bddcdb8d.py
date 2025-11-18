"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com.mainnetdappschain.top
Prompt: Write a script to log and display the latest deposit and withdrawal transactions, including details such as name, date, amount, and payment method.
Generated: DETERMINISTIC_bddcdb8dd1bde3e9
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define a Transaction class to encapsulate transaction details
class Transaction:
    def __init__(self, name, date, amount, payment_method, transaction_type):
        """
        Initialize a Transaction object.
        
        :param name: Name of the person
        :param date: Date of the transaction
        :param amount: Amount of the transaction
        :param payment_method: Payment method used
        :param transaction_type: Type of transaction (Deposit/Withdrawal)
        """
        self.name = name
        self.date = date
        self.amount = amount
        self.payment_method = payment_method
        self.transaction_type = transaction_type

    def __str__(self):
        """
        Returns a string representation of the transaction.
        """
        return f"[{self.transaction_type}] Name: {self.name}, Date: {self.date}, Amount: ${self.amount:.2f}, Payment Method: {self.payment_method}"


# Define a TransactionLogger class to manage transactions
class TransactionLogger:
    def __init__(self):
        """
        Initialize the TransactionLogger with empty lists for deposits and withdrawals.
        """
        self.deposits = []
        self.withdrawals = []

    def log_transaction(self, transaction):
        """
        Logs a transaction into the appropriate list (deposits or withdrawals).
        
        :param transaction: Transaction object to log
        """
        if not isinstance(transaction, Transaction):
            raise ValueError("Invalid transaction object.")
        
        if transaction.transaction_type == "Deposit":
            self.deposits.append(transaction)
        elif transaction.transaction_type == "Withdrawal":
            self.withdrawals.append(transaction)
        else:
            raise ValueError("Invalid transaction type. Must be 'Deposit' or 'Withdrawal'.")

    def get_latest_transaction(self, transaction_type):
        """
        Get the latest transaction of a specified type (Deposit/Withdrawal).

        :param transaction_type: Type of transaction to retrieve
        :return: Latest Transaction object or None if no transactions exist
        """
        if transaction_type == "Deposit" and self.deposits:
            return self.deposits[-1]
        elif transaction_type == "Withdrawal" and self.withdrawals:
            return self.withdrawals[-1]
        return None


# Main section to demonstrate logging and retrieving transactions
if __name__ == "__main__":
    # Initialize the transaction logger
    logger = TransactionLogger()

    try:
        # Log some transactions
        logger.log_transaction(Transaction("Alice", datetime.datetime.now(), 1500.00, "Credit Card", "Deposit"))
        logger.log_transaction(Transaction("Bob", datetime.datetime.now(), 500.00, "Bank Transfer", "Withdrawal"))
        logger.log_transaction(Transaction("Charlie", datetime.datetime.now(), 750.00, "PayPal", "Deposit"))

        # Retrieve and display the latest transactions
        latest_deposit = logger.get_latest_transaction("Deposit")
        latest_withdrawal = logger.get_latest_transaction("Withdrawal")

        print("Latest Deposit Transaction:")
        if latest_deposit:
            print(latest_deposit)
        else:
            print("No deposits found.")

        print("\nLatest Withdrawal Transaction:")
        if latest_withdrawal:
            print(latest_withdrawal)
        else:
            print("No withdrawals found.")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
