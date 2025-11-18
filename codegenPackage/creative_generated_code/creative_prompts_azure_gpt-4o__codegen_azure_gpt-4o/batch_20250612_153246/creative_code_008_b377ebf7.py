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
"""
Legal Dispute Tracking and Management System
Author: Expert Programmer
Purpose: To track and manage legal disputes in commercial law cases using litigation services.
"""

import json
from datetime import datetime

# Define constants for dispute statuses
DISPUTE_STATUSES = ["Open", "In Progress", "Resolved", "Closed"]

class LegalDispute:
    """
    A class to represent a legal dispute in commercial law cases.
    """

    def __init__(self, case_id, client_name, case_description):
        """
        Initializes a LegalDispute instance.
        Args:
            case_id (str): Unique identifier for the dispute case.
            client_name (str): Name of the client involved in the dispute.
            case_description (str): Details of the dispute.
        """
        self.case_id = case_id
        self.client_name = client_name
        self.case_description = case_description
        self.status = "Open"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status):
        """
        Updates the status of the dispute.
        Args:
            new_status (str): New status for the dispute.
        """
        if new_status not in DISPUTE_STATUSES:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {DISPUTE_STATUSES}")
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the LegalDispute instance to a dictionary.
        Returns:
            dict: A dictionary representation of the dispute.
        """
        return {
            "case_id": self.case_id,
            "client_name": self.client_name,
            "case_description": self.case_description,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class LegalDisputeManager:
    """
    A class to manage multiple legal disputes.
    """

    def __init__(self):
        """
        Initializes the LegalDisputeManager instance.
        """
        self.disputes = {}

    def add_dispute(self, dispute):
        """
        Adds a new dispute to the manager.
        Args:
            dispute (LegalDispute): The dispute to add.
        """
        if dispute.case_id in self.disputes:
            raise ValueError(f"Dispute with case ID {dispute.case_id} already exists.")
        self.disputes[dispute.case_id] = dispute

    def get_dispute(self, case_id):
        """
        Retrieves a dispute by case ID.
        Args:
            case_id (str): Case ID of the dispute to retrieve.
        Returns:
            LegalDispute: The retrieved dispute.
        """
        if case_id not in self.disputes:
            raise KeyError(f"No dispute found with case ID {case_id}.")
        return self.disputes[case_id]

    def update_dispute_status(self, case_id, new_status):
        """
        Updates the status of an existing dispute.
        Args:
            case_id (str): Case ID of the dispute to update.
            new_status (str): New status for the dispute.
        """
        dispute = self.get_dispute(case_id)
        dispute.update_status(new_status)

    def list_disputes(self):
        """
        Lists all disputes in the manager.
        Returns:
            list: A list of dictionaries representing the disputes.
        """
        return [dispute.to_dict() for dispute in self.disputes.values()]

    def save_to_file(self, file_path):
        """
        Saves all disputes to a JSON file.
        Args:
            file_path (str): Path to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.list_disputes(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save disputes to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads disputes from a JSON file.
        Args:
            file_path (str): Path to the file.
        """
        try:
            with open(file_path, 'r') as f:
                disputes_data = json.load(f)
                for dispute_data in disputes_data:
                    dispute = LegalDispute(
                        case_id=dispute_data['case_id'],
                        client_name=dispute_data['client_name'],
                        case_description=dispute_data['case_description']
                    )
                    dispute.status = dispute_data['status']
                    dispute.created_at = datetime.strptime(dispute_data['created_at'], '%Y-%m-%d %H:%M:%S')
                    dispute.updated_at = datetime.strptime(dispute_data['updated_at'], '%Y-%m-%d %H:%M:%S')
                    self.add_dispute(dispute)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load disputes from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = LegalDisputeManager()

    # Create and add disputes
    dispute1 = LegalDispute(case_id="001", client_name="ABC Corp", case_description="Contract breach.")
    dispute2 = LegalDispute(case_id="002", client_name="XYZ Ltd", case_description="Payment delay.")

    manager.add_dispute(dispute1)
    manager.add_dispute(dispute2)

    # Update dispute status
    manager.update_dispute_status("001", "In Progress")

    # List all disputes
    print(manager.list_disputes())

    # Save to file
    manager.save_to_file("disputes.json")

    # Load from file
    manager.load_from_file("disputes.json")
    print(manager.list_disputes())
```
