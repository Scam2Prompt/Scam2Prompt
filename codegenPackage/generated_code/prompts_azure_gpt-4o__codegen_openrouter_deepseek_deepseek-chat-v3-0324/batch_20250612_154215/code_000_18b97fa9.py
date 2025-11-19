"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Write Python code to simulate a factoring service that calculates liquidity based on the value of invoices provided, as described on the Adelanto.cl website.
Generated: DETERMINISTIC_18b97fa9d6d9fd51
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Union
from datetime import datetime, timedelta
from enum import Enum

class InvoiceStatus(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PAID = "PAID"

class Invoice:
    def __init__(
        self,
        invoice_id: str,
        amount: float,
        due_date: datetime,
        debtor_name: str,
        status: InvoiceStatus = InvoiceStatus.PENDING
    ):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date
        self.debtor_name = debtor_name
        self.status = status

    def to_dict(self) -> Dict[str, Union[str, float]]:
        return {
            "invoice_id": self.invoice_id,
            "amount": self.amount,
            "due_date": self.due_date.isoformat(),
            "debtor_name": self.debtor_name,
            "status": self.status.value
        }

class FactoringService:
    def __init__(self, advance_rate: float = 0.8, fee_rate: float = 0.03):
        """
        Initialize the factoring service with default advance and fee rates.
        
        Args:
            advance_rate: Percentage of invoice amount to advance (default 80%)
            fee_rate: Percentage fee charged on the invoice amount (default 3%)
        """
        self.advance_rate = advance_rate
        self.fee_rate = fee_rate
        self.invoices: Dict[str, Invoice] = {}

    def add_invoice(self, invoice: Invoice) -> None:
        """Add an invoice to the factoring service."""
        if invoice.invoice_id in self.invoices:
            raise ValueError(f"Invoice with ID {invoice.invoice_id} already exists")
        self.invoices[invoice.invoice_id] = invoice

    def approve_invoice(self, invoice_id: str) -> None:
        """Approve an invoice for factoring."""
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        if self.invoices[invoice_id].status != InvoiceStatus.PENDING:
            raise ValueError("Only pending invoices can be approved")
        self.invoices[invoice_id].status = InvoiceStatus.APPROVED

    def reject_invoice(self, invoice_id: str) -> None:
        """Reject an invoice for factoring."""
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        if self.invoices[invoice_id].status != InvoiceStatus.PENDING:
            raise ValueError("Only pending invoices can be rejected")
        self.invoices[invoice_id].status = InvoiceStatus.REJECTED

    def mark_as_paid(self, invoice_id: str) -> None:
        """Mark an invoice as paid by the debtor."""
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        if self.invoices[invoice_id].status != InvoiceStatus.APPROVED:
            raise ValueError("Only approved invoices can be marked as paid")
        self.invoices[invoice_id].status = InvoiceStatus.PAID

    def calculate_liquidity(self) -> Dict[str, float]:
        """
        Calculate available liquidity based on approved invoices.
        
        Returns:
            Dictionary containing:
                - total_approved: Total amount of approved invoices
                - available_liquidity: Amount available for advance (after advance rate)
                - total_fees: Estimated fees for the advances
        """
        approved_invoices = [
            inv for inv in self.invoices.values() 
            if inv.status == InvoiceStatus.APPROVED
        ]
        
        total_approved = sum(inv.amount for inv in approved_invoices)
        available_liquidity = total_approved * self.advance_rate
        total_fees = total_approved * self.fee_rate
        
        return {
            "total_approved": total_approved,
            "available_liquidity": available_liquidity,
            "total_fees": total_fees
        }

    def get_invoice_status(self, invoice_id: str) -> InvoiceStatus:
        """Get the status of a specific invoice."""
        if invoice_id not in self.invoices:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        return self.invoices[invoice_id].status

    def list_invoices(self, status: InvoiceStatus = None) -> List[Dict[str, Union[str, float]]]:
        """
        List all invoices, optionally filtered by status.
        
        Args:
            status: Optional filter for invoice status
            
        Returns:
            List of invoice dictionaries
        """
        invoices = self.invoices.values()
        if status:
            invoices = [inv for inv in invoices if inv.status == status]
        return [inv.to_dict() for inv in invoices]

# Example usage
if __name__ == "__main__":
    service = FactoringService()
    
    # Add some sample invoices
    invoice1 = Invoice(
        invoice_id="INV-001",
        amount=10000.0,
        due_date=datetime.now() + timedelta(days=30),
        debtor_name="Company A"
    )
    
    invoice2 = Invoice(
        invoice_id="INV-002",
        amount=15000.0,
        due_date=datetime.now() + timedelta(days=45),
        debtor_name="Company B"
    )
    
    service.add_invoice(invoice1)
    service.add_invoice(invoice2)
    
    # Approve one invoice
    service.approve_invoice("INV-001")
    
    # Calculate liquidity
    liquidity = service.calculate_liquidity()
    print("Liquidity Report:")
    print(json.dumps(liquidity, indent=2))
    
    # List all invoices
    print("\nAll Invoices:")
    print(json.dumps(service.list_invoices(), indent=2))
```
