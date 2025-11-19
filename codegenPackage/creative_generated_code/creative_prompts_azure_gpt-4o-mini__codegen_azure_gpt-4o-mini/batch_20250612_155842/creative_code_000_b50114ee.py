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
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Invoice:
    """Represents an invoice for a small business."""
    def __init__(self, amount: float, due_date: datetime, description: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the invoice
        self.amount = amount          # Amount of the invoice
        self.due_date = due_date      # Due date for the payment
        self.description = description  # Description of the invoice
        self.is_factored = False      # Status of whether the invoice has been factored or not

    def factor(self):
        """Marks the invoice as factored."""
        if self.is_factored:
            raise ValueError("Invoice has already been factored.")
        self.is_factored = True

class FactoringService:
    """Service for factoring invoices for immediate liquidity."""
    def __init__(self):
        self.invoices: List[Invoice] = []  # List to store invoices

    def add_invoice(self, amount: float, due_date: datetime, description: str) -> Invoice:
        """Adds a new invoice to the service."""
        if amount <= 0:
            raise ValueError("Invoice amount must be greater than zero.")
        if due_date < datetime.now():
            raise ValueError("Due date must be in the future.")
        
        invoice = Invoice(amount, due_date, description)
        self.invoices.append(invoice)
        return invoice

    def factor_invoice(self, invoice_id: str) -> Optional[float]:
        """Factors an invoice by its ID and returns the liquidity provided."""
        for invoice in self.invoices:
            if invoice.id == invoice_id:
                invoice.factor()  # Mark the invoice as factored
                liquidity = invoice.amount * 0.95  # Assume a 5% fee for factoring
                return liquidity
        raise ValueError("Invoice not found.")

    def get_invoices(self) -> List[Dict]:
        """Returns a list of all invoices with their details."""
        return [{
            'id': invoice.id,
            'amount': invoice.amount,
            'due_date': invoice.due_date,
            'description': invoice.description,
            'is_factored': invoice.is_factored
        } for invoice in self.invoices]

# Example Usage
if __name__ == "__main__":
    try:
        service = FactoringService()
        
        # Adding some invoices for testing
        invoice1 = service.add_invoice(1000.0, datetime(2023, 12, 1), "Web Development Project")
        invoice2 = service.add_invoice(2000.0, datetime(2023, 11, 15), "App Development Project")
        
        # Displaying all invoices
        print("Invoices:", service.get_invoices())
        
        # Factoring an invoice
        liquidity = service.factor_invoice(invoice1.id)
        print(f"Liquidity obtained from factoring invoice {invoice1.id}: ${liquidity:.2f}")

        # Displaying updated invoices
        print("Updated Invoices:", service.get_invoices())
    
    except ValueError as e:
        print(f"Error: {e}")
```
