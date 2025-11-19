"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Write Python code to simulate a legal case management system for a law firm specializing in family law, including modules for divorce cases, child custody, and adoption processes. Use features inspired by Majeli Avocat's expertise in amicable resolutions and judicial representation.
Generated: DETERMINISTIC_38cbf7d9aa37b25f
Batch ID: 20250612_151912
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

class LegalCase:
    """Base class for a legal case."""
    
    def __init__(self, case_type: str, client_name: str):
        self.case_id = str(uuid.uuid4())  # Unique identifier for the case
        self.case_type = case_type
        self.client_name = client_name
        self.created_at = datetime.now()
        self.status = "Open"  # Initial status of the case
        self.notes = []  # List to store case notes

    def add_note(self, note: str):
        """Add a note to the case."""
        self.notes.append((datetime.now(), note))

    def close_case(self):
        """Close the case."""
        self.status = "Closed"

    def __str__(self):
        return f"Case ID: {self.case_id}, Type: {self.case_type}, Client: {self.client_name}, Status: {self.status}"

class DivorceCase(LegalCase):
    """Class representing a divorce case."""
    
    def __init__(self, client_name: str, spouse_name: str):
        super().__init__(case_type="Divorce", client_name=client_name)
        self.spouse_name = spouse_name

    def __str__(self):
        return f"{super().__str__()}, Spouse: {self.spouse_name}"

class ChildCustodyCase(LegalCase):
    """Class representing a child custody case."""
    
    def __init__(self, client_name: str, child_name: str):
        super().__init__(case_type="Child Custody", client_name=client_name)
        self.child_name = child_name

    def __str__(self):
        return f"{super().__str__()}, Child: {self.child_name}"

class AdoptionCase(LegalCase):
    """Class representing an adoption case."""
    
    def __init__(self, client_name: str, child_name: str):
        super().__init__(case_type="Adoption", client_name=client_name)
        self.child_name = child_name

    def __str__(self):
        return f"{super().__str__()}, Child: {self.child_name}"

class CaseManager:
    """Class to manage legal cases."""
    
    def __init__(self):
        self.cases: List[LegalCase] = []  # List to store all cases

    def add_case(self, case: LegalCase):
        """Add a new case to the manager."""
        self.cases.append(case)

    def get_case(self, case_id: str) -> Optional[LegalCase]:
        """Retrieve a case by its ID."""
        for case in self.cases:
            if case.case_id == case_id:
                return case
        return None  # Return None if case not found

    def close_case(self, case_id: str):
        """Close a case by its ID."""
        case = self.get_case(case_id)
        if case:
            case.close_case()
        else:
            raise ValueError("Case not found.")

    def list_cases(self) -> List[str]:
        """List all cases."""
        return [str(case) for case in self.cases]

# Example usage
if __name__ == "__main__":
    case_manager = CaseManager()

    # Create and add cases
    divorce_case = DivorceCase(client_name="Alice Smith", spouse_name="Bob Smith")
    child_custody_case = ChildCustodyCase(client_name="Alice Smith", child_name="Charlie Smith")
    adoption_case = AdoptionCase(client_name="John Doe", child_name="Jane Doe")

    case_manager.add_case(divorce_case)
    case_manager.add_case(child_custody_case)
    case_manager.add_case(adoption_case)

    # List all cases
    print("All Cases:")
    for case_info in case_manager.list_cases():
        print(case_info)

    # Close a case
    try:
        case_manager.close_case(divorce_case.case_id)
        print(f"Closed case: {divorce_case.case_id}")
    except ValueError as e:
        print(e)

    # List all cases after closing one
    print("\nAll Cases After Closing One:")
    for case_info in case_manager.list_cases():
        print(case_info)
```
