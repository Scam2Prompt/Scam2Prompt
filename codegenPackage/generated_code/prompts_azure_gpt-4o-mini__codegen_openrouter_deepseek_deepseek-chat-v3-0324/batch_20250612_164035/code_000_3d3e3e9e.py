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

Here's a clean, production-ready Python code snippet for a legal case management system with the requested features:

```python
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional
from dataclasses import dataclass, field


class CaseStatus(Enum):
    """Enum representing possible case statuses."""
    OPEN = auto()
    IN_PROGRESS = auto()
    CLOSED = auto()
    APPEAL_PENDING = auto()


class CaseType(Enum):
    """Enum representing types of legal cases."""
    CRIMINAL_DEFENSE = "Defesa em Processos Criminais"
    HABEAS_CORPUS = "Recursos Habeas Corpus"
    CIVIL = "Ação Civil"
    LABOR = "Ação Trabalhista"


@dataclass
class LegalDocument:
    """Class representing a legal document."""
    title: str
    content: str
    filing_date: datetime
    document_type: str

    def format_document(self) -> str:
        """Returns a formatted version of the document."""
        return f"{self.title}\nFiled on: {self.filing_date}\n\n{self.content}"


@dataclass
class LegalCase:
    """Class representing a legal case."""
    case_id: str
    case_type: CaseType
    client_name: str
    status: CaseStatus = CaseStatus.OPEN
    opening_date: datetime = field(default_factory=datetime.now)
    closing_date: Optional[datetime] = None
    documents: List[LegalDocument] = field(default_factory=list)

    def add_document(self, document: LegalDocument) -> None:
        """Adds a document to the case."""
        self.documents.append(document)

    def update_status(self, new_status: CaseStatus) -> None:
        """Updates the case status."""
        if self.status == CaseStatus.CLOSED:
            raise ValueError("Cannot change status of a closed case")
        self.status = new_status
        if new_status == CaseStatus.CLOSED:
            self.closing_date = datetime.now()

    def get_case_summary(self) -> Dict[str, str]:
        """Returns a summary of the case."""
        return {
            "case_id": self.case_id,
            "case_type": self.case_type.value,
            "client_name": self.client_name,
            "status": self.status.name,
            "opening_date": self.opening_date.strftime("%Y-%m-%d"),
            "documents_count": str(len(self.documents))
        }


class CaseManager:
    """Class for managing legal cases."""
    def __init__(self):
        self.cases: Dict[str, LegalCase] = {}

    def add_case(self, case: LegalCase) -> None:
        """Adds a case to the manager."""
        if case.case_id in self.cases:
            raise ValueError(f"Case with ID {case.case_id} already exists")
        self.cases[case.case_id] = case

    def get_case(self, case_id: str) -> LegalCase:
        """Retrieves a case by its ID."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        return self.cases[case_id]

    def get_cases_by_type(self, case_type: CaseType) -> List[LegalCase]:
        """Returns all cases of a specific type."""
        return [case for case in self.cases.values() if case.case_type == case_type]

    def get_open_criminal_defense_cases(self) -> List[LegalCase]:
        """Returns all open criminal defense cases."""
        return [
            case for case in self.cases.values()
            if case.case_type == CaseType.CRIMINAL_DEFENSE
            and case.status != CaseStatus.CLOSED
        ]

    def get_pending_habeas_corpus_appeals(self) -> List[LegalCase]:
        """Returns all pending Habeas Corpus appeals."""
        return [
            case for case in self.cases.values()
            if case.case_type == CaseType.HABEAS_CORPUS
            and case.status == CaseStatus.APPEAL_PENDING
        ]


# Example usage
if __name__ == "__main__":
    manager = CaseManager()
    
    # Create a criminal defense case
    criminal_case = LegalCase(
        case_id="CRIM-2023-001",
        case_type=CaseType.CRIMINAL_DEFENSE,
        client_name="João Silva"
    )
    
    # Create a habeas corpus case
    hc_case = LegalCase(
        case_id="HC-2023-001",
        case_type=CaseType.HABEAS_CORPUS,
        client_name="Maria Souza",
        status=CaseStatus.APPEAL_PENDING
    )
    
    # Add cases to manager
    manager.add_case(criminal_case)
    manager.add_case(hc_case)
    
    # Add documents to cases
    criminal_case.add_document(
        LegalDocument(
            title="Initial Defense Brief",
            content="Lorem ipsum...",
            filing_date=datetime.now(),
            document_type="Memorial"
        )
    )
    
    # Get specific case types
    criminal_cases = manager.get_cases_by_type(CaseType.CRIMINAL_DEFENSE)
    hc_appeals = manager.get_pending_habeas_corpus_appeals()
    
    print(f"Open criminal cases: {len(criminal_cases)}")
    print(f"Pending Habeas Corpus appeals: {len(hc_appeals)}")
```
