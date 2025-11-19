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
# Return Management System for an Online Store
# Language: Python

import datetime

class Return:
    """
    Class representing a return request.
    """
    def __init__(self, order_id, product_id, reason, customer_id):
        self.return_id = self.generate_unique_id()
        self.order_id = order_id
        self.product_id = product_id
        self.reason = reason
        self.customer_id = customer_id
        self.request_date = datetime.datetime.now()
        self.status = "Pending"  # Initial status set to 'Pending'

    @staticmethod
    def generate_unique_id():
        """
        Generate a unique return ID using timestamp.
        """
        return f"RET-{int(datetime.datetime.now().timestamp())}"

    def approve_return(self):
        """
        Approve the return request.
        """
        self.status = "Approved"
        self.approval_date = datetime.datetime.now()

    def reject_return(self, rejection_reason):
        """
        Reject the return request.
        """
        self.status = "Rejected"
        self.rejection_reason = rejection_reason
        self.rejection_date = datetime.datetime.now()

    def __str__(self):
        """
        Convert the return request object into a user-friendly string.
        """
        return (f"Return ID: {self.return_id}, Order ID: {self.order_id}, Product ID: {self.product_id}, "
                f"Reason: {self.reason}, Status: {self.status}, Request Date: {self.request_date}")


class ReturnManagementSystem:
    """
    Class representing the Return Management System.
    """
    def __init__(self):
        self.returns = {}  # Dictionary to store return requests with return_id as the key

    def create_return_request(self, order_id, product_id, reason, customer_id):
        """
        Create a new return request.
        """
        try:
            new_return = Return(order_id, product_id, reason, customer_id)
            self.returns[new_return.return_id] = new_return
            print(f"Return request created successfully. Return ID: {new_return.return_id}")
            return new_return
        except Exception as e:
            print(f"Error creating return request: {e}")

    def process_return(self, return_id, action, rejection_reason=None):
        """
        Process a return request by approving or rejecting it.
        """
        try:
            if return_id not in self.returns:
                raise ValueError("Return ID not found.")

            return_request = self.returns[return_id]
            if action == "approve":
                return_request.approve_return()
                print(f"Return ID {return_id} approved successfully.")
            elif action == "reject":
                if not rejection_reason:
                    raise ValueError("Rejection reason is required.")
                return_request.reject_return(rejection_reason)
                print(f"Return ID {return_id} rejected successfully.")
            else:
                raise ValueError("Invalid action. Use 'approve' or 'reject'.")
        except Exception as e:
            print(f"Error processing return: {e}")

    def view_return_status(self, return_id):
        """
        Retrieve and display the status of a return request.
        """
        try:
            if return_id not in self.returns:
                raise ValueError("Return ID not found.")
            print(self.returns[return_id])
        except Exception as e:
            print(f"Error viewing return status: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize the return management system
    rms = ReturnManagementSystem()

    # Create a new return request
    return_request = rms.create_return_request(order_id="ORD1234", product_id="PRD5678", reason="Defective item", customer_id="CUST9999")

    # View the status of the return request
    if return_request:
        rms.view_return_status(return_request.return_id)

    # Approve the return request
    if return_request:
        rms.process_return(return_id=return_request.return_id, action="approve")

    # View the updated status of the return request
    if return_request:
        rms.view_return_status(return_request.return_id)
```
