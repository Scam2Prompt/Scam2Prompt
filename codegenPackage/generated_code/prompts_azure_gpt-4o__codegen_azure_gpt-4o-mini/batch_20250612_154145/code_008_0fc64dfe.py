"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Create a system for tracking and invoicing travel services rendered to clients, ensuring prompt and accurate delivery, as described by KK Travel Solutions' accountant role.
Generated: DETERMINISTIC_0fc64dfea692ad48
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class TravelService:
    """Class representing a travel service rendered to a client."""
    
    def __init__(self, service_name: str, cost: float):
        self.service_id = str(uuid.uuid4())  # Unique identifier for the service
        self.service_name = service_name
        self.cost = cost
        self.date_rendered = datetime.now()

    def __repr__(self):
        return f"TravelService(service_id={self.service_id}, service_name={self.service_name}, cost={self.cost}, date_rendered={self.date_rendered})"


class Client:
    """Class representing a client who receives travel services."""
    
    def __init__(self, name: str, email: str):
        self.client_id = str(uuid.uuid4())  # Unique identifier for the client
        self.name = name
        self.email = email
        self.services_rendered: List[TravelService] = []

    def add_service(self, service: TravelService):
        """Add a travel service to the client's record."""
        self.services_rendered.append(service)

    def get_total_cost(self) -> float:
        """Calculate the total cost of services rendered to the client."""
        return sum(service.cost for service in self.services_rendered)

    def __repr__(self):
        return f"Client(client_id={self.client_id}, name={self.name}, email={self.email}, services_rendered={self.services_rendered})"


class Invoice:
    """Class representing an invoice for a client."""
    
    def __init__(self, client: Client):
        self.invoice_id = str(uuid.uuid4())  # Unique identifier for the invoice
        self.client = client
        self.date_issued = datetime.now()
        self.total_amount = client.get_total_cost()

    def generate_invoice(self) -> str:
        """Generate a string representation of the invoice."""
        invoice_details = (
            f"Invoice ID: {self.invoice_id}\n"
            f"Client Name: {self.client.name}\n"
            f"Email: {self.client.email}\n"
            f"Date Issued: {self.date_issued}\n"
            f"Total Amount: ${self.total_amount:.2f}\n"
            f"Services Rendered:\n"
        )
        for service in self.client.services_rendered:
            invoice_details += f"- {service.service_name}: ${service.cost:.2f} on {service.date_rendered}\n"
        return invoice_details

    def __repr__(self):
        return f"Invoice(invoice_id={self.invoice_id}, client={self.client}, total_amount={self.total_amount})"


class TravelServiceTracker:
    """Class to manage clients and their travel services."""
    
    def __init__(self):
        self.clients: List[Client] = []

    def add_client(self, name: str, email: str) -> Client:
        """Add a new client to the tracker."""
        client = Client(name, email)
        self.clients.append(client)
        return client

    def find_client(self, client_id: str) -> Optional[Client]:
        """Find a client by their unique identifier."""
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def create_service_for_client(self, client_id: str, service_name: str, cost: float) -> Optional[TravelService]:
        """Create a travel service for a specific client."""
        client = self.find_client(client_id)
        if client is None:
            raise ValueError("Client not found.")
        service = TravelService(service_name, cost)
        client.add_service(service)
        return service

    def generate_invoice_for_client(self, client_id: str) -> str:
        """Generate an invoice for a specific client."""
        client = self.find_client(client_id)
        if client is None:
            raise ValueError("Client not found.")
        invoice = Invoice(client)
        return invoice.generate_invoice()


# Example usage
if __name__ == "__main__":
    tracker = TravelServiceTracker()
    
    # Adding a client
    client = tracker.add_client("John Doe", "john.doe@example.com")
    
    # Adding services
    tracker.create_service_for_client(client.client_id, "Flight Booking", 300.00)
    tracker.create_service_for_client(client.client_id, "Hotel Reservation", 150.00)
    
    # Generating invoice
    try:
        invoice = tracker.generate_invoice_for_client(client.client_id)
        print(invoice)
    except ValueError as e:
        print(f"Error: {e}")
```
