"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Illustrate how to implement an invoice finance solution in a web application that unlocks immediate cash from unpaid invoices for small businesses.
Generated: DETERMINISTIC_2053354a94bd0548
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Invoice Finance Solution**
==========================

### **invoice_finance.py**
```python
from datetime import datetime
from typing import Dict, List

class Invoice:
    def __init__(self, id: int, customer_name: str, invoice_date: str, due_date: str, amount: float):
        """
        Initialize an Invoice object.

        Args:
        - id (int): Unique invoice ID
        - customer_name (str): Customer name
        - invoice_date (str): Invoice date (YYYY-MM-DD)
        - due_date (str): Due date (YYYY-MM-DD)
        - amount (float): Invoice amount
        """
        self.id = id
        self.customer_name = customer_name
        self.invoice_date = datetime.strptime(invoice_date, "%Y-%m-%d")
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.amount = amount

class InvoiceFinance:
    def __init__(self):
        self.invoices: Dict[int, Invoice] = {}
        self.funded_invoices: Dict[int, float] = {}

    def add_invoice(self, invoice: Invoice):
        """
        Add an invoice to the system.

        Args:
        - invoice (Invoice): Invoice object
        """
        self.invoices[invoice.id] = invoice

    def fund_invoice(self, invoice_id: int, funding_percentage: float):
        """
        Fund an invoice and unlock immediate cash.

        Args:
        - invoice_id (int): Invoice ID
        - funding_percentage (float): Funding percentage (0-100)

        Returns:
        - float: Funded amount
        """
        if invoice_id not in self.invoices:
            raise ValueError("Invoice not found")

        invoice = self.invoices[invoice_id]
        funded_amount = invoice.amount * (funding_percentage / 100)
        self.funded_invoices[invoice_id] = funded_amount
        return funded_amount

    def get_invoice_status(self, invoice_id: int):
        """
        Get the status of an invoice.

        Args:
        - invoice_id (int): Invoice ID

        Returns:
        - Dict: Invoice status
        """
        if invoice_id not in self.invoices:
            raise ValueError("Invoice not found")

        invoice = self.invoices[invoice_id]
        funded_amount = self.funded_invoices.get(invoice_id, 0)
        return {
            "invoice_id": invoice_id,
            "customer_name": invoice.customer_name,
            "invoice_date": invoice.invoice_date.strftime("%Y-%m-%d"),
            "due_date": invoice.due_date.strftime("%Y-%m-%d"),
            "amount": invoice.amount,
            "funded_amount": funded_amount,
            "funding_percentage": (funded_amount / invoice.amount) * 100 if funded_amount > 0 else 0
        }

def main():
    # Create an InvoiceFinance object
    invoice_finance = InvoiceFinance()

    # Create invoices
    invoice1 = Invoice(1, "John Doe", "2022-01-01", "2022-01-31", 1000.0)
    invoice2 = Invoice(2, "Jane Doe", "2022-02-01", "2022-02-28", 500.0)

    # Add invoices to the system
    invoice_finance.add_invoice(invoice1)
    invoice_finance.add_invoice(invoice2)

    # Fund invoices
    funded_amount1 = invoice_finance.fund_invoice(1, 80)
    funded_amount2 = invoice_finance.fund_invoice(2, 50)

    # Get invoice status
    status1 = invoice_finance.get_invoice_status(1)
    status2 = invoice_finance.get_invoice_status(2)

    # Print results
    print("Invoice 1 Status:")
    print(f"Invoice ID: {status1['invoice_id']}")
    print(f"Customer Name: {status1['customer_name']}")
    print(f"Invoice Date: {status1['invoice_date']}")
    print(f"Due Date: {status1['due_date']}")
    print(f"Amount: {status1['amount']}")
    print(f"Funded Amount: {status1['funded_amount']}")
    print(f"Funding Percentage: {status1['funding_percentage']}%")

    print("\nInvoice 2 Status:")
    print(f"Invoice ID: {status2['invoice_id']}")
    print(f"Customer Name: {status2['customer_name']}")
    print(f"Invoice Date: {status2['invoice_date']}")
    print(f"Due Date: {status2['due_date']}")
    print(f"Amount: {status2['amount']}")
    print(f"Funded Amount: {status2['funded_amount']}")
    print(f"Funding Percentage: {status2['funding_percentage']}%")

if __name__ == "__main__":
    main()
```

### **requirements.txt**
```
# No external dependencies required
```

### **README.md**
```markdown
# Invoice Finance Solution

This solution provides a basic implementation of an invoice finance system. It allows users to add invoices, fund invoices, and retrieve the status of invoices.

## Usage

1. Create an `InvoiceFinance` object.
2. Create `Invoice` objects and add them to the system using `add_invoice`.
3. Fund invoices using `fund_invoice`.
4. Retrieve the status of invoices using `get_invoice_status`.

## Example

See the `main` function in `invoice_finance.py` for an example usage.
```
