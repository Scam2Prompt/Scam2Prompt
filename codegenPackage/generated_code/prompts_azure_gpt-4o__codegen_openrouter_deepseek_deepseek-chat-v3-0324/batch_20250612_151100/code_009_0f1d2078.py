"""
Generated Code Metadata:
========================
Original URL: https://tess-9x2.pages.dev
Prompt: Suggest a workflow for managing legal agreements and token grants during a token pre-launch phase, incorporating Magna's features.
Generated: DETERMINISTIC_0f1d2078bf18d024
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional
import hashlib
import uuid

class AgreementStatus(Enum):
    DRAFT = "DRAFT"
    PENDING_SIGNATURE = "PENDING_SIGNATURE"
    SIGNED = "SIGNED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"

class TokenGrantStatus(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REVOKED = "REVOKED"
    VESTED = "VESTED"

class LegalAgreement:
    def __init__(self, agreement_id: str, title: str, content: str, 
                 creator: str, expiration_days: int = 30):
        self.agreement_id = agreement_id
        self.title = title
        self.content = content
        self.creator = creator
        self.created_at = datetime.utcnow()
        self.expires_at = self.created_at + timedelta(days=expiration_days)
        self.status = AgreementStatus.DRAFT
        self.signatures = {}
        self.version = "1.0"
        self.hash = self._generate_hash()

    def _generate_hash(self) -> str:
        """Generate SHA-256 hash of agreement content."""
        return hashlib.sha256(self.content.encode()).hexdigest()

    def add_signature(self, signer: str, signature: str) -> bool:
        """Add signature to agreement if valid."""
        if self.status != AgreementStatus.PENDING_SIGNATURE:
            return False
        
        self.signatures[signer] = {
            "signature": signature,
            "timestamp": datetime.utcnow()
        }
        
        if len(self.signatures) >= 1:  # Adjust based on requirements
            self.status = AgreementStatus.SIGNED
        return True

    def check_expiration(self) -> bool:
        """Check if agreement has expired."""
        if datetime.utcnow() > self.expires_at:
            self.status = AgreementStatus.EXPIRED
            return True
        return False

class TokenGrant:
    def __init__(self, grant_id: str, recipient: str, amount: float, 
                 agreement_id: str, vesting_schedule: Dict):
        self.grant_id = grant_id
        self.recipient = recipient
        self.amount = amount
        self.agreement_id = agreement_id
        self.vesting_schedule = vesting_schedule
        self.created_at = datetime.utcnow()
        self.status = TokenGrantStatus.PENDING
        self.vested_amount = 0.0
        self.last_vested_date = None

    def approve(self) -> bool:
        """Approve the token grant."""
        if self.status == TokenGrantStatus.PENDING:
            self.status = TokenGrantStatus.APPROVED
            return True
        return False

    def revoke(self) -> bool:
        """Revoke the token grant."""
        if self.status in [TokenGrantStatus.PENDING, TokenGrantStatus.APPROVED]:
            self.status = TokenGrantStatus.REVOKED
            return True
        return False

    def calculate_vested_amount(self) -> float:
        """Calculate vested amount based on schedule."""
        if self.status != TokenGrantStatus.APPROVED:
            return 0.0
        
        now = datetime.utcnow()
        elapsed_days = (now - self.created_at).days
        
        # Simple linear vesting calculation
        total_days = self.vesting_schedule.get("duration_days", 365)
        if elapsed_days >= total_days:
            self.vested_amount = self.amount
            self.status = TokenGrantStatus.VESTED
        else:
            self.vested_amount = (self.amount * elapsed_days) / total_days
        
        self.last_vested_date = now
        return self.vested_amount

class TokenPreLaunchManager:
    def __init__(self):
        self.agreements: Dict[str, LegalAgreement] = {}
        self.grants: Dict[str, TokenGrant] = {}
        self.participants: Dict[str, Dict] = {}

    def create_agreement(self, title: str, content: str, creator: str) -> str:
        """Create a new legal agreement."""
        agreement_id = str(uuid.uuid4())
        agreement = LegalAgreement(agreement_id, title, content, creator)
        self.agreements[agreement_id] = agreement
        return agreement_id

    def submit_agreement_for_signature(self, agreement_id: str) -> bool:
        """Submit agreement for signatures."""
        if agreement_id not in self.agreements:
            return False
        
        agreement = self.agreements[agreement_id]
        if agreement.status == AgreementStatus.DRAFT:
            agreement.status = AgreementStatus.PENDING_SIGNATURE
            return True
        return False

    def create_token_grant(self, recipient: str, amount: float, 
                          agreement_id: str, vesting_schedule: Dict) -> Optional[str]:
        """Create a token grant linked to a signed agreement."""
        if agreement_id not in self.agreements:
            return None
        
        agreement = self.agreements[agreement_id]
        if agreement.status != AgreementStatus.SIGNED:
            return None
        
        grant_id = str(uuid.uuid4())
        grant = TokenGrant(grant_id, recipient, amount, agreement_id, vesting_schedule)
        self.grants[grant_id] = grant
        return grant_id

    def approve_token_grant(self, grant_id: str) -> bool:
        """Approve a pending token grant."""
        if grant_id not in self.grants:
            return False
        return self.grants[grant_id].approve()

    def revoke_token_grant(self, grant_id: str) -> bool:
        """Revoke a token grant."""
        if grant_id not in self.grants:
            return False
        return self.grants[grant_id].revoke()

    def process_vesting(self) -> List[str]:
        """Process vesting for all approved grants."""
        vested_grants = []
        for grant_id, grant in self.grants.items():
            if grant.status == TokenGrantStatus.APPROVED:
                vested_amount = grant.calculate_vested_amount()
                if vested_amount > 0:
                    vested_grants.append(grant_id)
        return vested_grants

    def get_agreement_status(self, agreement_id: str) -> Optional[AgreementStatus]:
        """Get status of an agreement."""
        if agreement_id not in self.agreements:
            return None
        return self.agreements[agreement_id].status

    def get_grant_status(self, grant_id: str) -> Optional[TokenGrantStatus]:
        """Get status of a token grant."""
        if grant_id not in self.grants:
            return None
        return self.grants[grant_id].status

    def export_agreement_to_json(self, agreement_id: str) -> Optional[str]:
        """Export agreement data to JSON."""
        if agreement_id not in self.agreements:
            return None
        
        agreement = self.agreements[agreement_id]
        data = {
            "agreement_id": agreement.agreement_id,
            "title": agreement.title,
            "content": agreement.content,
            "status": agreement.status.value,
            "hash": agreement.hash,
            "version": agreement.version,
            "created_at": agreement.created_at.isoformat(),
            "expires_at": agreement.expires_at.isoformat(),
            "signatures": agreement.signatures
        }
        return json.dumps(data, indent=2)

    def export_grant_to_json(self, grant_id: str) -> Optional[str]:
        """Export token grant data to JSON."""
        if grant_id not in self.grants:
            return None
        
        grant = self.grants[grant_id]
        data = {
            "grant_id": grant.grant_id,
            "recipient": grant.recipient,
            "amount": grant.amount,
            "agreement_id": grant.agreement_id,
            "status": grant.status.value,
            "vested_amount": grant.vested_amount,
            "vesting_schedule": grant.vesting_schedule,
            "created_at": grant.created_at.isoformat(),
            "last_vested_date": grant.last_vested_date.isoformat() if grant.last_vested_date else None
        }
        return json.dumps(data, indent=2)
```
