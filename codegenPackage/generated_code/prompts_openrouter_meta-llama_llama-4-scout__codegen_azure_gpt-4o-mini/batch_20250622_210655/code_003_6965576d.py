"""
Generated Code Metadata:
========================
Original URL: https://bee-property.com
Prompt: "Design a system for tracking and managing property maintenance and repairs for short-term rentals, ensuring high guest satisfaction and optimal property condition, as per Bee Property's approach."
Generated: DETERMINISTIC_6965576d73181de0
Batch ID: 20250622_210655
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

class MaintenanceRequest:
    """Class to represent a maintenance request for a property."""
    
    def __init__(self, property_id: str, description: str, request_date: datetime.date, status: str = "Pending"):
        self.property_id = property_id
        self.description = description
        self.request_date = request_date
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the maintenance request."""
        valid_statuses = ["Pending", "In Progress", "Completed", "Cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

class Property:
    """Class to represent a property in the rental system."""
    
    def __init__(self, property_id: str, address: str):
        self.property_id = property_id
        self.address = address
        self.maintenance_requests: List[MaintenanceRequest] = []

    def add_maintenance_request(self, description: str):
        """Add a new maintenance request to the property."""
        request_date = datetime.date.today()
        new_request = MaintenanceRequest(self.property_id, description, request_date)
        self.maintenance_requests.append(new_request)

    def get_pending_requests(self) -> List[MaintenanceRequest]:
        """Retrieve all pending maintenance requests for the property."""
        return [request for request in self.maintenance_requests if request.status == "Pending"]

class PropertyManagementSystem:
    """Class to manage multiple properties and their maintenance requests."""
    
    def __init__(self):
        self.properties: List[Property] = []

    def add_property(self, property_id: str, address: str):
        """Add a new property to the management system."""
        if any(prop.property_id == property_id for prop in self.properties):
            raise ValueError(f"Property with ID {property_id} already exists.")
        new_property = Property(property_id, address)
        self.properties.append(new_property)

    def find_property(self, property_id: str) -> Optional[Property]:
        """Find a property by its ID."""
        for property in self.properties:
            if property.property_id == property_id:
                return property
        return None

    def report_maintenance(self, property_id: str, description: str):
        """Report a maintenance issue for a specific property."""
        property = self.find_property(property_id)
        if property is None:
            raise ValueError(f"Property with ID {property_id} not found.")
        property.add_maintenance_request(description)

    def get_all_pending_requests(self) -> List[MaintenanceRequest]:
        """Retrieve all pending maintenance requests across all properties."""
        pending_requests = []
        for property in self.properties:
            pending_requests.extend(property.get_pending_requests())
        return pending_requests

# Example usage
if __name__ == "__main__":
    try:
        pms = PropertyManagementSystem()
        pms.add_property("001", "123 Bee St, Bee City")
        pms.report_maintenance("001", "Leaky faucet in kitchen.")
        
        pending_requests = pms.get_all_pending_requests()
        for request in pending_requests:
            print(f"Request for Property ID {request.property_id}: {request.description} - Status: {request.status}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
