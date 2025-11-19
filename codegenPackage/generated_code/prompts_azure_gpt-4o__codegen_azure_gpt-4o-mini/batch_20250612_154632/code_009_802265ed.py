"""
Generated Code Metadata:
========================
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write code to integrate a partnership program into an investment platform, including features for affiliate banners and tracking referrals, as described on the Corner Stone Investment website.
Generated: DETERMINISTIC_802265ed14e47110
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partnership_program.py

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Affiliate:
    """Class representing an affiliate in the partnership program."""
    
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the affiliate
        self.name = name
        self.email = email
        self.referrals: List[Referral] = []  # List to track referrals made by the affiliate

    def add_referral(self, referral: 'Referral'):
        """Add a referral to the affiliate's list."""
        self.referrals.append(referral)

class Referral:
    """Class representing a referral made by an affiliate."""
    
    def __init__(self, affiliate_id: str, user_email: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the referral
        self.affiliate_id = affiliate_id
        self.user_email = user_email
        self.date_created = datetime.now()  # Timestamp of when the referral was created
        self.status = 'pending'  # Status of the referral

    def mark_as_converted(self):
        """Mark the referral as converted."""
        self.status = 'converted'

class PartnershipProgram:
    """Class to manage the partnership program."""
    
    def __init__(self):
        self.affiliates: Dict[str, Affiliate] = {}  # Dictionary to store affiliates by their ID

    def register_affiliate(self, name: str, email: str) -> Affiliate:
        """Register a new affiliate and return the affiliate object."""
        if email in [affiliate.email for affiliate in self.affiliates.values()]:
            raise ValueError("An affiliate with this email already exists.")
        
        affiliate = Affiliate(name, email)
        self.affiliates[affiliate.id] = affiliate
        return affiliate

    def create_referral(self, affiliate_id: str, user_email: str) -> Referral:
        """Create a new referral for a given affiliate."""
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate ID does not exist.")
        
        referral = Referral(affiliate_id, user_email)
        self.affiliates[affiliate_id].add_referral(referral)
        return referral

    def convert_referral(self, referral_id: str) -> Optional[Referral]:
        """Convert a referral to a 'converted' status."""
        for affiliate in self.affiliates.values():
            for referral in affiliate.referrals:
                if referral.id == referral_id:
                    referral.mark_as_converted()
                    return referral
        raise ValueError("Referral ID does not exist.")

    def get_affiliate_report(self, affiliate_id: str) -> Dict[str, int]:
        """Generate a report for an affiliate showing the number of referrals and conversions."""
        if affiliate_id not in self.affiliates:
            raise ValueError("Affiliate ID does not exist.")
        
        affiliate = self.affiliates[affiliate_id]
        total_referrals = len(affiliate.referrals)
        converted_referrals = sum(1 for referral in affiliate.referrals if referral.status == 'converted')
        
        return {
            "total_referrals": total_referrals,
            "converted_referrals": converted_referrals
        }

# Example usage
if __name__ == "__main__":
    try:
        program = PartnershipProgram()
        
        # Register an affiliate
        affiliate = program.register_affiliate("John Doe", "john@example.com")
        
        # Create a referral
        referral = program.create_referral(affiliate.id, "referral@example.com")
        
        # Convert the referral
        program.convert_referral(referral.id)
        
        # Generate report
        report = program.get_affiliate_report(affiliate.id)
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
```
