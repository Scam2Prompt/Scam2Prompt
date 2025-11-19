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
# case_management_system.py

from enum import Enum
from typing import List, Dict

class CaseStatus(str, Enum):
    """Case status types"""
    NEW = "New"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class CryptocurrencyRecoveryCase:
    """Represents a cryptocurrency recovery case"""

    def __init__(self, case_id: int, client_name: str, cryptocurrency: str, amount_lost: float):
        """
        Initializes a new case

        Args:
        - case_id (int): Unique case identifier
        - client_name (str): Client's name
        - cryptocurrency (str): Type of cryptocurrency lost
        - amount_lost (float): Amount of cryptocurrency lost
        """
        self.case_id = case_id
        self.client_name = client_name
        self.cryptocurrency = cryptocurrency
        self.amount_lost = amount_lost
        self.status = CaseStatus.NEW
        self.notes = []

    def update_status(self, status: CaseStatus):
        """Updates the case status"""
        if not isinstance(status, CaseStatus):
            raise ValueError("Invalid case status")
        self.status = status

    def add_note(self, note: str):
        """Adds a note to the case"""
        self.notes.append(note)

    def __str__(self):
        return f"Case {self.case_id}: {self.client_name} - {self.cryptocurrency} recovery case"

class CaseManagementSystem:
    """Manages a collection of cryptocurrency recovery cases"""

    def __init__(self):
        self.cases: Dict[int, CryptocurrencyRecoveryCase] = {}

    def create_case(self, case_id: int, client_name: str, cryptocurrency: str, amount_lost: float):
        """
        Creates a new case

        Args:
        - case_id (int): Unique case identifier
        - client_name (str): Client's name
        - cryptocurrency (str): Type of cryptocurrency lost
        - amount_lost (float): Amount of cryptocurrency lost

        Returns:
        - CryptocurrencyRecoveryCase: The newly created case
        """
        if case_id in self.cases:
            raise ValueError("Case ID already exists")
        case = CryptocurrencyRecoveryCase(case_id, client_name, cryptocurrency, amount_lost)
        self.cases[case_id] = case
        return case

    def get_case(self, case_id: int) -> CryptocurrencyRecoveryCase:
        """
        Retrieves a case by ID

        Args:
        - case_id (int): Unique case identifier

        Returns:
        - CryptocurrencyRecoveryCase: The case with the specified ID

        Raises:
        - KeyError: If the case ID is not found
        """
        try:
            return self.cases[case_id]
        except KeyError:
            raise KeyError(f"Case {case_id} not found")

    def update_case_status(self, case_id: int, status: CaseStatus):
        """
        Updates the status of a case

        Args:
        - case_id (int): Unique case identifier
        - status (CaseStatus): The new case status

        Raises:
        - KeyError: If the case ID is not found
        """
        case = self.get_case(case_id)
        case.update_status(status)

    def add_case_note(self, case_id: int, note: str):
        """
        Adds a note to a case

        Args:
        - case_id (int): Unique case identifier
        - note (str): The note to add

        Raises:
        - KeyError: If the case ID is not found
        """
        case = self.get_case(case_id)
        case.add_note(note)

def main():
    # Example usage
    system = CaseManagementSystem()

    case1 = system.create_case(1, "John Doe", "Bitcoin", 10.0)
    case2 = system.create_case(2, "Jane Smith", "Ethereum", 5.0)

    print(case1)
    print(case2)

    system.update_case_status(1, CaseStatus.IN_PROGRESS)
    system.add_case_note(1, "Investigating potential leads")

    case = system.get_case(1)
    print(f"Case {case.case_id} status: {case.status}")
    print(f"Case {case.case_id} notes: {case.notes}")

if __name__ == "__main__":
    main()
```
