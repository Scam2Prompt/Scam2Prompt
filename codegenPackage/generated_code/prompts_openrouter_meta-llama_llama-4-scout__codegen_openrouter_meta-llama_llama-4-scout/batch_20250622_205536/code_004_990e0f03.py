"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Create a data model for storing and managing arbitration cases in Slovakia, including information about parties involved, dispute details, and case status.
Generated: DETERMINISTIC_990e0f03bef4958a
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import date
from typing import List

class CaseStatus(str, Enum):
    """Arbitration case status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Party:
    """Party involved in the arbitration case"""
    def __init__(self, 
                 name: str, 
                 address: str, 
                 contact_person: str = None, 
                 contact_email: str = None, 
                 contact_phone: str = None):
        """
        Initialize a Party object.

        Args:
        - name (str): Name of the party.
        - address (str): Address of the party.
        - contact_person (str, optional): Contact person of the party. Defaults to None.
        - contact_email (str, optional): Contact email of the party. Defaults to None.
        - contact_phone (str, optional): Contact phone number of the party. Defaults to None.
        """
        self.name = name
        self.address = address
        self.contact_person = contact_person
        self.contact_email = contact_email
        self.contact_phone = contact_phone

class ArbitrationCase:
    """Arbitration case data model"""
    def __init__(self, 
                 case_id: str, 
                 parties: List[Party], 
                 dispute_details: str, 
                 case_status: CaseStatus = CaseStatus.PENDING, 
                 arbitration_date: date = None):
        """
        Initialize an ArbitrationCase object.

        Args:
        - case_id (str): Unique identifier for the arbitration case.
        - parties (List[Party]): List of parties involved in the arbitration case.
        - dispute_details (str): Details of the dispute.
        - case_status (CaseStatus, optional): Status of the arbitration case. Defaults to CaseStatus.PENDING.
        - arbitration_date (date, optional): Date of arbitration. Defaults to None.
        """
        self.case_id = case_id
        self.parties = parties
        self.dispute_details = dispute_details
        self.case_status = case_status
        self.arbitration_date = arbitration_date

    def update_case_status(self, new_status: CaseStatus):
        """
        Update the status of the arbitration case.

        Args:
        - new_status (CaseStatus): New status of the arbitration case.

        Raises:
        - ValueError: If the new status is not a valid CaseStatus.
        """
        if not isinstance(new_status, CaseStatus):
            raise ValueError("Invalid case status")
        self.case_status = new_status

    def add_party(self, party: Party):
        """
        Add a new party to the arbitration case.

        Args:
        - party (Party): Party to be added.

        Raises:
        - TypeError: If the party is not an instance of Party.
        """
        if not isinstance(party, Party):
            raise TypeError("Invalid party")
        self.parties.append(party)

class ArbitrationCaseRepository:
    """Repository for storing and managing arbitration cases"""
    def __init__(self):
        self.cases = {}

    def add_case(self, case: ArbitrationCase):
        """
        Add a new arbitration case to the repository.

        Args:
        - case (ArbitrationCase): Arbitration case to be added.

        Raises:
        - TypeError: If the case is not an instance of ArbitrationCase.
        - ValueError: If a case with the same ID already exists.
        """
        if not isinstance(case, ArbitrationCase):
            raise TypeError("Invalid case")
        if case.case_id in self.cases:
            raise ValueError("Case with the same ID already exists")
        self.cases[case.case_id] = case

    def get_case(self, case_id: str) -> ArbitrationCase:
        """
        Get an arbitration case by its ID.

        Args:
        - case_id (str): ID of the arbitration case.

        Returns:
        - ArbitrationCase: Arbitration case with the given ID, or None if not found.
        """
        return self.cases.get(case_id)

# Example usage
if __name__ == "__main__":
    # Create parties
    party1 = Party("John Doe", "123 Main St", contact_person="John Doe", contact_email="john.doe@example.com")
    party2 = Party("Jane Smith", "456 Elm St", contact_person="Jane Smith", contact_email="jane.smith@example.com")

    # Create arbitration case
    case = ArbitrationCase("CASE-123", [party1, party2], "Dispute over contract terms")

    # Create repository and add case
    repository = ArbitrationCaseRepository()
    repository.add_case(case)

    # Get case and update status
    retrieved_case = repository.get_case("CASE-123")
    retrieved_case.update_case_status(CaseStatus.IN_PROGRESS)

    # Print case details
    print(f"Case ID: {retrieved_case.case_id}")
    print(f"Parties:")
    for party in retrieved_case.parties:
        print(f"- {party.name} ({party.address})")
    print(f"Dispute Details: {retrieved_case.dispute_details}")
    print(f"Case Status: {retrieved_case.case_status.value}")
```
