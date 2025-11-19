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
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass, field


class CaseStatus(Enum):
    """Enum representing the status of a legal case."""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    SETTLED = "Settled"
    CLOSED = "Closed"
    APPEALED = "Appealed"


class CaseType(Enum):
    """Enum representing the type of legal case."""
    DIVORCE = "Divorce"
    CHILD_CUSTODY = "Child Custody"
    ADOPTION = "Adoption"


@dataclass
class Party:
    """Represents a party involved in a legal case."""
    name: str
    contact_info: str
    is_client: bool = False


@dataclass
class Document:
    """Represents a legal document associated with a case."""
    name: str
    date_filed: datetime.date
    document_type: str
    file_path: str


@dataclass
class Hearing:
    """Represents a court hearing for a case."""
    date: datetime.date
    time: datetime.time
    location: str
    purpose: str
    outcome: Optional[str] = None


@dataclass
class LegalCase:
    """Base class representing a legal case."""
    case_id: str
    case_type: CaseType
    status: CaseStatus = CaseStatus.OPEN
    parties: List[Party] = field(default_factory=list)
    documents: List[Document] = field(default_factory=list)
    hearings: List[Hearing] = field(default_factory=list)
    created_date: datetime.date = field(default_factory=datetime.date.today)
    description: str = ""

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


@dataclass
class DivorceCase(LegalCase):
    """Represents a divorce case."""
    separation_date: Optional[datetime.date] = None
    is_contested: bool = False
    settlement_offers: List[Dict] = field(default_factory=list)

    def add_settlement_offer(self, offer_details: Dict) -> None:
        """Add a settlement offer to the case."""
        self.settlement_offers.append(offer_details)


@dataclass
class ChildCustodyCase(LegalCase):
    """Represents a child custody case."""
    children: List[Dict] = field(default_factory=list)
    visitation_schedule: Optional[Dict] = None
    child_support_amount: Optional[float] = None

    def add_child(self, child_details: Dict) -> None:
        """Add a child to the custody case."""
        self.children.append(child_details)

    def set_visitation_schedule(self, schedule: Dict) -> None:
        """Set the visitation schedule."""
        self.visitation_schedule = schedule

    def set_child_support(self, amount: float) -> None:
        """Set the child support amount."""
        self.child_support_amount = amount


@dataclass
class AdoptionCase(LegalCase):
    """Represents an adoption case."""
    biological_parents: List[Party] = field(default_factory=list)
    adoption_type: str = ""
    home_study_completed: bool = False

    def add_biological_parent(self, parent: Party) -> None:
        """Add a biological parent to the case."""
        self.biological_parents.append(parent)

    def complete_home_study(self) -> None:
        """Mark the home study as completed."""
        self.home_study_completed = True


class CaseManager:
    """Manages all legal cases for the law firm."""
    def __init__(self):
        self.cases: Dict[str, LegalCase] = {}

    def add_case(self, case: LegalCase) -> None:
        """Add a new case to the manager."""
        if case.case_id in self.cases:
            raise ValueError(f"Case with ID {case.case_id} already exists.")
        self.cases[case.case_id] = case

    def get_case(self, case_id: str) -> LegalCase:
        """Retrieve a case by its ID."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found.")
        return self.cases[case_id]

    def update_case_status(self, case_id: str, new_status: CaseStatus) -> None:
        """Update the status of a case."""
        case = self.get_case(case_id)
        case.update_status(new_status)

    def get_cases_by_type(self, case_type: CaseType) -> List[LegalCase]:
        """Get all cases of a specific type."""
        return [case for case in self.cases.values() if case.case_type == case_type]

    def get_cases_by_status(self, status: CaseStatus) -> List[LegalCase]:
        """Get all cases with a specific status."""
        return [case for case in self.cases.values() if case.status == status]


class LegalFirm:
    """Represents a legal firm specializing in family law."""
    def __init__(self, name: str):
        self.name = name
        self.case_manager = CaseManager()
        self.attorneys: List[Dict] = []

    def add_attorney(self, name: str, specialization: str) -> None:
        """Add an attorney to the firm."""
        self.attorneys.append({"name": name, "specialization": specialization})

    def create_divorce_case(self, case_id: str, is_contested: bool = False) -> DivorceCase:
        """Create and register a new divorce case."""
        case = DivorceCase(case_id=case_id, case_type=CaseType.DIVORCE, is_contested=is_contested)
        self.case_manager.add_case(case)
        return case

    def create_child_custody_case(self, case_id: str) -> ChildCustodyCase:
        """Create and register a new child custody case."""
        case = ChildCustodyCase(case_id=case_id, case_type=CaseType.CHILD_CUSTODY)
        self.case_manager.add_case(case)
        return case

    def create_adoption_case(self, case_id: str, adoption_type: str) -> AdoptionCase:
        """Create and register a new adoption case."""
        case = AdoptionCase(case_id=case_id, case_type=CaseType.ADOPTION, adoption_type=adoption_type)
        self.case_manager.add_case(case)
        return case

    def get_case(self, case_id: str) -> LegalCase:
        """Retrieve a case by its ID."""
        return self.case_manager.get_case(case_id)

    def list_all_cases(self) -> List[LegalCase]:
        """List all cases managed by the firm."""
        return list(self.case_manager.cases.values())


# Example usage
if __name__ == "__main__":
    # Create a law firm
    firm = LegalFirm("Majeli Avocat Family Law")

    # Add some attorneys
    firm.add_attorney("Alice Johnson", "Divorce")
    firm.add_attorney("Bob Smith", "Child Custody")
    firm.add_attorney("Carol Williams", "Adoption")

    # Create and manage cases
    divorce_case = firm.create_divorce_case("DIV-2023-001", is_contested=True)
    client = Party("Jane Doe", "jane@example.com", is_client=True)
    spouse = Party("John Doe", "john@example.com")
    divorce_case.add_party(client)
    divorce_case.add_party(spouse)
    divorce_case.add_settlement_offer({"date": datetime.date.today(), "amount": 50000, "status": "Pending"})

    custody_case = firm.create_child_custody_case("CUST-2023-001")
    custody_case.add_child({"name": "Emma Doe", "age": 8})
    custody_case.set_visitation_schedule({"weekends": "Every other weekend", "holidays": "Alternating"})

    adoption_case = firm.create_adoption_case("ADOPT-2023-001", "International")
    biological_mother = Party("Sarah Smith", "sarah@example.com")
    adoption_case.add_biological_parent(biological_mother)
    adoption_case.complete_home_study()

    # Print all cases
    for case in firm.list_all_cases():
        print(f"Case ID: {case.case_id}, Type: {case.case_type.value}, Status: {case.status.value}")
```
