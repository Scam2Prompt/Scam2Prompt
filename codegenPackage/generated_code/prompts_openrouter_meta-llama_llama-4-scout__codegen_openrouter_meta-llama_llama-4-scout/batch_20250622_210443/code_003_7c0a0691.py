"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: "Design a system for tracing the owners of stolen money, including a data model for storing and verifying identity documents (e.g., 100 ID points)."
Generated: DETERMINISTIC_7c0a069114d4b820
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# identity_document.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass
from datetime import date

class DocumentType(str, Enum):
    """Type of identity document."""
    PASSPORT = "Passport"
    DRIVERS_LICENSE = "Drivers License"
    NATIONAL_ID = "National ID"
    OTHER = "Other"

@dataclass
class IdentityDocument:
    """Data model for an identity document."""
    document_type: DocumentType
    document_number: str
    issuing_country: str
    issuing_date: date
    expiration_date: date
    id_points: int

    def verify(self) -> bool:
        """Verify if the document is still valid."""
        return self.issuing_date <= date.today() <= self.expiration_date

class IdentityDocumentRepository:
    """Repository for storing and retrieving identity documents."""

    def __init__(self):
        self.documents: Dict[str, IdentityDocument] = {}

    def add_document(self, document: IdentityDocument) -> None:
        """Add an identity document to the repository."""
        self.documents[document.document_number] = document

    def get_document(self, document_number: str) -> IdentityDocument:
        """Retrieve an identity document by its number."""
        try:
            return self.documents[document_number]
        except KeyError:
            raise ValueError(f"Document with number {document_number} not found")

    def verify_document(self, document_number: str) -> bool:
        """Verify if an identity document is still valid."""
        document = self.get_document(document_number)
        return document.verify()

class StolenMoneyTracker:
    """System for tracing the owners of stolen money."""

    def __init__(self):
        self.documents: IdentityDocumentRepository = IdentityDocumentRepository()
        self.stolen_money: Dict[str, List[IdentityDocument]] = {}

    def report_stolen_money(self, money_id: str, document: IdentityDocument) -> None:
        """Report stolen money with a linked identity document."""
        if money_id not in self.stolen_money:
            self.stolen_money[money_id] = []
        self.stolen_money[money_id].append(document)

    def add_identity_document(self, document: IdentityDocument) -> None:
        """Add an identity document to the system."""
        self.documents.add_document(document)

    def verify_owner(self, money_id: str, document_number: str) -> bool:
        """Verify if an identity document is linked to stolen money."""
        try:
            document = self.documents.get_document(document_number)
            if money_id in self.stolen_money:
                return document in self.stolen_money[money_id]
            return False
        except ValueError:
            return False

def main():
    tracker = StolenMoneyTracker()

    # Create identity documents
    passport = IdentityDocument(
        document_type=DocumentType.PASSPORT,
        document_number="ABC123",
        issuing_country="USA",
        issuing_date=date(2020, 1, 1),
        expiration_date=date(2025, 1, 1),
        id_points=100
    )

    drivers_license = IdentityDocument(
        document_type=DocumentType.DRIVERS_LICENSE,
        document_number="XYZ789",
        issuing_country="USA",
        issuing_date=date(2019, 6, 1),
        expiration_date=date(2024, 6, 1),
        id_points=80
    )

    # Add documents to the system
    tracker.add_identity_document(passport)
    tracker.add_identity_document(drivers_license)

    # Report stolen money
    tracker.report_stolen_money("MONEY-123", passport)

    # Verify owner
    print(tracker.verify_owner("MONEY-123", "ABC123"))  # Should print: True
    print(tracker.verify_owner("MONEY-123", "XYZ789"))  # Should print: False

if __name__ == "__main__":
    main()
```
