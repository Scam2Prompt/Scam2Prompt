"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ropesfirm.com
Prompt: Generate a code snippet that simulates a case management system for tracking cryptocurrency recovery cases, inspired by Riesger Law Firm's case studies.
Generated: DETERMINISTIC_4dcd3c51623eac98
Batch ID: 20250612_161514
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


class CaseStatus:
    """Enumeration for Case Status"""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"


class Case:
    """Represents a cryptocurrency recovery case"""

    def __init__(self, client_name, case_description):
        """
        Initializes a new case.

        :param client_name: Name of the client raising the case
        :param case_description: Description of the case
        """
        self.case_id = str(uuid.uuid4())  # Generate a unique ID for the case
        self.client_name = client_name
        self.case_description = case_description
        self.status = CaseStatus.OPEN  # Default status is 'Open'
        self.created_at = datetime.now()  # Timestamp when the case was created
        self.updated_at = self.created_at  # Timestamp when the case was last updated

    def update_status(self, new_status):
        """
        Updates the case status.

        :param new_status: New status to be set
        :raises ValueError: If the new status is invalid
        """
        if new_status not in [CaseStatus.OPEN, CaseStatus.IN_PROGRESS, CaseStatus.RESOLVED, CaseStatus.CLOSED]:
            raise ValueError("Invalid status provided.")
        self.status = new_status
        self.updated_at = datetime.now()  # Update the timestamp for the last modification

    def __str__(self):
        """
        Returns a string representation of the case.
        """
        return (
            f"Case ID: {self.case_id}\n"
            f"Client: {self.client_name}\n"
            f"Description: {self.case_description}\n"
            f"Status: {self.status}\n"
            f"Created At: {self.created_at}\n"
            f"Last Updated: {self.updated_at}\n"
        )


class CaseManagementSystem:
    """Manages cryptocurrency recovery cases"""

    def __init__(self):
        """
        Initializes the case management system
        """
        self.cases = {}  # Dictionary to store cases by their unique ID

    def create_case(self, client_name, case_description):
        """
        Creates a new case and adds it to the system.

        :param client_name: Name of the client
        :param case_description: Description of the case
        :return: The newly created case
        """
        new_case = Case(client_name, case_description)
        self.cases[new_case.case_id] = new_case
        return new_case

    def get_case(self, case_id):
        """
        Retrieves a case by its ID.

        :param case_id: ID of the case to retrieve
        :return: The requested case
        :raises KeyError: If the case ID does not exist
        """
        if case_id not in self.cases:
            raise KeyError(f"Case ID {case_id} not found.")
        return self.cases[case_id]

    def update_case_status(self, case_id, new_status):
        """
        Updates the status of a case.

        :param case_id: ID of the case to update
        :param new_status: New status to set for the case
        :raises KeyError: If the case ID does not exist
        :raises ValueError: If the new status is invalid
        """
        case = self.get_case(case_id)
        case.update_status(new_status)

    def list_cases(self):
        """
        Lists all cases in the system.

        :return: List of all cases
        """
        return list(self.cases.values())


# Example usage
if __name__ == "__main__":
    cms = CaseManagementSystem()

    # Create a new case
    case = cms.create_case("John Doe", "Lost access to wallet containing 5 BTC.")
    print("Case Created:\n", case)

    # Update case status
    cms.update_case_status(case.case_id, CaseStatus.IN_PROGRESS)
    print("\nCase Updated:\n", cms.get_case(case.case_id))

    # List all cases
    print("\nAll Cases:")
    for c in cms.list_cases():
        print(c)
```
