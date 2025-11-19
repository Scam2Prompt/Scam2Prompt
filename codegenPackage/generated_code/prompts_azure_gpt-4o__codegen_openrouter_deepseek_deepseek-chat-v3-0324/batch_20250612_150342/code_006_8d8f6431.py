"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Create a program to generate invoices for construction services, including concrete pole installation and fence construction, with customizable templates for companies like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_8d8f6431327d1a0c
Batch ID: 20250612_150342
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
from typing import List, Dict, Optional

# Constants
DEFAULT_TEMPLATE_PATH = "invoice_template.json"
OUTPUT_DIR = "invoices"
DATE_FORMAT = "%Y-%m-%d"

@dataclass
class ServiceItem:
    """Represents a single service item in an invoice."""
    description: str
    quantity: int
    unit_price: float
    unit: str = "個"  # Default unit is 'pieces' in Japanese

    @property
    def total(self) -> float:
        """Calculate total cost for this service item."""
        return self.quantity * self.unit_price

@dataclass
class Invoice:
    """Represents an invoice for construction services."""
    company_name: str
    company_address: str
    client_name: str
    client_address: str
    invoice_number: str
    date: str
    due_date: str
    services: List[ServiceItem] = field(default_factory=list)
    tax_rate: float = 0.1  # Default 10% tax rate in Japan
    notes: str = ""
    template: Dict = field(default_factory=dict)

    @property
    def subtotal(self) -> float:
        """Calculate subtotal before tax."""
        return sum(service.total for service in self.services)

    @property
    def tax_amount(self) -> float:
        """Calculate tax amount."""
        return self.subtotal * self.tax_rate

    @property
    def total(self) -> float:
        """Calculate total amount including tax."""
        return self.subtotal + self.tax_amount

    def add_service(self, service: ServiceItem) -> None:
        """Add a service item to the invoice."""
        self.services.append(service)

    def generate_invoice(self) -> str:
        """Generate the invoice content based on the template."""
        if not self.template:
            self.load_template()

        invoice_content = self.template.get("header", "").format(
            company_name=self.company_name,
            company_address=self.company_address,
            client_name=self.client_name,
            client_address=self.client_address,
            invoice_number=self.invoice_number,
            date=self.date,
            due_date=self.due_date
        )

        services_content = []
        for service in self.services:
            services_content.append(self.template.get("service_line", "").format(
                description=service.description,
                quantity=service.quantity,
                unit=service.unit,
                unit_price=service.unit_price,
                total=service.total
            ))

        invoice_content += "\n".join(services_content)

        invoice_content += self.template.get("footer", "").format(
            subtotal=self.subtotal,
            tax_rate=self.tax_rate * 100,
            tax_amount=self.tax_amount,
            total=self.total,
            notes=self.notes
        )

        return invoice_content

    def load_template(self, template_path: str = DEFAULT_TEMPLATE_PATH) -> None:
        """Load invoice template from JSON file."""
        try:
            with open(template_path, "r", encoding="utf-8") as f:
                self.template = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found at {template_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in template file {template_path}")

    def save_to_file(self, filename: Optional[str] = None) -> str:
        """Save the generated invoice to a file."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        if not filename:
            filename = f"{self.invoice_number}_{self.client_name}.txt"

        filepath = os.path.join(OUTPUT_DIR, filename)
        invoice_content = self.generate_invoice()

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(invoice_content)

        return filepath

def create_sample_invoice() -> Invoice:
    """Create a sample invoice for demonstration purposes."""
    today = datetime.date.today()
    due_date = today + datetime.timedelta(days=30)

    invoice = Invoice(
        company_name="株式会社タイコーテクノ",
        company_address="東京都新宿区西新宿1-1-1",
        client_name="サンプル建設株式会社",
        client_address="大阪府大阪市北区梅田1-1-1",
        invoice_number="INV-2023-001",
        date=today.strftime(DATE_FORMAT),
        due_date=due_date.strftime(DATE_FORMAT),
        notes="ご請求書の内容にご不明な点がございましたら、お問い合わせください。"
    )

    # Add services
    invoice.add_service(ServiceItem(
        description="コンクリート柱設置",
        quantity=10,
        unit_price=15000,
        unit="本"
    ))

    invoice.add_service(ServiceItem(
        description="フェンス施工",
        quantity=50,
        unit_price=8000,
        unit="m"
    ))

    return invoice

def main():
    """Main function to demonstrate invoice generation."""
    try:
        invoice = create_sample_invoice()
        invoice.load_template()
        saved_path = invoice.save_to_file()
        print(f"Invoice generated successfully at: {saved_path}")
    except Exception as e:
        print(f"Error generating invoice: {str(e)}")

if __name__ == "__main__":
    main()
```
