"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Generate a Python script to manage plumbing service requests for a residential building using ERA ENGINEERING's services."
Generated: DETERMINISTIC_d25d8c8886e82724
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class ServiceRequest:
    """Class to represent a plumbing service request."""
    
    def __init__(self, request_id: int, resident_name: str, apartment_number: str, issue_description: str):
        self.request_id = request_id
        self.resident_name = resident_name
        self.apartment_number = apartment_number
        self.issue_description = issue_description
        self.status = "Pending"
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the service request to a dictionary."""
        return {
            "request_id": self.request_id,
            "resident_name": self.resident_name,
            "apartment_number": self.apartment_number,
            "issue_description": self.issue_description,
            "status": self.status,
            "timestamp": self.timestamp
        }

class ServiceRequestManager:
    """Class to manage plumbing service requests."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.requests: List[ServiceRequest] = []
        self.load_requests()

    def load_requests(self) -> None:
        """Load service requests from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                requests_data = json.load(file)
                self.requests = [ServiceRequest(**data) for data in requests_data]
        except FileNotFoundError:
            # If the file does not exist, we start with an empty list
            self.requests = []
        except json.JSONDecodeError as e:
            print(f"Error loading requests: {e}")
            self.requests = []

    def save_requests(self) -> None:
        """Save service requests to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([request.to_dict() for request in self.requests], file, indent=4)
        except IOError as e:
            print(f"Error saving requests: {e}")

    def add_request(self, resident_name: str, apartment_number: str, issue_description: str) -> None:
        """Add a new service request."""
        request_id = len(self.requests) + 1  # Simple ID generation
        new_request = ServiceRequest(request_id, resident_name, apartment_number, issue_description)
        self.requests.append(new_request)
        self.save_requests()

    def update_request_status(self, request_id: int, new_status: str) -> None:
        """Update the status of a service request."""
        for request in self.requests:
            if request.request_id == request_id:
                request.status = new_status
                self.save_requests()
                return
        print(f"Request ID {request_id} not found.")

    def list_requests(self) -> List[Dict[str, Any]]:
        """List all service requests."""
        return [request.to_dict() for request in self.requests]

def main():
    """Main function to run the service request manager."""
    manager = ServiceRequestManager('service_requests.json')

    # Example usage
    manager.add_request("John Doe", "101", "Leaky faucet")
    manager.add_request("Jane Smith", "202", "Clogged drain")
    
    print("Current Service Requests:")
    for request in manager.list_requests():
        print(request)

    # Update a request status
    manager.update_request_status(1, "Completed")

if __name__ == "__main__":
    main()
```
