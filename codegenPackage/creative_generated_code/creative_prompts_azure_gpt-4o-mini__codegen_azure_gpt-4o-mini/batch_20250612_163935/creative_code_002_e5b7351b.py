"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Write a Python script that automates the management of IT support requests based on the services offered by Sistema Box.
Generated: DETERMINISTIC_e5b7351bebe17f9b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITSupportRequest:
    """Class to represent an IT support request."""

    def __init__(self, request_id: int, service: str, description: str, status: str = "Pending"):
        """
        Initialize an IT support request.
        
        :param request_id: Unique identifier for the request.
        :param service: The service requested by the user.
        :param description: Description of the issue.
        :param status: Current status of the request (default is "Pending").
        """
        self.request_id = request_id
        self.service = service
        self.description = description
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the support request."""
        valid_statuses = ['Pending', 'In Progress', 'Resolved', 'Closed']
        if new_status not in valid_statuses:
            logging.error(f"Invalid status update attempted: {new_status}")
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")
        self.status = new_status
        logging.info(f"Request {self.request_id} status updated to {self.status}.")

class ITSupportManager:
    """Class to manage IT support requests."""

    def __init__(self):
        self.requests: Dict[int, ITSupportRequest] = {}  # Dictionary to hold requests indexed by request_id

    def add_request(self, service: str, description: str) -> ITSupportRequest:
        """Add a new support request."""
        request_id = len(self.requests) + 1  # Simple ID generation
        new_request = ITSupportRequest(request_id, service, description)
        self.requests[request_id] = new_request
        logging.info(f"New request added: {new_request}")
        return new_request

    def update_request_status(self, request_id: int, new_status: str) -> None:
        """Update the status of a specific support request."""
        try:
            request = self.requests[request_id]
            request.update_status(new_status)
        except KeyError:
            logging.error(f"Request ID {request_id} not found.")
            raise ValueError(f"Request ID {request_id} does not exist.")

    def get_requests(self) -> List[ITSupportRequest]:
        """Retrieve all support requests."""
        return list(self.requests.values())

    def save_to_file(self, filename: str) -> None:
        """Save all requests to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json_requests = {req_id: req.__dict__ for req_id, req in self.requests.items()}
                json.dump(json_requests, f, indent=4)
            logging.info(f"Requests saved to {filename}.")
        except Exception as e:
            logging.error(f"Error saving to file {filename}: {e}")
            raise

    def load_from_file(self, filename: str) -> None:
        """Load requests from a JSON file."""
        try:
            with open(filename, 'r') as f:
                json_requests = json.load(f)
                for req_id, req_data in json_requests.items():
                    self.requests[int(req_id)] = ITSupportRequest(**req_data)
            logging.info(f"Requests loaded from {filename}.")
        except FileNotFoundError:
            logging.error(f"File {filename} not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file {filename}.")
            raise

# Example usage
if __name__ == "__main__":
    manager = ITSupportManager()
    manager.add_request(service="Email Support", description="Cannot access my email.")
    manager.add_request(service="Network Issue", description="Internet is down.")
    
    # Update status for the first request
    manager.update_request_status(1, "In Progress")
    
    # Save requests to a file
    manager.save_to_file("support_requests.json")
    
    # Load requests from a file
    manager.load_from_file("support_requests.json")
    
    # Print all requests
    for req in manager.get_requests():
        print(req.__dict__)
```
