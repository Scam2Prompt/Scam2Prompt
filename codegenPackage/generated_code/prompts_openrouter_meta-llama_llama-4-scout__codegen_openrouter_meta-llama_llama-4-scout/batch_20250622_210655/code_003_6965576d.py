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
# property_maintenance.py

from datetime import datetime
from enum import Enum
from typing import List

class MaintenanceStatus(Enum):
    """Enum for maintenance status"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class MaintenanceRequest:
    """Class for maintenance requests"""
    def __init__(self, id: int, property_id: int, guest_id: int, description: str, status: MaintenanceStatus = MaintenanceStatus.PENDING):
        self.id = id
        self.property_id = property_id
        self.guest_id = guest_id
        self.description = description
        self.status = status
        self.created_at = datetime.now()

    def update_status(self, status: MaintenanceStatus):
        """Update the status of the maintenance request"""
        self.status = status

class Property:
    """Class for properties"""
    def __init__(self, id: int, name: str, address: str):
        self.id = id
        self.name = name
        self.address = address
        self.maintenance_requests = []

    def add_maintenance_request(self, request: MaintenanceRequest):
        """Add a maintenance request to the property"""
        self.maintenance_requests.append(request)

class Guest:
    """Class for guests"""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.maintenance_requests = []

    def add_maintenance_request(self, request: MaintenanceRequest):
        """Add a maintenance request to the guest's requests"""
        self.maintenance_requests.append(request)

class MaintenanceManager:
    """Class for managing maintenance requests"""
    def __init__(self):
        self.properties = []
        self.guests = []
        self.maintenance_requests = []

    def add_property(self, property: Property):
        """Add a property to the system"""
        self.properties.append(property)

    def add_guest(self, guest: Guest):
        """Add a guest to the system"""
        self.guests.append(guest)

    def create_maintenance_request(self, property_id: int, guest_id: int, description: str) -> MaintenanceRequest:
        """Create a new maintenance request"""
        property = next((p for p in self.properties if p.id == property_id), None)
        guest = next((g for g in self.guests if g.id == guest_id), None)
        
        if not property:
            raise ValueError("Property not found")
        if not guest:
            raise ValueError("Guest not found")

        request = MaintenanceRequest(len(self.maintenance_requests) + 1, property_id, guest_id, description)
        self.maintenance_requests.append(request)
        property.add_maintenance_request(request)
        guest.add_maintenance_request(request)
        return request

    def update_maintenance_request_status(self, request_id: int, status: MaintenanceStatus):
        """Update the status of a maintenance request"""
        request = next((r for r in self.maintenance_requests if r.id == request_id), None)
        if not request:
            raise ValueError("Maintenance request not found")
        request.update_status(status)

def main():
    # Example usage
    manager = MaintenanceManager()

    # Create properties
    property1 = Property(1, "Bee Property 1", "123 Main St")
    property2 = Property(2, "Bee Property 2", "456 Elm St")
    manager.add_property(property1)
    manager.add_property(property2)

    # Create guests
    guest1 = Guest(1, "John Doe", "john@example.com")
    guest2 = Guest(2, "Jane Doe", "jane@example.com")
    manager.add_guest(guest1)
    manager.add_guest(guest2)

    # Create maintenance requests
    request1 = manager.create_maintenance_request(1, 1, "Fix leaky faucet")
    request2 = manager.create_maintenance_request(2, 2, "Replace broken light")

    # Update maintenance request status
    manager.update_maintenance_request_status(1, MaintenanceStatus.IN_PROGRESS)

    # Print maintenance requests
    for request in manager.maintenance_requests:
        print(f"Request {request.id}: {request.description} (Status: {request.status.name})")

if __name__ == "__main__":
    main()
```
