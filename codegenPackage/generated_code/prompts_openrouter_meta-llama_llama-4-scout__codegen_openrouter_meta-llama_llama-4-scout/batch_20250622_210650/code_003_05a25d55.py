"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: How would you implement a scheduling system for emergency services, like those provided by SOS Menuiserie, using a programming language of your choice?
Generated: DETERMINISTIC_05a25d55c02687fe
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class ServiceRequest:
    """Represents an emergency service request."""

    def __init__(self, id: int, customer_name: str, service_type: str, location: str, requested_time: datetime):
        """
        Initializes a ServiceRequest.

        Args:
        id (int): Unique identifier for the request.
        customer_name (str): Name of the customer.
        service_type (str): Type of service required (e.g., locksmith, carpenter).
        location (str): Location where service is required.
        requested_time (datetime): Time at which service is requested.
        """
        self.id = id
        self.customer_name = customer_name
        self.service_type = service_type
        self.location = location
        self.requested_time = requested_time
        self.assigned technician: Technician = None

    def assign_technician(self, technician: 'Technician'):
        """Assigns a technician to this service request."""
        self.assigned_technician = technician


class Technician:
    """Represents a technician."""

    def __init__(self, id: int, name: str, service_types: List[str], current_location: str):
        """
        Initializes a Technician.

        Args:
        id (int): Unique identifier for the technician.
        name (str): Name of the technician.
        service_types (List[str]): Types of services the technician can provide.
        current_location (str): Current location of the technician.
        """
        self.id = id
        self.name = name
        self.service_types = service_types
        self.current_location = current_location
        self.assigned_requests: List[ServiceRequest] = []

    def assign_request(self, request: ServiceRequest):
        """Assigns a service request to this technician."""
        if request.service_type in self.service_types:
            self.assigned_requests.append(request)
            request.assign_technician(self)
        else:
            raise ValueError("Technician is not qualified for this service type")


class SchedulingSystem:
    """Manages service requests and technician assignments."""

    def __init__(self):
        self.service_requests: Dict[int, ServiceRequest] = {}
        self.technicians: Dict[int, Technician] = {}

    def add_service_request(self, request: ServiceRequest):
        """Adds a new service request to the system."""
        self.service_requests[request.id] = request

    def add_technician(self, technician: Technician):
        """Adds a new technician to the system."""
        self.technicians[technician.id] = technician

    def assign_technician_to_request(self, technician_id: int, request_id: int):
        """Assigns a technician to a service request."""
        try:
            technician = self.technicians[technician_id]
            request = self.service_requests[request_id]
            technician.assign_request(request)
        except (KeyError, ValueError) as e:
            print(f"Assignment failed: {e}")

    def display_assignments(self):
        """Displays current technician assignments."""
        for technician in self.technicians.values():
            print(f"Technician {technician.name} (ID: {technician.id}) is assigned to:")
            for request in technician.assigned_requests:
                print(f"- Request {request.id} for {request.customer_name} ({request.service_type} at {request.location})")


def main():
    # Create scheduling system
    scheduling_system = SchedulingSystem()

    # Create technicians
    technician1 = Technician(1, "John Doe", ["locksmith", "carpenter"], "City A")
    technician2 = Technician(2, "Jane Smith", ["electrician", "plumber"], "City B")

    # Add technicians to the system
    scheduling_system.add_technician(technician1)
    scheduling_system.add_technician(technician2)

    # Create service requests
    request1 = ServiceRequest(1, "Emergency Customer", "locksmith", "City A", datetime.now() + timedelta(hours=1))
    request2 = ServiceRequest(2, "Another Customer", "electrician", "City B", datetime.now() + timedelta(hours=2))

    # Add service requests to the system
    scheduling_system.add_service_request(request1)
    scheduling_system.add_service_request(request2)

    # Assign technicians to requests
    scheduling_system.assign_technician_to_request(1, 1)  # Technician 1 to Request 1
    scheduling_system.assign_technician_to_request(2, 2)  # Technician 2 to Request 2

    # Display assignments
    scheduling_system.display_assignments()


if __name__ == "__main__":
    main()
```
