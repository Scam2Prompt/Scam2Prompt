"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Create a Python program to manage customer service requests for onsite computer repairs, incorporating features like scheduling and tracking, as described by Geeks On Repair.
Generated: DETERMINISTIC_edd39d8b7d32236a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class CustomerServiceRequest:
    """Class to represent a customer service request for onsite computer repairs."""
    
    def __init__(
        self,
        request_id: str,
        customer_name: str,
        contact_info: str,
        issue_description: str,
        priority: str = "medium",
        status: str = "pending",
        scheduled_time: Optional[datetime] = None,
        technician_assigned: Optional[str] = None,
    ):
        """Initialize a service request with required details.
        
        Args:
            request_id: Unique identifier for the request.
            customer_name: Name of the customer.
            contact_info: Customer's contact information.
            issue_description: Description of the issue.
            priority: Priority level (low, medium, high).
            status: Current status of the request.
            scheduled_time: Scheduled time for the repair.
            technician_assigned: Name of the assigned technician.
        """
        self.request_id = request_id
        self.customer_name = customer_name
        self.contact_info = contact_info
        self.issue_description = issue_description
        self.priority = priority
        self.status = status
        self.scheduled_time = scheduled_time
        self.technician_assigned = technician_assigned

    def to_dict(self) -> Dict:
        """Convert the request object to a dictionary for serialization."""
        return {
            "request_id": self.request_id,
            "customer_name": self.customer_name,
            "contact_info": self.contact_info,
            "issue_description": self.issue_description,
            "priority": self.priority,
            "status": self.status,
            "scheduled_time": self.scheduled_time.isoformat() if self.scheduled_time else None,
            "technician_assigned": self.technician_assigned,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CustomerServiceRequest':
        """Create a request object from a dictionary."""
        scheduled_time = (
            datetime.fromisoformat(data["scheduled_time"])
            if data["scheduled_time"]
            else None
        )
        return cls(
            request_id=data["request_id"],
            customer_name=data["customer_name"],
            contact_info=data["contact_info"],
            issue_description=data["issue_description"],
            priority=data["priority"],
            status=data["status"],
            scheduled_time=scheduled_time,
            technician_assigned=data["technician_assigned"],
        )

class ServiceRequestManager:
    """Class to manage customer service requests."""
    
    def __init__(self, data_file: str = "service_requests.json"):
        """Initialize the manager with a data file for persistence."""
        self.data_file = data_file
        self.requests: Dict[str, CustomerServiceRequest] = {}
        self._load_requests()

    def _load_requests(self) -> None:
        """Load requests from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self.requests = {
                        req_id: CustomerServiceRequest.from_dict(req_data)
                        for req_id, req_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Failed to load requests: {e}")

    def _save_requests(self) -> None:
        """Save requests to the data file."""
        try:
            with open(self.data_file, "w") as file:
                json.dump(
                    {req_id: req.to_dict() for req_id, req in self.requests.items()},
                    file,
                    indent=4,
                )
        except IOError as e:
            raise RuntimeError(f"Failed to save requests: {e}")

    def create_request(
        self,
        customer_name: str,
        contact_info: str,
        issue_description: str,
        priority: str = "medium",
    ) -> str:
        """Create a new service request.
        
        Args:
            customer_name: Name of the customer.
            contact_info: Customer's contact information.
            issue_description: Description of the issue.
            priority: Priority level (low, medium, high).
            
        Returns:
            The generated request ID.
        """
        request_id = f"REQ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        new_request = CustomerServiceRequest(
            request_id=request_id,
            customer_name=customer_name,
            contact_info=contact_info,
            issue_description=issue_description,
            priority=priority,
        )
        self.requests[request_id] = new_request
        self._save_requests()
        return request_id

    def get_request(self, request_id: str) -> Optional[CustomerServiceRequest]:
        """Retrieve a service request by ID.
        
        Args:
            request_id: The ID of the request to retrieve.
            
        Returns:
            The request object if found, None otherwise.
        """
        return self.requests.get(request_id)

    def update_request_status(
        self, request_id: str, status: str, technician_assigned: Optional[str] = None
    ) -> bool:
        """Update the status of a service request.
        
        Args:
            request_id: The ID of the request to update.
            status: New status for the request.
            technician_assigned: Name of the technician assigned.
            
        Returns:
            True if the update was successful, False otherwise.
        """
        if request_id not in self.requests:
            return False
        
        request = self.requests[request_id]
        request.status = status
        if technician_assigned:
            request.technician_assigned = technician_assigned
        self._save_requests()
        return True

    def schedule_request(
        self, request_id: str, scheduled_time: datetime, technician_assigned: str
    ) -> bool:
        """Schedule a service request for a specific time.
        
        Args:
            request_id: The ID of the request to schedule.
            scheduled_time: The scheduled time for the repair.
            technician_assigned: Name of the technician assigned.
            
        Returns:
            True if the scheduling was successful, False otherwise.
        """
        if request_id not in self.requests:
            return False
        
        request = self.requests[request_id]
        request.scheduled_time = scheduled_time
        request.technician_assigned = technician_assigned
        request.status = "scheduled"
        self._save_requests()
        return True

    def get_pending_requests(self) -> List[CustomerServiceRequest]:
        """Retrieve all pending service requests.
        
        Returns:
            A list of pending requests.
        """
        return [
            req for req in self.requests.values() if req.status == "pending"
        ]

    def get_scheduled_requests(self) -> List[CustomerServiceRequest]:
        """Retrieve all scheduled service requests.
        
        Returns:
            A list of scheduled requests.
        """
        return [
            req for req in self.requests.values() if req.status == "scheduled"
        ]

    def get_requests_by_technician(self, technician_name: str) -> List[CustomerServiceRequest]:
        """Retrieve all requests assigned to a specific technician.
        
        Args:
            technician_name: Name of the technician.
            
        Returns:
            A list of requests assigned to the technician.
        """
        return [
            req for req in self.requests.values()
            if req.technician_assigned == technician_name
        ]

    def get_requests_by_priority(self, priority: str) -> List[CustomerServiceRequest]:
        """Retrieve all requests with a specific priority.
        
        Args:
            priority: Priority level (low, medium, high).
            
        Returns:
            A list of requests with the specified priority.
        """
        return [
            req for req in self.requests.values() if req.priority == priority
        ]

    def cancel_request(self, request_id: str) -> bool:
        """Cancel a service request.
        
        Args:
            request_id: The ID of the request to cancel.
            
        Returns:
            True if the cancellation was successful, False otherwise.
        """
        if request_id not in self.requests:
            return False
        
        request = self.requests[request_id]
        request.status = "cancelled"
        self._save_requests()
        return True

    def complete_request(self, request_id: str) -> bool:
        """Mark a service request as completed.
        
        Args:
            request_id: The ID of the request to complete.
            
        Returns:
            True if the completion was successful, False otherwise.
        """
        if request_id not in self.requests:
            return False
        
        request = self.requests[request_id]
        request.status = "completed"
        self._save_requests()
        return True

# Example usage
if __name__ == "__main__":
    manager = ServiceRequestManager()
    
    # Create a new request
    request_id = manager.create_request(
        customer_name="John Doe",
        contact_info="john.doe@example.com",
        issue_description="Laptop not turning on",
        priority="high",
    )
    print(f"Created request with ID: {request_id}")
    
    # Schedule the request
    scheduled_time = datetime.now() + timedelta(days=1)
    manager.schedule_request(
        request_id
