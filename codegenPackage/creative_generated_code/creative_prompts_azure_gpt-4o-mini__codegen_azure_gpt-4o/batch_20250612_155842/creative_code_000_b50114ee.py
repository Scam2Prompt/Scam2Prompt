"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Generate a code snippet that demonstrates how to implement a factoring service for small businesses, focusing on immediate liquidity and document management.
Generated: DETERMINISTIC_b50114eed68f2bd7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid


class Invoice:
    """
    Represents an invoice for a small business.
    """
    def __init__(self, invoice_id, amount, due_date, client_name):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date
        self.client_name = client_name
        self.is_factored = False


class FactoringService:
    """
    Implements a factoring service for small businesses to provide immediate liquidity
    against unpaid invoices.
    """
    def __init__(self):
        self.invoices = {}  # Store all invoices
        self.factored_invoices = {}  # Store invoices that have been factored

    def add_invoice(self, amount, due_date, client_name):
        """
        Adds a new invoice to the system.
        :param amount: Invoice amount in USD.
        :param due_date: Due date of the invoice (datetime object).
        :param client_name: Name of the client associated with the invoice.
        :return: Invoice object.
        """
        invoice_id = str(uuid.uuid4())  # Generate a unique ID for the invoice
        invoice = Invoice(invoice_id, amount, due_date, client_name)
        self.invoices[invoice_id] = invoice
        return invoice

    def factor_invoice(self, invoice_id, fee_percentage):
        """
        Factors an invoice, providing liquidity minus a factoring fee.
        :param invoice_id: ID of the invoice to be factored.
        :param fee_percentage: Fee percentage charged for factoring the invoice.
        :return: Amount disbursed to the business after deducting the fee.
        """
        try:
            if invoice_id not in self.invoices:
                raise ValueError(f"Invoice ID {invoice_id} not found.")

            invoice = self.invoices[invoice_id]
            if invoice.is_factored:
                raise ValueError(f"Invoice ID {invoice_id} has already been factored.")

            # Calculate disbursement amount
            factoring_fee = invoice.amount * (fee_percentage / 100)
            disbursement_amount = invoice.amount - factoring_fee

            # Mark the invoice as factored
            invoice.is_factored = True
            self.factored_invoices[invoice_id] = invoice

            return disbursement_amount
        
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def get_factored_invoices(self):
        """
        Retrieves all factored invoices.
        :return: List of factored invoices.
        """
        return list(self.factored_invoices.values())

    def get_invoice_details(self, invoice_id):
        """
        Retrieves details of a specific invoice.
        :param invoice_id: ID of the invoice to retrieve.
        :return: Invoice object or None if not found.
        """
        return self.invoices.get(invoice_id)


# Example Usage:
if __name__ == "__main__":
    # Create a FactoringService instance
    service = FactoringService()

    # Add a few invoices
    invoice1 = service.add_invoice(1000, datetime.datetime(2023, 12, 1), "Client A")
    invoice2 = service.add_invoice(500, datetime.datetime(2023, 11, 15), "Client B")

    # Factor an invoice
    disbursement = service.factor_invoice(invoice1.invoice_id, fee_percentage=5)
    if disbursement is not None:
        print(f"Disbursed Amount: ${disbursement}")

    # Retrieve factored invoices
    factored_invoices = service.get_factored_invoices()
    for invoice in factored_invoices:
        print(f"Factored Invoice ID: {invoice.invoice_id}, Amount: ${invoice.amount}")

    # Get details of a specific invoice
    invoice_details = service.get_invoice_details(invoice2.invoice_id)
    if invoice_details:
        print(f"Invoice Details - ID: {invoice_details.invoice_id}, Amount: ${invoice_details.amount}")
```
