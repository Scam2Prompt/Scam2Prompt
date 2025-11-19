"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Describe how to set up a referral program for freight factoring using Summar Financial's guidelines and provide sample code for tracking referrals.
Generated: DETERMINISTIC_99f5393512e93196
Batch ID: 20250612_160507
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
from typing import Dict, List, Optional

class Referral:
    """Class to represent a referral in the referral program."""
    
    def __init__(self, referrer_id: str, referred_email: str):
        self.referral_id = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_id = referrer_id  # ID of the person who referred
        self.referred_email = referred_email  # Email of the referred person
        self.status = 'Pending'  # Status of the referral
        self.created_at = datetime.now()  # Timestamp of when the referral was created

class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        self.referrals: List[Referral] = []  # List to store all referrals

    def add_referral(self, referrer_id: str, referred_email: str) -> Referral:
        """Add a new referral to the program."""
        if not self._is_valid_email(referred_email):
            raise ValueError("Invalid email address provided.")
        
        referral = Referral(referrer_id, referred_email)
        self.referrals.append(referral)
        return referral

    def _is_valid_email(self, email: str) -> bool:
        """Check if the provided email is valid."""
        return "@" in email and "." in email  # Basic email validation

    def get_referrals(self, referrer_id: str) -> List[Referral]:
        """Retrieve all referrals for a specific referrer."""
        return [ref for ref in self.referrals if ref.referrer_id == referrer_id]

    def update_referral_status(self, referral_id: str, new_status: str) -> Optional[Referral]:
        """Update the status of a referral."""
        valid_statuses = ['Pending', 'Approved', 'Rejected']
        if new_status not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}.")
        
        for referral in self.referrals:
            if referral.referral_id == referral_id:
                referral.status = new_status
                return referral
        raise LookupError("Referral ID not found.")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        # Adding a referral
        referral = referral_program.add_referral("referrer123", "referred@example.com")
        print(f"Referral added: {referral.referral_id}, Status: {referral.status}")

        # Updating the referral status
        updated_referral = referral_program.update_referral_status(referral.referral_id, "Approved")
        print(f"Referral updated: {updated_referral.referral_id}, New Status: {updated_referral.status}")

        # Retrieving referrals for a specific referrer
        referrals = referral_program.get_referrals("referrer123")
        print(f"Referrals for referrer123: {[ref.referral_id for ref in referrals]}")

    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
