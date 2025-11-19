"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Write a code snippet to generate an invoice for a client based on the accounting services provided by Lund & Kieck in South Africa.
Generated: DETERMINISTIC_af36335d0f8f959b
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for service types
class ServiceType(str, Enum):
    """Service types provided by Lund & Kieck"""
    ACCOUNTING = "Accounting"
    AUDITING = "Auditing"
    CONSULTING = "Consulting"

# Define a data class for services
@dataclass
class Service:
    """Service provided to a client"""
    service_type: ServiceType
    hours_worked: float
    rate: float

# Define a data class for clients
@dataclass
class Client:
    """Client information"""
    name: str
    address: str

# Define a class for invoices
class Invoice:
    """Invoice for a client"""
    def __init__(self, client: Client, services: List[Service]):
        self.client = client
        self.services = services
        self.invoice_date = datetime.date.today()

    def calculate_subtotal(self) -> float:
        """Calculate subtotal for the invoice"""
        return sum(service.hours_worked * service.rate for service in self.services)

    def calculate_vat(self, subtotal: float) -> float:
        """Calculate VAT (15% for South Africa)"""
        vat_rate = 0.15
        return subtotal * vat_rate

    def generate_invoice(self) -> None:
        """Generate the invoice"""
        try:
            # Calculate subtotal and VAT
            subtotal = self.calculate_subtotal()
            vat = self.calculate_vat(subtotal)
            total = subtotal + vat

            # Print invoice
            print("#" * 40)
            print(f"Invoice for {self.client.name}")
            print(f"Address: {self.client.address}")
            print(f"Date: {self.invoice_date}")
            print("-" * 40)
            print("Service\tHours Worked\tRate\tTotal")
            print("-" * 40)
            for i, service in enumerate(self.services, start=1):
                service_total = service.hours_worked * service.rate
                print(f"{i}. {service.service_type.value}\t{service.hours_worked:.2f}\tR {service.rate:.2f}\tR {service_total:.2f}")
            print("-" * 40)
            print(f"Subtotal:\t\t\tR {subtotal:.2f}")
            print(f"VAT (15%):\t\t\tR {vat:.2f}")
            print(f"Total:\t\t\tR {total:.2f}")
            print("#" * 40)
        except Exception as e:
            print(f"Error generating invoice: {str(e)}")

# Example usage
if __name__ == "__main__":
    client = Client("John Doe", "123 Main St, Cape Town, 8000")
    services = [
        Service(ServiceType.ACCOUNTING, 5, 500),
        Service(ServiceType.CONSULTING, 3, 750)
    ]
    invoice = Invoice(client, services)
    invoice.generate_invoice()
```
