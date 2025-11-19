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
import datetime
import json
from typing import List, Dict, Optional

class ServiceRequest:
    """Class to represent a service request for onsite computer repairs."""
    
    def __init__(self, customer_name: str, issue_description: str, scheduled_time: datetime.datetime):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.scheduled_time = scheduled_time
        self.status = 'Pending'  # Initial status of the request

    def __repr__(self):
        return f"ServiceRequest(customer_name={self.customer_name}, issue_description={self.issue_description}, scheduled_time={self.scheduled_time}, status={self.status})"

class ServiceRequestManager:
    """Class to manage service requests."""
    
    def __init__(self):
        self.requests: List[ServiceRequest] = []

    def add_request(self, customer_name: str, issue_description: str, scheduled_time: datetime.datetime) -> None:
        """Add a new service request."""
        new_request = ServiceRequest(customer_name, issue_description, scheduled_time)
        self.requests.append(new_request)
        print(f"Added request: {new_request}")

    def get_requests(self) -> List[ServiceRequest]:
        """Retrieve all service requests."""
        return self.requests

    def update_request_status(self, request_index: int, new_status: str) -> None:
        """Update the status of a service request."""
        try:
            self.requests[request_index].status = new_status
            print(f"Updated request status to '{new_status}': {self.requests[request_index]}")
        except IndexError:
            print("Error: Request index out of range.")

    def save_requests_to_file(self, filename: str) -> None:
        """Save service requests to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([request.__dict__ for request in self.requests], file, default=str)
            print(f"Requests saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_requests_from_file(self, filename: str) -> None:
        """Load service requests from a JSON file."""
        try:
            with open(filename, 'r') as file:
                requests_data = json.load(file)
                self.requests = [ServiceRequest(**data) for data in requests_data]
            print(f"Requests loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to run the service request manager."""
    manager = ServiceRequestManager()

    # Example usage
    manager.add_request("John Doe", "Laptop won't start", datetime.datetime(2023, 10, 15, 10, 0))
    manager.add_request("Jane Smith", "Screen flickering", datetime.datetime(2023, 10, 16, 14, 30))

    print("\nCurrent Service Requests:")
    for request in manager.get_requests():
        print(request)

    # Update a request status
    manager.update_request_status(0, "Completed")

    # Save requests to a file
    manager.save_requests_to_file("service_requests.json")

    # Load requests from a file
    manager.load_requests_from_file("service_requests.json")

if __name__ == "__main__":
    main()
```
