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
# factoring_service.py

from typing import Dict, List
from enum import Enum
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InvoiceStatus(str, Enum):
    """Invoice status"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class Invoice:
    """Invoice document"""
    def __init__(self, id: int, customer_name: str, amount: float, due_date: datetime):
        self.id = id
        self.customer_name = customer_name
        self.amount = amount
        self.due_date = due_date
        self.status = InvoiceStatus.PENDING

    def __repr__(self):
        return f"Invoice(id={self.id}, customer_name='{self.customer_name}', amount={self.amount}, due_date={self.due_date}, status={self.status})"

class FactoringService:
    """Factoring service for small businesses"""
    def __init__(self):
        self.invoices: Dict[int, Invoice] = {}
        self.advance_rate = 0.8  # 80% advance rate

    def add_invoice(self, invoice: Invoice):
        """Add an invoice to the system"""
        self.invoices[invoice.id] = invoice
        logger.info(f"Added invoice {invoice.id}")

    def approve_invoice(self, invoice_id: int):
        """Approve an invoice for factoring"""
        if invoice_id not in self.invoices:
            logger.error(f"Invoice {invoice_id} not found")
            raise ValueError(f"Invoice {invoice_id} not found")
        
        invoice = self.invoices[invoice_id]
        invoice.status = InvoiceStatus.APPROVED
        logger.info(f"Approved invoice {invoice_id}")

    def reject_invoice(self, invoice_id: int):
        """Reject an invoice for factoring"""
        if invoice_id not in self.invoices:
            logger.error(f"Invoice {invoice_id} not found")
            raise ValueError(f"Invoice {invoice_id} not found")
        
        invoice = self.invoices[invoice_id]
        invoice.status = InvoiceStatus.REJECTED
        logger.info(f"Rejected invoice {invoice_id}")

    def calculate_advance(self, invoice_id: int) -> float:
        """Calculate the advance amount for an approved invoice"""
        if invoice_id not in self.invoices:
            logger.error(f"Invoice {invoice_id} not found")
            raise ValueError(f"Invoice {invoice_id} not found")
        
        invoice = self.invoices[invoice_id]
        if invoice.status != InvoiceStatus.APPROVED:
            logger.error(f"Invoice {invoice_id} is not approved")
            raise ValueError(f"Invoice {invoice_id} is not approved")
        
        advance_amount = invoice.amount * self.advance_rate
        logger.info(f"Calculated advance amount {advance_amount} for invoice {invoice_id}")
        return advance_amount

    def get_invoice_status(self, invoice_id: int) -> str:
        """Get the status of an invoice"""
        if invoice_id not in self.invoices:
            logger.error(f"Invoice {invoice_id} not found")
            raise ValueError(f"Invoice {invoice_id} not found")
        
        invoice = self.invoices[invoice_id]
        logger.info(f"Retrieved status {invoice.status} for invoice {invoice_id}")
        return invoice.status.value

def main():
    # Create a factoring service
    service = FactoringService()

    # Create invoices
    invoice1 = Invoice(1, "Customer A", 1000.0, datetime(2024, 9, 20))
    invoice2 = Invoice(2, "Customer B", 500.0, datetime(2024, 9, 15))

    # Add invoices to the service
    service.add_invoice(invoice1)
    service.add_invoice(invoice2)

    # Approve an invoice
    service.approve_invoice(1)

    # Calculate advance amount
    advance_amount = service.calculate_advance(1)
    print(f"Advance amount for invoice 1: {advance_amount}")

    # Get invoice status
    status = service.get_invoice_status(1)
    print(f"Status of invoice 1: {status}")

if __name__ == "__main__":
    main()
```
