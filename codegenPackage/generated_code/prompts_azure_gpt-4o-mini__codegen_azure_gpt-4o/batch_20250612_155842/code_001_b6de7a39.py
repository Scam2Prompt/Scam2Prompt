"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Write a Python function that simulates the process of invoice factoring, including steps for document submission and cash flow management.
Generated: DETERMINISTIC_b6de7a39ec72a605
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class InvoiceFactoring:
    def __init__(self):
        """
        Initializes the InvoiceFactoring system with empty records for invoices and cash flow.
        """
        self.invoices = []  # List to store submitted invoices
        self.cash_flow = 0  # Tracks the current cash flow balance

    def submit_invoice(self, invoice_id, amount, due_date):
        """
        Submits an invoice for factoring.

        Args:
            invoice_id (str): Unique identifier for the invoice.
            amount (float): Amount of the invoice.
            due_date (str): Due date of the invoice in 'YYYY-MM-DD' format.

        Returns:
            str: Confirmation message for invoice submission.
        """
        try:
            # Validate due_date format
            due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d')
            if due_date_obj < datetime.datetime.now():
                return "Error: Due date cannot be in the past."

            # Add invoice to the system
            self.invoices.append({
                'invoice_id': invoice_id,
                'amount': amount,
                'due_date': due_date_obj
            })
            return f"Invoice {invoice_id} submitted successfully."
        except ValueError:
            return "Error: Invalid date format. Use 'YYYY-MM-DD'."

    def factor_invoice(self, invoice_id, discount_rate):
        """
        Factors an invoice by providing immediate cash flow at a discounted rate.

        Args:
            invoice_id (str): Unique identifier for the invoice to be factored.
            discount_rate (float): Discount rate as a percentage (e.g., 5 for 5%).

        Returns:
            str: Confirmation message for factoring or error message if invoice not found.
        """
        for invoice in self.invoices:
            if invoice['invoice_id'] == invoice_id:
                # Calculate discounted amount
                discounted_amount = invoice['amount'] * (1 - discount_rate / 100)
                self.cash_flow += discounted_amount

                # Remove the factored invoice from the system
                self.invoices.remove(invoice)
                return (f"Invoice {invoice_id} factored successfully. "
                        f"Cash flow increased by ${discounted_amount:.2f}.")
        return f"Error: Invoice {invoice_id} not found."

    def get_cash_flow(self):
        """
        Retrieves the current cash flow balance.

        Returns:
            float: Current cash flow balance.
        """
        return self.cash_flow

    def get_pending_invoices(self):
        """
        Retrieves a list of all pending invoices.

        Returns:
            list: List of dictionaries representing pending invoices.
        """
        return self.invoices


# Example usage:
if __name__ == "__main__":
    factoring_system = InvoiceFactoring()

    # Submit invoices
    print(factoring_system.submit_invoice("INV001", 1000.0, "2023-12-01"))
    print(factoring_system.submit_invoice("INV002", 500.0, "2023-11-15"))

    # Factor an invoice
    print(factoring_system.factor_invoice("INV001", 5))  # 5% discount

    # Check cash flow
    print(f"Current cash flow: ${factoring_system.get_cash_flow():.2f}")

    # Check pending invoices
    print("Pending invoices:", factoring_system.get_pending_invoices())
```
