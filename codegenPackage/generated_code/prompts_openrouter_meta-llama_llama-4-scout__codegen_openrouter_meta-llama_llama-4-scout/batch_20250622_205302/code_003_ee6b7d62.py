"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Design a data model for managing industrial maintenance requests, including scheduling and resource allocation, inspired by Tether's maintenance services."
Generated: DETERMINISTIC_ee6b7d62aa1dad68
Batch ID: 20250622_205302
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
from typing import List, Optional

class MaintenanceStatus(Enum):
    """Enum for maintenance request status"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class MaintenancePriority(Enum):
    """Enum for maintenance request priority"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class ResourceType(Enum):
    """Enum for resource type"""
    TECHNICIAN = 1
    EQUIPMENT = 2
    MATERIAL = 3

class Resource:
    """Resource data model"""
    def __init__(self, id: int, name: str, resource_type: ResourceType):
        self.id = id
        self.name = name
        self.resource_type = resource_type

class MaintenanceRequest:
    """Maintenance request data model"""
    def __init__(self, id: int, title: str, description: str, priority: MaintenancePriority):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = MaintenanceStatus.PENDING
        self.scheduled_start = None
        self.scheduled_end = None
        self.resources = []

    def schedule(self, start: datetime, end: datetime):
        """Schedule the maintenance request"""
        self.scheduled_start = start
        self.scheduled_end = end

    def assign_resource(self, resource: Resource):
        """Assign a resource to the maintenance request"""
        self.resources.append(resource)

    def update_status(self, status: MaintenanceStatus):
        """Update the status of the maintenance request"""
        self.status = status

class MaintenanceScheduler:
    """Maintenance scheduler"""
    def __init__(self):
        self.requests = []

    def add_request(self, request: MaintenanceRequest):
        """Add a maintenance request"""
        self.requests.append(request)

    def get_requests(self, status: Optional[MaintenanceStatus] = None):
        """Get maintenance requests by status"""
        if status:
            return [r for r in self.requests if r.status == status]
        return self.requests

    def schedule_request(self, request: MaintenanceRequest, start: datetime, end: datetime):
        """Schedule a maintenance request"""
        request.schedule(start, end)

def main():
    # Create resources
    technician = Resource(1, "John Doe", ResourceType.TECHNICIAN)
    equipment = Resource(2, "Equipment 1", ResourceType.EQUIPMENT)

    # Create maintenance requests
    request1 = MaintenanceRequest(1, "Request 1", "Description 1", MaintenancePriority.HIGH)
    request2 = MaintenanceRequest(2, "Request 2", "Description 2", MaintenancePriority.MEDIUM)

    # Schedule requests
    scheduler = MaintenanceScheduler()
    scheduler.add_request(request1)
    scheduler.add_request(request2)
    scheduler.schedule_request(request1, datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=1, hours=2))
    scheduler.schedule_request(request2, datetime.now() + timedelta(days=3), datetime.now() + timedelta(days=3, hours=4))

    # Assign resources
    request1.assign_resource(technician)
    request1.assign_resource(equipment)

    # Update status
    request1.update_status(MaintenanceStatus.IN_PROGRESS)

    # Get requests
    all_requests = scheduler.get_requests()
    in_progress_requests = scheduler.get_requests(MaintenanceStatus.IN_PROGRESS)

    # Print requests
    for request in all_requests:
        print(f"Request {request.id}: {request.title} - {request.status.name}")

if __name__ == "__main__":
    main()
```
