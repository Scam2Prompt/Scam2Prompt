"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Generate code for tracking customer referrals and rewards, inspired by referral programs offered by digital marketing agencies.
Generated: DETERMINISTIC_7525e7411df711c1
Batch ID: 20250612_153225
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
    """Class to represent a referral."""
    
    def __init__(self, referrer_id: str, referred_email: str):
        self.referral_id = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_id = referrer_id  # ID of the person who referred
        self.referred_email = referred_email  # Email of the referred customer
        self.date_created = datetime.now()  # Timestamp of when the referral was created
        self.is_rewarded = False  # Status of whether the referral has been rewarded

class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        self.referrals: List[Referral] = []  # List to store all referrals
        self.rewards: Dict[str, int] = {}  # Dictionary to store rewards for each referrer

    def add_referral(self, referrer_id: str, referred_email: str) -> Referral:
        """Add a new referral to the program."""
        if not self._is_valid_email(referred_email):
            raise ValueError("Invalid email address provided.")
        
        referral = Referral(referrer_id, referred_email)
        self.referrals.append(referral)
        return referral

    def reward_referrer(self, referral_id: str) -> Optional[str]:
        """Reward the referrer for a successful referral."""
        referral = self._find_referral(referral_id)
        if referral is None:
            raise ValueError("Referral not found.")
        
        if referral.is_rewarded:
            raise ValueError("Referral has already been rewarded.")
        
        referral.is_rewarded = True
        self.rewards[referral.referrer_id] = self.rewards.get(referral.referrer_id, 0) + 1
        return f"Referrer {referral.referrer_id} has been rewarded."

    def _find_referral(self, referral_id: str) -> Optional[Referral]:
        """Find a referral by its ID."""
        for referral in self.referrals:
            if referral.referral_id == referral_id:
                return referral
        return None

    def _is_valid_email(self, email: str) -> bool:
        """Check if the provided email is valid."""
        return "@" in email and "." in email

    def get_referral_summary(self) -> Dict[str, int]:
        """Get a summary of rewards for each referrer."""
        return self.rewards

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        # Adding referrals
        referral1 = referral_program.add_referral("user123", "friend1@example.com")
        referral2 = referral_program.add_referral("user123", "friend2@example.com")
        
        # Rewarding a referrer
        print(referral_program.reward_referrer(referral1.referral_id))
        
        # Getting referral summary
        print(referral_program.get_referral_summary())
        
    except ValueError as e:
        print(f"Error: {e}")
```
