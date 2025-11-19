"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Write Python code to simulate a claims management workflow for fraud recovery, including steps for case assessment, bank submission, and escalation to the Financial Ombudsman Service (FOS).
Generated: DETERMINISTIC_477a9abc3151fd8d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Optional, Dict, List
import random

class ClaimStatus(Enum):
    """Enum representing the possible statuses of a fraud claim."""
    RECEIVED = auto()
    UNDER_ASSESSMENT = auto()
    BANK_SUBMITTED = auto()
    BANK_REJECTED = auto()
    BANK_APPROVED = auto()
    FOS_ESCALATED = auto()
    FOS_RESOLVED = auto()
    CLOSED = auto()

class Claim:
    """Class representing a fraud claim."""
    
    def __init__(self, customer_id: str, claim_amount: float, description: str):
        self.claim_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.claim_amount = claim_amount
        self.description = description
        self.status = ClaimStatus.RECEIVED
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.assessment_notes: List[str] = []
        self.bank_reference: Optional[str] = None
        self.fos_reference: Optional[str] = None
    
    def update_status(self, new_status: ClaimStatus, notes: Optional[str] = None) -> None:
        """Update the status of the claim and add optional notes."""
        self.status = new_status
        self.updated_at = datetime.now()
        if notes:
            self.assessment_notes.append(f"{datetime.now()}: {notes}")
    
    def __str__(self) -> str:
        return (f"Claim ID: {self.claim_id}\n"
                f"Customer ID: {self.customer_id}\n"
                f"Amount: £{self.claim_amount:.2f}\n"
                f"Status: {self.status.name}\n"
                f"Created: {self.created_at}\n"
                f"Last Updated: {self.updated_at}")

class ClaimsManager:
    """Class to manage the fraud claims workflow."""
    
    def __init__(self):
        self.claims: Dict[str, Claim] = {}
    
    def create_claim(self, customer_id: str, claim_amount: float, description: str) -> Claim:
        """Create a new fraud claim."""
        claim = Claim(customer_id, claim_amount, description)
        self.claims[claim.claim_id] = claim
        return claim
    
    def assess_claim(self, claim_id: str, notes: str) -> bool:
        """Assess a claim and determine if it should be submitted to the bank."""
        claim = self.claims.get(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != ClaimStatus.RECEIVED:
            raise ValueError("Claim already assessed or processed")
        
        # Simulate assessment decision (80% chance of submission)
        if random.random() < 0.8:
            claim.update_status(ClaimStatus.UNDER_ASSESSMENT, notes)
            return True
        else:
            claim.update_status(ClaimStatus.CLOSED, "Claim rejected during assessment")
            return False
    
    def submit_to_bank(self, claim_id: str) -> str:
        """Submit the claim to the bank and get a reference number."""
        claim = self.claims.get(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != ClaimStatus.UNDER_ASSESSMENT:
            raise ValueError("Claim not ready for bank submission")
        
        claim.bank_reference = f"BANK-{uuid.uuid4().hex[:8].upper()}"
        claim.update_status(ClaimStatus.BANK_SUBMITTED, f"Submitted to bank with reference {claim.bank_reference}")
        return claim.bank_reference
    
    def process_bank_response(self, claim_id: str, approved: bool) -> None:
        """Process the bank's response to the claim."""
        claim = self.claims.get(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != ClaimStatus.BANK_SUBMITTED:
            raise ValueError("Claim not in submitted state")
        
        if approved:
            claim.update_status(ClaimStatus.BANK_APPROVED, "Bank approved the claim")
        else:
            claim.update_status(ClaimStatus.BANK_REJECTED, "Bank rejected the claim")
    
    def escalate_to_fos(self, claim_id: str) -> str:
        """Escalate the claim to the Financial Ombudsman Service."""
        claim = self.claims.get(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != ClaimStatus.BANK_REJECTED:
            raise ValueError("Claim not eligible for FOS escalation")
        
        claim.fos_reference = f"FOS-{uuid.uuid4().hex[:8].upper()}"
        claim.update_status(ClaimStatus.FOS_ESCALATED, f"Escalated to FOS with reference {claim.fos_reference}")
        return claim.fos_reference
    
    def resolve_fos_case(self, claim_id: str, approved: bool) -> None:
        """Resolve the FOS case and update claim status."""
        claim = self.claims.get(claim_id)
        if not claim:
            raise ValueError("Claim not found")
        
        if claim.status != ClaimStatus.FOS_ESCALATED:
            raise ValueError("Claim not escalated to FOS")
        
        if approved:
            claim.update_status(ClaimStatus.FOS_RESOLVED, "FOS ruled in customer's favor")
        else:
            claim.update_status(ClaimStatus.CLOSED, "FOS upheld bank's decision")
    
    def get_claim(self, claim_id: str) -> Optional[Claim]:
        """Retrieve a claim by its ID."""
        return self.claims.get(claim_id)

# Example usage
if __name__ == "__main__":
    manager = ClaimsManager()
    
    # Create a claim
    claim = manager.create_claim("CUST123", 1500.00, "Unauthorized transaction on 01/01/2023")
    print(f"Created claim:\n{claim}\n")
    
    # Assess claim
    if manager.assess_claim(claim.claim_id, "Initial assessment completed - appears valid"):
        print("Claim assessment passed, submitting to bank...")
        
        # Submit to bank
        bank_ref = manager.submit_to_bank(claim.claim_id)
        print(f"Submitted to bank with reference: {bank_ref}\n")
        
        # Simulate bank response (random for demo)
        approved = random.choice([True, False])
        manager.process_bank_response(claim.claim_id, approved)
        print(f"Bank response: {'Approved' if approved else 'Rejected'}\n")
        
        if not approved:
            # Escalate to FOS
            fos_ref = manager.escalate_to_fos(claim.claim_id)
            print(f"Escalated to FOS with reference: {fos_ref}\n")
            
            # Simulate FOS resolution (random for demo)
            fos_approved = random.choice([True, False])
            manager.resolve_fos_case(claim.claim_id, fos_approved)
            print(f"FOS resolution: {'Approved' if fos_approved else 'Rejected'}\n")
    
    # Display final claim status
    print(f"Final claim status:\n{manager.get_claim(claim.claim_id)}\n")
```
