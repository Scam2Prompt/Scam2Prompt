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
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto


class InvoiceStatus(Enum):
    """Enum representing the status of an invoice in the factoring process."""
    DRAFT = auto()
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    FUNDED = auto()
    REJECTED = auto()
    PAID = auto()


class DocumentType(Enum):
    """Enum representing types of documents required for invoice factoring."""
    INVOICE = auto()
    PURCHASE_ORDER = auto()
    DELIVERY_RECEIPT = auto()
    CONTRACT = auto()


class Document:
    """Class representing a document submitted for invoice factoring."""
    
    def __init__(self, document_type: DocumentType, content: str, submission_date: datetime):
        self.id = str(uuid.uuid4())
        self.type = document_type
        self.content = content
        self.submission_date = submission_date
        self.is_verified = False


class Invoice:
    """Class representing an invoice being factored."""
    
    def __init__(self, invoice_number: str, amount: float, due_date: datetime, client_name: str):
        self.invoice_number = invoice_number
        self.amount = amount
        self.due_date = due_date
        self.client_name = client_name
        self.status = InvoiceStatus.DRAFT
        self.documents: List[Document] = []
        self.funded_amount: Optional[float] = None
        self.funding_date: Optional[datetime] = None
        self.rejection_reason: Optional[str] = None


class FactoringCompany:
    """Class representing a factoring company that processes invoices."""
    
    def __init__(self, name: str, advance_rate: float, fee_percentage: float):
        self.name = name
        self.advance_rate = advance_rate  # Percentage of invoice amount advanced
        self.fee_percentage = fee_percentage  # Factoring fee percentage
        self.processed_invoices: Dict[str, Invoice] = {}
    
    def submit_invoice(self, invoice: Invoice, documents: List[Document]) -> bool:
        """Submit an invoice with supporting documents for factoring."""
        if invoice.status != InvoiceStatus.DRAFT:
            return False
        
        required_docs = {DocumentType.INVOICE, DocumentType.PURCHASE_ORDER}
        submitted_doc_types = {doc.type for doc in documents}
        
        if not required_docs.issubset(submitted_doc_types):
            return False
        
        invoice.documents = documents
        invoice.status = InvoiceStatus.SUBMITTED
        self.processed_invoices[invoice.invoice_number] = invoice
        return True
    
    def review_invoice(self, invoice_number: str) -> Tuple[bool, Optional[str]]:
        """Review a submitted invoice and approve or reject it."""
        if invoice_number not in self.processed_invoices:
            return False, "Invoice not found"
        
        invoice = self.processed_invoices[invoice_number]
        
        if invoice.status != InvoiceStatus.SUBMITTED:
            return False, "Invoice is not in SUBMITTED status"
        
        # Verify all documents
        for doc in invoice.documents:
            if not self._verify_document(doc):
                invoice.status = InvoiceStatus.REJECTED
                invoice.rejection_reason = f"Document verification failed: {doc.type.name}"
                return False, invoice.rejection_reason
        
        invoice.status = InvoiceStatus.APPROVED
        return True, None
    
    def fund_invoice(self, invoice_number: str) -> Tuple[bool, Optional[str], Optional[float]]:
        """Fund an approved invoice by advancing cash to the client."""
        if invoice_number not in self.processed_invoices:
            return False, "Invoice not found", None
        
        invoice = self.processed_invoices[invoice_number]
        
        if invoice.status != InvoiceStatus.APPROVED:
            return False, "Invoice is not APPROVED", None
        
        advance_amount = invoice.amount * self.advance_rate
        invoice.funded_amount = advance_amount
        invoice.funding_date = datetime.now()
        invoice.status = InvoiceStatus.FUNDED
        
        return True, None, advance_amount
    
    def process_payment(self, invoice_number: str, amount_paid: float) -> Tuple[bool, Optional[str], Optional[float]]:
        """Process payment from the debtor and calculate remaining amounts."""
        if invoice_number not in self.processed_invoices:
            return False, "Invoice not found", None
        
        invoice = self.processed_invoices[invoice_number]
        
        if invoice.status != InvoiceStatus.FUNDED:
            return False, "Invoice is not FUNDED", None
        
        if amount_paid <= 0:
            return False, "Payment amount must be positive", None
        
        # Calculate factoring fee
        factoring_fee = invoice.amount * self.fee_percentage
        remaining_amount = invoice.amount - amount_paid
        
        if amount_paid >= invoice.amount:
            invoice.status = InvoiceStatus.PAID
            # Calculate reserve amount to return to client
            reserve_amount = invoice.amount - factoring_fee - invoice.funded_amount
            return True, None, reserve_amount if reserve_amount > 0 else 0
        else:
            return True, f"Partial payment received. Remaining: {remaining_amount}", None
    
    def _verify_document(self, document: Document) -> bool:
        """Internal method to verify a document (simplified for demo)."""
        # In a real implementation, this would involve actual verification logic
        document.is_verified = True
        return True


