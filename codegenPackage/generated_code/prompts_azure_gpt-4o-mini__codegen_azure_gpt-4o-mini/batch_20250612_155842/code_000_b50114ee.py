"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Generate a code snippet that demonstrates how to implement a factoring service for small businesses, focusing on immediate liquidity and document management.
Generated: DETERMINISTIC_b50114eed68f2bd7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Invoice:
    """Class representing an invoice."""
    
    def __init__(self, amount: float, due_date: datetime, client_name: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the invoice
        self.amount = amount          # Total amount of the invoice
        self.due_date = due_date      # Due date for the invoice
        self.client_name = client_name # Name of the client

    def __repr__(self):
        return f"Invoice(id={self.id}, amount={self.amount}, due_date={self.due_date}, client_name={self.client_name})"


class FactoringService:
    """Class representing a factoring service for small businesses."""
    
    def __init__(self):
        self.invoices: List[Invoice] = []  # List to store invoices

    def add_invoice(self, amount: float, due_date: datetime, client_name: str) -> Invoice:
        """Add a new invoice to the factoring service."""
        if amount <= 0:
            raise ValueError("Invoice amount must be greater than zero.")
        if due_date < datetime.now():
            raise ValueError("Due date must be in the future.")
        
        invoice = Invoice(amount, due_date, client_name)
        self.invoices.append(invoice)
        return invoice

    def factor_invoice(self, invoice_id: str) -> Optional[float]:
        """Factor an invoice to provide immediate liquidity."""
        invoice = self._find_invoice(invoice_id)
        if invoice is None:
            raise ValueError("Invoice not found.")
        
        # Assuming a factoring fee of 10%
        factoring_fee = 0.10
        liquidity = invoice.amount * (1 - factoring_fee)
        
        # Remove the invoice from the list after factoring
        self.invoices.remove(invoice)
        return liquidity

    def _find_invoice(self, invoice_id: str) -> Optional[Invoice]:
        """Private method to find an invoice by its ID."""
        for invoice in self.invoices:
            if invoice.id == invoice_id:
                return invoice
        return None

    def list_invoices(self) -> List[Dict]:
        """List all invoices in a readable format."""
        return [vars(invoice) for invoice in self.invoices]


# Example usage
if __name__ == "__main__":
    try:
        factoring_service = FactoringService()
        
        # Adding invoices
        invoice1 = factoring_service.add_invoice(1000.0, datetime(2023, 12, 1), "Client A")
        invoice2 = factoring_service.add_invoice(2000.0, datetime(2023, 11, 15), "Client B")
        
        print("Invoices added:")
        print(factoring_service.list_invoices())
        
        # Factoring an invoice
        liquidity = factoring_service.factor_invoice(invoice1.id)
        print(f"Liquidity obtained from factoring invoice {invoice1.id}: ${liquidity:.2f}")
        
        print("Remaining invoices:")
        print(factoring_service.list_invoices())
        
    except ValueError as e:
        print(f"Error: {e}")
```
