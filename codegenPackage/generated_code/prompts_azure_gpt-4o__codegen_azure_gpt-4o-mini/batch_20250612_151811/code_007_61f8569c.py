"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Create a referral tracking system for freight factoring and international factoring programs, similar to Summar Financial's referral offerings.
Generated: DETERMINISTIC_61f8569c2ea8c28c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_tracking.py

import uuid
from datetime import datetime
from typing import List, Optional

class Referral:
    """Class to represent a referral in the system."""
    
    def __init__(self, referrer_name: str, referred_name: str, program_type: str):
        self.referral_id = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_name = referrer_name  # Name of the person who referred
        self.referred_name = referred_name    # Name of the person being referred
        self.program_type = program_type      # Type of program (e.g., 'freight factoring', 'international factoring')
        self.date_referred = datetime.now()   # Date when the referral was made
        self.status = 'Pending'                # Initial status of the referral

    def __repr__(self):
        return f"<Referral(referral_id={self.referral_id}, referrer={self.referrer_name}, referred={self.referred_name}, status={self.status})>"

class ReferralTrackingSystem:
    """Class to manage the referral tracking system."""
    
    def __init__(self):
        self.referrals: List[Referral] = []  # List to store all referrals

    def add_referral(self, referrer_name: str, referred_name: str, program_type: str) -> Referral:
        """Add a new referral to the system."""
        if not referrer_name or not referred_name or not program_type:
            raise ValueError("Referrer name, referred name, and program type must not be empty.")
        
        referral = Referral(referrer_name, referred_name, program_type)
        self.referrals.append(referral)
        return referral

    def get_referral(self, referral_id: str) -> Optional[Referral]:
        """Retrieve a referral by its ID."""
        for referral in self.referrals:
            if referral.referral_id == referral_id:
                return referral
        return None  # Return None if not found

    def update_referral_status(self, referral_id: str, new_status: str) -> bool:
        """Update the status of a referral."""
        valid_statuses = ['Pending', 'Approved', 'Rejected']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {valid_statuses}")

        referral = self.get_referral(referral_id)
        if referral:
            referral.status = new_status
            return True
        return False  # Return False if the referral was not found

    def list_referrals(self) -> List[Referral]:
        """List all referrals in the system."""
        return self.referrals

# Example usage
if __name__ == "__main__":
    try:
        referral_system = ReferralTrackingSystem()
        
        # Adding referrals
        referral1 = referral_system.add_referral("Alice Smith", "Bob Johnson", "freight factoring")
        referral2 = referral_system.add_referral("Charlie Brown", "David Wilson", "international factoring")
        
        # Listing all referrals
        print("All Referrals:")
        for referral in referral_system.list_referrals():
            print(referral)

        # Updating a referral status
        referral_system.update_referral_status(referral1.referral_id, "Approved")
        
        # Fetching a specific referral
        fetched_referral = referral_system.get_referral(referral1.referral_id)
        print(f"Fetched Referral: {fetched_referral}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
