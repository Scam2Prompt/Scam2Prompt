"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Write a Python script to simulate the admin approval process for star purchases and TON payments as described on the StarsBot website.
Generated: DETERMINISTIC_cda1aa1a6b721302
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict


class PurchaseRequest:
    """
    Represents a purchase request for stars or TON payments.
    """
    def __init__(self, user_id: int, item: str, amount: float):
        self.user_id = user_id  # Unique ID of the user making the request
        self.item = item  # Item being purchased (e.g., "stars" or "TON")
        self.amount = amount  # Amount being purchased
        self.status = 'Pending'  # Status of the request (Pending, Approved, Rejected)
        self.timestamp = time.time()  # Timestamp when the request was created

    def __repr__(self):
        return (f"PurchaseRequest(user_id={self.user_id}, item={self.item}, "
                f"amount={self.amount}, status={self.status})")


class AdminApprovalSystem:
    """
    Simulates an admin approval process for purchase requests.
    """

    def __init__(self):
        self.requests: List[PurchaseRequest] = []  # List to store purchase requests

    def submit_request(self, user_id: int, item: str, amount: float):
        """
        Submit a new purchase request.
        :param user_id: ID of the user making the request
        :param item: Item being purchased
        :param amount: Amount being purchased
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        new_request = PurchaseRequest(user_id, item, amount)
        self.requests.append(new_request)
        print(f"Request submitted: {new_request}")

    def list_pending_requests(self) -> List[PurchaseRequest]:
        """
        List all pending purchase requests.
        :return: List of pending requests
        """
        return [req for req in self.requests if req.status == 'Pending']

    def approve_request(self, request_index: int):
        """
        Approve a specific purchase request by index.
        :param request_index: Index of the request in the list of pending requests
        """
        try:
            pending_requests = self.list_pending_requests()
            request_to_approve = pending_requests[request_index]
            request_to_approve.status = 'Approved'
            print(f"Request approved: {request_to_approve}")
        except IndexError:
            print("Invalid request index. No such pending request.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def reject_request(self, request_index: int):
        """
        Reject a specific purchase request by index.
        :param request_index: Index of the request in the list of pending requests
        """
        try:
            pending_requests = self.list_pending_requests()
            request_to_reject = pending_requests[request_index]
            request_to_reject.status = 'Rejected'
            print(f"Request rejected: {request_to_reject}")
        except IndexError:
            print("Invalid request index. No such pending request.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def generate_report(self) -> Dict[str, int]:
        """
        Generate a summary report of all requests by status.
        :return: Dictionary summarizing the number of requests in each status
        """
        report = {'Pending': 0, 'Approved': 0, 'Rejected': 0}
        for req in self.requests:
            if req.status in report:
                report[req.status] += 1
        return report


if __name__ == "__main__":
    # Example usage of AdminApprovalSystem
    approval_system = AdminApprovalSystem()

    # Simulate users submitting requests
    approval_system.submit_request(user_id=1, item="stars", amount=50)
    approval_system.submit_request(user_id=2, item="TON", amount=100)
    approval_system.submit_request(user_id=3, item="stars", amount=200)

    # List all pending requests
    print("\nPending Requests:")
    for i, req in enumerate(approval_system.list_pending_requests()):
        print(f"{i}: {req}")

    # Approve the first request
    approval_system.approve_request(0)

    # Reject the second request
    approval_system.reject_request(1)

    # Generate and display a summary report
    print("\nSummary Report:")
    report = approval_system.generate_report()
    for status, count in report.items():
        print(f"{status}: {count}")
```
