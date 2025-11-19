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
import uuid
from datetime import datetime
from typing import List, Dict

class Invoice:
    """
    Represents an invoice with an ID, amount, due date, and factoring status.
    """
    def __init__(self, invoice_id: str, amount: float, due_date: datetime):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date
        self.is_factored = False

class FactoringCompany:
    """
    Represents the factoring company that manages cash flow and invoice factoring.
    """
    def __init__(self, cash_reserve: float):
        self.cash_reserve = cash_reserve
        self.factored_invoices: List[Dict[str, any]] = []

    def submit_invoice(self, invoice: Invoice) -> str:
        """
        Simulates submission of an invoice for factoring.
        """
        if invoice.is_factored:
            return f"Invoice {invoice.invoice_id} is already factored."
        if invoice.amount > self.cash_reserve:
            return "Insufficient cash reserve to factor this invoice."
        
        # Generate a unique factoring ID for tracking
        factoring_id = str(uuid.uuid4())
        invoice.is_factored = True
        
        # Update cash flow and record the factored invoice
        self.cash_reserve -= invoice.amount
        self.factored_invoices.append({
            "factoring_id": factoring_id,
            "invoice_id": invoice.invoice_id,
            "amount": invoice.amount,
            "due_date": invoice.due_date,
            "factored_date": datetime.now()
        })
        
        return f"Invoice {invoice.invoice_id} factored successfully. Factoring ID: {factoring_id}"

    def check_cash_reserve(self) -> float:
        """
        Returns the current cash reserve available.
        """
        return self.cash_reserve

    def list_factored_invoices(self) -> List[Dict[str, any]]:
        """
        Retrieves all invoices that have been factored.
        """
        return self.factored_invoices


# Example usage
def simulate_invoice_factoring():
    """
    Function to simulate invoice factoring process.
    """
    # Initialize the factoring company with a cash reserve of $10,000
    factoring_company = FactoringCompany(cash_reserve=10000.0)
    
    # Create some sample invoices
    invoice_1 = Invoice(invoice_id="INV001", amount=3000.0, due_date=datetime(2023, 12, 31))
    invoice_2 = Invoice(invoice_id="INV002", amount=7000.0, due_date=datetime(2024, 1, 15))
    invoice_3 = Invoice(invoice_id="INV003", amount=12000.0, due_date=datetime(2024, 2, 1))

    # Simulate invoice submission and factoring
    print(factoring_company.submit_invoice(invoice_1))  # Should succeed
    print(factoring_company.submit_invoice(invoice_2))  # Should succeed
    print(factoring_company.submit_invoice(invoice_3))  # Should fail due to insufficient cash reserve

    # Check the cash reserve after factoring
    print(f"Remaining cash reserve: ${factoring_company.check_cash_reserve():,.2f}")

    # List all factored invoices
    print("Factored Invoices:")
    for factored_invoice in factoring_company.list_factored_invoices():
        print(factored_invoice)


# Run the simulation
if __name__ == "__main__":
    simulate_invoice_factoring()
```
