"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Create a Python function that simulates a legal case management system, incorporating features relevant to the specialties of Pérez Bernalte Abogados, such as criminal and civil law.
Generated: DETERMINISTIC_14bf8c17e3aea9e2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass, field


class CaseType(Enum):
    """Enum representing different types of legal cases."""
    CRIMINAL = "Criminal"
    CIVIL = "Civil"
    FAMILY = "Family"
    LABOR = "Labor"
    COMMERCIAL = "Commercial"


class CaseStatus(Enum):
    """Enum representing different statuses of a legal case."""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"
    APPEALED = "Appealed"
    ARCHIVED = "Archived"


@dataclass
class Document:
    """Class representing a legal document associated with a case."""
    title: str
    content: str
    date_created: datetime.date = field(default_factory=datetime.date.today)
    is_confidential: bool = False


@dataclass
class Party:
    """Class representing a party involved in a legal case."""
    name: str
    contact_info: str
    is_client: bool = False


@dataclass
class Hearing:
    """Class representing a court hearing for a case."""
    date: datetime.datetime
    location: str
    purpose: str
    outcome: Optional[str] = None


@dataclass
class LegalCase:
    """Class representing a legal case in the management system."""
    case_id: str
    title: str
    case_type: CaseType
    status: CaseStatus = CaseStatus.OPEN
    description: str = ""
    parties: List[Party] = field(default_factory=list)
    documents: List[Document] = field(default_factory=list)
    hearings: List[Hearing] = field(default_factory=list)
    opened_date: datetime.date = field(default_factory=datetime.date.today)
    closed_date: Optional[datetime.date] = None

    def add_party(self, party: Party) -> None:
        """Add a party to the case."""
        self.parties.append(party)

    def add_document(self, document: Document) -> None:
        """Add a document to the case."""
        self.documents.append(document)

    def schedule_hearing(self, hearing: Hearing) -> None:
        """Schedule a hearing for the case."""
        self.hearings.append(hearing)

    def update_status(self, new_status: CaseStatus) -> None:
        """Update the status of the case."""
        self.status = new_status
        if new_status == CaseStatus.CLOSED:
            self.closed_date = datetime.date.today()

    def get_case_summary(self) -> Dict:
        """Return a summary of the case."""
        return {
            "case_id": self.case_id,
            "title": self.title,
            "type": self.case_type.value,
            "status": self.status.value,
            "parties_count": len(self.parties),
            "documents_count": len(self.documents),
            "hearings_count": len(self.hearings),
            "opened_date": self.opened_date,
            "closed_date": self.closed_date
        }


class CaseManagementSystem:
    """Class representing a legal case management system."""
    def __init__(self):
        self.cases: Dict[str, LegalCase] = {}

    def create_case(self, case_id: str, title: str, case_type: CaseType) -> LegalCase:
        """Create a new legal case."""
        if case_id in self.cases:
            raise ValueError(f"Case with ID {case_id} already exists.")
        
        new_case = LegalCase(case_id=case_id, title=title, case_type=case_type)
        self.cases[case_id] = new_case
        return new_case

    def get_case(self, case_id: str) -> LegalCase:
        """Retrieve a case by its ID."""
        if case_id not in self.cases:
            raise KeyError(f"Case with ID {case_id} not found.")
        return self.cases[case_id]

    def close_case(self, case_id: str) -> None:
        """Close a case by updating its status."""
        case = self.get_case(case_id)
        case.update_status(CaseStatus.CLOSED)

    def search_cases(self, case_type: Optional[CaseType] = None, 
                    status: Optional[CaseStatus] = None) -> List[Dict]:
        """Search for cases based on type and/or status."""
        results = []
        for case in self.cases.values():
            if (case_type is None or case.case_type == case_type) and \
               (status is None or case.status == status):
                results.append(case.get_case_summary())
        return results

    def generate_report(self) -> Dict:
        """Generate a report of all cases in the system."""
        report = {
            "total_cases": len(self.cases),
            "open_cases": 0,
            "closed_cases": 0,
            "by_type": {t.value: 0 for t in CaseType}
        }
        
        for case in self.cases.values():
            if case.status == CaseStatus.CLOSED:
                report["closed_cases"] += 1
            else:
                report["open_cases"] += 1
            
            report["by_type"][case.case_type.value] += 1
        
        return report


# Example usage
if __name__ == "__main__":
    system = CaseManagementSystem()
    
    # Create a criminal case
    criminal_case = system.create_case("CR-2023-001", "Theft Case", CaseType.CRIMINAL)
    client = Party("John Doe", "john@example.com", is_client=True)
    defendant = Party("Jane Smith", "jane@example.com")
    
    criminal_case.add_party(client)
    criminal_case.add_party(defendant)
    criminal_case.add_document(Document("Police Report", "Initial police report content"))
    
    hearing = Hearing(
        datetime.datetime(2023, 6, 15, 10, 0),
        "District Court Room 5",
        "Initial Hearing"
    )
    criminal_case.schedule_hearing(hearing)
    
    # Create a civil case
    civil_case = system.create_case("CV-2023-001", "Contract Dispute", CaseType.CIVIL)
    civil_case.add_party(Party("ABC Corp", "contact@abccorp.com", is_client=True))
    civil_case.add_party(Party("XYZ Ltd", "legal@xyzltd.com"))
    
    # Generate report
    print("System Report:")
    print(system.generate_report())
    
    # Search for criminal cases
    print("\nCriminal Cases:")
    for case in system.search_cases(case_type=CaseType.CRIMINAL):
        print(case)
```
