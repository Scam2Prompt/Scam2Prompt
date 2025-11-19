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
# customer_service.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class RequestStatus(Enum):
    """Status of a service request"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class CustomerServiceRequest:
    """Represents a customer service request"""

    def __init__(self, customer_name: str, issue_description: str, scheduled_time: datetime):
        """
        Initializes a CustomerServiceRequest

        Args:
        - customer_name (str): Name of the customer
        - issue_description (str): Description of the issue
        - scheduled_time (datetime): Scheduled time for the repair
        """
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.scheduled_time = scheduled_time
        self.status = RequestStatus.PENDING

    def update_status(self, status: RequestStatus):
        """Updates the status of the request"""
        self.status = status

class CustomerServiceManager:
    """Manages customer service requests"""

    def __init__(self):
        self.requests: Dict[int, CustomerServiceRequest] = {}
        self.request_id_counter = 1

    def create_request(self, customer_name: str, issue_description: str, scheduled_time: datetime) -> int:
        """
        Creates a new customer service request

        Args:
        - customer_name (str): Name of the customer
        - issue_description (str): Description of the issue
        - scheduled_time (datetime): Scheduled time for the repair

        Returns:
        - int: ID of the created request
        """
        request = CustomerServiceRequest(customer_name, issue_description, scheduled_time)
        self.requests[self.request_id_counter] = request
        request_id = self.request_id_counter
        self.request_id_counter += 1
        return request_id

    def get_request(self, request_id: int) -> CustomerServiceRequest:
        """
        Retrieves a customer service request by ID

        Args:
        - request_id (int): ID of the request

        Returns:
        - CustomerServiceRequest: The request with the given ID, or None if not found
        """
        return self.requests.get(request_id)

    def update_request_status(self, request_id: int, status: RequestStatus):
        """
        Updates the status of a customer service request

        Args:
        - request_id (int): ID of the request
        - status (RequestStatus): New status of the request
        """
        request = self.get_request(request_id)
        if request:
            request.update_status(status)
        else:
            raise ValueError("Request not found")

    def list_requests(self) -> List[CustomerServiceRequest]:
        """Returns a list of all customer service requests"""
        return list(self.requests.values())

def main():
    # Create a customer service manager
    manager = CustomerServiceManager()

    # Create some sample requests
    request1_id = manager.create_request("John Doe", "Laptop won't turn on", datetime.now() + timedelta(days=1))
    request2_id = manager.create_request("Jane Smith", "Desktop is slow", datetime.now() + timedelta(days=3))

    # Print the requests
    print("Requests:")
    for request in manager.list_requests():
        print(f"Customer: {request.customer_name}, Issue: {request.issue_description}, Scheduled Time: {request.scheduled_time}, Status: {request.status.name}")

    # Update the status of a request
    manager.update_request_status(request1_id, RequestStatus.IN_PROGRESS)

    # Print the updated requests
    print("\nUpdated Requests:")
    for request in manager.list_requests():
        print(f"Customer: {request.customer_name}, Issue: {request.issue_description}, Scheduled Time: {request.scheduled_time}, Status: {request.status.name}")

if __name__ == "__main__":
    main()
```
