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
# travel_services.py

from datetime import datetime
from typing import Dict, List

class TravelService:
    """Represents a travel service rendered to a client."""

    def __init__(self, service_id: int, client_name: str, service_date: datetime, service_type: str, cost: float):
        """
        Initializes a TravelService object.

        Args:
        - service_id (int): Unique identifier for the service.
        - client_name (str): Name of the client.
        - service_date (datetime): Date the service was rendered.
        - service_type (str): Type of service rendered (e.g., flight, hotel, rental car).
        - cost (float): Cost of the service.
        """
        self.service_id = service_id
        self.client_name = client_name
        self.service_date = service_date
        self.service_type = service_type
        self.cost = cost

class Client:
    """Represents a client with a list of travel services rendered."""

    def __init__(self, client_id: int, client_name: str):
        """
        Initializes a Client object.

        Args:
        - client_id (int): Unique identifier for the client.
        - client_name (str): Name of the client.
        """
        self.client_id = client_id
        self.client_name = client_name
        self.services: List[TravelService] = []

    def add_service(self, service: TravelService):
        """Adds a travel service to the client's list of services."""
        self.services.append(service)

class Invoice:
    """Represents an invoice for a client with a list of travel services."""

    def __init__(self, invoice_id: int, client: Client):
        """
        Initializes an Invoice object.

        Args:
        - invoice_id (int): Unique identifier for the invoice.
        - client (Client): Client object with a list of travel services.
        """
        self.invoice_id = invoice_id
        self.client = client
        self.services: List[TravelService] = client.services
        self.total_cost: float = self.calculate_total_cost()

    def calculate_total_cost(self) -> float:
        """Calculates the total cost of all services on the invoice."""
        return sum(service.cost for service in self.services)

    def generate_invoice(self) -> str:
        """Generates a formatted invoice string."""
        invoice_str = f"Invoice {self.invoice_id} for {self.client.client_name}:\n"
        for service in self.services:
            invoice_str += f"- {service.service_date.strftime('%Y-%m-%d')}: {service.service_type} (${service.cost:.2f})\n"
        invoice_str += f"Total: ${self.total_cost:.2f}"
        return invoice_str

class TravelServiceSystem:
    """Manages a list of clients and their travel services."""

    def __init__(self):
        self.clients: Dict[int, Client] = {}
        self.invoices: Dict[int, Invoice] = {}

    def add_client(self, client: Client):
        """Adds a client to the system."""
        self.clients[client.client_id] = client

    def add_service(self, client_id: int, service: TravelService):
        """Adds a travel service to a client's list of services."""
        if client_id in self.clients:
            self.clients[client_id].add_service(service)
        else:
            raise ValueError("Client not found")

    def generate_invoice(self, invoice_id: int, client_id: int) -> Invoice:
        """Generates an invoice for a client."""
        if client_id in self.clients:
            client = self.clients[client_id]
            invoice = Invoice(invoice_id, client)
            self.invoices[invoice_id] = invoice
            return invoice
        else:
            raise ValueError("Client not found")

def main():
    # Create a travel service system
    system = TravelServiceSystem()

    # Create clients
    client1 = Client(1, "John Doe")
    client2 = Client(2, "Jane Smith")

    # Add clients to the system
    system.add_client(client1)
    system.add_client(client2)

    # Create travel services
    service1 = TravelService(1, "John Doe", datetime(2022, 1, 1), "Flight", 200.0)
    service2 = TravelService(2, "John Doe", datetime(2022, 1, 2), "Hotel", 150.0)
    service3 = TravelService(3, "Jane Smith", datetime(2022, 1, 3), "Rental Car", 100.0)

    # Add services to clients
    system.add_service(1, service1)
    system.add_service(1, service2)
    system.add_service(2, service3)

    # Generate invoices
    invoice1 = system.generate_invoice(1, 1)
    invoice2 = system.generate_invoice(2, 2)

    # Print invoices
    print(invoice1.generate_invoice())
    print("\n")
    print(invoice2.generate_invoice())

if __name__ == "__main__":
    main()
```
