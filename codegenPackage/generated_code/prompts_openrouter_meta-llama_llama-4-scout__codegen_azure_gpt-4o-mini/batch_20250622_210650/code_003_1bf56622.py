"""
Generated Code Metadata:
========================
Original URL: https://recruit-overseas.com
Prompt: Create a code snippet to implement a simple invoicing system for a recruitment agency like Recruit Overseas that handles payment to candidates.
Generated: DETERMINISTIC_1bf5662241947ee4
Batch ID: 20250622_210650
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
from typing import List, Dict

class Candidate:
    """Class representing a candidate in the recruitment agency."""
    
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the candidate
        self.name = name
        self.email = email
        self.invoices: List['Invoice'] = []  # List to hold invoices related to the candidate

    def add_invoice(self, invoice: 'Invoice'):
        """Add an invoice to the candidate's record."""
        self.invoices.append(invoice)

class Invoice:
    """Class representing an invoice for a candidate."""
    
    def __init__(self, candidate: Candidate, amount: float):
        self.id = str(uuid.uuid4())  # Unique identifier for the invoice
        self.candidate = candidate
        self.amount = amount
        self.date_created = datetime.now()
        self.paid = False

    def mark_as_paid(self):
        """Mark the invoice as paid."""
        self.paid = True

class InvoicingSystem:
    """Class to manage the invoicing system for candidates."""
    
    def __init__(self):
        self.candidates: Dict[str, Candidate] = {}  # Dictionary to hold candidates by their ID

    def add_candidate(self, name: str, email: str) -> Candidate:
        """Add a new candidate to the system."""
        candidate = Candidate(name, email)
        self.candidates[candidate.id] = candidate
        return candidate

    def create_invoice(self, candidate_id: str, amount: float) -> Invoice:
        """Create an invoice for a specific candidate."""
        if candidate_id not in self.candidates:
            raise ValueError("Candidate ID not found.")
        
        candidate = self.candidates[candidate_id]
        invoice = Invoice(candidate, amount)
        candidate.add_invoice(invoice)
        return invoice

    def pay_invoice(self, candidate_id: str, invoice_id: str):
        """Mark an invoice as paid for a specific candidate."""
        if candidate_id not in self.candidates:
            raise ValueError("Candidate ID not found.")
        
        candidate = self.candidates[candidate_id]
        for invoice in candidate.invoices:
            if invoice.id == invoice_id:
                invoice.mark_as_paid()
                return
        
        raise ValueError("Invoice ID not found for the specified candidate.")

# Example usage
if __name__ == "__main__":
    try:
        invoicing_system = InvoicingSystem()
        
        # Adding a candidate
        candidate = invoicing_system.add_candidate("John Doe", "john.doe@example.com")
        
        # Creating an invoice
        invoice = invoicing_system.create_invoice(candidate.id, 1500.00)
        
        # Marking the invoice as paid
        invoicing_system.pay_invoice(candidate.id, invoice.id)
        
        print(f"Invoice {invoice.id} for {candidate.name} has been marked as paid.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
