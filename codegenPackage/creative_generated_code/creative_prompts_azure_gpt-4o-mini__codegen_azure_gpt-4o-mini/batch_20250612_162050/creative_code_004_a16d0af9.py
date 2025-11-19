"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: Create a function that handles accounts payable and receivable management, inspired by the services listed on CGBókhald's website.
Generated: DETERMINISTIC_a16d0af9cd800bdd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountManager:
    """
    A class to manage accounts payable and receivable for a business.
    """

    def __init__(self):
        """
        Initializes a new instance of the AccountManager class.
        """
        self.accounts_payable = {}
        self.accounts_receivable = {}

    def add_payable(self, vendor, amount, due_date):
        """
        Adds a payable entry to the accounts payable list.

        Args:
            vendor (str): The name of the vendor.
            amount (float): The amount owed.
            due_date (str): The due date for the payment (format: YYYY-MM-DD).

        Raises:
            ValueError: If the amount is negative or if the due date is invalid.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if not self._is_valid_date(due_date):
            raise ValueError("Due date must be in the format YYYY-MM-DD.")

        self.accounts_payable[vendor] = {
            'amount': amount,
            'due_date': due_date
        }

    def add_receivable(self, customer, amount, due_date):
        """
        Adds a receivable entry to the accounts receivable list.

        Args:
            customer (str): The name of the customer.
            amount (float): The amount owed to the business.
            due_date (str): The due date for the payment (format: YYYY-MM-DD).

        Raises:
            ValueError: If the amount is negative or if the due date is invalid.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if not self._is_valid_date(due_date):
            raise ValueError("Due date must be in the format YYYY-MM-DD.")

        self.accounts_receivable[customer] = {
            'amount': amount,
            'due_date': due_date
        }

    def _is_valid_date(self, date_str):
        """
        Checks if the given date string is in the correct format (YYYY-MM-DD).

        Args:
            date_str (str): The date string to validate.

        Returns:
            bool: True if the date is valid, False otherwise.
        """
        from datetime import datetime

        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_payables(self):
        """
        Returns the current accounts payable.

        Returns:
            dict: A dictionary of current accounts payable.
        """
        return self.accounts_payable

    def get_receivables(self):
        """
        Returns the current accounts receivable.

        Returns:
            dict: A dictionary of current accounts receivable.
        """
        return self.accounts_receivable

    def settle_payable(self, vendor):
        """
        Settles (removes) a payable for a given vendor.

        Args:
            vendor (str): The name of the vendor.

        Raises:
            KeyError: If the vendor does not exist in accounts payable.
        """
        if vendor not in self.accounts_payable:
            raise KeyError(f"No payable entry found for vendor '{vendor}'.")

        del self.accounts_payable[vendor]

    def settle_receivable(self, customer):
        """
        Settles (removes) a receivable for a given customer.

        Args:
            customer (str): The name of the customer.

        Raises:
            KeyError: If the customer does not exist in accounts receivable.
        """
        if customer not in self.accounts_receivable:
            raise KeyError(f"No receivable entry found for customer '{customer}'.")

        del self.accounts_receivable[customer]
```
