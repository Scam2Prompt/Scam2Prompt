"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Develop code to manage after-sales service for maintaining and servicing equipment installations, such as gates and filtration systems, based on Alphamor’s offerings.
Generated: DETERMINISTIC_adad9f10c000c910
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class ServiceRequest:
    """Class to represent a service request for equipment maintenance."""
    
    def __init__(self, equipment_id: str, customer_name: str, service_type: str, request_date: Optional[datetime.date] = None):
        self.equipment_id = equipment_id
        self.customer_name = customer_name
        self.service_type = service_type
        self.request_date = request_date or datetime.date.today()
        self.status = 'Pending'  # Initial status of the service request

    def __str__(self):
        return f"ServiceRequest(equipment_id={self.equipment_id}, customer_name={self.customer_name}, service_type={self.service_type}, request_date={self.request_date}, status={self.status})"


class ServiceManager:
    """Class to manage service requests for equipment installations."""
    
    def __init__(self):
        self.service_requests: List[ServiceRequest] = []

    def create_service_request(self, equipment_id: str, customer_name: str, service_type: str) -> ServiceRequest:
        """Create a new service request and add it to the list."""
        try:
            request = ServiceRequest(equipment_id, customer_name, service_type)
            self.service_requests.append(request)
            return request
        except Exception as e:
            print(f"Error creating service request: {e}")
            raise

    def list_service_requests(self) -> List[ServiceRequest]:
        """Return a list of all service requests."""
        return self.service_requests

    def update_service_request_status(self, equipment_id: str, new_status: str) -> bool:
        """Update the status of a service request based on equipment ID."""
        try:
            for request in self.service_requests:
                if request.equipment_id == equipment_id:
                    request.status = new_status
                    return True
            print(f"No service request found for equipment ID: {equipment_id}")
            return False
        except Exception as e:
            print(f"Error updating service request status: {e}")
            return False

    def find_service_request(self, equipment_id: str) -> Optional[ServiceRequest]:
        """Find a service request by equipment ID."""
        try:
            for request in self.service_requests:
                if request.equipment_id == equipment_id:
                    return request
            return None
        except Exception as e:
            print(f"Error finding service request: {e}")
            return None


# Example usage
if __name__ == "__main__":
    service_manager = ServiceManager()
    
    # Create service requests
    service_manager.create_service_request("GATE-001", "John Doe", "Maintenance")
    service_manager.create_service_request("FILTER-002", "Jane Smith", "Repair")
    
    # List all service requests
    for request in service_manager.list_service_requests():
        print(request)
    
    # Update a service request status
    service_manager.update_service_request_status("GATE-001", "Completed")
    
    # Find a specific service request
    request = service_manager.find_service_request("FILTER-002")
    if request:
        print(f"Found request: {request}")
    else:
        print("Service request not found.")
```
