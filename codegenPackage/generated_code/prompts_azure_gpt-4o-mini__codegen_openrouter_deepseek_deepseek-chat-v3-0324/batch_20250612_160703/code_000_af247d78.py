"""
Generated Code Metadata:
========================
Original URL: https://blocichain.com
Prompt: Generate a Python script that demonstrates how to securely manage domain rental agreements, including payment tracking and compliance with legal regulations.
Generated: DETERMINISTIC_af247d787cddea71
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import uuid
import os
from abc import ABC, abstractmethod

# Constants
LEGAL_REQUIREMENTS = {
    "privacy_policy": True,
    "terms_of_service": True,
    "refund_policy": True,
    "data_protection": True
}

class DomainRentalAgreement:
    """Class representing a domain rental agreement."""
    
    def __init__(
        self,
        domain_name: str,
        renter_id: str,
        owner_id: str,
        start_date: str,
        end_date: str,
        monthly_price: float,
        payment_terms: str = "monthly"
    ):
        """
        Initialize a domain rental agreement.
        
        Args:
            domain_name: Name of the domain being rented
            renter_id: Unique identifier for the renter
            owner_id: Unique identifier for the domain owner
            start_date: Start date of the rental (YYYY-MM-DD)
            end_date: End date of the rental (YYYY-MM-DD)
            monthly_price: Monthly rental price
            payment_terms: Payment frequency (default: monthly)
        """
        self.agreement_id = str(uuid.uuid4())
        self.domain_name = domain_name
        self.renter_id = renter_id
        self.owner_id = owner_id
        self.start_date = start_date
        self.end_date = end_date
        self.monthly_price = monthly_price
        self.payment_terms = payment_terms
        self.payments = []
        self.compliance_checks = LEGAL_REQUIREMENTS.copy()
        self.created_at = datetime.now().isoformat()
        self.last_updated = self.created_at
        
    def add_payment(self, amount: float, payment_date: str, payment_method: str) -> bool:
        """
        Record a payment for this agreement.
        
        Args:
            amount: Payment amount
            payment_date: Date of payment (YYYY-MM-DD)
            payment_method: Payment method used
            
        Returns:
            bool: True if payment was recorded successfully
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
            
        payment = {
            "payment_id": str(uuid.uuid4()),
            "amount": amount,
            "payment_date": payment_date,
            "payment_method": payment_method,
            "recorded_at": datetime.now().isoformat()
        }
        
        self.payments.append(payment)
        self.last_updated = datetime.now().isoformat()
        return True
        
    def check_compliance(self) -> Dict[str, bool]:
        """
        Check if the agreement meets all legal requirements.
        
        Returns:
            Dict[str, bool]: Dictionary of compliance checks and their status
        """
        return self.compliance_checks
        
    def to_dict(self) -> Dict:
        """Convert the agreement to a dictionary for serialization."""
        return {
            "agreement_id": self.agreement_id,
            "domain_name": self.domain_name,
            "renter_id": self.renter_id,
            "owner_id": self.owner_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "monthly_price": self.monthly_price,
            "payment_terms": self.payment_terms,
            "payments": self.payments,
            "compliance_checks": self.compliance_checks,
            "created_at": self.created_at,
            "last_updated": self.last_updated
        }
        
    @classmethod
    def from_dict(cls, data: Dict):
        """Create an agreement from a dictionary."""
        agreement = cls(
            data["domain_name"],
            data["renter_id"],
            data["owner_id"],
            data["start_date"],
            data["end_date"],
            data["monthly_price"],
            data.get("payment_terms", "monthly")
        )
        
        agreement.agreement_id = data["agreement_id"]
        agreement.payments = data.get("payments", [])
        agreement.compliance_checks = data.get("compliance_checks", LEGAL_REQUIREMENTS.copy())
        agreement.created_at = data["created_at"]
        agreement.last_updated = data.get("last_updated", data["created_at"])
        
        return agreement

