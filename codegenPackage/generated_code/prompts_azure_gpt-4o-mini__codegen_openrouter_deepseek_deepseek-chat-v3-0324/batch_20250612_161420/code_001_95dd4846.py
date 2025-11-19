"""
Generated Code Metadata:
========================
Original URL: https://tolaandtola.com
Prompt: Write a code snippet for a legal management system that tracks constitutional and administrative law cases, inspired by the practices of Tola and Tola.
Generated: DETERMINISTIC_95dd4846239926e9
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Legal Management System for Constitutional and Administrative Law Cases
Inspired by Tola and Tola practices
"""

from datetime import datetime
from typing import List, Dict, Optional
import json
import uuid
from enum import Enum, auto


class CaseStatus(Enum):
    """Enum representing different case statuses"""
    FILED = auto()
    IN_PROGRESS = auto()
    DECIDED = auto()
    APPEALED = auto()
    CLOSED = auto()


class CaseType(Enum):
    """Enum representing different case types"""
    CONSTITUTIONAL = auto()
    ADMINISTRATIVE = auto()
    MIXED = auto()


class CourtLevel(Enum):
    """Enum representing different court levels"""
    HIGH_COURT = auto()
    APPEAL_COURT = auto()
    SUPREME_COURT = auto()
    TRIBUNAL = auto()


class LegalCase:
    """Class representing a legal case"""
    
    def __init__(
        self,
        title: str,
        case_type: CaseType,
        description: str,
        parties: List[str],
        filing_date: datetime,
        status: CaseStatus = CaseStatus.FILED,
        case_id: Optional[str] = None,
        court_level: Optional[CourtLevel] = None,
        related_cases: Optional[List[str]] = None,
        documents: Optional[List[str]] = None
    ):
        self.case_id = case_id or str(uuid.uuid4())
        self.title = title
        self.case_type = case_type
        self.description = description
        self.parties = parties
        self.filing_date = filing_date
        self.status = status
        self.court_level = court_level
        self.related_cases = related_cases or []
        self.documents = documents or []
        self.history = [{"timestamp": datetime.now(), "action": "Case created"}]

    def update_status(self, new_status: CaseStatus, notes: str = "") -> None:
        """Update the case status and record in history"""
        self.status = new_status
        self.history.append({
            "timestamp": datetime.now(),
            "action": f"Status changed to {new_status.name}",
            "notes": notes
        })

    def add_document(self, document_name: str) -> None:
        """Add a document reference to the case"""
        self.documents.append(document_name)
        self.history.append({
            "timestamp": datetime.now(),
            "action": f"Document added: {document_name}"
        })

    def add_related_case(self, case_id: str) -> None:
        """Add a related case reference"""
        if case_id not in self.related_cases:
            self.related_cases.append(case_id)
            self.history.append({
                "timestamp": datetime.now(),
                "action": f"Related case added: {case_id}"
            })

    def to_dict(self) -> Dict:
        """Convert case to dictionary for serialization"""
        return {
            "case_id": self.case_id,
            "title": self.title,
            "case_type": self.case_type.name,
            "description": self.description,
            "parties": self.parties,
            "filing_date": self.filing_date.isoformat(),
            "status": self.status.name,
            "court_level": self.court_level.name if self.court_level else None,
            "related_cases": self.related_cases,
            "documents": self.documents,
            "history": self.history
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'LegalCase':
        """Create case from dictionary"""
        return cls(
            title=data["title"],
            case_type=CaseType[data["case_type"]],
            description=data["description"],
            parties=data["parties"],
            filing_date=datetime.fromisoformat(data["filing_date"]),
            status=CaseStatus[data["status"]],
            case_id=data["case_id"],
            court_level=CourtLevel[data["court_level"]] if data["court_level"] else None,
            related_cases=data["related_cases"],
            documents=data["documents"]
        )


class CaseManager:
    """Class for managing legal cases"""
    
    def __init__(self, storage_file: str = "cases.json"):
        self.storage_file = storage_file
        self.cases: Dict[str, LegalCase] = {}
        self.load_cases()

    def add_case(self, case: LegalCase) -> None:
        """Add a new case to the system"""
        if case.case_id in self.cases:
            raise ValueError(f"Case with ID {case.case_id} already exists")
        self.cases[case.case_id] = case
        self.save_cases()

    def get_case(self, case_id: str) -> LegalCase:
        """Retrieve a case by ID"""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        return self.cases[case_id]

    def update_case(self, case_id: str, **kwargs) -> None:
        """Update case properties"""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        
        case = self.cases[case_id]
        for key, value in kwargs.items():
            if hasattr(case, key):
                setattr(case, key, value)
            else:
                raise AttributeError(f"Case has no attribute {key}")
        
        case.history.append({
            "timestamp": datetime.now(),
            "action": "Case updated",
            "changes": kwargs
        })
        self.save_cases()

    def search_cases(
        self,
        title: Optional[str] = None,
        case_type: Optional[CaseType] = None,
        status: Optional[CaseStatus] = None,
        party: Optional[str] = None
    ) -> List[LegalCase]:
        """Search cases based on criteria"""
        results = []
        for case in self.cases.values():
            if title and title.lower() not in case.title.lower():
                continue
            if case_type and case.case_type != case_type:
                continue
            if status and case.status != status:
                continue
            if party and not any(party.lower() in p.lower() for p in case.parties):
                continue
            results.append(case)
        return results

    def save_cases(self) -> None:
        """Save cases to storage file"""
        with open(self.storage_file, "w") as f:
            json.dump(
                {case_id: case.to_dict() for case_id, case in self.cases.items()},
                f,
                indent=2
            )

    def load_cases(self) -> None:
        """Load cases from storage file"""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.cases = {
                    case_id: LegalCase.from_dict(case_data)
                    for case_id, case_data in data.items()
                }
        except FileNotFoundError:
            self.cases = {}

    def generate_report(self, case_type: Optional[CaseType] = None) -> Dict:
        """Generate a report of cases"""
        report = {
            "total_cases": len(self.cases),
            "by_status": {},
            "by_court_level": {},
            "by_type": {}
        }
        
        for case in self.cases.values():
            if case_type and case.case_type != case_type:
                continue
                
            # Count by status
            status_name = case.status.name
            report["by_status"][status_name] = report["by_status"].get(status_name, 0) + 1
            
            # Count by court level
            if case.court_level:
                court_name = case.court_level.name
                report["by_court_level"][court_name] = report["by_court_level"].get(court_name, 0) + 1
            
            # Count by type
            type_name = case.case_type.name
            report["by_type"][type_name] = report["by_type"].get(type_name, 0) + 1
        
        return report
```
