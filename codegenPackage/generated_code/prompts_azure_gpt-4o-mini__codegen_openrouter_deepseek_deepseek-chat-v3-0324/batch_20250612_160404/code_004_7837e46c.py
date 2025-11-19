"""
Generated Code Metadata:
========================
Original URL: https://mainecotrust.cc
Prompt: Illustrate how to implement a referral commission tracking system in Python, inspired by the 10% referral commission structure mentioned on mainecotrust.cc.
Generated: DETERMINISTIC_7837e46c294c9658
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum

class CommissionStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    PAID = "paid"
    REJECTED = "rejected"

class Referral:
    def __init__(self, referrer_id: str, referee_id: str, amount: float):
        self.id = str(uuid.uuid4())
        self.referrer_id = referrer_id
        self.referee_id = referee_id
        self.amount = amount
        self.commission = amount * 0.10  # 10% commission
        self.created_at = datetime.now()
        self.status = CommissionStatus.PENDING

    def update_status(self, new_status: CommissionStatus) -> None:
        """Update the status of the referral commission."""
        self.status = new_status

class ReferralSystem:
    def __init__(self):
        self.referrals: Dict[str, Referral] = {}
        self.user_commissions: Dict[str, List[Referral]] = {}

    def add_referral(self, referrer_id: str, referee_id: str, amount: float) -> Referral:
        """Record a new referral transaction."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        referral = Referral(referrer_id, referee_id, amount)
        self.referrals[referral.id] = referral
        
        if referrer_id not in self.user_commissions:
            self.user_commissions[referrer_id] = []
        self.user_commissions[referrer_id].append(referral)
        
        return referral

    def get_referral(self, referral_id: str) -> Optional[Referral]:
        """Retrieve a referral by its ID."""
        return self.referrals.get(referral_id)

    def get_user_commissions(self, user_id: str) -> List[Referral]:
        """Get all commissions for a specific user."""
        return self.user_commissions.get(user_id, [])

    def get_pending_commissions(self) -> List[Referral]:
        """Get all pending commissions."""
        return [r for r in self.referrals.values() if r.status == CommissionStatus.PENDING]

    def approve_commission(self, referral_id: str) -> None:
        """Approve a commission payment."""
        referral = self.get_referral(referral_id)
        if not referral:
            raise ValueError("Referral not found")
        referral.update_status(CommissionStatus.APPROVED)

    def pay_commission(self, referral_id: str) -> None:
        """Mark a commission as paid."""
        referral = self.get_referral(referral_id)
        if not referral:
            raise ValueError("Referral not found")
        if referral.status != CommissionStatus.APPROVED:
            raise ValueError("Commission must be approved before payment")
        referral.update_status(CommissionStatus.PAID)

    def reject_commission(self, referral_id: str) -> None:
        """Reject a commission."""
        referral = self.get_referral(referral_id)
        if not referral:
            raise ValueError("Referral not found")
        referral.update_status(CommissionStatus.REJECTED)

    def calculate_total_earnings(self, user_id: str) -> float:
        """Calculate total approved and paid commissions for a user."""
        commissions = self.get_user_commissions(user_id)
        return sum(
            r.commission for r in commissions 
            if r.status in [CommissionStatus.APPROVED, CommissionStatus.PAID]
        )

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()
    
    # Add referrals
    referral1 = system.add_referral("user1", "user2", 100.0)
    referral2 = system.add_referral("user1", "user3", 200.0)
    
    # Approve and pay first referral
    system.approve_commission(referral1.id)
    system.pay_commission(referral1.id)
    
    # Check user's total earnings
    earnings = system.calculate_total_earnings("user1")
    print(f"User1 total earnings: ${earnings:.2f}")
```
