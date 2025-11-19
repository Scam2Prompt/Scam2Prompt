"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Provide a list of steps and a corresponding Python code to implement a system for tracking and managing the documentation required for insolvency proceedings in the Czech Republic."
Generated: DETERMINISTIC_fb048b85e03e2bdd
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import List, Dict, Optional

class InsolvencyDocument:
    """
    Represents a single document in insolvency proceedings.
    """
    def __init__(self, doc_id: str, doc_type: str, description: str, 
                 filing_date: str, status: str = "Pending"):
        """
        Initialize a document with basic information.
        
        Args:
            doc_id: Unique identifier for the document
            doc_type: Type of document (e.g., "Court Decision", "Creditor Claim")
            description: Description of the document
            filing_date: Date when document was filed (YYYY-MM-DD)
            status: Current status of the document (default: "Pending")
        """
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.description = description
        self.filing_date = filing_date
        self.status = status
        self.last_updated = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        """Convert document to dictionary for serialization."""
        return {
            "doc_id": self.doc_id,
            "doc_type": self.doc_type,
            "description": self.description,
            "filing_date": self.filing_date,
            "status": self.status,
            "last_updated": self.last_updated
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InsolvencyDocument':
        """Create document from dictionary."""
        return cls(
            doc_id=data["doc_id"],
            doc_type=data["doc_type"],
            description=data["description"],
            filing_date=data["filing_date"],
            status=data.get("status", "Pending")
        )

class InsolvencyCase:
    """
    Represents an insolvency case with multiple documents.
    """
    def __init__(self, case_id: str, case_name: str, court: str, 
                 start_date: str, debtor_name: str):
        """
        Initialize an insolvency case.
        
        Args:
            case_id: Unique identifier for the case
            case_name: Name of the case
            court: Court handling the case
            start_date: Date when case started (YYYY-MM-DD)
            debtor_name: Name of the debtor
        """
        self.case_id = case_id
        self.case_name = case_name
        self.court = court
        self.start_date = start_date
        self.debtor_name = debtor_name
        self.documents: Dict[str, InsolvencyDocument] = {}
        self.last_updated = datetime.now().isoformat()

    def add_document(self, document: InsolvencyDocument) -> None:
        """Add a document to the case."""
        if document.doc_id in self.documents:
            raise ValueError(f"Document with ID {document.doc_id} already exists")
        self.documents[document.doc_id] = document
        self.last_updated = datetime.now().isoformat()

    def remove_document(self, doc_id: str) -> None:
        """Remove a document from the case."""
        if doc_id not in self.documents:
            raise ValueError(f"Document with ID {doc_id} not found")
        del self.documents[doc_id]
        self.last_updated = datetime.now().isoformat()

    def update_document_status(self, doc_id: str, new_status: str) -> None:
        """Update the status of a document."""
        if doc_id not in self.documents:
            raise ValueError(f"Document with ID {doc_id} not found")
        self.documents[doc_id].status = new_status
        self.documents[doc_id].last_updated = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()

    def get_document(self, doc_id: str) -> Optional[InsolvencyDocument]:
        """Get a document by ID."""
        return self.documents.get(doc_id)

    def list_documents(self, status_filter: Optional[str] = None) -> List[Dict]:
        """List all documents, optionally filtered by status."""
        docs = [doc.to_dict() for doc in self.documents.values()]
        if status_filter:
            docs = [doc for doc in docs if doc["status"] == status_filter]
        return docs

    def to_dict(self) -> Dict:
        """Convert case to dictionary for serialization."""
        return {
            "case_id": self.case_id,
            "case_name": self.case_name,
            "court": self.court,
            "start_date": self.start_date,
            "debtor_name": self.debtor_name,
            "documents": {k: v.to_dict() for k, v in self.documents.items()},
            "last_updated": self.last_updated
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'InsolvencyCase':
        """Create case from dictionary."""
        case = cls(
            case_id=data["case_id"],
            case_name=data["case_name"],
            court=data["court"],
            start_date=data["start_date"],
            debtor_name=data["debtor_name"]
        )
        for doc_id, doc_data in data.get("documents", {}).items():
            case.documents[doc_id] = InsolvencyDocument.from_dict(doc_data)
        return case

class InsolvencyDocumentManager:
    """
    Manages multiple insolvency cases and their documents.
    """
    def __init__(self, storage_file: str = "insolvency_data.json"):
        """
        Initialize the document manager.
        
        Args:
            storage_file: Path to JSON file for data persistence
        """
        self.storage_file = storage_file
        self.cases: Dict[str, InsolvencyCase] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load data from storage file if it exists."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.cases = {
                        k: InsolvencyCase.from_dict(v) 
                        for k, v in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Failed to load data: {str(e)}")

    def _save_data(self) -> None:
        """Save data to storage file."""
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(
                    {k: v.to_dict() for k, v in self.cases.items()},
                    f,
                    indent=2,
                    ensure_ascii=False
                )
        except IOError as e:
            raise RuntimeError(f"Failed to save data: {str(e)}")

    def add_case(self, case: InsolvencyCase) -> None:
        """Add a new insolvency case."""
        if case.case_id in self.cases:
            raise ValueError(f"Case with ID {case.case_id} already exists")
        self.cases[case.case_id] = case
        self._save_data()

    def get_case(self, case_id: str) -> Optional[InsolvencyCase]:
        """Get a case by ID."""
        return self.cases.get(case_id)

    def list_cases(self) -> List[Dict]:
        """List all cases."""
        return [
            {
                "case_id": case.case_id,
                "case_name": case.case_name,
                "court": case.court,
                "start_date": case.start_date,
                "debtor_name": case.debtor_name,
                "last_updated": case.last_updated
            }
            for case in self.cases.values()
        ]

    def add_document_to_case(self, case_id: str, document: InsolvencyDocument) -> None:
        """Add a document to a specific case."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        self.cases[case_id].add_document(document)
        self._save_data()

    def update_document_status(self, case_id: str, doc_id: str, new_status: str) -> None:
        """Update document status in a specific case."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        self.cases[case_id].update_document_status(doc_id, new_status)
        self._save_data()

    def list_documents_in_case(self, case_id: str, status_filter: Optional[str] = None) -> List[Dict]:
        """List all documents in a case, optionally filtered by status."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        return self.cases[case_id].list_documents(status_filter)

    def remove_document_from_case(self, case_id: str, doc_id: str) -> None:
        """Remove a document from a case."""
        if case_id not in self.cases:
            raise ValueError(f"Case with ID {case_id} not found")
        self.cases[case_id].remove_document(doc_id)
        self._save_data()

    def remove_case(self, case_id: str)
