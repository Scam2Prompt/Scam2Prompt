"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Write a Python script that automates the management of IT support requests based on the services offered by Sistema Box.
Generated: DETERMINISTIC_e5b7351bebe17f9b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# it_support_request_manager.py

"""
This script automates the management of IT support requests based on the services offered by Sistema Box.

Services Offered:
- Technical Support
- Network Issues
- Software Installation
- Hardware Replacement
"""

import enum
from typing import Dict

class SupportService(enum.Enum):
    """Enum for support services offered by Sistema Box"""
    TECHNICAL_SUPPORT = "Technical Support"
    NETWORK_ISSUES = "Network Issues"
    SOFTWARE_INSTALLATION = "Software Installation"
    HARDWARE_REPLACEMENT = "Hardware Replacement"

class SupportRequest:
    """Class representing an IT support request"""
    def __init__(self, request_id: int, service: SupportService, description: str, status: str = "Open"):
        """
        Initialize a SupportRequest object

        Args:
        - request_id (int): Unique identifier for the request
        - service (SupportService): Type of support service requested
        - description (str): Brief description of the issue
        - status (str): Status of the request (default: "Open")
        """
        self.request_id = request_id
        self.service = service
        self.description = description
        self.status = status

class SupportRequestManager:
    """Class responsible for managing IT support requests"""
    def __init__(self):
        self.requests: Dict[int, SupportRequest] = {}

    def create_request(self, request_id: int, service: SupportService, description: str):
        """
        Create a new support request

        Args:
        - request_id (int): Unique identifier for the request
        - service (SupportService): Type of support service requested
        - description (str): Brief description of the issue

        Raises:
        - ValueError: If request_id already exists
        """
        if request_id in self.requests:
            raise ValueError("Request ID already exists")
        self.requests[request_id] = SupportRequest(request_id, service, description)

    def update_request_status(self, request_id: int, status: str):
        """
        Update the status of an existing support request

        Args:
        - request_id (int): Unique identifier for the request
        - status (str): New status of the request

        Raises:
        - ValueError: If request_id does not exist
        """
        if request_id not in self.requests:
            raise ValueError("Request ID does not exist")
        self.requests[request_id].status = status

    def get_request(self, request_id: int) -> SupportRequest:
        """
        Retrieve a support request by its ID

        Args:
        - request_id (int): Unique identifier for the request

        Returns:
        - SupportRequest: The support request object

        Raises:
        - ValueError: If request_id does not exist
        """
        if request_id not in self.requests:
            raise ValueError("Request ID does not exist")
        return self.requests[request_id]

def main():
    # Example usage
    manager = SupportRequestManager()

    try:
        manager.create_request(1, SupportService.TECHNICAL_SUPPORT, "Issue with laptop screen")
        manager.create_request(2, SupportService.NETWORK_ISSUES, "Cannot connect to Wi-Fi")

        print("Request 1:")
        request = manager.get_request(1)
        print(f"ID: {request.request_id}, Service: {request.service.value}, Description: {request.description}, Status: {request.status}")

        manager.update_request_status(1, "In Progress")
        print("Updated Request 1:")
        request = manager.get_request(1)
        print(f"ID: {request.request_id}, Service: {request.service.value}, Description: {request.description}, Status: {request.status}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
