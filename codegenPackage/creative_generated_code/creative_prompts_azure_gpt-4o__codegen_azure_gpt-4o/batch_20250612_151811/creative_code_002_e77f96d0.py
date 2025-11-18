"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Generate code to implement a same-day funding feature for invoice factoring, ensuring non-recourse terms as outlined by Summar Financial.
Generated: DETERMINISTIC_e77f96d0d0ce3188
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Invoice Factoring - Same-Day Funding Feature (Non-recourse Terms)
# This script implements a system for processing invoices for factoring
# with same-day funding and non-recourse terms as outlined by Summar Financial.

import datetime
from typing import List, Dict, Union

class InvoiceFactoringService:
    """
    Service for managing invoice factoring with same-day funding
    and non-recourse terms.
    """

    def __init__(self):
        """
        Initialize the service with an empty list of invoices.
        """
        self.invoices = []

    def add_invoice(self, invoice_id: str, amount: float, due_date: datetime.date, debtor_credit_rating: int) -> None:
        """
        Add a new invoice for factoring.

        :param invoice_id: Unique identifier for the invoice
        :param amount: Amount of the invoice (in USD)
        :param due_date: Due date of the invoice
        :param debtor_credit_rating: Credit rating of the debtor (1-100 scale)
        :raises ValueError: If amount is negative or credit rating is invalid
        """
        if amount <= 0:
            raise ValueError("Invoice amount must be greater than zero.")
        if not (1 <= debtor_credit_rating <= 100):
            raise ValueError("Debtor credit rating must be between 1 and 100.")

        self.invoices.append({
            "invoice_id": invoice_id,
            "amount": amount,
            "due_date": due_date,
            "debtor_credit_rating": debtor_credit_rating,
            "status": "pending",  # Initial status
            "funding_date": None
        })

    def process_invoices(self) -> List[Dict[str, Union[str, float, datetime.date]]]:
        """
        Process invoices for same-day funding under non-recourse terms.

        :return: List of successfully funded invoices
        """
        funded_invoices = []
        today = datetime.date.today()

        for invoice in self.invoices:
            # Check for eligibility: Non-recourse terms require debtor's credit rating >= 75
            if invoice['debtor_credit_rating'] < 75:
                invoice['status'] = "rejected"
                continue

            # Invoice must be due in the future to qualify for factoring
            if invoice['due_date'] <= today:
                invoice['status'] = "rejected"
                continue

            # Mark invoice as funded
            invoice['status'] = "funded"
            invoice['funding_date'] = today
            funded_invoices.append(invoice)

        return funded_invoices

    def get_invoice_status(self, invoice_id: str) -> Union[Dict[str, Union[str, float, datetime.date]], None]:
        """
        Retrieve the status of a specific invoice.

        :param invoice_id: Unique identifier of the invoice
        :return: Invoice details if found, None otherwise
        """
        for invoice in self.invoices:
            if invoice['invoice_id'] == invoice_id:
                return invoice
        return None


# Example Usage
if __name__ == "__main__":
    try:
        factoring_service = InvoiceFactoringService()

        # Add invoices for processing
        factoring_service.add_invoice("INV001", 1000.0, datetime.date(2023, 11, 15), 85)
        factoring_service.add_invoice("INV002", 500.0, datetime.date(2023, 10, 20), 70)
        factoring_service.add_invoice("INV003", 1500.0, datetime.date(2023, 12, 1), 95)

        # Process invoices for same-day funding
        funded = factoring_service.process_invoices()
        print("Funded Invoices:")
        for invoice in funded:
            print(invoice)

        # Check invoice statuses
        print("\nInvoice Statuses:")
        for invoice_id in ["INV001", "INV002", "INV003"]:
            status = factoring_service.get_invoice_status(invoice_id)
            print(status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
