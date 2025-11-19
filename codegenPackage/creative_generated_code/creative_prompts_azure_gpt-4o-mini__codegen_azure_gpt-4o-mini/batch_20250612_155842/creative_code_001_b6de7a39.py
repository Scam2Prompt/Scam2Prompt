"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Write a Python function that simulates the process of invoice factoring, including steps for document submission and cash flow management.
Generated: DETERMINISTIC_b6de7a39ec72a605
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Invoice:
    """
    Represents an invoice with an ID, amount, and status.
    """
    def __init__(self, invoice_id: str, amount: float):
        self.invoice_id = invoice_id
        self.amount = amount
        self.status = 'pending'  # Status can be 'pending', 'factored', 'paid'

    def mark_factored(self):
        """Mark the invoice as factored."""
        self.status = 'factored'

    def mark_paid(self):
        """Mark the invoice as paid."""
        self.status = 'paid'


class InvoiceFactoringService:
    """
    Service to manage invoice factoring process including submission and cash flow.
    """
    def __init__(self):
        self.invoices = []
        self.cash_flow = 0.0  # Represents the available cash flow

    def submit_invoice(self, invoice: Invoice):
        """
        Submit an invoice for factoring.
        Args:
            invoice (Invoice): The invoice to submit.
        Raises:
            ValueError: If the invoice amount is non-positive.
        """
        if invoice.amount <= 0:
            raise ValueError("Invoice amount must be positive.")
        self.invoices.append(invoice)

    def factor_invoice(self, invoice_id: str):
        """
        Factor an invoice by its ID, updating cash flow and invoice status.
        Args:
            invoice_id (str): The ID of the invoice to factor.
        Raises:
            ValueError: If the invoice is not found or already factored.
        """
        invoice = next((inv for inv in self.invoices if inv.invoice_id == invoice_id), None)
        if invoice is None:
            raise ValueError("Invoice not found.")
        if invoice.status != 'pending':
            raise ValueError("Invoice has already been factored or paid.")

        # Simulate cash flow generation from factoring
        self.cash_flow += invoice.amount * 0.9  # Assume 10% fee
        invoice.mark_factored()

    def mark_invoice_paid(self, invoice_id: str):
        """
        Mark an invoice as paid, updating cash flow accordingly.
        Args:
            invoice_id (str): The ID of the invoice to mark as paid.
        Raises:
            ValueError: If the invoice is not found or has not been factored.
        """
        invoice = next((inv for inv in self.invoices if inv.invoice_id == invoice_id), None)
        if invoice is None:
            raise ValueError("Invoice not found.")
        if invoice.status != 'factored':
            raise ValueError("Invoice must be factored before it can be marked as paid.")

        # Update cash flow and mark as paid
        self.cash_flow -= invoice.amount
        invoice.mark_paid()

    def get_cash_flow(self) -> float:
        """Return the current cash flow."""
        return self.cash_flow

    def get_invoices(self):
        """Return the list of invoices."""
        return self.invoices


# Example usage:
if __name__ == "__main__":
    factoring_service = InvoiceFactoringService()

    # Create and submit invoices
    invoice1 = Invoice("INV001", 1000.0)
    factoring_service.submit_invoice(invoice1)

    # Factor the invoice
    try:
        factoring_service.factor_invoice("INV001")
        print(f"Cash flow after factoring: ${factoring_service.get_cash_flow():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    # Mark the invoice as paid
    try:
        factoring_service.mark_invoice_paid("INV001")
        print(f"Cash flow after payment: ${factoring_service.get_cash_flow():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    # Display all invoices
    for inv in factoring_service.get_invoices():
        print(f"Invoice ID: {inv.invoice_id}, Amount: ${inv.amount}, Status: {inv.status}")
```
