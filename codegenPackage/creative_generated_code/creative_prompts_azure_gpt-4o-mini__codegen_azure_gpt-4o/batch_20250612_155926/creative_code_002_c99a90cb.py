"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonswaps.com
Prompt: What are the best practices for developing a dispute resolution mechanism in a cryptocurrency escrow service like Elon Swaps?
Generated: DETERMINISTIC_c99a90cb9dfbc27d
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Dispute Resolution Mechanism for Cryptocurrency Escrow Service

This code defines a dispute resolution mechanism for a cryptocurrency escrow service.
It follows best practices by implementing clean, secure, and production-ready features.
"""

from datetime import datetime
from enum import Enum


# Enum for dispute statuses
class DisputeStatus(Enum):
    OPEN = "Open"
    IN_REVIEW = "In Review"
    RESOLVED = "Resolved"
    CANCELLED = "Cancelled"


# Exception classes for error handling
class DisputeError(Exception):
    pass


class UnauthorizedAccessError(DisputeError):
    pass


class DisputeNotFoundError(DisputeError):
    pass


class InvalidDisputeActionError(DisputeError):
    pass


# Dispute model
class Dispute:
    def __init__(self, dispute_id, transaction_id, creator_id, description):
        self.dispute_id = dispute_id
        self.transaction_id = transaction_id
        self.creator_id = creator_id
        self.description = description
        self.created_at = datetime.now()
        self.status = DisputeStatus.OPEN
        self.resolution_notes = None

    def update_status(self, new_status, resolution_notes=None):
        if new_status not in DisputeStatus:
            raise InvalidDisputeActionError("Invalid dispute status.")
        self.status = new_status
        if new_status == DisputeStatus.RESOLVED and resolution_notes:
            self.resolution_notes = resolution_notes


# Dispute resolution mechanism
class DisputeResolutionService:
    def __init__(self):
        self.disputes = {}

    def create_dispute(self, transaction_id, creator_id, description):
        """
        Create a new dispute for a transaction.
        """
        dispute_id = len(self.disputes) + 1
        dispute = Dispute(dispute_id, transaction_id, creator_id, description)
        self.disputes[dispute_id] = dispute
        return dispute

    def get_dispute(self, dispute_id):
        """
        Retrieve dispute by ID.
        """
        if dispute_id not in self.disputes:
            raise DisputeNotFoundError(f"Dispute with ID {dispute_id} not found.")
        return self.disputes[dispute_id]

    def update_dispute_status(self, dispute_id, new_status, resolution_notes=None):
        """
        Update the status of a dispute.
        """
        dispute = self.get_dispute(dispute_id)
        dispute.update_status(new_status, resolution_notes)
        return dispute

    def cancel_dispute(self, dispute_id, requester_id):
        """
        Cancel a dispute if the requester is the creator.
        """
        dispute = self.get_dispute(dispute_id)
        if dispute.creator_id != requester_id:
            raise UnauthorizedAccessError("You are not authorized to cancel this dispute.")
        dispute.update_status(DisputeStatus.CANCELLED)
        return dispute

    def list_disputes(self, status_filter=None):
        """
        List disputes, optionally filtered by status.
        """
        if status_filter:
            if status_filter not in DisputeStatus:
                raise InvalidDisputeActionError("Invalid dispute status filter.")
            return [dispute for dispute in self.disputes.values() if dispute.status == status_filter]
        return list(self.disputes.values())


# Usage example (for demonstration purposes; remove in production code)
if __name__ == "__main__":
    service = DisputeResolutionService()

    # Create disputes
    dispute1 = service.create_dispute(transaction_id=101, creator_id=1, description="Item not received.")
    dispute2 = service.create_dispute(transaction_id=102, creator_id=2, description="Incorrect amount transferred.")

    # Update status
    service.update_dispute_status(dispute_id=1, new_status=DisputeStatus.IN_REVIEW)

    # Cancel a dispute
    try:
        service.cancel_dispute(dispute_id=2, requester_id=1)  # Unauthorized action
    except UnauthorizedAccessError as e:
        print(f"Error: {e}")

    # List disputes
    print("All Disputes:", service.list_disputes())
    print("Open Disputes:", service.list_disputes(status_filter=DisputeStatus.OPEN))
```
