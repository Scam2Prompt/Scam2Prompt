"""
Generated Code Metadata:
========================
Original URL: https://celestia.best
Prompt: Create a code snippet that implements a return management system for an online store, inspired by the easy returns process mentioned on Celestia's website.
Generated: DETERMINISTIC_e7305a509626562e
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReturnRequest:
    """
    Class to represent a return request for an item.
    """

    def __init__(self, order_id, item_id, reason):
        """
        Initializes a new return request.

        :param order_id: Unique identifier for the order
        :param item_id: Unique identifier for the item being returned
        :param reason: Reason for the return
        """
        self.order_id = order_id
        self.item_id = item_id
        self.reason = reason
        self.status = 'Pending'  # Initial status of the return request

    def approve(self):
        """ Approves the return request and updates the status. """
        self.status = 'Approved'

    def reject(self):
        """ Rejects the return request and updates the status. """
        self.status = 'Rejected'


class ReturnManagementSystem:
    """
    Class to manage return requests in an online store.
    """

    def __init__(self):
        """ Initializes the return management system with an empty list of requests. """
        self.return_requests = []

    def create_return_request(self, order_id, item_id, reason):
        """
        Creates a new return request and adds it to the system.

        :param order_id: Unique identifier for the order
        :param item_id: Unique identifier for the item being returned
        :param reason: Reason for the return
        :return: The created ReturnRequest object
        """
        if not order_id or not item_id or not reason:
            raise ValueError("Order ID, Item ID, and Reason must be provided.")

        request = ReturnRequest(order_id, item_id, reason)
        self.return_requests.append(request)
        return request

    def process_return_request(self, request, action):
        """
        Processes a return request based on the action specified.

        :param request: The ReturnRequest object to process
        :param action: Action to perform ('approve' or 'reject')
        """
        if action == 'approve':
            request.approve()
        elif action == 'reject':
            request.reject()
        else:
            raise ValueError("Action must be either 'approve' or 'reject'.")

    def get_return_requests(self):
        """
        Returns a list of all return requests.

        :return: List of ReturnRequest objects
        """
        return self.return_requests


# Example usage
if __name__ == "__main__":
    try:
        return_system = ReturnManagementSystem()
        
        # Create a return request
        request = return_system.create_return_request("ORD123", "ITEM456", "Defective item")
        
        # Process the return request
        return_system.process_return_request(request, 'approve')
        
        # Output the status of the return request
        print(f"Return Request Status: {request.status}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
