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
from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass

class Priority(Enum):
    """Priority levels for service requests."""
    COMFORT_CLUB = auto()
    STANDARD = auto()

@dataclass
class Customer:
    """Represents a customer with their details."""
    name: str
    contact: str
    is_comfort_club_member: bool

@dataclass
class ServiceRequest:
    """Represents a service request with customer and issue details."""
    customer: Customer
    issue_description: str
    timestamp: datetime.datetime
    priority: Priority

@dataclass
class ServiceRecord:
    """Represents a completed service record with details."""
    service_request: ServiceRequest
    technician: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    parts_cost: float
    labor_hours: float

class HVACServiceScheduler:
    """Manages scheduling and processing of HVAC service requests."""
    
    def __init__(self):
        self.service_queue: List[ServiceRequest] = []
        self.completed_services: List[ServiceRecord] = []
    
    def add_service_request(self, customer: Customer, issue_description: str) -> None:
        """Add a new service request to the queue with appropriate priority."""
        priority = Priority.COMFORT_CLUB if customer.is_comfort_club_member else Priority.STANDARD
        request = ServiceRequest(
            customer=customer,
            issue_description=issue_description,
            timestamp=datetime.datetime.now(),
            priority=priority
        )
        self.service_queue.append(request)
        self._prioritize_queue()
    
    def _prioritize_queue(self) -> None:
        """Prioritize Comfort Club members to the front of the queue."""
        self.service_queue.sort(key=lambda x: x.priority.value)
    
    def process_next_request(self, technician: str) -> Optional[ServiceRecord]:
        """Process the next service request and return the service record."""
        if not self.service_queue:
            return None
        
        request = self.service_queue.pop(0)
        start_time = datetime.datetime.now()
        
        # Simulate service processing
        # In a real system, this would involve actual repair logic
        end_time = start_time + datetime.timedelta(hours=1)  # Default 1 hour labor
        parts_cost = 100.00  # Default parts cost
        
        record = ServiceRecord(
            service_request=request,
            technician=technician,
            start_time=start_time,
            end_time=end_time,
            parts_cost=parts_cost,
            labor_hours=1.0
        )
        
        self.completed_services.append(record)
        return record
    
    def generate_invoice(self, service_record: ServiceRecord) -> Dict:
        """Generate an invoice for the completed service."""
        labor_rate = 75.00  # Standard labor rate per hour
        
        total_labor_cost = labor_rate * service_record.labor_hours
        total_cost = total_labor_cost + service_record.parts_cost
        
        invoice = {
            'customer_name': service_record.service_request.customer.name,
            'customer_contact': service_record.service_request.customer.contact,
            'issue_description': service_record.service_request.issue_description,
            'technician': service_record.technician,
            'service_date': service_record.start_time.date().isoformat(),
            'start_time': service_record.start_time.time().isoformat(),
            'end_time': service_record.end_time.time().isoformat(),
            'labor_hours': service_record.labor_hours,
            'labor_rate': labor_rate,
            'labor_cost': total_labor_cost,
            'parts_cost': service_record.parts_cost,
            'total_cost': total_cost,
            'notes': 'Thank you for your business! Overtime charges do not apply.'
        }
        
        return invoice

# Example usage
if __name__ == "__main__":
    scheduler = HVACServiceScheduler()
    
    # Create customers
    member_customer = Customer(
        name="John Doe",
        contact="555-1234",
        is_comfort_club_member=True
    )
    
    regular_customer = Customer(
        name="Jane Smith",
        contact="555-5678",
        is_comfort_club_member=False
    )
    
    # Add service requests
    scheduler.add_service_request(
        customer=regular_customer,
        issue_description="AC not cooling"
    )
    
    scheduler.add_service_request(
        customer=member_customer,
        issue_description="Furnace not heating"
    )
    
    # Process requests
    technician = "Mike Johnson"
    record1 = scheduler.process_next_request(technician)
    record2 = scheduler.process_next_request(technician)
    
    # Generate invoices
    if record1:
        invoice1 = scheduler.generate_invoice(record1)
        print("Invoice 1:", invoice1)
    
    if record2:
        invoice2 = scheduler.generate_invoice(record2)
        print("Invoice 2:", invoice2)
```
