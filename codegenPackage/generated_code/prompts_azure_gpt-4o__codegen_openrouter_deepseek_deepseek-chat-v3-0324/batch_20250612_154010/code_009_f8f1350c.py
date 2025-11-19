"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Create a feature to track billable hours and generate invoices for lawyers in a cloud-based application, inspired by BillYourTime.com.
Generated: DETERMINISTIC_f8f1350cce3b7a73
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
import json
import uuid
from decimal import Decimal
from enum import Enum, auto


class InvoiceStatus(Enum):
    DRAFT = auto()
    SENT = auto()
    PAID = auto()
    OVERDUE = auto()


class TimeEntryStatus(Enum):
    ACTIVE = auto()
    BILLED = auto()
    WRITTEN_OFF = auto()


@dataclass
class Client:
    id: str
    name: str
    email: str
    billing_address: str
    phone: Optional[str] = None


@dataclass
class Lawyer:
    id: str
    name: str
    email: str
    hourly_rate: Decimal


@dataclass
class TimeEntry:
    id: str
    lawyer_id: str
    client_id: str
    description: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    status: TimeEntryStatus = TimeEntryStatus.ACTIVE

    @property
    def duration(self) -> Decimal:
        duration = self.end_time - self.start_time
        hours = duration.total_seconds() / 3600
        return Decimal(str(round(hours, 2)))


@dataclass
class InvoiceItem:
    time_entry_id: str
    description: str
    hours: Decimal
    rate: Decimal
    amount: Decimal


@dataclass
class Invoice:
    id: str
    client_id: str
    lawyer_id: str
    issue_date: datetime.date
    due_date: datetime.date
    status: InvoiceStatus
    items: List[InvoiceItem]
    notes: Optional[str] = None

    @property
    def subtotal(self) -> Decimal:
        return sum(item.amount for item in self.items)

    @property
    def tax(self) -> Decimal:
        # Assuming 10% tax for simplicity
        return self.subtotal * Decimal("0.1")

    @property
    def total(self) -> Decimal:
        return self.subtotal + self.tax


