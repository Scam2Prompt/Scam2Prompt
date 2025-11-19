"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a code example that implements a scheduling system for plumbing services, focusing on urgent requests similar to those handled by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_ff273ce22379495c
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class ServiceStatus(Enum):
    """Service status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class PlumbingService:
    """Represents a plumbing service request"""
    def __init__(self, customer_name: str, service_description: str, urgency_level: int):
        """
        Initializes a plumbing service request

        Args:
        - customer_name (str): The name of the customer
        - service_description (str): A brief description of the service required
        - urgency_level (int): The urgency level of the request (1-5)
        """
        self.customer_name = customer_name
        self.service_description = service_description
        self.urgency_level = urgency_level
        self.status = ServiceStatus.PENDING
        self.request_time = datetime.now()

    def __str__(self):
        return f"Customer: {self.customer_name}, Service: {self.service_description}, Urgency: {self.urgency_level}, Status: {self.status.name}"

class SchedulingSystem:
    """Manages plumbing service requests"""
    def __init__(self):
        self.services: Dict[int, PlumbingService] = {}
        self.service_id_counter = 1

    def add_service_request(self, customer_name: str, service_description: str, urgency_level: int) -> int:
        """
        Adds a new service request to the system

        Args:
        - customer_name (str): The name of the customer
        - service_description (str): A brief description of the service required
        - urgency_level (int): The urgency level of the request (1-5)

        Returns:
        - int: The ID of the newly added service request
        """
        if urgency_level < 1 or urgency_level > 5:
            raise ValueError("Urgency level must be between 1 and 5")

        service = PlumbingService(customer_name, service_description, urgency_level)
        self.services[self.service_id_counter] = service
        service_id = self.service_id_counter
        self.service_id_counter += 1
        return service_id

    def update_service_status(self, service_id: int, status: ServiceStatus):
        """
        Updates the status of a service request

        Args:
        - service_id (int): The ID of the service request
        - status (ServiceStatus): The new status of the service request

        Raises:
        - KeyError: If the service ID is not found
        """
        if service_id not in self.services:
            raise KeyError("Service ID not found")

        self.services[service_id].status = status

    def get_urgent_services(self) -> List[PlumbingService]:
        """
        Retrieves a list of urgent service requests (urgency level 1-2)

        Returns:
        - List[PlumbingService]: A list of urgent service requests
        """
        urgent_services = [service for service in self.services.values() if service.urgency_level <= 2]
        return urgent_services

    def get_service_request(self, service_id: int) -> PlumbingService:
        """
        Retrieves a service request by ID

        Args:
        - service_id (int): The ID of the service request

        Returns:
        - PlumbingService: The service request object

        Raises:
        - KeyError: If the service ID is not found
        """
        if service_id not in self.services:
            raise KeyError("Service ID not found")

        return self.services[service_id]

def main():
    scheduling_system = SchedulingSystem()

    # Add service requests
    service_id1 = scheduling_system.add_service_request("John Doe", "Unclog drain", 1)
    service_id2 = scheduling_system.add_service_request("Jane Smith", "Fix leaky faucet", 3)
    service_id3 = scheduling_system.add_service_request("Bob Johnson", "Emergency pipe repair", 1)

    # Update service status
    scheduling_system.update_service_status(service_id1, ServiceStatus.IN_PROGRESS)

    # Get urgent services
    urgent_services = scheduling_system.get_urgent_services()
    print("Urgent Services:")
    for service in urgent_services:
        print(service)

    # Get service request by ID
    service_request = scheduling_system.get_service_request(service_id2)
    print("\nService Request:")
    print(service_request)

if __name__ == "__main__":
    main()
```
