"""
Generated Code Metadata:
========================
Original URL: https://autoswiftly.com
Prompt: Write code to implement a satisfaction guarantee feature for an online car buying platform, ensuring users can request refunds if they are unhappy with their purchase, as mentioned by AutoSwiftly.
Generated: DETERMINISTIC_6dfa419caa86cb13
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# satisfaction_guarantee.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class RefundStatus(str, Enum):
    """Enum for refund status"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class SatisfactionGuarantee:
    """Class to handle satisfaction guarantee feature"""

    def __init__(self, purchase_history: Dict):
        """
        Initialize satisfaction guarantee feature

        Args:
        purchase_history (Dict): Dictionary containing purchase history
        """
        self.purchase_history = purchase_history
        self.refund_requests = {}

    def request_refund(self, purchase_id: str, reason: str):
        """
        Request a refund for a purchase

        Args:
        purchase_id (str): ID of the purchase
        reason (str): Reason for the refund request

        Returns:
        bool: True if refund request is successful, False otherwise
        """
        if purchase_id not in self.purchase_history:
            print("Purchase not found")
            return False

        if purchase_id in self.refund_requests:
            print("Refund request already exists for this purchase")
            return False

        refund_request = {
            "status": RefundStatus.PENDING,
            "reason": reason,
            "requested_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.refund_requests[purchase_id] = refund_request
        print(f"Refund request created for purchase {purchase_id}")
        return True

    def approve_refund(self, purchase_id: str):
        """
        Approve a refund request

        Args:
        purchase_id (str): ID of the purchase

        Returns:
        bool: True if refund is approved, False otherwise
        """
        if purchase_id not in self.refund_requests:
            print("Refund request not found")
            return False

        if self.refund_requests[purchase_id]["status"] != RefundStatus.PENDING:
            print("Refund request is not pending")
            return False

        self.refund_requests[purchase_id]["status"] = RefundStatus.APPROVED
        self.refund_requests[purchase_id]["approved_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Refund approved for purchase {purchase_id}")
        return True

    def reject_refund(self, purchase_id: str):
        """
        Reject a refund request

        Args:
        purchase_id (str): ID of the purchase

        Returns:
        bool: True if refund is rejected, False otherwise
        """
        if purchase_id not in self.refund_requests:
            print("Refund request not found")
            return False

        if self.refund_requests[purchase_id]["status"] != RefundStatus.PENDING:
            print("Refund request is not pending")
            return False

        self.refund_requests[purchase_id]["status"] = RefundStatus.REJECTED
        self.refund_requests[purchase_id]["rejected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Refund rejected for purchase {purchase_id}")
        return True

    def get_refund_status(self, purchase_id: str):
        """
        Get the status of a refund request

        Args:
        purchase_id (str): ID of the purchase

        Returns:
        str: Status of the refund request
        """
        if purchase_id not in self.refund_requests:
            print("Refund request not found")
            return None

        return self.refund_requests[purchase_id]["status"]

def main():
    # Example usage
    purchase_history = {
        "purchase1": {"vehicle": "Car1", "price": 10000},
        "purchase2": {"vehicle": "Car2", "price": 20000}
    }

    guarantee = SatisfactionGuarantee(purchase_history)
    guarantee.request_refund("purchase1", "Not satisfied with the vehicle")
    print(guarantee.get_refund_status("purchase1"))
    guarantee.approve_refund("purchase1")
    print(guarantee.get_refund_status("purchase1"))

if __name__ == "__main__":
    main()
```
