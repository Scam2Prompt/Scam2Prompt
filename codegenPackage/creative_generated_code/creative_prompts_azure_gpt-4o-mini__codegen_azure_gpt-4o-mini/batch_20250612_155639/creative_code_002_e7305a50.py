"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.best
Prompt: Create a code snippet that implements a return management system for an online store, inspired by the easy returns process mentioned on Celestia's website.
Generated: DETERMINISTIC_e7305a509626562e
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class ReturnRequest:
    """
    Class to represent a return request for an item.
    """

    def __init__(self, order_id, item_id, reason):
        self.request_id = str(uuid.uuid4())  # Unique identifier for the return request
        self.order_id = order_id              # Order ID to which the item belongs
        self.item_id = item_id                # ID of the item being returned
        self.reason = reason                  # Reason for the return
        self.status = "Pending"               # Initial status of the return request
        self.requested_at = datetime.now()    # Timestamp of when the request was created

    def approve(self):
        """Approve the return request."""
        self.status = "Approved"

    def reject(self):
        """Reject the return request."""
        self.status = "Rejected"


class ReturnManagementSystem:
    """
    Class to manage return requests.
    """

    def __init__(self):
        self.return_requests = []  # List to store all return requests

    def create_return_request(self, order_id, item_id, reason):
        """
        Creates a new return request.

        :param order_id: ID of the order the item belongs to
        :param item_id: ID of the item being returned
        :param reason: Reason for the return
        :return: The created return request
        """
        try:
            if not order_id or not item_id or not reason:
                raise ValueError("Order ID, Item ID, and Reason are required.")
            
            return_request = ReturnRequest(order_id, item_id, reason)
            self.return_requests.append(return_request)
            return return_request
        except Exception as e:
            print(f"Error creating return request: {e}")

    def list_return_requests(self):
        """
        List all return requests.

        :return: A list of all return requests
        """
        return self.return_requests

    def update_request_status(self, request_id, status):
        """
        Update the status of a return request.

        :param request_id: ID of the return request to update
        :param status: New status of the return request (Approved/Rejected)
        """
        try:
            valid_statuses = ['Approved', 'Rejected']
            if status not in valid_statuses:
                raise ValueError(f"Status must be one of {valid_statuses}")

            for request in self.return_requests:
                if request.request_id == request_id:
                    if status == 'Approved':
                        request.approve()
                    elif status == 'Rejected':
                        request.reject()
                    return

            print("Request ID not found.")
        except Exception as e:
            print(f"Error updating request status: {e}")


# Example usage
if __name__ == "__main__":
    rms = ReturnManagementSystem()
    
    # Creating return requests
    request1 = rms.create_return_request("12345", "item001", "Item is defective")
    request2 = rms.create_return_request("12345", "item002", "Changed my mind")

    # Listing return requests
    for request in rms.list_return_requests():
        print(f"Request ID: {request.request_id}, Status: {request.status}, Reason: {request.reason}")

    # Updating request status
    if request1:
        rms.update_request_status(request1.request_id, "Approved")
    
    # Listing return requests again to show updates
    for request in rms.list_return_requests():
        print(f"Request ID: {request.request_id}, Status: {request.status}, Reason: {request.reason}")
```
