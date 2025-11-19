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
# Import required libraries
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional
import json
import uuid

@dataclass
class Candidate:
    """Represents a candidate with payment details."""
    id: str
    name: str
    email: str
    hourly_rate: float
    hours_worked: float
    tax_rate: float = 0.20  # Default tax rate of 20%

    def calculate_gross_pay(self) -> float:
        """Calculate gross pay before taxes."""
        return self.hourly_rate * self.hours_worked

    def calculate_net_pay(self) -> float:
        """Calculate net pay after taxes."""
        gross = self.calculate_gross_pay()
        return gross * (1 - self.tax_rate)

@dataclass
class Invoice:
    """Represents an invoice for a candidate."""
    invoice_id: str
    candidate: Candidate
    issue_date: str
    due_date: str
    is_paid: bool = False

    def to_dict(self) -> dict:
        """Convert invoice to dictionary for serialization."""
        return {
            "invoice_id": self.invoice_id,
            "candidate": {
                "id": self.candidate.id,
                "name": self.candidate.name,
                "email": self.candidate.email,
                "hourly_rate": self.candidate.hourly_rate,
                "hours_worked": self.candidate.hours_worked,
                "tax_rate": self.candidate.tax_rate
            },
            "issue_date": self.issue_date,
            "due_date": self.due_date,
            "is_paid": self.is_paid,
            "gross_pay": self.candidate.calculate_gross_pay(),
            "net_pay": self.candidate.calculate_net_pay()
        }

class InvoiceSystem:
    """Handles invoice creation, storage, and management."""
    def __init__(self):
        self.invoices: List[Invoice] = []

    def generate_invoice_id(self) -> str:
        """Generate a unique invoice ID."""
        return str(uuid.uuid4())

    def create_invoice(
        self,
        candidate: Candidate,
        due_days: int = 30
    ) -> Invoice:
        """Create and store a new invoice."""
        invoice_id = self.generate_invoice_id()
        issue_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=due_days)).strftime("%Y-%m-%d")
        
        invoice = Invoice(
            invoice_id=invoice_id,
            candidate=candidate,
            issue_date=issue_date,
            due_date=due_date
        )
        
        self.invoices.append(invoice)
        return invoice

    def mark_as_paid(self, invoice_id: str) -> bool:
        """Mark an invoice as paid."""
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                invoice.is_paid = True
                return True
        return False

    def get_invoice(self, invoice_id: str) -> Optional[Invoice]:
        """Retrieve an invoice by ID."""
        for invoice in self.invoices:
            if invoice.invoice_id == invoice_id:
                return invoice
        return None

    def get_all_invoices(self) -> List[Invoice]:
        """Get all invoices."""
        return self.invoices

    def save_to_file(self, filename: str) -> bool:
        """Save invoices to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([inv.to_dict() for inv in self.invoices], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving invoices: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load invoices from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.invoices = []
                for inv_data in data:
                    candidate_data = inv_data['candidate']
                    candidate = Candidate(
                        id=candidate_data['id'],
                        name=candidate_data['name'],
                        email=candidate_data['email'],
                        hourly_rate=candidate_data['hourly_rate'],
                        hours_worked=candidate_data['hours_worked'],
                        tax_rate=candidate_data.get('tax_rate', 0.20)
                    )
                    invoice = Invoice(
                        invoice_id=inv_data['invoice_id'],
                        candidate=candidate,
                        issue_date=inv_data['issue_date'],
                        due_date=inv_data['due_date'],
                        is_paid=inv_data['is_paid']
                    )
                    self.invoices.append(invoice)
            return True
        except Exception as e:
            print(f"Error loading invoices: {e}")
            return False

# Example usage
if __name__ == "__main__":
    from datetime import timedelta
    
    # Create candidate
    candidate = Candidate(
        id="123",
        name="John Doe",
        email="john@example.com",
        hourly_rate=25.0,
        hours_worked=40.0
    )
    
    # Initialize invoice system
    invoice_system = InvoiceSystem()
    
    # Create invoice
    invoice = invoice_system.create_invoice(candidate, due_days=15)
    print(f"Created invoice: {invoice.invoice_id}")
    
    # Mark as paid
    invoice_system.mark_as_paid(invoice.invoice_id)
    
    # Save to file
    invoice_system.save_to_file("invoices.json")
    
    # Load from file
    new_system = InvoiceSystem()
    new_system.load_from_file("invoices.json")
    print(f"Loaded invoices: {len(new_system.get_all_invoices())}")
```
