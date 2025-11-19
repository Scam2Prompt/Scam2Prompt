"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Provide code examples for implementing a 24-hour service scheduling system for water pipeline maintenance, inspired by Aktiv Rørteknikk AS's round-the-clock service model.
Generated: DETERMINISTIC_f72812eb8687f006
Batch ID: 20250612_154209
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

class ServiceStatus(Enum):
    """Enum for service status"""
    SCHEDULED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class ServiceRequest:
    """Class for service requests"""
    def __init__(self, id, description, scheduled_time):
        """
        Initialize a service request

        Args:
            id (int): Unique identifier for the service request
            description (str): Description of the service request
            scheduled_time (datetime): Scheduled time for the service request
        """
        self.id = id
        self.description = description
        self.scheduled_time = scheduled_time
        self.status = ServiceStatus.SCHEDULED

    def update_status(self, status):
        """
        Update the status of the service request

        Args:
            status (ServiceStatus): New status for the service request
        """
        self.status = status

class ServiceSchedulingSystem:
    """Class for service scheduling system"""
    def __init__(self):
        self.service_requests = []

    def schedule_service(self, id, description, scheduled_time):
        """
        Schedule a new service request

        Args:
            id (int): Unique identifier for the service request
            description (str): Description of the service request
            scheduled_time (datetime): Scheduled time for the service request

        Returns:
            ServiceRequest: The scheduled service request
        """
        if not isinstance(scheduled_time, datetime):
            raise ValueError("Scheduled time must be a datetime object")

        service_request = ServiceRequest(id, description, scheduled_time)
        self.service_requests.append(service_request)
        return service_request

    def get_service_requests(self, status=None):
        """
        Get a list of service requests

        Args:
            status (ServiceStatus, optional): Filter by status. Defaults to None.

        Returns:
            list: List of service requests
        """
        if status:
            return [sr for sr in self.service_requests if sr.status == status]
        return self.service_requests

    def update_service_request_status(self, id, status):
        """
        Update the status of a service request

        Args:
            id (int): Unique identifier for the service request
            status (ServiceStatus): New status for the service request

        Returns:
            bool: True if the status was updated, False otherwise
        """
        for sr in self.service_requests:
            if sr.id == id:
                sr.update_status(status)
                return True
        return False

def main():
    # Create a service scheduling system
    system = ServiceSchedulingSystem()

    # Schedule some service requests
    now = datetime.now()
    system.schedule_service(1, "Inspect pipeline", now + timedelta(hours=2))
    system.schedule_service(2, "Repair leak", now + timedelta(days=1))
    system.schedule_service(3, "Replace valve", now + timedelta(hours=4))

    # Get all service requests
    print("All Service Requests:")
    for sr in system.get_service_requests():
        print(f"ID: {sr.id}, Description: {sr.description}, Scheduled Time: {sr.scheduled_time}, Status: {sr.status.name}")

    # Update the status of a service request
    system.update_service_request_status(1, ServiceStatus.IN_PROGRESS)

    # Get service requests by status
    print("\nService Requests in Progress:")
    for sr in system.get_service_requests(ServiceStatus.IN_PROGRESS):
        print(f"ID: {sr.id}, Description: {sr.description}, Scheduled Time: {sr.scheduled_time}, Status: {sr.status.name}")

if __name__ == "__main__":
    main()
```
