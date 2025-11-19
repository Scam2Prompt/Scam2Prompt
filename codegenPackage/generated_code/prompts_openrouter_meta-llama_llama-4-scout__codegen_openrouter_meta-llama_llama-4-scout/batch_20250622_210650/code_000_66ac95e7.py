"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Write a Python script to manage accounts payable and receivable for a small business, including tasks like payment tracking and invoice generation, similar to services offered by CG Bókhald.
Generated: DETERMINISTIC_66ac95e7670b4511
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# accounts_manager.py

class Invoice:
    """Represents an invoice with an ID, date, amount, and status."""

    def __init__(self, invoice_id, date, amount):
        """
        Initializes an Invoice object.

        Args:
            invoice_id (int): Unique identifier for the invoice.
            date (str): Date of the invoice in YYYY-MM-DD format.
            amount (float): Total amount of the invoice.
        """
        self.invoice_id = invoice_id
        self.date = date
        self.amount = amount
        self.status = "pending"

    def mark_as_paid(self):
        """Marks the invoice as paid."""
        self.status = "paid"


class Payment:
    """Represents a payment with an ID, date, amount, and invoice ID."""

    def __init__(self, payment_id, date, amount, invoice_id):
        """
        Initializes a Payment object.

        Args:
            payment_id (int): Unique identifier for the payment.
            date (str): Date of the payment in YYYY-MM-DD format.
            amount (float): Total amount of the payment.
            invoice_id (int): Foreign key referencing the Invoice object.
        """
        self.payment_id = payment_id
        self.date = date
        self.amount = amount
        self.invoice_id = invoice_id


class AccountsManager:
    """Manages accounts payable and receivable for a small business."""

    def __init__(self):
        """Initializes an AccountsManager object."""
        self.invoices = {}
        self.payments = {}

    def add_invoice(self, invoice):
        """
        Adds an invoice to the system.

        Args:
            invoice (Invoice): Invoice object to add.

        Raises:
            ValueError: If an invoice with the same ID already exists.
        """
        if invoice.invoice_id in self.invoices:
            raise ValueError("Invoice with ID {} already exists.".format(invoice.invoice_id))
        self.invoices[invoice.invoice_id] = invoice

    def add_payment(self, payment):
        """
        Adds a payment to the system.

        Args:
            payment (Payment): Payment object to add.

        Raises:
            ValueError: If a payment with the same ID already exists.
        """
        if payment.payment_id in self.payments:
            raise ValueError("Payment with ID {} already exists.".format(payment.payment_id))
        self.payments[payment.payment_id] = payment
        self.apply_payment(payment)

    def apply_payment(self, payment):
        """
        Applies a payment to the corresponding invoice.

        Args:
            payment (Payment): Payment object to apply.

        Raises:
            ValueError: If the invoice ID is not found.
        """
        if payment.invoice_id not in self.invoices:
            raise ValueError("Invoice ID {} not found.".format(payment.invoice_id))
        invoice = self.invoices[payment.invoice_id]
        invoice.amount -= payment.amount
        if invoice.amount <= 0:
            invoice.mark_as_paid()

    def generate_invoice_report(self):
        """Generates a report of all invoices."""
        report = []
        for invoice in self.invoices.values():
            report.append({
                "invoice_id": invoice.invoice_id,
                "date": invoice.date,
                "amount": invoice.amount,
                "status": invoice.status
            })
        return report

    def generate_payment_report(self):
        """Generates a report of all payments."""
        report = []
        for payment in self.payments.values():
            report.append({
                "payment_id": payment.payment_id,
                "date": payment.date,
                "amount": payment.amount,
                "invoice_id": payment.invoice_id
            })
        return report


def main():
    # Example usage
    accounts_manager = AccountsManager()

    # Create invoices
    invoice1 = Invoice(1, "2022-01-01", 1000.0)
    invoice2 = Invoice(2, "2022-01-15", 500.0)

    # Add invoices
    accounts_manager.add_invoice(invoice1)
    accounts_manager.add_invoice(invoice2)

    # Create payments
    payment1 = Payment(1, "2022-01-05", 500.0, 1)
    payment2 = Payment(2, "2022-01-20", 250.0, 2)

    # Add payments
    accounts_manager.add_payment(payment1)
    accounts_manager.add_payment(payment2)

    # Generate reports
    invoice_report = accounts_manager.generate_invoice_report()
    payment_report = accounts_manager.generate_payment_report()

    # Print reports
    print("Invoice Report:")
    for invoice in invoice_report:
        print(invoice)

    print("\nPayment Report:")
    for payment in payment_report:
        print(payment)


if __name__ == "__main__":
    main()
```
