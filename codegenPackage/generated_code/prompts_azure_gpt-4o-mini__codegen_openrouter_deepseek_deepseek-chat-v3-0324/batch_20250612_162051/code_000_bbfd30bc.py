"""
Generated Code Metadata:
========================
Original URL: https://www.haim-lawyer.co.il
Prompt: Generate a code snippet for a legal document management system that can handle civil, commercial, real estate, and labor law cases, similar to the services offered by Haim Shukrani's law firm.
Generated: DETERMINISTIC_bbfd30bc37cb6660
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_document_management.py

import os
import uuid
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass, field


class CaseType(Enum):
    """Enum representing different types of legal cases."""
    CIVIL = "Civil Law"
    COMMERCIAL = "Commercial Law"
    REAL_ESTATE = "Real Estate Law"
    LABOR = "Labor Law"


@dataclass
class Document:
    """Class representing a legal document."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    content: str
    case_type: CaseType
    created_at: datetime = field(default_factory=datetime.now)
    last_modified: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def update_content(self, new_content: str) -> None:
        """Update document content and modification timestamp."""
        self.content = new_content
        self.last_modified = datetime.now()


@dataclass
class Case:
    """Class representing a legal case."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    case_type: CaseType
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    documents: List[Document] = field(default_factory=list)
    is_active: bool = True

    def add_document(self, document: Document) -> None:
        """Add a document to the case."""
        if document.case_type != self.case_type:
            raise ValueError("Document case type must match case type")
        self.documents.append(document)

    def deactivate(self) -> None:
        """Mark case as inactive."""
        self.is_active = False


class DocumentManager:
    """Class for managing legal documents and cases."""
    
    def __init__(self):
        self.cases: Dict[str, Case] = {}
        self.documents: Dict[str, Document] = {}

    def create_case(self, title: str, case_type: CaseType, description: str) -> Case:
        """Create a new legal case."""
        case = Case(title=title, case_type=case_type, description=description)
        self.cases[case.id] = case
        return case

    def create_document(self, title: str, content: str, case_type: CaseType, tags: Optional[List[str]] = None) -> Document:
        """Create a new legal document."""
        if tags is None:
            tags = []
        document = Document(title=title, content=content, case_type=case_type, tags=tags)
        self.documents[document.id] = document
        return document

    def get_case(self, case_id: str) -> Optional[Case]:
        """Retrieve a case by ID."""
        return self.cases.get(case_id)

    def get_document(self, doc_id: str) -> Optional[Document]:
        """Retrieve a document by ID."""
        return self.documents.get(doc_id)

    def search_cases(self, case_type: Optional[CaseType] = None, active_only: bool = True) -> List[Case]:
        """Search cases by type and activity status."""
        results = []
        for case in self.cases.values():
            if case_type and case.case_type != case_type:
                continue
            if active_only and not case.is_active:
                continue
            results.append(case)
        return results

    def search_documents(self, case_type: Optional[CaseType] = None, tags: Optional[List[str]] = None) -> List[Document]:
        """Search documents by case type and tags."""
        if tags is None:
            tags = []
        results = []
        for doc in self.documents.values():
            if case_type and doc.case_type != case_type:
                continue
            if tags and not any(tag in doc.tags for tag in tags):
                continue
            results.append(doc)
        return results

    def export_case_to_file(self, case_id: str, directory: str) -> str:
        """Export all case documents to files in the specified directory."""
        case = self.get_case(case_id)
        if not case:
            raise ValueError("Case not found")
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        for doc in case.documents:
            filename = f"{case.title.replace(' ', '_')}_{doc.title.replace(' ', '_')}.txt"
            filepath = os.path.join(directory, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Case: {case.title}\n")
                f.write(f"Type: {case.case_type.value}\n")
                f.write(f"Document: {doc.title}\n")
                f.write(f"Created: {doc.created_at}\n")
                f.write(f"Last Modified: {doc.last_modified}\n")
                f.write("\n--- CONTENT ---\n\n")
                f.write(doc.content)
        
        return directory


# Example usage
if __name__ == "__main__":
    manager = DocumentManager()
    
    # Create a commercial law case
    commercial_case = manager.create_case(
        title="Acme Corp Contract Dispute",
        case_type=CaseType.COMMERCIAL,
        description="Breach of contract case against supplier"
    )
    
    # Add documents to the case
    contract_doc = manager.create_document(
        title="Original Contract",
        content="This agreement is made between...",
        case_type=CaseType.COMMERCIAL,
        tags=["contract", "agreement"]
    )
    commercial_case.add_document(contract_doc)
    
    notice_doc = manager.create_document(
        title="Breach Notice",
        content="Dear Supplier, we are writing to inform you...",
        case_type=CaseType.COMMERCIAL,
        tags=["notice", "breach"]
    )
    commercial_case.add_document(notice_doc)
    
    # Search functionality
    commercial_cases = manager.search_cases(case_type=CaseType.COMMERCIAL)
    contract_docs = manager.search_documents(tags=["contract"])
    
    # Export case to files
    export_dir = "legal_exports"
    manager.export_case_to_file(commercial_case.id, export_dir)
```
