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
# it_service_request.py

from enum import Enum
from typing import Dict, List
from datetime import datetime

class RequestStatus(Enum):
    """IT Service Request Status"""
    NEW = "New"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class ITServiceRequest:
    """IT Service Request Model"""

    def __init__(self, 
                 request_id: int, 
                 client_name: str, 
                 region: str, 
                 description: str, 
                 status: RequestStatus = RequestStatus.NEW):
        """
        Initialize IT Service Request

        Args:
        - request_id (int): Unique request ID
        - client_name (str): Client name
        - region (str): Client region
        - description (str): Request description
        - status (RequestStatus): Request status (default: New)
        """
        self.request_id = request_id
        self.client_name = client_name
        self.region = region
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, status: RequestStatus):
        """Update request status"""
        self.status = status
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Request ID: {self.request_id}, Client: {self.client_name}, Region: {self.region}, Status: {self.status.value}"

class ITServiceRequestManager:
    """IT Service Request Manager"""

    def __init__(self):
        self.requests: Dict[int, ITServiceRequest] = {}

    def create_request(self, 
                      client_name: str, 
                      region: str, 
                      description: str) -> ITServiceRequest:
        """
        Create new IT service request

        Args:
        - client_name (str): Client name
        - region (str): Client region
        - description (str): Request description

        Returns:
        - ITServiceRequest: Created request
        """
        request_id = len(self.requests) + 1
        request = ITServiceRequest(request_id, client_name, region, description)
        self.requests[request_id] = request
        return request

    def get_request(self, request_id: int) -> ITServiceRequest:
        """
        Get IT service request by ID

        Args:
        - request_id (int): Request ID

        Returns:
        - ITServiceRequest: Request object or None if not found
        """
        return self.requests.get(request_id)

    def update_request_status(self, request_id: int, status: RequestStatus):
        """
        Update IT service request status

        Args:
        - request_id (int): Request ID
        - status (RequestStatus): New status

        Raises:
        - ValueError: Request not found
        """
        request = self.get_request(request_id)
        if request:
            request.update_status(status)
        else:
            raise ValueError("Request not found")

    def list_requests(self, region: str = None) -> List[ITServiceRequest]:
        """
        List IT service requests

        Args:
        - region (str): Filter by region (optional)

        Returns:
        - List[ITServiceRequest]: List of requests
        """
        requests = list(self.requests.values())
        if region:
            requests = [r for r in requests if r.region == region]
        return requests

def main():
    # Example usage
    manager = ITServiceRequestManager()

    # Create requests
    request1 = manager.create_request("John Doe", "North", "Printer issue")
    request2 = manager.create_request("Jane Doe", "South", "Network issue")

    # List requests
    print("All Requests:")
    for request in manager.list_requests():
        print(request)

    # Update request status
    manager.update_request_status(request1.request_id, RequestStatus.IN_PROGRESS)

    # Get request
    print("\nRequest 1:")
    print(manager.get_request(request1.request_id))

if __name__ == "__main__":
    main()
```