class PaymentTracker:
    """Class for tracking payments across multiple agreements."""
    
    def __init__(self):
        self.agreements = {}
        
    def add_agreement(self, agreement: DomainRentalAgreement) -> bool:
        """Add an agreement to be tracked."""
        if agreement.agreement_id in self.agreements:
            raise ValueError("Agreement already exists")
            
        self.agreements[agreement.agreement_id] = agreement
        return True
        
    def record_payment(
        self,
        agreement_id: str,
        amount: float,
        payment_date: str,
        payment_method: str
    ) -> bool:
        """
        Record a payment for a specific agreement.
        
        Args:
            agreement_id: ID of the agreement
            amount: Payment amount
            payment_date: Date of payment (YYYY-MM-DD)
            payment_method: Payment method used
            
        Returns:
            bool: True if payment was recorded successfully
        """
        if agreement_id not in self.agreements:
            raise ValueError("Agreement not found")
            
        return self.agreements[agreement_id].add_payment(
            amount, payment_date, payment_method
        )
        
    def get_payment_history(self, agreement_id: str) -> List[Dict]:
        """
        Get payment history for an agreement.
        
        Args:
            agreement_id: ID of the agreement
            
        Returns:
            List[Dict]: List of payment records
        """
        if agreement_id not in self.agreements:
            raise ValueError("Agreement not found")
            
        return self.agreements[agreement_id].payments
        
    def check_agreement_compliance(self, agreement_id: str) -> Dict[str, bool]:
        """
        Check compliance for a specific agreement.
        
        Args:
            agreement_id: ID of the agreement
            
        Returns:
            Dict[str, bool]: Compliance check results
        """
        if agreement_id not in self.agreements:
            raise ValueError("Agreement not found")
            
        return self.agreements[agreement_id].check_compliance()

class StorageProvider(ABC):
    """Abstract base class for storage providers."""
    
    @abstractmethod
    def save_agreement(self, agreement: DomainRentalAgreement) -> bool:
        """Save an agreement to storage."""
        pass
        
    @abstractmethod
    def load_agreement(self, agreement_id: str) -> Optional[DomainRentalAgreement]:
        """Load an agreement from storage."""
        pass
        
    @abstractmethod
    def delete_agreement(self, agreement_id: str) -> bool:
        """Delete an agreement from storage."""
        pass

class FileStorageProvider(StorageProvider):
    """File-based storage provider for agreements."""
    
    def __init__(self, storage_dir: str = "agreements"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
        
    def _get_file_path(self, agreement_id: str) -> str:
        """Get the file path for an agreement."""
        return os.path.join(self.storage_dir, f"{agreement_id}.json")
        
    def save_agreement(self, agreement: DomainRentalAgreement) -> bool:
        """Save an agreement to a file."""
        file_path = self._get_file_path(agreement.agreement_id)
        
        try:
            with open(file_path, "w") as f:
                json.dump(agreement.to_dict(), f, indent=2)
            return True
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to save agreement: {str(e)}")
            
    def load_agreement(self, agreement_id: str) -> Optional[DomainRentalAgreement]:
        """Load an agreement from a file."""
        file_path = self._get_file_path(agreement_id)
        
        if not os.path.exists(file_path):
            return None
            
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            return DomainRentalAgreement.from_dict(data)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load agreement: {str(e)}")
            
    def delete_agreement(self, agreement_id: str) -> bool:
        """Delete an agreement file."""
        file_path = self._get_file_path(agreement_id)
        
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except IOError as e:
            raise RuntimeError(f"Failed to delete agreement: {str(e)}")

class DomainRentalManager:
    """Main class for managing domain rental agreements."""
    
    def __init__(self, storage_provider: StorageProvider = None):
        self.payment_tracker = PaymentTracker()
        self.storage_provider = storage_provider or FileStorageProvider()
        
    def create_agreement(
        self,
        domain_name: str,
        renter_id: str,
        owner
