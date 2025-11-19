"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write code to manage referrals for a training program, including tracking enrollments and rewards, similar to the referral system described on SMART Training Resources' website.
Generated: DETERMINISTIC_944bbb8ce05baa02
Batch ID: 20250612_151417
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

class Referral:
    """Class to represent a referral in the training program."""
    
    def __init__(self, referrer_id: str, referred_email: str):
        self.referral_id = str(uuid.uuid4())
        self.referrer_id = referrer_id
        self.referred_email = referred_email
        self.enrollment_date: Optional[datetime] = None
        self.reward_claimed: bool = False

    def enroll(self):
        """Enroll the referred user and set the enrollment date."""
        self.enrollment_date = datetime.now()

    def claim_reward(self):
        """Claim the reward for the referrer."""
        if self.enrollment_date and not self.reward_claimed:
            self.reward_claimed = True
            return True
        return False


class ReferralManager:
    """Class to manage referrals and track enrollments and rewards."""
    
    def __init__(self):
        self.referrals: List[Referral] = []

    def create_referral(self, referrer_id: str, referred_email: str) -> Referral:
        """Create a new referral and add it to the list."""
        referral = Referral(referrer_id, referred_email)
        self.referrals.append(referral)
        return referral

    def enroll_referral(self, referral_id: str) -> bool:
        """Enroll a referred user by their referral ID."""
        referral = self._find_referral(referral_id)
        if referral:
            referral.enroll()
            return True
        return False

    def claim_referral_reward(self, referral_id: str) -> bool:
        """Claim the reward for the referrer associated with the referral ID."""
        referral = self._find_referral(referral_id)
        if referral:
            return referral.claim_reward()
        return False

    def _find_referral(self, referral_id: str) -> Optional[Referral]:
        """Private method to find a referral by its ID."""
        for referral in self.referrals:
            if referral.referral_id == referral_id:
                return referral
        return None

    def get_referral_status(self, referral_id: str) -> Dict[str, Optional[str]]:
        """Get the status of a referral."""
        referral = self._find_referral(referral_id)
        if referral:
            return {
                "referral_id": referral.referral_id,
                "referrer_id": referral.referrer_id,
                "referred_email": referral.referred_email,
                "enrollment_date": referral.enrollment_date,
                "reward_claimed": referral.reward_claimed
            }
        return {"error": "Referral not found."}


# Example usage
if __name__ == "__main__":
    manager = ReferralManager()
    
    # Create a referral
    referral = manager.create_referral("user123", "newuser@example.com")
    print(f"Created referral: {referral.referral_id}")

    # Enroll the referred user
    if manager.enroll_referral(referral.referral_id):
        print("Referred user enrolled successfully.")

    # Claim the reward
    if manager.claim_referral_reward(referral.referral_id):
        print("Reward claimed successfully.")

    # Get referral status
    status = manager.get_referral_status(referral.referral_id)
    print(status)
```
