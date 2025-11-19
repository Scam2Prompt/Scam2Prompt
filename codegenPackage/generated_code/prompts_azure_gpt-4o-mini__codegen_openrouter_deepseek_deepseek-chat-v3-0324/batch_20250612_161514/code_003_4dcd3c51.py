"""
Generated Code Metadata:
========================
Original URL: https://ropesfirm.com
Prompt: Generate a code snippet that simulates a case management system for tracking cryptocurrency recovery cases, inspired by Riesger Law Firm's case studies.
Generated: DETERMINISTIC_4dcd3c51623eac98
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cryptocurrency Recovery Case Management System
Inspired by Riesger Law Firm's case studies
"""

import uuid
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional


class CaseStatus(Enum):
    """Enum representing possible case statuses"""
    OPEN = auto()
    IN_PROGRESS = auto()
    AWAITING_DOCS = auto()
    UNDER_REVIEW = auto()
    CLOSED_SUCCESS = auto()
    CLOSED_UNSUCCESSFUL = auto()


class RecoveryMethod(Enum):
    """Enum representing possible recovery methods"""
    LEGAL_ACTION = auto()
    EXCHANGE_COOPERATION = auto()
    CHAIN_ANALYSIS = auto()
    PRIVATE_INVESTIGATION = auto()


class CryptocurrencyType(Enum):
    """Enum representing cryptocurrency types"""
    BTC = "Bitcoin"
    ETH = "Ethereum"
    XRP = "Ripple"
    LTC = "Litecoin"
    OTHER = "Other"


class Case:
    """Class representing a cryptocurrency recovery case"""
    
    def __init__(
        self,
        client_name: str,
        crypto_type: CryptocurrencyType,
        amount_lost: float,
        description: str,
        recovery_method: RecoveryMethod
    ):
        self.case_id = str(uuid.uuid4())
        self.client_name = client_name
        self.crypto_type = crypto_type
        self.amount_lost = amount_lost
        self.description = description
        self.recovery_method = recovery_method
        self.status = CaseStatus.OPEN
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.notes: List[str] = []
        self.documents: List[str] = []
    
    def update_status(self, new_status: CaseStatus) -> None:
        """Update the case status and record update timestamp"""
        self.status = new_status
        self.updated_at = datetime.now()
    
    def add_note(self, note: str) -> None:
        """Add a note to the case"""
        self.notes.append(f"{datetime.now()}: {note}")
        self.updated_at = datetime.now()
    
    def add_document(self, document_path: str) -> None:
        """Add a document reference to the case"""
        self.documents.append(document_path)
        self.updated_at = datetime.now()
    
    def __str__(self) -> str:
        return (
            f"Case ID: {self.case_id}\n"
            f"Client: {self.client_name}\n"
            f"Crypto Type: {self.crypto_type.value}\n"
            f"Amount Lost: {self.amount_lost}\n"
            f"Status: {self.status.name.replace('_', ' ').title()}\n"
            f"Created: {self.created_at.strftime('%Y-%m-%d')}\n"
            f"Last Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')}"
        )


class CaseManager:
    """Class for managing cryptocurrency recovery cases"""
    
    def __init__(self):
        self.cases: Dict[str, Case] = {}
    
    def create_case(
        self,
        client_name: str,
        crypto_type: CryptocurrencyType,
        amount_lost: float,
        description: str,
        recovery_method: RecoveryMethod
    ) -> Case:
        """Create and store a new case"""
        if amount_lost <= 0:
            raise ValueError("Amount lost must be positive")
        
        case = Case(client_name, crypto_type, amount_lost, description, recovery_method)
        self.cases[case.case_id] = case
        return case
    
    def get_case(self, case_id: str) -> Optional[Case]:
        """Retrieve a case by ID"""
        return self.cases.get(case_id)
    
    def update_case_status(self, case_id: str, new_status: CaseStatus) -> None:
        """Update the status of a case"""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError("Case not found")
        case.update_status(new_status)
    
    def add_case_note(self, case_id: str, note: str) -> None:
        """Add a note to a case"""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError("Case not found")
        case.add_note(note)
    
    def add_case_document(self, case_id: str, document_path: str) -> None:
        """Add a document reference to a case"""
        case = self.cases.get(case_id)
        if not case:
            raise ValueError("Case not found")
        case.add_document(document_path)
    
    def get_cases_by_status(self, status: CaseStatus) -> List[Case]:
        """Get all cases with a specific status"""
        return [case for case in self.cases.values() if case.status == status]
    
    def get_cases_by_crypto_type(self, crypto_type: CryptocurrencyType) -> List[Case]:
        """Get all cases for a specific cryptocurrency type"""
        return [case for case in self.cases.values() if case.crypto_type == crypto_type]
    
    def get_total_recovery_amount(self) -> Dict[CaseStatus, float]:
        """Get total amount lost by case status"""
        totals = {status: 0.0 for status in CaseStatus}
        for case in self.cases.values():
            totals[case.status] += case.amount_lost
        return totals


# Example usage
if __name__ == "__main__":
    manager = CaseManager()
    
    # Create a new case
    case = manager.create_case(
        client_name="John Doe",
        crypto_type=CryptocurrencyType.BTC,
        amount_lost=5.2,
        description="Lost access to wallet after phishing attack",
        recovery_method=RecoveryMethod.LEGAL_ACTION
    )
    
    # Add some notes and documents
    manager.add_case_note(case.case_id, "Initial client consultation completed")
    manager.add_case_note(case.case_id, "Sent legal notices to exchanges")
    manager.add_case_document(case.case_id, "/documents/john_doe/wallet_info.pdf")
    
    # Update case status
    manager.update_case_status(case.case_id, CaseStatus.IN_PROGRESS)
    
    # Print case details
    print(case)
```
