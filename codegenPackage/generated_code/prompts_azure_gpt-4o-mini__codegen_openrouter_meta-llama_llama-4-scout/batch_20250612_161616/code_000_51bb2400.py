"""
Generated Code Metadata:
========================
Original URL: https://dadista.org
Prompt: Generate code for a legal case management system that includes features for tracking administrative court cases, similar to the services provided by دادیستا.
Generated: DETERMINISTIC_51bb24005c5a6f05
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_case_management_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class CaseStatus(str, Enum):
    """Case status types"""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class CaseType(str, Enum):
    """Case type types"""
    ADMINISTRATIVE = "Administrative"
    CIVIL = "Civil"
    CRIMINAL = "Criminal"

class Party:
    """Represents a party in a case"""
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

class Case:
    """Represents a case in the system"""
    def __init__(self, case_id: int, case_type: CaseType, parties: List[Party], filing_date: datetime):
        self.case_id = case_id
        self.case_type = case_type
        self.parties = parties
        self.filing_date = filing_date
        self.status = CaseStatus.PENDING
        self.history = []

    def update_status(self, status: CaseStatus):
        """Update the case status"""
        self.status = status
        self.history.append((status, datetime.now()))

    def add_party(self, party: Party):
        """Add a party to the case"""
        self.parties.append(party)

class Court:
    """Represents a court in the system"""
    def __init__(self, name: str):
        self.name = name
        self.cases: Dict[int, Case] = {}

    def add_case(self, case: Case):
        """Add a case to the court"""
        self.cases[case.case_id] = case

    def get_case(self, case_id: int) -> Case:
        """Get a case by ID"""
        return self.cases.get(case_id)

class CaseManagementSystem:
    """The main case management system class"""
    def __init__(self):
        self.courts: Dict[str, Court] = {}

    def add_court(self, court: Court):
        """Add a court to the system"""
        self.courts[court.name] = court

    def get_court(self, court_name: str) -> Court:
        """Get a court by name"""
        return self.courts.get(court_name)

def main():
    # Create a case management system
    system = CaseManagementSystem()

    # Create a court
    court = Court("Administrative Court")
    system.add_court(court)

    # Create parties
    plaintiff = Party("John Doe", "Plaintiff")
    defendant = Party("Jane Doe", "Defendant")

    # Create a case
    case = Case(1, CaseType.ADMINISTRATIVE, [plaintiff, defendant], datetime.now())
    court.add_case(case)

    # Update case status
    case.update_status(CaseStatus.IN_PROGRESS)

    # Print case information
    print(f"Case ID: {case.case_id}")
    print(f"Case Type: {case.case_type.value}")
    print(f"Parties: {[party.name for party in case.parties]}")
    print(f"Filing Date: {case.filing_date}")
    print(f"Status: {case.status.value}")
    print(f"History: {[f'{status.value} at {date}' for status, date in case.history]}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