class CashFlowManager:
    """Class to manage cash flow for invoice factoring."""
    
    def __init__(self, factoring_company: FactoringCompany):
        self.factoring_company = factoring_company
        self.cash_balance = 0.0
        self.outstanding_advances: Dict[str, float] = {}
    
    def add_funds(self, amount: float) -> bool:
        """Add funds to the cash flow balance."""
        if amount <= 0:
            return False
        self.cash_balance += amount
        return True
    
    def process_advance(self, invoice_number: str) -> Tuple[bool, Optional[str]]:
        """Process an advance payment if sufficient funds are available."""
        if invoice_number not in self.factoring_company.processed_invoices:
            return False, "Invoice not found"
        
        invoice = self.factoring_company.processed_invoices[invoice_number]
        
        if invoice.status != InvoiceStatus.APPROVED:
            return False, "Invoice is not APPROVED"
        
        advance_amount = invoice.amount * self.factoring_company.advance_rate
        
        if self.cash_balance < advance_amount:
            return False, "Insufficient funds for advance"
        
        success, _, amount = self.factoring_company.fund_invoice(invoice_number)
        if not success:
            return False, "Failed to fund invoice"
        
        self.cash_balance -= advance_amount
        self.outstanding_advances[invoice_number] = advance_amount
        return True, None
    
    def process_payment(self, invoice_number: str, amount_paid: float) -> Tuple[bool, Optional[str], Optional[float]]:
        """Process payment from debtor and update cash flow."""
        if invoice_number not in self.factoring_company.processed_invoices:
            return False, "Invoice not found", None
        
        success, msg, reserve_amount = self.factoring_company.process_payment(invoice_number, amount_paid)
        if not success:
            return False, msg, None
        
        self.cash_balance += amount_paid
        
        if invoice_number in self.outstanding_advances:
            del self.outstanding_advances[invoice_number]
        
        return True, msg, reserve_amount


# Example usage
if __name__ == "__main__":
    # Create a factoring company
    factoring_co = FactoringCompany("QuickFunds Inc.", 0.8, 0.03)  # 80% advance, 3% fee
    
    # Create an invoice
    due_date = datetime.now() + timedelta(days=30)
    invoice = Invoice("INV-2023-001", 10000.0, due_date, "Acme Corp")
    
    # Create documents
    documents = [
        Document(DocumentType.INVOICE, "Invoice content", datetime.now()),
        Document(DocumentType.PURCHASE_ORDER, "PO content", datetime.now())
    ]
    
    # Submit invoice
    if factoring_co.submit_invoice(invoice, documents):
        print("Invoice submitted successfully")
        
        # Review invoice
        success, message = factoring_co.review_invoice(invoice.invoice_number)
        if success:
            print("Invoice approved")
            
            # Set up cash flow
            cash_flow = CashFlowManager(factoring_co)
            cash_flow.add_funds(100000.0)  # Add funds to the cash flow
            
            # Fund invoice
            success, message = cash_flow.process_advance(invoice.invoice_number)
            if success:
                print(f"Invoice funded with {invoice.fund
