"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadista.org
Prompt: Generate code for a legal case management system that includes features for tracking administrative court cases, similar to the services provided by دادیستا.
Generated: DETERMINISTIC_51bb24005c5a6f05
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# legal_case_management.py

from datetime import datetime
from typing import List, Optional

class Case:
    """
    A class to represent a legal case.
    """
    
    def __init__(self, case_id: int, title: str, status: str, date_filed: datetime, party_names: List[str]):
        self.case_id = case_id
        self.title = title
        self.status = status
        self.date_filed = date_filed
        self.party_names = party_names

    def __repr__(self) -> str:
        return f"Case(case_id={self.case_id}, title='{self.title}', status='{self.status}', date_filed={self.date_filed}, party_names={self.party_names})"


class CaseManager:
    """
    A class to manage legal cases in the system.
    """

    def __init__(self):
        self.cases: List[Case] = []

    def add_case(self, case: Case) -> None:
        """
        Adds a new case to the case manager.
        
        :param case: The case to add.
        :raises ValueError: If the case ID already exists.
        """
        if any(existing_case.case_id == case.case_id for existing_case in self.cases):
            raise ValueError(f"Case ID {case.case_id} already exists.")
        self.cases.append(case)

    def get_case(self, case_id: int) -> Optional[Case]:
        """
        Retrieves a case by its ID.

        :param case_id: The ID of the case to retrieve.
        :return: The case object if found, otherwise None.
        """
        for case in self.cases:
            if case.case_id == case_id:
                return case
        return None

    def update_case_status(self, case_id: int, new_status: str) -> None:
        """
        Updates the status of an existing case.

        :param case_id: The ID of the case to update.
        :param new_status: The new status to set.
        :raises ValueError: If the case ID does not exist.
        """
        case = self.get_case(case_id)
        if case is None:
            raise ValueError(f"Case ID {case_id} does not exist.")
        case.status = new_status

    def list_cases(self) -> List[Case]:
        """
        Lists all cases in the case manager.

        :return: A list of all cases.
        """
        return self.cases


def main():
    """
    Main function to demonstrate the functionality of the CaseManager.
    """
    case_manager = CaseManager()

    # Adding new cases
    try:
        case1 = Case(case_id=1, title="Smith vs. Jones", status="Pending", date_filed=datetime.now(), party_names=["Smith", "Jones"])
        case_manager.add_case(case1)

        case2 = Case(case_id=2, title="Brown vs. Board", status="Closed", date_filed=datetime.now(), party_names=["Brown", "Board"])
        case_manager.add_case(case2)

        print("Cases after addition:")
        print(case_manager.list_cases())

        # Updating case status
        case_manager.update_case_status(case_id=1, new_status="Active")
        print("\nCases after updating status:")
        print(case_manager.list_cases())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
