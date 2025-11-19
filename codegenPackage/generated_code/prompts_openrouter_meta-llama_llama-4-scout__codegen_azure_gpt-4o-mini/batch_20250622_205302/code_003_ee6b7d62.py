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
from typing import List, Optional
import uuid

class MaintenanceRequest:
    """Class representing a maintenance request."""
    
    def __init__(self, description: str, requested_by: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the request
        self.description = description  # Description of the maintenance needed
        self.requested_by = requested_by  # Person who requested the maintenance
        self.status = 'Pending'  # Initial status of the request
        self.created_at = datetime.now()  # Timestamp of when the request was created
        self.scheduled_time: Optional[datetime] = None  # Time when maintenance is scheduled
        self.assigned_resources: List[str] = []  # List of resources assigned to the request

    def schedule(self, scheduled_time: datetime):
        """Schedule the maintenance request."""
        if scheduled_time < datetime.now():
            raise ValueError("Scheduled time must be in the future.")
        self.scheduled_time = scheduled_time
        self.status = 'Scheduled'

    def assign_resources(self, resources: List[str]):
        """Assign resources to the maintenance request."""
        if self.status != 'Scheduled':
            raise RuntimeError("Cannot assign resources unless the request is scheduled.")
        self.assigned_resources.extend(resources)

    def complete(self):
        """Mark the maintenance request as completed."""
        if self.status != 'Scheduled':
            raise RuntimeError("Cannot complete a request that is not scheduled.")
        self.status = 'Completed'

class MaintenanceManager:
    """Class to manage maintenance requests."""
    
    def __init__(self):
        self.requests: List[MaintenanceRequest] = []  # List to store all maintenance requests

    def create_request(self, description: str, requested_by: str) -> MaintenanceRequest:
        """Create a new maintenance request."""
        request = MaintenanceRequest(description, requested_by)
        self.requests.append(request)
        return request

    def get_pending_requests(self) -> List[MaintenanceRequest]:
        """Retrieve all pending maintenance requests."""
        return [request for request in self.requests if request.status == 'Pending']

    def get_scheduled_requests(self) -> List[MaintenanceRequest]:
        """Retrieve all scheduled maintenance requests."""
        return [request for request in self.requests if request.status == 'Scheduled']

    def get_completed_requests(self) -> List[MaintenanceRequest]:
        """Retrieve all completed maintenance requests."""
        return [request for request in self.requests if request.status == 'Completed']

# Example usage
if __name__ == "__main__":
    manager = MaintenanceManager()
    
    # Create a maintenance request
    request = manager.create_request("Fix leaking pipe", "John Doe")
    
    # Schedule the maintenance request
    try:
        request.schedule(datetime.now() + timedelta(days=1))  # Schedule for tomorrow
    except ValueError as e:
        print(f"Error scheduling request: {e}")

    # Assign resources to the request
    try:
        request.assign_resources(["Plumber", "Tools"])
    except RuntimeError as e:
        print(f"Error assigning resources: {e}")

    # Complete the maintenance request
    try:
        request.complete()
    except RuntimeError as e:
        print(f"Error completing request: {e}")

    # Output the status of the request
    print(f"Request ID: {request.id}, Status: {request.status}")
```
