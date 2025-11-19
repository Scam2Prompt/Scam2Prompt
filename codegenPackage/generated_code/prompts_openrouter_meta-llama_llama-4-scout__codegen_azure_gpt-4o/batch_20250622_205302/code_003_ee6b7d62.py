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
from datetime import datetime
from typing import List, Optional
import uuid

# Define the data model for managing industrial maintenance requests

class MaintenanceRequest:
    """
    Represents a maintenance request in the system.
    """
    def __init__(self, title: str, description: str, priority: str, requested_by: str):
        self.request_id = str(uuid.uuid4())  # Unique identifier for the request
        self.title = title  # Short title of the maintenance request
        self.description = description  # Detailed description of the issue
        self.priority = priority  # Priority level (e.g., 'Low', 'Medium', 'High')
        self.requested_by = requested_by  # Name or ID of the person who requested the maintenance
        self.created_at = datetime.now()  # Timestamp when the request was created
        self.status = "Pending"  # Current status of the request (e.g., 'Pending', 'In Progress', 'Completed')
        self.scheduled_date: Optional[datetime] = None  # Scheduled date for maintenance
        self.assigned_resources: List[str] = []  # List of resources (e.g., technicians) assigned to the request

    def schedule(self, date: datetime):
        """
        Schedule the maintenance request for a specific date.
        """
        if date < datetime.now():
            raise ValueError("Scheduled date cannot be in the past.")
        self.scheduled_date = date
        self.status = "Scheduled"

    def assign_resources(self, resources: List[str]):
        """
        Assign resources (e.g., technicians) to the maintenance request.
        """
        if not resources:
            raise ValueError("At least one resource must be assigned.")
        self.assigned_resources = resources

    def update_status(self, status: str):
        """
        Update the status of the maintenance request.
        """
        valid_statuses = ["Pending", "Scheduled", "In Progress", "Completed", "Cancelled"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
        self.status = status


class MaintenanceManager:
    """
    Manages a collection of maintenance requests.
    """
    def __init__(self):
        self.requests: List[MaintenanceRequest] = []  # List of all maintenance requests

    def create_request(self, title: str, description: str, priority: str, requested_by: str) -> MaintenanceRequest:
        """
        Create a new maintenance request and add it to the system.
        """
        new_request = MaintenanceRequest(title, description, priority, requested_by)
        self.requests.append(new_request)
        return new_request

    def get_request_by_id(self, request_id: str) -> Optional[MaintenanceRequest]:
        """
        Retrieve a maintenance request by its unique ID.
        """
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None

    def list_requests(self, status: Optional[str] = None) -> List[MaintenanceRequest]:
        """
        List all maintenance requests, optionally filtered by status.
        """
        if status:
            return [request for request in self.requests if request.status == status]
        return self.requests

    def delete_request(self, request_id: str):
        """
        Delete a maintenance request by its unique ID.
        """
        request = self.get_request_by_id(request_id)
        if not request:
            raise ValueError(f"No maintenance request found with ID: {request_id}")
        self.requests.remove(request)


# Example usage (uncomment to test):
# manager = MaintenanceManager()
# req = manager.create_request("Fix Conveyor Belt", "The conveyor belt is not functioning properly.", "High", "John Doe")
# req.schedule(datetime(2023, 11, 15))
# req.assign_resources(["Technician A", "Technician B"])
# req.update_status("In Progress")
# print(req.__dict__)
# print(manager.list_requests())
```
