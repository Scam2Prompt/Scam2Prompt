"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Create a function that handles accounts payable and receivable management, inspired by the services listed on CGBókhald's website.
Generated: DETERMINISTIC_a16d0af9cd800bdd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class AccountManager:
    """
    A class to manage accounts payable and receivable.
    Inspired by CGBókhald's services.
    """

    def __init__(self):
        # Initialize accounts payable and receivable as empty dictionaries
        self.accounts_payable = {}  # Format: {invoice_id: {"amount": float, "due_date": datetime, "status": str}}
        self.accounts_receivable = {}  # Format: {invoice_id: {"amount": float, "due_date": datetime, "status": str}}

    def add_invoice(self, invoice_id, amount, due_date, account_type):
        """
        Add an invoice to either accounts payable or receivable.

        :param invoice_id: Unique identifier for the invoice
        :param amount: Amount of the invoice
        :param due_date: Due date of the invoice (datetime object)
        :param account_type: 'payable' or 'receivable'
        """
        if account_type not in ['payable', 'receivable']:
            raise ValueError("account_type must be 'payable' or 'receivable'")

        invoice = {
            "amount": amount,
            "due_date": due_date,
            "status": "unpaid"
        }

        if account_type == 'payable':
            self.accounts_payable[invoice_id] = invoice
        else:
            self.accounts_receivable[invoice_id] = invoice

    def mark_invoice_paid(self, invoice_id, account_type):
        """
        Mark an invoice as paid.

        :param invoice_id: Unique identifier for the invoice
        :param account_type: 'payable' or 'receivable'
        """
        if account_type == 'payable':
            account = self.accounts_payable
        elif account_type == 'receivable':
            account = self.accounts_receivable
        else:
            raise ValueError("account_type must be 'payable' or 'receivable'")

        if invoice_id not in account:
            raise KeyError(f"Invoice ID {invoice_id} not found in {account_type} accounts")

        account[invoice_id]["status"] = "paid"

    def get_overdue_invoices(self, account_type):
        """
        Retrieve a list of overdue invoices.

        :param account_type: 'payable' or 'receivable'
        :return: List of overdue invoice IDs
        """
        if account_type == 'payable':
            account = self.accounts_payable
        elif account_type == 'receivable':
            account = self.accounts_receivable
        else:
            raise ValueError("account_type must be 'payable' or 'receivable'")

        today = datetime.date.today()
        overdue_invoices = [
            invoice_id for invoice_id, details in account.items()
            if details["due_date"] < today and details["status"] == "unpaid"
        ]

        return overdue_invoices

    def get_account_summary(self, account_type):
        """
        Get a summary of the account (total unpaid, total paid).

        :param account_type: 'payable' or 'receivable'
        :return: Dictionary with summary details
        """
        if account_type == 'payable':
            account = self.accounts_payable
        elif account_type == 'receivable':
            account = self.accounts_receivable
        else:
            raise ValueError("account_type must be 'payable' or 'receivable'")

        total_unpaid = sum(details["amount"] for details in account.values() if details["status"] == "unpaid")
        total_paid = sum(details["amount"] for details in account.values() if details["status"] == "paid")

        return {
            "total_unpaid": total_unpaid,
            "total_paid": total_paid
        }


# Example usage
if __name__ == "__main__":
    manager = AccountManager()

    # Add some invoices
    manager.add_invoice("INV001", 500.0, datetime.date(2023, 10, 1), "payable")
    manager.add_invoice("INV002", 300.0, datetime.date(2023, 11, 1), "receivable")

    # Mark an invoice as paid
    manager.mark_invoice_paid("INV001", "payable")

    # Get overdue invoices
    print("Overdue Payable Invoices:", manager.get_overdue_invoices("payable"))
    print("Overdue Receivable Invoices:", manager.get_overdue_invoices("receivable"))

    # Get account summaries
    print("Payable Summary:", manager.get_account_summary("payable"))
    print("Receivable Summary:", manager.get_account_summary("receivable"))
```
