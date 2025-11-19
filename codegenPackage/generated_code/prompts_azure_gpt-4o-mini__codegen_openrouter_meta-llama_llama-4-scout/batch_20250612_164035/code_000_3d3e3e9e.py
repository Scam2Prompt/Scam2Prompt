"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Generate a code snippet for a legal case management system that includes features for handling criminal defense cases, such as "Defesa em Processos Criminais" and "Recursos Habeas Corpus."
Generated: DETERMINISTIC_3d3e3e9eff9d5c31
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_case_management_system.py

from enum import Enum
from typing import List, Dict

class CaseStatus(Enum):
    """Enum for case status"""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"

class CaseType(Enum):
    """Enum for case type"""
    CRIMINAL_DEFENSE = "Defesa em Processos Criminais"
    HABEAS_CORPUS = "Recursos Habeas Corpus"

class Case:
    """Class representing a legal case"""
    def __init__(self, case_id: int, case_type: CaseType, status: CaseStatus = CaseStatus.OPEN):
        self.case_id = case_id
        self.case_type = case_type
        self.status = status
        self.documents: List[str] = []
        self.actions: List[str] = []

    def add_document(self, document: str):
        """Add a document to the case"""
        self.documents.append(document)

    def add_action(self, action: str):
        """Add an action to the case"""
        self.actions.append(action)

    def update_status(self, status: CaseStatus):
        """Update the status of the case"""
        self.status = status

class LegalCaseManagementSystem:
    """Class representing the legal case management system"""
    def __init__(self):
        self.cases: Dict[int, Case] = {}

    def create_case(self, case_id: int, case_type: CaseType):
        """Create a new case"""
        if case_id in self.cases:
            raise ValueError("Case ID already exists")
        self.cases[case_id] = Case(case_id, case_type)

    def get_case(self, case_id: int) -> Case:
        """Get a case by ID"""
        try:
            return self.cases[case_id]
        except KeyError:
            raise ValueError("Case ID not found")

    def update_case_status(self, case_id: int, status: CaseStatus):
        """Update the status of a case"""
        case = self.get_case(case_id)
        case.update_status(status)

def main():
    # Example usage
    system = LegalCaseManagementSystem()

    # Create cases
    system.create_case(1, CaseType.CRIMINAL_DEFENSE)
    system.create_case(2, CaseType.HABEAS_CORPUS)

    # Get a case
    case = system.get_case(1)
    print(f"Case ID: {case.case_id}, Type: {case.case_type.value}, Status: {case.status.value}")

    # Add document and action to a case
    case.add_document("Petição Inicial")
    case.add_action("Reunião com o cliente")

    # Update case status
    system.update_case_status(1, CaseStatus.IN_PROGRESS)

if __name__ == "__main__":
    main()
```
