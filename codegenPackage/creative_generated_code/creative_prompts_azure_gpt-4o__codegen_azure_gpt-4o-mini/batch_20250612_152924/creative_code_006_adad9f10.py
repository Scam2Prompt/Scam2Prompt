"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Develop code to manage after-sales service for maintaining and servicing equipment installations, such as gates and filtration systems, based on Alphamor’s offerings.
Generated: DETERMINISTIC_adad9f10c000c910
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class ServiceRequest:
    """Class to represent a service request for equipment maintenance."""
    
    def __init__(self, request_id: int, equipment_id: str, service_type: str, customer_id: str, scheduled_date: datetime.date):
        self.request_id = request_id
        self.equipment_id = equipment_id
        self.service_type = service_type
        self.customer_id = customer_id
        self.scheduled_date = scheduled_date
        self.completed = False
        self.completion_date: Optional[datetime.date] = None

    def complete_service(self):
        """Mark the service request as completed."""
        self.completed = True
        self.completion_date = datetime.date.today()

class ServiceManager:
    """Class to manage service requests for after-sales service."""

    def __init__(self):
        self.service_requests: List[ServiceRequest] = []

    def create_service_request(self, equipment_id: str, service_type: str, customer_id: str, scheduled_date: datetime.date) -> ServiceRequest:
        """Create a new service request."""
        request_id = len(self.service_requests) + 1
        service_request = ServiceRequest(request_id, equipment_id, service_type, customer_id, scheduled_date)
        self.service_requests.append(service_request)
        return service_request

    def get_service_request(self, request_id: int) -> Optional[ServiceRequest]:
        """Retrieve a service request by its ID."""
        for request in self.service_requests:
            if request.request_id == request_id:
                return request
        return None

    def complete_service_request(self, request_id: int) -> bool:
        """Complete a service request if it exists."""
        service_request = self.get_service_request(request_id)
        if service_request is None:
            raise ValueError(f"Service request with ID {request_id} does not exist.")
        
        if service_request.completed:
            raise ValueError(f"Service request with ID {request_id} has already been completed.")
        
        service_request.complete_service()
        return True

    def list_service_requests(self) -> List[ServiceRequest]:
        """Return a list of all service requests."""
        return self.service_requests

# Example usage
if __name__ == "__main__":
    service_manager = ServiceManager()
    
    # Create service requests
    request1 = service_manager.create_service_request("EQUIP001", "Maintenance", "CUST001", datetime.date(2023, 10, 20))
    request2 = service_manager.create_service_request("EQUIP002", "Repair", "CUST002", datetime.date(2023, 10, 22))
    
    # List service requests
    for request in service_manager.list_service_requests():
        print(f"Request ID: {request.request_id}, Equipment ID: {request.equipment_id}, Service Type: {request.service_type}, Scheduled Date: {request.scheduled_date}")
    
    # Complete a service request
    try:
        service_manager.complete_service_request(1)
        print(f"Service request {request1.request_id} completed successfully.")
    except ValueError as e:
        print(e)
```