class BillingSystem:
    def __init__(self):
        self.clients = {}
        self.lawyers = {}
        self.time_entries = {}
        self.invoices = {}

    def add_client(self, name: str, email: str, billing_address: str, phone: Optional[str] = None) -> Client:
        client_id = str(uuid.uuid4())
        client = Client(client_id, name, email, billing_address, phone)
        self.clients[client_id] = client
        return client

    def add_lawyer(self, name: str, email: str, hourly_rate: Decimal) -> Lawyer:
        lawyer_id = str(uuid.uuid4())
        lawyer = Lawyer(lawyer_id, name, email, hourly_rate)
        self.lawyers[lawyer_id] = lawyer
        return lawyer

    def create_time_entry(
        self,
        lawyer_id: str,
        client_id: str,
        description: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
    ) -> TimeEntry:
        if lawyer_id not in self.lawyers:
            raise ValueError("Lawyer not found")
        if client_id not in self.clients:
            raise ValueError("Client not found")
        if end_time <= start_time:
            raise ValueError("End time must be after start time")

        entry_id = str(uuid.uuid4())
        entry = TimeEntry(entry_id, lawyer_id, client_id, description, start_time, end_time)
        self.time_entries[entry_id] = entry
        return entry

    def generate_invoice(
        self,
        client_id: str,
        lawyer_id: str,
        time_entry_ids: List[str],
        due_days: int = 30,
        notes: Optional[str] = None,
    ) -> Invoice:
        if client_id not in self.clients:
            raise ValueError("Client not found")
        if lawyer_id not in self.lawyers:
            raise ValueError("Lawyer not found")

        lawyer = self.lawyers[lawyer_id]
        invoice_items = []
        valid_entry_ids = []

        for entry_id in time_entry_ids:
            if entry_id not in self.time_entries:
                continue
            entry = self.time_entries[entry_id]
            if entry.status != TimeEntryStatus.ACTIVE:
                continue
            if entry.client_id != client_id:
                continue
            if entry.lawyer_id != lawyer_id:
                continue

            amount = entry.duration * lawyer.hourly_rate
            invoice_items.append(
                InvoiceItem(
                    time_entry_id=entry_id,
                    description=entry.description,
                    hours=entry.duration,
                    rate=lawyer.hourly_rate,
                    amount=amount,
                )
            )
            valid_entry_ids.append(entry_id)

        if not invoice_items:
            raise ValueError("No valid time entries to invoice")

        invoice_id = str(uuid.uuid4())
        today = datetime.date.today()
        due_date = today + datetime.timedelta(days=due_days)

        invoice = Invoice(
            id=invoice_id,
            client_id=client_id,
            lawyer_id=lawyer_id,
            issue_date=today,
            due_date=due_date,
            status=InvoiceStatus.DRAFT,
            items=invoice_items,
            notes=notes,
        )

        self.invoices[invoice_id] = invoice

        # Mark time entries as billed
        for entry_id in valid_entry_ids:
            self.time_entries[entry_id].status = TimeEntryStatus.BILLED

        return invoice

    def send_invoice(self, invoice_id: str) -> Invoice:
        if invoice_id not in self.invoices:
            raise ValueError("Invoice not found")
        invoice = self.invoices[invoice_id]
        if invoice.status != InvoiceStatus.DRAFT:
            raise ValueError("Only draft invoices can be sent")
        invoice.status = InvoiceStatus.SENT
        return invoice

    def mark_invoice_as_paid(self, invoice_id: str) -> Invoice:
        if invoice_id not in self.invoices:
            raise ValueError("Invoice not found")
        invoice = self.invoices[invoice_id]
        if invoice.status not in (InvoiceStatus.SENT, InvoiceStatus.OVERDUE):
            raise ValueError("Only sent or overdue invoices can be marked as paid")
        invoice.status = InvoiceStatus.PAID
        return invoice

    def check_overdue_invoices(self) -> List[Invoice]:
        today = datetime.date.today()
        overdue_invoices = []
        for invoice in self.invoices.values():
            if invoice.status == InvoiceStatus.SENT and invoice.due_date < today:
                invoice.status = InvoiceStatus.OVERDUE
                overdue_invoices.append(invoice)
        return overdue_invoices

    def get_client_invoices(self, client_id: str) -> List[Invoice]:
        if client_id not in self.clients:
            raise ValueError("Client not found")
        return [inv for inv in self.invoices.values() if inv.client_id == client_id]

    def get_lawyer_time_entries(self, lawyer_id: str, status: Optional[TimeEntryStatus] = None) -> List[TimeEntry]:
        if lawyer_id not in self.lawyers:
            raise ValueError("Lawyer not found")
        entries = [entry for entry in self.time_entries.values() if entry.lawyer_id == lawyer_id]
        if status is not None:
            entries = [entry for entry in entries if entry.status == status]
        return entries

    def export_invoice_to_json(self, invoice_id: str) -> str:
        if invoice_id not in self.invoices:
            raise ValueError("Invoice not found")
        invoice = self.invoices[invoice_id]
        invoice_dict = {
            "id": invoice.id,
            "client_id": invoice.client_id,
            "lawyer_id": invoice.lawyer_id,
            "issue_date": invoice.issue_date.isoformat(),
            "due_date": invoice.due_date.isoformat(),
            "status": invoice.status.name,
            "subtotal": str(invoice.subtotal),
            "tax": str(invoice.tax),
            "total": str(invoice.total),
            "notes": invoice.notes,
            "items": [
                {
                    "time_entry_id": item.time_entry_id,
                    "description": item.description,
                    "hours": str(item.hours),
                    "rate": str(item.rate),
                    "amount": str(item.amount),
                }
                for item in invoice.items
            ],
        }
        return json.dumps(invoice_dict, indent=2)
```
