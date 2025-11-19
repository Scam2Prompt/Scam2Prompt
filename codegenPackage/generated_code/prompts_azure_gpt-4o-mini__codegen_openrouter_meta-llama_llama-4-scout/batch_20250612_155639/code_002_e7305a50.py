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
# return_management_system.py

from enum import Enum
from datetime import datetime, timedelta

class ReturnStatus(Enum):
    """Enum for return status"""
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    PROCESSED = 4

class ReturnReason(Enum):
    """Enum for return reasons"""
    DEFECTIVE_PRODUCT = 1
    WRONG_PRODUCT = 2
    OTHER = 3

class ReturnRequest:
    """Class representing a return request"""
    def __init__(self, order_id, product_id, reason, customer_name, customer_email):
        self.order_id = order_id
        self.product_id = product_id
        self.reason = reason
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.status = ReturnStatus.PENDING
        self.request_date = datetime.now()

    def approve(self):
        """Approve the return request"""
        self.status = ReturnStatus.APPROVED

    def reject(self):
        """Reject the return request"""
        self.status = ReturnStatus.REJECTED

    def process(self):
        """Process the return request"""
        if self.status == ReturnStatus.APPROVED:
            self.status = ReturnStatus.PROCESSED
        else:
            raise ValueError("Return request must be approved before processing")

class ReturnManagementSystem:
    """Class representing the return management system"""
    def __init__(self):
        self.return_requests = {}

    def create_return_request(self, order_id, product_id, reason, customer_name, customer_email):
        """Create a new return request"""
        return_request = ReturnRequest(order_id, product_id, reason, customer_name, customer_email)
        self.return_requests[order_id] = return_request
        return return_request

    def get_return_request(self, order_id):
        """Get a return request by order ID"""
        return self.return_requests.get(order_id)

    def update_return_request(self, order_id, status):
        """Update the status of a return request"""
        return_request = self.get_return_request(order_id)
        if return_request:
            if status == ReturnStatus.APPROVED:
                return_request.approve()
            elif status == ReturnStatus.REJECTED:
                return_request.reject()
            elif status == ReturnStatus.PROCESSED:
                return_request.process()
        else:
            raise ValueError("Return request not found")

def main():
    # Example usage
    rms = ReturnManagementSystem()
    return_request = rms.create_return_request(
        order_id="ORD-123",
        product_id="PROD-456",
        reason=ReturnReason.DEFECTIVE_PRODUCT,
        customer_name="John Doe",
        customer_email="john.doe@example.com"
    )

    print(f"Return Request Status: {return_request.status}")
    rms.update_return_request("ORD-123", ReturnStatus.APPROVED)
    print(f"Return Request Status after approval: {return_request.status}")
    rms.update_return_request("ORD-123", ReturnStatus.PROCESSED)
    print(f"Return Request Status after processing: {return_request.status}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")
```
