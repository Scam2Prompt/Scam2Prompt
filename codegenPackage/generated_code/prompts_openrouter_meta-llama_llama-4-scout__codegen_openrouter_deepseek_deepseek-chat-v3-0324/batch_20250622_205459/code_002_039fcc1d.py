"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Generate a code example for claims registration and management in the insurance industry, inspired by KEK Insurance Brokers' claims consulting services and swift premiums and claims settlement.
Generated: DETERMINISTIC_039fcc1d7fc705b4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Insurance Claims Management System
Inspired by KEK Insurance Brokers' services
"""

from datetime import datetime
from typing import List, Dict, Optional
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ClaimStatus(Enum):
    """Enum representing possible claim statuses"""
    REGISTERED = "Registered"
    UNDER_REVIEW = "Under Review"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    SETTLED = "Settled"


class Claim:
    """Class representing an insurance claim"""
    
    def __init__(
        self,
        policy_number: str,
        claimant_name: str,
        claim_type: str,
        claim_amount: float,
        incident_date: datetime,
        description: str
    ):
        self.claim_id = str(uuid.uuid4())
        self.policy_number = policy_number
        self.claimant_name = claimant_name
        self.claim_type = claim_type
        self.claim_amount = claim_amount
        self.incident_date = incident_date
        self.description = description
        self.status = ClaimStatus.REGISTERED
        self.registration_date = datetime.now()
        self.last_updated = datetime.now()
        self.documents: List[str] = []
        self.notes: List[str] = []
        
    def update_status(self, new_status: ClaimStatus, note: Optional[str] = None) -> None:
        """Update the claim status and add optional note"""
        self.status = new_status
        self.last_updated = datetime.now()
        if note:
            self.notes.append(f"{datetime.now()}: {note}")
        logger.info(f"Claim {self.claim_id} status updated to {new_status.value}")


class ClaimsManager:
    """Class for managing insurance claims"""
    
    def __init__(self):
        self.claims: Dict[str, Claim] = {}
        
    def register_claim(
        self,
        policy_number: str,
        claimant_name: str,
        claim_type: str,
        claim_amount: float,
        incident_date: datetime,
        description: str
    ) -> Claim:
        """Register a new claim"""
        try:
            claim = Claim(
                policy_number=policy_number,
                claimant_name=claimant_name,
                claim_type=claim_type,
                claim_amount=claim_amount,
                incident_date=incident_date,
                description=description
            )
            self.claims[claim.claim_id] = claim
            logger.info(f"New claim registered: {claim.claim_id}")
            return claim
        except Exception as e:
            logger.error(f"Error registering claim: {str(e)}")
            raise
            
    def get_claim(self, claim_id: str) -> Optional[Claim]:
        """Retrieve a claim by ID"""
        return self.claims.get(claim_id)
    
    def update_claim_status(
        self,
        claim_id: str,
        new_status: ClaimStatus,
        note: Optional[str] = None
    ) -> bool:
        """Update the status of a claim"""
        claim = self.claims.get(claim_id)
        if not claim:
            logger.warning(f"Claim {claim_id} not found")
            return False
            
        try:
            claim.update_status(new_status, note)
            return True
        except Exception as e:
            logger.error(f"Error updating claim status: {str(e)}")
            return False
    
    def add_document_to_claim(self, claim_id: str, document_path: str) -> bool:
        """Add supporting document to a claim"""
        claim = self.claims.get(claim_id)
        if not claim:
            logger.warning(f"Claim {claim_id} not found")
            return False
            
        try:
            claim.documents.append(document_path)
            claim.last_updated = datetime.now()
            logger.info(f"Document added to claim {claim_id}")
            return True
        except Exception as e:
            logger.error(f"Error adding document: {str(e)}")
            return False
    
    def settle_claim(self, claim_id: str, settlement_amount: float) -> bool:
        """Settle a claim with given amount"""
        claim = self.claims.get(claim_id)
        if not claim:
            logger.warning(f"Claim {claim_id} not found")
            return False
            
        try:
            if settlement_amount > 0:
                claim.update_status(ClaimStatus.SETTLED, f"Settled for {settlement_amount}")
                logger.info(f"Claim {claim_id} settled for {settlement_amount}")
                return True
            else:
                logger.warning("Settlement amount must be positive")
                return False
        except Exception as e:
            logger.error(f"Error settling claim: {str(e)}")
            return False
    
    def get_claims_by_status(self, status: ClaimStatus) -> List[Claim]:
        """Get all claims with given status"""
        return [claim for claim in self.claims.values() if claim.status == status]
    
    def get_claims_by_policy(self, policy_number: str) -> List[Claim]:
        """Get all claims for a specific policy"""
        return [
            claim for claim in self.claims.values()
            if claim.policy_number == policy_number
        ]


# Example usage
if __name__ == "__main__":
    manager = ClaimsManager()
    
    # Register a new claim
    new_claim = manager.register_claim(
        policy_number="POL123456",
        claimant_name="John Doe",
        claim_type="Auto Accident",
        claim_amount=5000.00,
        incident_date=datetime(2023, 5, 15),
        description="Rear-end collision at Main Street intersection"
    )
    
    # Add supporting document
    manager.add_document_to_claim(new_claim.claim_id, "/documents/police_report.pdf")
    
    # Update claim status
    manager.update_claim_status(
        new_claim.claim_id,
        ClaimStatus.UNDER_REVIEW,
        "Initial review completed"
    )
    
    # Settle the claim
    manager.settle_claim(new_claim.claim_id, 4500.00)
    
    # Retrieve settled claims
    settled_claims = manager.get_claims_by_status(ClaimStatus.SETTLED)
    print(f"Total settled claims: {len(settled_claims)}")
```
