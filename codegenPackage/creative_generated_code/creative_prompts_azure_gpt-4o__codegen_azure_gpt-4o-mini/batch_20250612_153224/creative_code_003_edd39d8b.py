"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Create a Python program to manage customer service requests for onsite computer repairs, incorporating features like scheduling and tracking, as described by Geeks On Repair.
Generated: DETERMINISTIC_edd39d8b7d32236a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Optional

class ServiceRequest:
    """Class to represent a service request for onsite computer repairs."""

    def __init__(self, customer_name: str, issue_description: str, request_time: datetime.datetime):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.request_time = request_time
        self.status = "Pending"  # Initial status of the service request

    def to_dict(self) -> Dict:
        """Convert the service request to a dictionary format."""
        return {
            "customer_name": self.customer_name,
            "issue_description": self.issue_description,
            "request_time": self.request_time.isoformat(),
            "status": self.status
        }

class ServiceRequestManager:
    """Class to manage service requests."""

    def __init__(self):
        self.requests: List[ServiceRequest] = []

    def add_request(self, customer_name: str, issue_description: str) -> None:
        """Add a new service request to the manager."""
        request_time = datetime.datetime.now()
        new_request = ServiceRequest(customer_name, issue_description, request_time)
        self.requests.append(new_request)

    def get_pending_requests(self) -> List[Dict]:
        """Retrieve all pending service requests."""
        return [request.to_dict() for request in self.requests if request.status == "Pending"]

    def track_request(self, customer_name: str) -> Optional[Dict]:
        """Track a specific service request by customer name."""
        for request in self.requests:
            if request.customer_name == customer_name:
                return request.to_dict()
        return None  # Return None if no request found

    def update_request_status(self, customer_name: str, new_status: str) -> bool:
        """Update the status of a service request."""
        for request in self.requests:
            if request.customer_name == customer_name:
                if new_status in ["Pending", "In Progress", "Completed"]:
                    request.status = new_status
                    return True
                else:
                    raise ValueError("Invalid status. Must be 'Pending', 'In Progress', or 'Completed'.")
        return False  # Return False if no request found

    def save_requests_to_file(self, filename: str) -> None:
        """Save all service requests to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([request.to_dict() for request in self.requests], file, indent=4)
        except IOError as e:
            print(f"Error saving requests to file: {e}")

    def load_requests_from_file(self, filename: str) -> None:
        """Load service requests from a JSON file."""
        try:
            with open(filename, 'r') as file:
                requests_data = json.load(file)
                for req in requests_data:
                    request_time = datetime.datetime.fromisoformat(req["request_time"])
                    loaded_request = ServiceRequest(req["customer_name"], req["issue_description"], request_time)
                    loaded_request.status = req["status"]
                    self.requests.append(loaded_request)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading requests from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ServiceRequestManager()
    
    # Load existing requests
    manager.load_requests_from_file("service_requests.json")

    # Adding a new service request
    manager.add_request("John Doe", "Laptop won't start.")
    
    # Update request status
    manager.update_request_status("John Doe", "In Progress")
    
    # Track a specific request
    print(manager.track_request("John Doe"))
    
    # Save requests to file
    manager.save_requests_to_file("service_requests.json")
```
