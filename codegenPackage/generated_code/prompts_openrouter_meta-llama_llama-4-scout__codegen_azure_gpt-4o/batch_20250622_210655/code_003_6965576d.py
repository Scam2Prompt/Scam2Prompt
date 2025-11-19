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
"""
Property Maintenance and Repair Management System for Short-Term Rentals
This system is designed to track and manage property maintenance and repairs, ensuring high guest satisfaction and optimal property condition.
"""

import datetime
import json

# Define custom exceptions for error handling
class PropertyNotFoundError(Exception):
    pass

class MaintenanceRequestNotFoundError(Exception):
    pass

# Property class to represent individual properties
class Property:
    def __init__(self, property_id, name, address):
        """
        Initialize a Property instance.

        :param property_id: Unique identifier for the property
        :param name: Name of the property
        :param address: Address of the property
        """
        self.property_id = property_id
        self.name = name
        self.address = address
        self.maintenance_requests = []

    def add_maintenance_request(self, request):
        """
        Add a maintenance request to the property.

        :param request: MaintenanceRequest object
        """
        self.maintenance_requests.append(request)

    def get_open_requests(self):
        """
        Get all open maintenance requests for the property.

        :return: List of open maintenance requests
        """
        return [req for req in self.maintenance_requests if not req.is_resolved]

# MaintenanceRequest class to represent individual maintenance requests
class MaintenanceRequest:
    def __init__(self, request_id, description, priority, created_at=None):
        """
        Initialize a MaintenanceRequest instance.

        :param request_id: Unique identifier for the request
        :param description: Description of the maintenance issue
        :param priority: Priority level (e.g., 'Low', 'Medium', 'High')
        :param created_at: Timestamp of when the request was created
        """
        self.request_id = request_id
        self.description = description
        self.priority = priority
        self.created_at = created_at or datetime.datetime.now()
        self.is_resolved = False
        self.resolved_at = None

    def resolve(self):
        """
        Mark the maintenance request as resolved.
        """
        self.is_resolved = True
        self.resolved_at = datetime.datetime.now()

# PropertyManager class to manage multiple properties
class PropertyManager:
    def __init__(self):
        """
        Initialize a PropertyManager instance.
        """
        self.properties = {}

    def add_property(self, property):
        """
        Add a property to the manager.

        :param property: Property object
        """
        self.properties[property.property_id] = property

    def get_property(self, property_id):
        """
        Retrieve a property by its ID.

        :param property_id: Unique identifier for the property
        :return: Property object
        :raises PropertyNotFoundError: If the property is not found
        """
        if property_id not in self.properties:
            raise PropertyNotFoundError(f"Property with ID {property_id} not found.")
        return self.properties[property_id]

    def list_properties(self):
        """
        List all properties managed by the system.

        :return: List of Property objects
        """
        return list(self.properties.values())

    def generate_report(self):
        """
        Generate a report of all properties and their maintenance requests.

        :return: JSON-formatted report
        """
        report = {}
        for property in self.properties.values():
            report[property.name] = {
                "Address": property.address,
                "Open Requests": [
                    {
                        "Request ID": req.request_id,
                        "Description": req.description,
                        "Priority": req.priority,
                        "Created At": req.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    for req in property.get_open_requests()
                ]
            }
        return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the property manager
        manager = PropertyManager()

        # Create properties
        property1 = Property(property_id=1, name="Ocean View Villa", address="123 Beachside Ave")
        property2 = Property(property_id=2, name="Mountain Retreat", address="456 Alpine Rd")

        # Add properties to the manager
        manager.add_property(property1)
        manager.add_property(property2)

        # Create maintenance requests
        request1 = MaintenanceRequest(request_id=101, description="Leaky faucet in kitchen", priority="Medium")
        request2 = MaintenanceRequest(request_id=102, description="Broken window in living room", priority="High")

        # Add maintenance requests to properties
        property1.add_maintenance_request(request1)
        property1.add_maintenance_request(request2)

        # Resolve a maintenance request
        request1.resolve()

        # Generate and print the report
        print(manager.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}")
```
