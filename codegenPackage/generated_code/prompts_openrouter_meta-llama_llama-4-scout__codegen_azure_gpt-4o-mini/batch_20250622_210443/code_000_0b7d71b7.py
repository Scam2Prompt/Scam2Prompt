"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Write a Python script to manage electrical service requests for residential and commercial clients, including client contact information and service details.
Generated: DETERMINISTIC_0b7d71b7888df944
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
import os
from typing import List, Dict, Any

class ServiceRequest:
    """Class to represent a service request for electrical services."""
    
    def __init__(self, client_name: str, client_contact: str, service_type: str, details: str):
        self.client_name = client_name
        self.client_contact = client_contact
        self.service_type = service_type
        self.details = details

    def to_dict(self) -> Dict[str, Any]:
        """Convert the service request to a dictionary."""
        return {
            "client_name": self.client_name,
            "client_contact": self.client_contact,
            "service_type": self.service_type,
            "details": self.details
        }

class ServiceRequestManager:
    """Class to manage service requests."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.requests: List[ServiceRequest] = []
        self.load_requests()

    def load_requests(self) -> None:
        """Load service requests from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    requests_data = json.load(file)
                    self.requests = [ServiceRequest(**data) for data in requests_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading requests: {e}")
                    self.requests = []

    def save_requests(self) -> None:
        """Save service requests to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([request.to_dict() for request in self.requests], file, indent=4)

    def add_request(self, request: ServiceRequest) -> None:
        """Add a new service request."""
        self.requests.append(request)
        self.save_requests()

    def get_requests(self) -> List[ServiceRequest]:
        """Get all service requests."""
        return self.requests

def main():
    """Main function to manage service requests."""
    manager = ServiceRequestManager('service_requests.json')

    # Example of adding a new service request
    try:
        new_request = ServiceRequest(
            client_name="John Doe",
            client_contact="john.doe@example.com",
            service_type="Residential",
            details="Install new lighting fixtures"
        )
        manager.add_request(new_request)
        print("Service request added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the service request: {e}")

    # Display all service requests
    print("\nCurrent Service Requests:")
    for request in manager.get_requests():
        print(f"{request.client_name} - {request.client_contact} - {request.service_type} - {request.details}")

if __name__ == "__main__":
    main()
```
