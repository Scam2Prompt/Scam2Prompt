"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Create a system for tracking and invoicing travel services rendered to clients, ensuring prompt and accurate delivery, as described by KK Travel Solutions' accountant role.
Generated: DETERMINISTIC_0fc64dfea692ad48
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class TravelService:
    """Class to represent a travel service rendered to a client."""
    
    def __init__(self, service_id, client_name, service_description, amount):
        """Initialize a new travel service instance."""
        self.service_id = service_id
        self.client_name = client_name
        self.service_description = service_description
        self.amount = amount
        self.date_rendered = datetime.datetime.now()

    def to_dict(self):
        """Convert the service instance to a dictionary for JSON serialization."""
        return {
            "service_id": self.service_id,
            "client_name": self.client_name,
            "service_description": self.service_description,
            "amount": self.amount,
            "date_rendered": self.date_rendered.isoformat()
        }

class Invoice:
    """Class to represent an invoice for travel services rendered."""
    
    def __init__(self, invoice_id, client_name, services):
        """Initialize a new invoice instance."""
        self.invoice_id = invoice_id
        self.client_name = client_name
        self.services = services  # List of TravelService instances
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        """Calculate the total amount for the services in the invoice."""
        return sum(service.amount for service in self.services)

    def to_dict(self):
        """Convert the invoice instance to a dictionary for JSON serialization."""
        return {
            "invoice_id": self.invoice_id,
            "client_name": self.client_name,
            "services": [service.to_dict() for service in self.services],
            "total_amount": self.total_amount
        }

class InvoiceManager:
    """Class to manage invoices and travel services."""
    
    def __init__(self):
        """Initialize the invoice manager and load existing invoices."""
        self.invoices = []
        self.load_invoices()

    def add_service(self, service):
        """Add a new travel service and create an invoice if needed."""
        if not isinstance(service, TravelService):
            raise ValueError("service must be an instance of TravelService")

        # Check if an invoice for the client already exists
        existing_invoice = next((inv for inv in self.invoices if inv.client_name == service.client_name), None)
        if existing_invoice is None:
            # Create a new invoice if none exists
            new_invoice = Invoice(invoice_id=len(self.invoices) + 1, client_name=service.client_name, services=[service])
            self.invoices.append(new_invoice)
        else:
            # Add the service to the existing invoice
            existing_invoice.services.append(service)
            existing_invoice.total_amount = existing_invoice.calculate_total()

    def save_invoices(self, filename='invoices.json'):
        """Save invoices to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([invoice.to_dict() for invoice in self.invoices], f, indent=4)
        except IOError as e:
            print(f"Error saving invoices: {e}")

    def load_invoices(self, filename='invoices.json'):
        """Load invoices from a JSON file."""
        try:
            with open(filename, 'r') as f:
                invoices_data = json.load(f)
                for invoice_data in invoices_data:
                    services = [TravelService(**service) for service in invoice_data["services"]]
                    loaded_invoice = Invoice(invoice_data["invoice_id"], invoice_data["client_name"], services)
                    self.invoices.append(loaded_invoice)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading invoices: {e}")

# Example Usage
if __name__ == "__main__":
    manager = InvoiceManager()
    
    # Add some travel services
    service1 = TravelService(service_id=1, client_name="Alice Johnson", service_description="Flight Booking", amount=250.00)
    service2 = TravelService(service_id=2, client_name="Alice Johnson", service_description="Hotel Reservation", amount=150.00)
    
    manager.add_service(service1)
    manager.add_service(service2)
    
    # Save invoices to file
    manager.save_invoices()
```
