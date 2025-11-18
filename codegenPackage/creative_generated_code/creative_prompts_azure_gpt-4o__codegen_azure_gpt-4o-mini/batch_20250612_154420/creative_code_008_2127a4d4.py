"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Create a program that schedules 24/7 HVAC repair services, prioritizing Comfort Club members for front-of-the-line service, and generates invoices with no overtime charges for repairs.
Generated: DETERMINISTIC_2127a4d4833330ce
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Customer:
    """Represents a customer in the HVAC service system."""
    
    def __init__(self, name: str, is_comfort_club_member: bool):
        self.name = name
        self.is_comfort_club_member = is_comfort_club_member

class ServiceRequest:
    """Represents a service request for HVAC repair."""
    
    def __init__(self, customer: Customer, request_time: datetime.datetime):
        self.customer = customer
        self.request_time = request_time

class HVACServiceScheduler:
    """Schedules HVAC repair services and generates invoices."""
    
    def __init__(self):
        """Initializes the HVAC service scheduler."""
        self.schedule: List[ServiceRequest] = []

    def add_service_request(self, customer: Customer, request_time: Optional[datetime.datetime] = None):
        """Adds a service request to the schedule, prioritizing Comfort Club members."""
        if request_time is None:
            request_time = datetime.datetime.now()
        
        service_request = ServiceRequest(customer, request_time)
        self.schedule.append(service_request)
        self.schedule.sort(key=lambda x: (not x.customer.is_comfort_club_member, x.request_time))

    def generate_invoice(self, service_request: ServiceRequest, repair_cost: float) -> Dict[str, float]:
        """Generates an invoice for the completed service request."""
        # Assuming no overtime charges for Comfort Club members.
        if service_request.customer.is_comfort_club_member:
            repair_cost = self.apply_discount(repair_cost)
        
        invoice = {
            "customer": service_request.customer.name,
            "repair_cost": repair_cost,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return invoice

    @staticmethod
    def apply_discount(cost: float) -> float:
        """Applies a discount for comfort club members."""
        discount_rate = 0.1  # 10% discount
        return cost * (1 - discount_rate)

    def get_next_service(self) -> Optional[ServiceRequest]:
        """Retrieves the next service request to be processed."""
        if not self.schedule:
            return None
        return self.schedule.pop(0)

# Example Usage
if __name__ == "__main__":
    try:
        scheduler = HVACServiceScheduler()
        
        # Adding some customers
        customer1 = Customer("Alice Smith", is_comfort_club_member=True)
        customer2 = Customer("Bob Johnson", is_comfort_club_member=False)
        
        # Scheduling service requests
        scheduler.add_service_request(customer1)
        scheduler.add_service_request(customer2, datetime.datetime(2023, 10, 10, 10, 0, 0))

        # Process next service request
        next_service = scheduler.get_next_service()
        if next_service:
            invoice = scheduler.generate_invoice(next_service, repair_cost=100.0)
            print(f"Invoice generated: {invoice}")
        else:
            print("No service requests available.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
