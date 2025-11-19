"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Write Python code to automate the process of generating invoices for fiduciary services, including company creation and auditing, as described by Hub Experts in Geneva. Include fields for client trust metrics, deadlines, and service descriptions.
Generated: DETERMINISTIC_11fd480b28fda86e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from dataclasses import dataclass, field
from typing import List, Optional

# Constants
INVOICE_TEMPLATE = "invoice_template.html"
OUTPUT_DIR = "invoices"
CLIENTS_FILE = "clients.json"
SERVICES_FILE = "services.json"
COMPANY_INFO_FILE = "company_info.json"

@dataclass
class Client:
    id: str
    name: str
    email: str
    address: str
    trust_score: float  # 0.0 to 1.0
    payment_terms: str  # e.g., "NET 30"

@dataclass
class Service:
    code: str
    description: str
    hourly_rate: float
    category: str  # e.g., "Company Creation", "Auditing"

@dataclass
class InvoiceItem:
    service: Service
    quantity: float  # hours or units
    deadline: Optional[datetime.date] = None

@dataclass
class Invoice:
    invoice_number: str
    issue_date: datetime.date
    due_date: datetime.date
    client: Client
    items: List[InvoiceItem] = field(default_factory=list)
    notes: str = ""
    tax_rate: float = 0.08  # Default VAT for Switzerland

    def total_amount(self) -> float:
        subtotal = sum(item.service.hourly_rate * item.quantity for item in self.items)
        return subtotal * (1 + self.tax_rate)

class InvoiceGenerator:
    def __init__(self):
        self.clients = self._load_clients()
        self.services = self._load_services()
        self.company_info = self._load_company_info()
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def _load_clients(self) -> List[Client]:
        try:
            with open(CLIENTS_FILE, 'r') as f:
                clients_data = json.load(f)
                return [Client(**client) for client in clients_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading clients: {str(e)}")

    def _load_services(self) -> List[Service]:
        try:
            with open(SERVICES_FILE, 'r') as f:
                services_data = json.load(f)
                return [Service(**service) for service in services_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading services: {str(e)}")

    def _load_company_info(self) -> dict:
        try:
            with open(COMPANY_INFO_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading company info: {str(e)}")

    def find_client(self, client_id: str) -> Client:
        for client in self.clients:
            if client.id == client_id:
                return client
        raise ValueError(f"Client with ID {client_id} not found")

    def find_service(self, service_code: str) -> Service:
        for service in self.services:
            if service.code == service_code:
                return service
        raise ValueError(f"Service with code {service_code} not found")

    def generate_invoice_number(self) -> str:
        today = datetime.date.today()
        return f"INV-{today.year}-{today.month:02d}-{len(os.listdir(OUTPUT_DIR)) + 1:04d}"

    def create_invoice(
        self,
        client_id: str,
        service_items: List[dict],
        due_days: int = 30,
        notes: str = ""
    ) -> Invoice:
        client = self.find_client(client_id)
        items = []
        
        for item in service_items:
            service = self.find_service(item['service_code'])
            deadline = datetime.datetime.strptime(item['deadline'], "%Y-%m-%d").date() if 'deadline' in item else None
            items.append(InvoiceItem(service=service, quantity=item['quantity'], deadline=deadline))
        
        today = datetime.date.today()
        due_date = today + datetime.timedelta(days=due_days)
        
        invoice = Invoice(
            invoice_number=self.generate_invoice_number(),
            issue_date=today,
            due_date=due_date,
            client=client,
            items=items,
            notes=notes
        )
        
        return invoice

    def render_invoice(self, invoice: Invoice) -> str:
        try:
            with open(INVOICE_TEMPLATE, 'r') as f:
                template = f.read()
        except FileNotFoundError:
            template = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Invoice {invoice_number}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .header {{ display: flex; justify-content: space-between; }}
                    .company-info {{ text-align: right; }}
                    .invoice-info {{ margin-top: 30px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                    .total {{ font-weight: bold; text-align: right; margin-top: 20px; }}
                    .notes {{ margin-top: 30px; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <div>
                        <h1>Invoice {invoice_number}</h1>
                        <p>Issued: {issue_date}</p>
                        <p>Due: {due_date}</p>
                    </div>
                    <div class="company-info">
                        <h2>{company_name}</h2>
                        <p>{company_address}</p>
                        <p>VAT: {company_vat}</p>
                    </div>
                </div>
                
                <div class="invoice-info">
                    <h3>Bill To:</h3>
                    <p>{client_name}</p>
                    <p>{client_address}</p>
                    <p>Trust Score: {trust_score}%</p>
                    <p>Payment Terms: {payment_terms}</p>
                </div>
                
                <table>
                    <thead>
                        <tr>
                            <th>Service Code</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Rate</th>
                            <th>Amount</th>
                            <th>Deadline</th>
                        </tr>
                    </thead>
                    <tbody>
                        {items_html}
                    </tbody>
                </table>
                
                <div class="total">
                    <p>Subtotal: CHF {subtotal:.2f}</p>
                    <p>Tax ({tax_rate:.0%}): CHF {tax_amount:.2f}</p>
                    <p>Total: CHF {total:.2f}</p>
                </div>
                
                <div class="notes">
                    <h3>Notes:</h3>
                    <p>{notes}</p>
                </div>
            </body>
            </html>
            """
        
        items_html = ""
        subtotal = sum(item.service.hourly_rate * item.quantity for item in invoice.items)
        tax_amount = subtotal * invoice.tax_rate
        
        for item in invoice.items:
            deadline_str = item.deadline.strftime("%Y-%m-%d") if item.deadline else "N/A"
            items_html += f"""
                <tr>
                    <td>{item.service.code}</td>
                    <td>{item.service.description}</td>
                    <td>{item.quantity}</td>
                    <td>CHF {item.service.hourly_rate:.2f}</td>
                    <td>CHF {item.service.hourly_rate * item.quantity:.2f}</td>
                    <td>{deadline_str}</td>
                </tr>
            """
        
        return template.format(
            invoice_number=invoice.invoice_number,
            issue_date=invoice.issue_date.strftime("%Y-%m-%d"),
            due_date=invoice.due_date.strftime("%Y-%m-%d"),
            company_name=self.company_info.get("name", "Hub Experts"),
            company_address=self.company_info.get("address", "Geneva, Switzerland"),
            company_vat=self.company_info.get("vat", "CHE-123.456.789"),
            client_name=invoice.client.name,
            client_address=invoice.client.address,
            trust_score=invoice.client.trust_score * 100,
            payment_terms=invoice.client.payment_terms,
            items_html=items_html,
            subtotal=subtotal,
            tax_rate=invoice.tax_rate,
            tax_amount=tax_amount,
            total=invoice.total_amount(),
            notes=invoice.notes
        )

    def save_invoice(self, invoice: Invoice) -> str:
        html_content = self.render_invoice(invoice)
        filename = f"{OUTPUT_DIR}/{invoice.invoice_number}.html"
        
        try:
            with
