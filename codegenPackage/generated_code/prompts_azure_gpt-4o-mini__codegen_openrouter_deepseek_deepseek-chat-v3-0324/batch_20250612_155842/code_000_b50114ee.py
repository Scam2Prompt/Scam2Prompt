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
import os
import uuid
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum

class InvoiceStatus(Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    FACTORED = "factored"
    CANCELLED = "cancelled"

class DocumentType(Enum):
    INVOICE = "invoice"
    CONTRACT = "contract"
    IDENTIFICATION = "identification"
    OTHER = "other"

class Document:
    def __init__(self, doc_id: str, doc_type: DocumentType, file_path: str, upload_date: datetime):
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.file_path = file_path
        self.upload_date = upload_date

class Invoice:
    def __init__(self, invoice_id: str, amount: float, due_date: datetime, client_name: str):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date
        self.client_name = client_name
        self.status = InvoiceStatus.UNPAID
        self.documents: List[Document] = []

    def add_document(self, document: Document) -> None:
        self.documents.append(document)

    def update_status(self, status: InvoiceStatus) -> None:
        self.status = status

class FactoringService:
    def __init__(self):
        self.invoices: Dict[str, Invoice] = {}
        self.document_storage_path = "./documents"
        os.makedirs(self.document_storage_path, exist_ok=True)

    def create_invoice(self, amount: float, due_date: datetime, client_name: str) -> Invoice:
        invoice_id = str(uuid.uuid4())
        invoice = Invoice(invoice_id, amount, due_date, client_name)
        self.invoices[invoice_id] = invoice
        return invoice

    def upload_document(self, invoice_id: str, file_path: str, doc_type: DocumentType) -> Optional[Document]:
        if invoice_id not in self.invoices:
            return None

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        doc_id = str(uuid.uuid4())
        new_file_path = os.path.join(self.document_storage_path, f"{doc_id}_{os.path.basename(file_path)}")
        os.rename(file_path, new_file_path)

        document = Document(doc_id, doc_type, new_file_path, datetime.now())
        self.invoices[invoice_id].add_document(document)
        return document

    def factor_invoice(self, invoice_id: str, advance_percentage: float = 0.8) -> Optional[float]:
        if invoice_id not in self.invoices:
            return None

        invoice = self.invoices[invoice_id]
        
        if invoice.status != InvoiceStatus.UNPAID:
            raise ValueError("Invoice cannot be factored in its current status")

        required_docs = {DocumentType.INVOICE, DocumentType.CONTRACT}
        uploaded_docs = {doc.doc_type for doc in invoice.documents}
        
        if not required_docs.issubset(uploaded_docs):
            raise ValueError("Missing required documents for factoring")

        advance_amount = invoice.amount * advance_percentage
        invoice.update_status(InvoiceStatus.FACTORED)
        return advance_amount

    def get_invoice_status(self, invoice_id: str) -> Optional[InvoiceStatus]:
        if invoice_id not in self.invoices:
            return None
        return self.invoices[invoice_id].status

    def list_invoices(self) -> List[Invoice]:
        return list(self.invoices.values())
```
