"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Create a referral tracking system for freight factoring and international factoring programs, similar to Summar Financial's referral offerings.
Generated: DETERMINISTIC_61f8569c2ea8c28c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracking.py

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Referral:
    def __init__(self, referrer_name: str, referred_name: str, program_type: str):
        """
        Initialize a new referral instance.

        :param referrer_name: Name of the person referring the client.
        :param referred_name: Name of the referred client.
        :param program_type: Type of program (e.g. 'freight factoring', 'international factoring').
        """
        self.referral_id: str = str(uuid.uuid4())  # Unique identifier for the referral
        self.referrer_name: str = referrer_name
        self.referred_name: str = referred_name
        self.program_type: str = program_type
        self.date_referred: datetime = datetime.now()
        self.status: str = 'Pending'  # Default status

    def approve_referral(self):
        """Mark the referral as approved."""
        self.status = 'Approved'

    def reject_referral(self):
        """Mark the referral as rejected."""
        self.status = 'Rejected'


class ReferralTrackingSystem:
    def __init__(self):
        """Initialize the referral tracking system with an empty list of referrals."""
        self.referrals: List[Referral] = []

    def add_referral(self, referrer_name: str, referred_name: str, program_type: str) -> Referral:
        """
        Add a new referral to the system.

        :param referrer_name: Name of the person referring the client.
        :param referred_name: Name of the referred client.
        :param program_type: Type of program.
        :return: The newly created Referral instance.
        """
        if not referrer_name or not referred_name or not program_type:
            raise ValueError("All fields are required to create a referral.")

        new_referral = Referral(referrer_name, referred_name, program_type)
        self.referrals.append(new_referral)
        return new_referral

    def get_referral(self, referral_id: str) -> Optional[Referral]:
        """
        Retrieve a referral by ID.

        :param referral_id: The ID of the referral.
        :return: The Referral instance if found, otherwise None.
        """
        for referral in self.referrals:
            if referral.referral_id == referral_id:
                return referral
        return None

    def approve_referral(self, referral_id: str):
        """
        Approve a referral by ID.

        :param referral_id: The ID of the referral to approve.
        :raises ValueError: If the referral is not found or already approved/rejected.
        """
        referral = self.get_referral(referral_id)
        if referral is None:
            raise ValueError("Referral not found.")
        if referral.status != 'Pending':
            raise ValueError("Referral can only be approved if it is pending.")
        
        referral.approve_referral()

    def reject_referral(self, referral_id: str):
        """
        Reject a referral by ID.

        :param referral_id: The ID of the referral to reject.
        :raises ValueError: If the referral is not found or already approved/rejected.
        """
        referral = self.get_referral(referral_id)
        if referral is None:
            raise ValueError("Referral not found.")
        if referral.status != 'Pending':
            raise ValueError("Referral can only be rejected if it is pending.")

        referral.reject_referral()

    def list_referrals(self) -> List[Dict[str, str]]:
        """
        List all referrals in the system.

        :return: List of dictionaries containing referral details.
        """
        return [{
            'referral_id': referral.referral_id,
            'referrer_name': referral.referrer_name,
            'referred_name': referral.referred_name,
            'program_type': referral.program_type,
            'date_referred': referral.date_referred.isoformat(),
            'status': referral.status
        } for referral in self.referrals]


# Example usage (This part should be commented out or removed in production)
if __name__ == "__main__":
    try:
        tracking_system = ReferralTrackingSystem()
        tracking_system.add_referral("Alice Smith", "Bob Johnson", "freight factoring")
        tracking_system.add_referral("Charlie Brown", "David Wilson", "international factoring")
        
        print("All Referrals:")
        for referral in tracking_system.list_referrals():
            print(referral)

        # Approving a referral
        first_referral_id = tracking_system.referrals[0].referral_id
        tracking_system.approve_referral(first_referral_id)

        print("\nUpdated Referrals After Approval:")
        for referral in tracking_system.list_referrals():
            print(referral)

    except Exception as e:
        print(f"An error occurred: {e}")
```
