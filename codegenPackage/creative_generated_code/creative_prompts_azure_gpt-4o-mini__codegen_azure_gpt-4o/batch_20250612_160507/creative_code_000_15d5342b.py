"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Write a Python script that utilizes Summar Financial's freight factoring services to convert invoices into cash flow. Include error handling for same-day funding requests.
Generated: DETERMINISTIC_15d5342bd27db5ef
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List

class Invoice:
    """
    Represents an invoice with necessary details.
    """
    def __init__(self, invoice_id: str, amount: float, due_date: datetime.date):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date


class FreightFactoringService:
    """
    A mock class simulating Summar Financial's freight factoring services.
    """
    def __init__(self):
        self.allowed_invoices = []  # List to store invoices eligible for factoring

    def validate_invoice(self, invoice: Invoice) -> bool:
        """
        Validates whether an invoice is eligible for factoring.
        Criteria: Invoice must have a positive amount and must not be overdue.
        """
        if invoice.amount <= 0:
            return False
        if invoice.due_date < datetime.date.today():
            return False
        return True

    def request_funding(self, invoice: Invoice, same_day: bool = False) -> str:
        """
        Requests funding for a given invoice.
        If same_day is True, include specific error handling for same-day funding.
        """
        if not self.validate_invoice(invoice):
            return f"Invoice {invoice.invoice_id} is not eligible for funding."

        if same_day:
            # Simulate error handling for same-day funding
            try:
                if datetime.datetime.now().hour > 14:  # Assume cutoff time is 2 PM
                    raise ValueError("Same-day funding requests must be submitted before 2 PM.")
                # Simulate processing
                return f"Same-day funding request for Invoice {invoice.invoice_id} is approved."
            except ValueError as e:
                return f"Error: {str(e)}"

        # Standard funding processing
        self.allowed_invoices.append(invoice)
        return f"Funding request for Invoice {invoice.invoice_id} is approved."


def main():
    """
    Main function to demonstrate the freight factoring process.
    """
    service = FreightFactoringService()

    # Example invoices
    invoices = [
        Invoice("INV001", 1500.50, datetime.date(2023, 10, 15)),
        Invoice("INV002", -100.00, datetime.date(2023, 10, 12)),  # Invalid amount
        Invoice("INV003", 2000.00, datetime.date(2023, 10, 10)),  # Past due date
    ]

    # Process invoices and request funding
    for invoice in invoices:
        print(service.request_funding(invoice))

    # Demonstrate same-day funding request
    same_day_invoice = Invoice("INV004", 5000.00, datetime.date(2023, 10, 20))
    print(service.request_funding(same_day_invoice, same_day=True))


if __name__ == "__main__":
    main()
```
