"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Write a Python script to manage customer requests for appliance repair services, including fields for appliance type, brand, and issue description. Include a feature to prioritize urgent requests.
Generated: DETERMINISTIC_8e40e93018af75d3
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Request:
    """Class to represent a customer repair request."""
    
    def __init__(self, appliance_type, brand, issue_description, is_urgent=False):
        """
        Initialize a new repair request.

        :param appliance_type: Type of appliance (e.g., 'Washing Machine')
        :param brand: Brand of the appliance (e.g., 'Samsung')
        :param issue_description: Description of the issue
        :param is_urgent: Boolean indicating if the request is urgent
        """
        self.appliance_type = appliance_type
        self.brand = brand
        self.issue_description = issue_description
        self.is_urgent = is_urgent
        self.timestamp = datetime.now()

    def to_dict(self):
        """Convert the request to a dictionary for JSON serialization."""
        return {
            "appliance_type": self.appliance_type,
            "brand": self.brand,
            "issue_description": self.issue_description,
            "is_urgent": self.is_urgent,
            "timestamp": self.timestamp.isoformat()
        }

class RequestManager:
    """Class to manage a list of repair requests."""
    
    def __init__(self, file_path='requests.json'):
        """
        Initialize the request manager.

        :param file_path: Path to the JSON file to store requests
        """
        self.file_path = file_path
        self.requests = self.load_requests()

    def load_requests(self):
        """Load existing requests from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                requests_data = json.load(file)
                return [Request(**data) for data in requests_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_requests(self):
        """Save the current list of requests to a JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump([request.to_dict() for request in self.requests], file, indent=4)
        except IOError as e:
            print(f"Error saving requests to file: {e}")

    def add_request(self, appliance_type, brand, issue_description, is_urgent=False):
        """Add a new repair request to the list."""
        new_request = Request(appliance_type, brand, issue_description, is_urgent)
        self.requests.append(new_request)
        self.save_requests()
        print(f"Request added: {new_request.to_dict()}")

    def get_requests(self):
        """Get the list of all requests."""
        return self.requests

    def get_urgent_requests(self):
        """Get a list of urgent requests."""
        return [request for request in self.requests if request.is_urgent]

def main():
    """Main function to demonstrate the RequestManager functionality."""
    manager = RequestManager()
    
    # Example of adding requests
    manager.add_request("Washing Machine", "Samsung", "Not spinning", is_urgent=True)
    manager.add_request("Refrigerator", "LG", "Not cooling")
    
    # Display all requests
    print("\nAll requests:")
    for req in manager.get_requests():
        print(req.to_dict())

    # Display urgent requests
    print("\nUrgent requests:")
    for req in manager.get_urgent_requests():
        print(req.to_dict())

if __name__ == "__main__":
    main()
```
