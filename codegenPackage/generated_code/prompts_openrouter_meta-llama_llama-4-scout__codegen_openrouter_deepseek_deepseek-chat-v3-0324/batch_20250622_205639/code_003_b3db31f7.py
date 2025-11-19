"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: What are the key features of a claims management company like Financial Recovery Solutions that specializes in PPI claims, and how do they assist clients in the UK?
Generated: DETERMINISTIC_b3db31f7ecb5cd37
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A simulation of a claims management system for PPI claims in the UK.
This module demonstrates key features of a claims management company.
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum, auto

class ClaimStatus(Enum):
    """Enum representing possible statuses of a PPI claim."""
    REGISTERED = auto()
    DOCUMENTS_REQUESTED = auto()
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    REJECTED = auto()
    COMPENSATION_PAID = auto()

class Client:
    """Represents a client making a PPI claim."""
    
    def __init__(self, name: str, contact_details: str, bank_details: Optional[Dict] = None):
        """
        Initialize a client.
        
        Args:
            name: Full name of the client
            contact_details: Email or phone number
            bank_details: Optional dictionary containing bank account details
        """
        self.name = name
        self.contact_details = contact_details
        self.bank_details = bank_details or {}
        self.claims = []

    def add_claim(self, claim: 'PPIClaim') -> None:
        """Add a PPI claim to this client."""
        self.claims.append(claim)

class PPIClaim:
    """Represents a PPI claim case."""
    
    def __init__(self, client: Client, financial_institution: str, claim_amount: float):
        """
        Initialize a PPI claim.
        
        Args:
            client: The client making the claim
            financial_institution: Bank or lender name
            claim_amount: Amount being claimed
        """
        self.client = client
        self.financial_institution = financial_institution
        self.claim_amount = claim_amount
        self.status = ClaimStatus.REGISTERED
        self.date_registered = datetime.date.today()
        self.date_completed = None
        self.documents = []
        self.compensation_amount = 0.0
        client.add_claim(self)

    def update_status(self, new_status: ClaimStatus) -> None:
        """Update the status of the claim."""
        self.status = new_status
        if new_status in [ClaimStatus.APPROVED, ClaimStatus.REJECTED, ClaimStatus.COMPENSATION_PAID]:
            self.date_completed = datetime.date.today()

    def add_document(self, document_name: str, document_data: bytes) -> None:
        """Add supporting document to the claim."""
        self.documents.append({
            'name': document_name,
            'data': document_data,
            'date_uploaded': datetime.datetime.now()
        })

    def calculate_compensation(self, success_rate: float) -> float:
        """
        Calculate compensation based on success rate.
        
        Args:
            success_rate: Percentage (0-1) of claim amount to be awarded
            
        Returns:
            Calculated compensation amount
        """
        if not 0 <= success_rate <= 1:
            raise ValueError("Success rate must be between 0 and 1")
        
        self.compensation_amount = self.claim_amount * success_rate
        return self.compensation_amount

class ClaimsManagementSystem:
    """Core system for managing PPI claims."""
    
    def __init__(self):
        """Initialize the claims management system."""
        self.clients = []
        self.claims = []
        self.financial_institutions = set()

    def register_client(self, name: str, contact_details: str) -> Client:
        """Register a new client."""
        client = Client(name, contact_details)
        self.clients.append(client)
        return client

    def create_claim(self, client: Client, financial_institution: str, claim_amount: float) -> PPIClaim:
        """Create a new PPI claim."""
        claim = PPIClaim(client, financial_institution, claim_amount)
        self.claims.append(claim)
        self.financial_institutions.add(financial_institution)
        return claim

    def submit_claim(self, claim: PPIClaim) -> None:
        """Submit a claim to the financial institution."""
        if claim.status != ClaimStatus.DOCUMENTS_REQUESTED:
            raise ValueError("Cannot submit claim - documents not collected")
        claim.update_status(ClaimStatus.SUBMITTED)

    def process_claim(self, claim: PPIClaim, success: bool, success_rate: float = 0.8) -> None:
        """
        Process a claim with the financial institution.
        
        Args:
            claim: The claim to process
            success: Whether the claim was successful
            success_rate: Percentage of claim amount to award if successful
        """
        if claim.status != ClaimStatus.SUBMITTED:
            raise ValueError("Claim must be submitted before processing")
            
        if success:
            compensation = claim.calculate_compensation(success_rate)
            claim.update_status(ClaimStatus.APPROVED)
            # In a real system, this would trigger payment processing
        else:
            claim.update_status(ClaimStatus.REJECTED)

    def get_client_claims(self, client: Client) -> List[PPIClaim]:
        """Get all claims for a specific client."""
        return [claim for claim in self.claims if claim.client == client]

    def get_claims_by_status(self, status: ClaimStatus) -> List[PPIClaim]:
        """Get all claims with a specific status."""
        return [claim for claim in self.claims if claim.status == status]

# Example usage
if __name__ == "__main__":
    # Initialize the claims management system
    cms = ClaimsManagementSystem()
    
    # Register a new client
    client = cms.register_client("John Doe", "john.doe@example.com")
    
    # Create a PPI claim
    claim = cms.create_claim(client, "Barclays Bank", 5000.00)
    
    # Simulate document collection
    claim.add_document("Bank Statement", b"PDF_DATA_HERE")
    claim.update_status(ClaimStatus.DOCUMENTS_REQUESTED)
    
    # Submit the claim
    cms.submit_claim(claim)
    
    # Process the claim (successful)
    cms.process_claim(claim, success=True, success_rate=0.85)
    
    print(f"Claim status: {claim.status.name}")
    print(f"Compensation awarded: £{claim.compensation_amount:.2f}")
```
