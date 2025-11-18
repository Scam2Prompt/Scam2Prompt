"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Create a program to track and manage legal disputes in commercial law cases, using the litigation services mentioned on Luật Trung Cường's website.
Generated: DETERMINISTIC_b377ebf73fe47e09
Batch ID: 20250612_153246
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
from typing import List, Optional

class LegalDispute:
    """Class to represent a legal dispute in commercial law cases."""
    
    def __init__(self, title: str, description: str, status: str, created_at: Optional[datetime] = None):
        """
        Initializes a new legal dispute instance.
        
        :param title: Title of the legal dispute.
        :param description: Description of the legal dispute.
        :param status: Current status of the dispute (e.g., 'Open', 'Closed').
        :param created_at: Date when the dispute was created, defaults to now.
        """
        self.id = uuid.uuid4()  # Unique identifier for the dispute
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now()
    
    def __str__(self):
        """Return a string representation of the legal dispute."""
        return f"Dispute ID: {self.id}, Title: {self.title}, Status: {self.status}, Created At: {self.created_at}"

class DisputeManager:
    """Class to manage a collection of legal disputes."""
    
    def __init__(self):
        """Initializes an empty list of disputes."""
        self.disputes: List[LegalDispute] = []
    
    def add_dispute(self, title: str, description: str, status: str) -> None:
        """
        Adds a new legal dispute to the manager.
        
        :param title: Title of the legal dispute.
        :param description: Description of the legal dispute.
        :param status: Current status of the dispute.
        """
        if not title or not description or not status:
            raise ValueError("Title, description, and status must not be empty.")

        dispute = LegalDispute(title, description, status)
        self.disputes.append(dispute)
        print(f"Added legal dispute: {dispute}")

    def update_dispute(self, dispute_id: uuid.UUID, status: str) -> None:
        """
        Updates the status of an existing legal dispute.
        
        :param dispute_id: Unique identifier of the dispute to update.
        :param status: New status of the dispute.
        """
        dispute = self.get_dispute(dispute_id)
        if dispute is None:
            raise LookupError("Dispute not found.")
        
        dispute.status = status
        print(f"Updated legal dispute: {dispute}")

    def get_dispute(self, dispute_id: uuid.UUID) -> Optional[LegalDispute]:
        """
        Retrieves a legal dispute by its ID.
        
        :param dispute_id: Unique identifier of the dispute to retrieve.
        :return: LegalDispute object if found, otherwise None.
        """
        for dispute in self.disputes:
            if dispute.id == dispute_id:
                return dispute
        return None

    def list_disputes(self) -> List[LegalDispute]:
        """Returns a list of all legal disputes managed."""
        return self.disputes

def main():
    """Main function to demonstrate the LegalDispute and DisputeManager classes."""
    try:
        manager = DisputeManager()
        
        # Adding some legal disputes
        manager.add_dispute("Contract Breach", "Dispute over contract terms.", "Open")
        manager.add_dispute("Intellectual Property", "Unauthorized use of IP.", "Open")
        
        # Listing all disputes
        print("\nCurrent Legal Disputes:")
        for dispute in manager.list_disputes():
            print(dispute)

        # Update a dispute status
        dispute_to_update = manager.disputes[0].id
        manager.update_dispute(dispute_to_update, "Closed")
        
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except LookupError as le:
        print(f"Lookup Error: {le}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
