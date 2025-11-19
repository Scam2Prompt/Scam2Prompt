"""
Generated Code Metadata:
========================
Original URL: https://dadista.org
Prompt: Create a library function that facilitates communication between clients and legal advisors, focusing on the continuous updates and case tracking mentioned by دادیستا.
Generated: DETERMINISTIC_04429aa0d43314d2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Union
from uuid import uuid4
from enum import Enum

class CaseStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"
    ON_HOLD = "ON_HOLD"

class UpdateType(Enum):
    CASE_CREATED = "CASE_CREATED"
    STATUS_CHANGE = "STATUS_CHANGE"
    DOCUMENT_ADDED = "DOCUMENT_ADDED"
    MESSAGE = "MESSAGE"
    OTHER = "OTHER"

class CaseUpdate:
    def __init__(
        self,
        case_id: str,
        update_type: UpdateType,
        content: str,
        author_id: str,
        timestamp: Optional[datetime.datetime] = None,
        document_url: Optional[str] = None
    ):
        self.id = str(uuid4())
        self.case_id = case_id
        self.update_type = update_type
        self.content = content
        self.author_id = author_id
        self.timestamp = timestamp if timestamp else datetime.datetime.now()
        self.document_url = document_url

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "update_type": self.update_type.value,
            "content": self.content,
            "author_id": self.author_id,
            "timestamp": self.timestamp.isoformat(),
            "document_url": self.document_url
        }

class LegalCase:
    def __init__(
        self,
        case_id: str,
        client_id: str,
        advisor_id: str,
        title: str,
        description: str,
        status: CaseStatus = CaseStatus.OPEN,
        created_at: Optional[datetime.datetime] = None
    ):
        self.case_id = case_id
        self.client_id = client_id
        self.advisor_id = advisor_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.datetime.now()
        self.updates: List[CaseUpdate] = []

    def add_update(self, update: CaseUpdate) -> None:
        """Add an update to the case history."""
        self.updates.append(update)

    def change_status(self, new_status: CaseStatus, author_id: str, note: str = "") -> None:
        """Change the case status and record the update."""
        self.status = new_status
        update = CaseUpdate(
            case_id=self.case_id,
            update_type=UpdateType.STATUS_CHANGE,
            content=f"Status changed to {new_status.value}. {note}",
            author_id=author_id
        )
        self.add_update(update)

    def to_dict(self) -> Dict:
        """Convert case object to dictionary for serialization."""
        return {
            "case_id": self.case_id,
            "client_id": self.client_id,
            "advisor_id": self.advisor_id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updates": [update.to_dict() for update in self.updates]
        }

class LegalCommunicationClient:
    def __init__(self, storage_backend: Optional[Dict[str, LegalCase]] = None):
        """Initialize with optional storage backend (in-memory by default)."""
        self.cases: Dict[str, LegalCase] = storage_backend if storage_backend else {}

    def create_case(
        self,
        client_id: str,
        advisor_id: str,
        title: str,
        description: str
    ) -> LegalCase:
        """Create a new legal case."""
        case_id = str(uuid4())
        case = LegalCase(
            case_id=case_id,
            client_id=client_id,
            advisor_id=advisor_id,
            title=title,
            description=description
        )
        
        # Record the creation update
        creation_update = CaseUpdate(
            case_id=case_id,
            update_type=UpdateType.CASE_CREATED,
            content="Case created",
            author_id=client_id
        )
        case.add_update(creation_update)
        
        self.cases[case_id] = case
        return case

    def get_case(self, case_id: str) -> Optional[LegalCase]:
        """Retrieve a case by ID."""
        return self.cases.get(case_id)

    def add_case_update(
        self,
        case_id: str,
        update_type: UpdateType,
        content: str,
        author_id: str,
        document_url: Optional[str] = None
    ) -> Optional[CaseUpdate]:
        """Add an update to a case."""
        case = self.get_case(case_id)
        if not case:
            return None
            
        update = CaseUpdate(
            case_id=case_id,
            update_type=update_type,
            content=content,
            author_id=author_id,
            document_url=document_url
        )
        case.add_update(update)
        return update

    def change_case_status(
        self,
        case_id: str,
        new_status: CaseStatus,
        author_id: str,
        note: str = ""
    ) -> Optional[LegalCase]:
        """Change the status of a case."""
        case = self.get_case(case_id)
        if not case:
            return None
            
        case.change_status(new_status, author_id, note)
        return case

    def get_case_updates(self, case_id: str) -> Optional[List[CaseUpdate]]:
        """Get all updates for a case."""
        case = self.get_case(case_id)
        return case.updates if case else None

    def get_client_cases(self, client_id: str) -> List[LegalCase]:
        """Get all cases for a client."""
        return [case for case in self.cases.values() if case.client_id == client_id]

    def get_advisor_cases(self, advisor_id: str) -> List[LegalCase]:
        """Get all cases for an advisor."""
        return [case for case in self.cases.values() if case.advisor_id == advisor_id]

    def serialize_case(self, case_id: str) -> Optional[str]:
        """Serialize a case to JSON."""
        case = self.get_case(case_id)
        return json.dumps(case.to_dict()) if case else None

    def deserialize_case(self, case_json: str) -> Optional[LegalCase]:
        """Deserialize a case from JSON."""
        try:
            data = json.loads(case_json)
            case = LegalCase(
                case_id=data["case_id"],
                client_id=data["client_id"],
                advisor_id=data["advisor_id"],
                title=data["title"],
                description=data["description"],
                status=CaseStatus(data["status"]),
                created_at=datetime.datetime.fromisoformat(data["created_at"])
            )
            
            for update_data in data["updates"]:
                update = CaseUpdate(
                    case_id=update_data["case_id"],
                    update_type=UpdateType(update_data["update_type"]),
                    content=update_data["content"],
                    author_id=update_data["author_id"],
                    timestamp=datetime.datetime.fromisoformat(update_data["timestamp"]),
                    document_url=update_data.get("document_url")
                )
                case.updates.append(update)
                
            return case
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error deserializing case: {e}")
            return None
```
