"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Develop a software solution for managing elevator repairs, focusing on qualitative service delivery as outlined by ICON Elevator.
Generated: DETERMINISTIC_0594ae4e8356a868
Batch ID: 20250612_153246
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

class RepairRequest:
    """Class to represent a repair request for an elevator."""
    
    def __init__(self, elevator_id: str, description: str, request_date: Optional[datetime.date] = None):
        self.elevator_id = elevator_id
        self.description = description
        self.request_date = request_date or datetime.date.today()
        self.status = 'Pending'  # Initial status of the repair request

    def __str__(self):
        return f"RepairRequest(elevator_id={self.elevator_id}, description={self.description}, " \
               f"request_date={self.request_date}, status={self.status})"


class RepairManager:
    """Class to manage elevator repair requests."""
    
    def __init__(self):
        self.requests: List[RepairRequest] = []

    def add_request(self, elevator_id: str, description: str) -> None:
        """Add a new repair request to the system."""
        if not elevator_id or not description:
            raise ValueError("Elevator ID and description must not be empty.")
        
        request = RepairRequest(elevator_id, description)
        self.requests.append(request)
        print(f"Added repair request: {request}")

    def update_request_status(self, elevator_id: str, new_status: str) -> None:
        """Update the status of a repair request."""
        if new_status not in ['Pending', 'In Progress', 'Completed']:
            raise ValueError("Invalid status. Must be one of: 'Pending', 'In Progress', 'Completed'.")

        for request in self.requests:
            if request.elevator_id == elevator_id:
                request.status = new_status
                print(f"Updated request status: {request}")
                return
        
        raise ValueError(f"No repair request found for elevator ID: {elevator_id}")

    def get_pending_requests(self) -> List[RepairRequest]:
        """Retrieve all pending repair requests."""
        pending_requests = [request for request in self.requests if request.status == 'Pending']
        print(f"Pending requests: {pending_requests}")
        return pending_requests

    def get_all_requests(self) -> List[RepairRequest]:
        """Retrieve all repair requests."""
        print(f"All requests: {self.requests}")
        return self.requests


# Example usage
if __name__ == "__main__":
    repair_manager = RepairManager()
    
    try:
        repair_manager.add_request("Elevator_1", "Door malfunction")
        repair_manager.add_request("Elevator_2", "Overheating issue")
        
        repair_manager.update_request_status("Elevator_1", "In Progress")
        
        pending_requests = repair_manager.get_pending_requests()
        all_requests = repair_manager.get_all_requests()
        
    except ValueError as e:
        print(f"Error: {e}")
```
