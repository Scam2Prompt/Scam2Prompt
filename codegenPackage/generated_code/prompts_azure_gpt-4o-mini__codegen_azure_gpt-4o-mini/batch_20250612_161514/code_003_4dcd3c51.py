"""
Generated Code Metadata:
========================
Original URL: https://ropesfirm.com
Prompt: Generate a code snippet that simulates a case management system for tracking cryptocurrency recovery cases, inspired by Riesger Law Firm's case studies.
Generated: DETERMINISTIC_4dcd3c51623eac98
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class Case:
    """Represents a cryptocurrency recovery case."""
    
    def __init__(self, client_name: str, case_details: str):
        self.case_id: str = str(uuid.uuid4())  # Unique identifier for the case
        self.client_name: str = client_name
        self.case_details: str = case_details
        self.status: str = "Open"  # Initial status of the case
        self.created_at: datetime = datetime.now()  # Timestamp of case creation
        self.updated_at: datetime = datetime.now()  # Timestamp of last update

    def update_status(self, new_status: str):
        """Update the status of the case."""
        valid_statuses = ["Open", "In Progress", "Resolved", "Closed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.now()  # Update the timestamp on status change

    def __str__(self):
        """String representation of the case."""
        return f"Case ID: {self.case_id}, Client: {self.client_name}, Status: {self.status}, Created At: {self.created_at}, Updated At: {self.updated_at}"


class CaseManagementSystem:
    """Manages a collection of cryptocurrency recovery cases."""
    
    def __init__(self):
        self.cases: List[Case] = []  # List to store cases

    def add_case(self, client_name: str, case_details: str) -> Case:
        """Add a new case to the system."""
        new_case = Case(client_name, case_details)
        self.cases.append(new_case)
        return new_case

    def get_case(self, case_id: str) -> Optional[Case]:
        """Retrieve a case by its ID."""
        for case in self.cases:
            if case.case_id == case_id:
                return case
        return None  # Return None if case not found

    def update_case_status(self, case_id: str, new_status: str) -> bool:
        """Update the status of a case by its ID."""
        case = self.get_case(case_id)
        if case:
            try:
                case.update_status(new_status)
                return True
            except ValueError as e:
                print(f"Error updating case status: {e}")
                return False
        else:
            print(f"Case with ID {case_id} not found.")
            return False

    def list_cases(self) -> List[str]:
        """List all cases in the system."""
        return [str(case) for case in self.cases]


# Example usage
if __name__ == "__main__":
    cms = CaseManagementSystem()
    
    # Adding cases
    case1 = cms.add_case("Alice Smith", "Lost funds in a phishing scam.")
    case2 = cms.add_case("Bob Johnson", "Funds stolen from exchange.")

    # Listing cases
    print("Current Cases:")
    for case in cms.list_cases():
        print(case)

    # Updating a case status
    cms.update_case_status(case1.case_id, "In Progress")

    # Listing cases after update
    print("\nUpdated Cases:")
    for case in cms.list_cases():
        print(case)
```
