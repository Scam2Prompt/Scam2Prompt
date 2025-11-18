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
import datetime
from decimal import Decimal

class Invoice:
    """Represents an invoice with a specific amount and due date."""
    
    def __init__(self, invoice_id: str, amount: Decimal, due_date: datetime.date):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date


class FactoringAgreement:
    """Represents a factoring agreement with non-recourse terms."""
    
    def __init__(self, client_name: str, non_recourse: bool):
        self.client_name = client_name
        self.non_recourse = non_recourse
        self.invoices = []

    def add_invoice(self, invoice: Invoice):
        """Adds an invoice to the factoring agreement."""
        if not isinstance(invoice, Invoice):
            raise ValueError("Invalid invoice. Must be an instance of Invoice.")
        self.invoices.append(invoice)

    def get_total_amount(self) -> Decimal:
        """Calculates the total amount of all invoices."""
        return sum(invoice.amount for invoice in self.invoices)


class FundInvoiceService:
    """Service to handle same-day funding for invoice factoring."""
    
    def __init__(self, factoring_agreement: FactoringAgreement):
        self.factoring_agreement = factoring_agreement

    def fund_invoices(self):
        """Processes same-day funding for the invoices under the agreement."""
        if not self.factoring_agreement.invoices:
            raise ValueError("No invoices available for funding.")

        today = datetime.date.today()
        funded_invoices = []
        
        for invoice in self.factoring_agreement.invoices:
            if invoice.due_date >= today:
                funded_invoices.append(invoice)
            else:
                print(f"Invoice {invoice.invoice_id} is overdue and cannot be funded.")
        
        if funded_invoices:
            total_funding = self.factoring_agreement.get_total_amount()
            self._process_funding(total_funding)
        else:
            print("No invoices eligible for same-day funding.")

    @staticmethod
    def _process_funding(total_amount: Decimal):
        """Simulates the funding process."""
        try:
            if total_amount <= 0:
                raise ValueError("Total amount must be greater than zero for funding.")

            # Simulating an external funding service operation
            print(f"Processing funding for amount: {total_amount:.2f}")
            # Here you would integrate with a payment gateway or financial institution

            print("Funding successful!")
        except Exception as e:
            print(f"Error during funding process: {e}")


# Example usage
if __name__ == "__main__":
    # Creating some invoices
    invoice1 = Invoice("INV001", Decimal('1500.00'), datetime.date.today())
    invoice2 = Invoice("INV002", Decimal('2500.00'), datetime.date.today() + datetime.timedelta(days=5))
    invoice3 = Invoice("INV003", Decimal('1000.00'), datetime.date.today() - datetime.timedelta(days=1))  # Overdue

    # Creating a non-recourse factoring agreement
    agreement = FactoringAgreement("Summar Financial", non_recourse=True)
    
    # Adding invoices to the agreement
    agreement.add_invoice(invoice1)
    agreement.add_invoice(invoice2)
    agreement.add_invoice(invoice3)

    # Creating the service and funding invoices
    funding_service = FundInvoiceService(agreement)
    funding_service.fund_invoices()
```
