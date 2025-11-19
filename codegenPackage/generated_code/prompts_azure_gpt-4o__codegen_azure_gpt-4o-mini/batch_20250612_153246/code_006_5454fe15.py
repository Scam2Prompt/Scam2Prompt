"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Create a solution for managing and organizing IT service requests for regional clients, inspired by DESSC's localized IT support approach.
Generated: DETERMINISTIC_5454fe157c730bdf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class ServiceRequest:
    """Class to represent a service request."""
    
    def __init__(self, client_name: str, description: str):
        self.request_id: str = str(uuid.uuid4())  # Unique identifier for the request
        self.client_name: str = client_name        # Name of the client
        self.description: str = description        # Description of the service request
        self.status: str = "Open"                  # Status of the request
        self.created_at: datetime = datetime.now() # Timestamp of when the request was created

    def __repr__(self):
        return f"ServiceRequest(request_id={self.request_id}, client_name={self.client_name}, status={self.status})"


class ServiceRequestManager:
    """Class to manage service requests."""
    
    def __init__(self):
        self.requests: List[ServiceRequest] = []  # List to store service requests

    def create_request(self, client_name: str, description: str) -> ServiceRequest:
        """Create a new service request."""
        if not client_name or not description:
            raise ValueError("Client name and description cannot be empty.")
        
        request = ServiceRequest(client_name, description)
        self.requests.append(request)
        return request

    def get_request(self, request_id: str) -> Optional[ServiceRequest]:
        """Retrieve a service request by its ID."""
        for request in self.requests:
            if request.request_id == request_id:
                return request
        return None  # Return None if request not found

    def update_request_status(self, request_id: str, new_status: str) -> bool:
        """Update the status of a service request."""
        request = self.get_request(request_id)
        if request is None:
            raise ValueError("Request not found.")
        
        valid_statuses = ["Open", "In Progress", "Resolved", "Closed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
        
        request.status = new_status
        return True

    def list_requests(self) -> List[ServiceRequest]:
        """List all service requests."""
        return self.requests


# Example usage
if __name__ == "__main__":
    manager = ServiceRequestManager()
    
    # Create service requests
    try:
        request1 = manager.create_request("Client A", "Need help with network issues.")
        request2 = manager.create_request("Client B", "Software installation request.")
        
        print("Created Requests:")
        print(manager.list_requests())
        
        # Update request status
        manager.update_request_status(request1.request_id, "In Progress")
        print("Updated Request:")
        print(manager.get_request(request1.request_id))
        
    except ValueError as e:
        print(f"Error: {e}")
```
