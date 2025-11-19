"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Create a program that schedules 24/7 HVAC repair services, prioritizing Comfort Club members for front-of-the-line service, and generates invoices with no overtime charges for repairs.
Generated: DETERMINISTIC_2127a4d4833330ce
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Customer:
    """Class representing a customer."""
    def __init__(self, name: str, is_comfort_club_member: bool):
        self.name = name
        self.is_comfort_club_member = is_comfort_club_member

class ServiceRequest:
    """Class representing a service request."""
    def __init__(self, customer: Customer, request_time: datetime.datetime):
        self.customer = customer
        self.request_time = request_time
        self.invoice: Optional[Invoice] = None

class Invoice:
    """Class representing an invoice for a service request."""
    def __init__(self, service_request: ServiceRequest, amount: float):
        self.service_request = service_request
        self.amount = amount
        self.date_issued = datetime.datetime.now()

class HVACServiceScheduler:
    """Class to manage HVAC service requests and invoicing."""
    def __init__(self):
        self.service_requests: List[ServiceRequest] = []

    def schedule_service(self, customer: Customer) -> ServiceRequest:
        """Schedule a service for a customer, prioritizing Comfort Club members."""
        request_time = datetime.datetime.now()
        service_request = ServiceRequest(customer, request_time)
        self.service_requests.append(service_request)
        self.service_requests.sort(key=lambda x: (not x.customer.is_comfort_club_member, x.request_time))
        return service_request

    def generate_invoice(self, service_request: ServiceRequest, repair_cost: float) -> Invoice:
        """Generate an invoice for a service request."""
        if service_request.invoice is not None:
            raise ValueError("Invoice already generated for this service request.")
        
        # No overtime charges are applied
        invoice = Invoice(service_request, repair_cost)
        service_request.invoice = invoice
        return invoice

    def get_service_requests(self) -> List[ServiceRequest]:
        """Return the list of service requests."""
        return self.service_requests

# Example usage
if __name__ == "__main__":
    scheduler = HVACServiceScheduler()

    # Create customers
    customer1 = Customer("Alice", True)  # Comfort Club member
    customer2 = Customer("Bob", False)    # Non-member

    # Schedule services
    request1 = scheduler.schedule_service(customer1)
    request2 = scheduler.schedule_service(customer2)

    # Generate invoices
    try:
        invoice1 = scheduler.generate_invoice(request1, 150.00)
        invoice2 = scheduler.generate_invoice(request2, 200.00)
        
        print(f"Invoice for {invoice1.service_request.customer.name}: ${invoice1.amount} issued on {invoice1.date_issued}")
        print(f"Invoice for {invoice2.service_request.customer.name}: ${invoice2.amount} issued on {invoice2.date_issued}")
    except ValueError as e:
        print(f"Error: {e}")
```
