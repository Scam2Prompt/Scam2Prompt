"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write code to integrate a partnership program into an investment platform, including features for affiliate banners and tracking referrals, as described on the Corner Stone Investment website.
Generated: DETERMINISTIC_802265ed14e47110
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# partnership_program.py

import uuid
from datetime import datetime
from typing import List, Optional, Dict

class Affiliate:
    """Class to represent an affiliate in the partnership program."""
    
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each affiliate
        self.name = name
        self.email = email
        self.referrals: List[str] = []  # List to track referral IDs

    def add_referral(self, referral_id: str):
        """Add a referral ID to the affiliate's record."""
        self.referrals.append(referral_id)

class Referral:
    """Class to represent a referral transaction."""
    
    def __init__(self, affiliate_id: str, investment_amount: float):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each referral
        self.affiliate_id = affiliate_id
        self.investment_amount = investment_amount
        self.timestamp = datetime.utcnow()

class PartnershipProgram:
    """Class to manage the partnership program."""
    
    def __init__(self):
        self.affiliates: Dict[str, Affiliate] = {}  # Store affiliates by ID
        self.referrals: Dict[str, Referral] = {}    # Store referrals by ID

    def register_affiliate(self, name: str, email: str) -> Affiliate:
        """Register a new affiliate."""
        if email in [aff.email for aff in self.affiliates.values()]:
            raise ValueError(f"Affiliate with email {email} already exists.")
        
        affiliate = Affiliate(name, email)
        self.affiliates[affiliate.id] = affiliate
        return affiliate

    def track_referral(self, affiliate_id: str, investment_amount: float) -> Referral:
        """Track a referral if the affiliate exists."""
        if affiliate_id not in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} not found.")
        
        referral = Referral(affiliate_id, investment_amount)
        self.referrals[referral.id] = referral
        self.affiliates[affiliate_id].add_referral(referral.id)
        return referral

    def get_affiliate_report(self, affiliate_id: str) -> Optional[Dict]:
        """Generate a report for a specific affiliate."""
        if affiliate_id not in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} not found.")
        
        affiliate = self.affiliates[affiliate_id]
        total_investments = sum(self.referrals[ref_id].investment_amount for ref_id in affiliate.referrals)
        return {
            'affiliate_id': affiliate.id,
            'name': affiliate.name,
            'email': affiliate.email,
            'total_investments': total_investments,
            'referral_count': len(affiliate.referrals)
        }

# Example usage (this would typically be in a separate module or script):
if __name__ == "__main__":
    try:
        program = PartnershipProgram()
        
        # Register affiliates
        affiliate1 = program.register_affiliate("John Doe", "john@example.com")
        affiliate2 = program.register_affiliate("Jane Smith", "jane@example.com")
        
        # Track referrals
        program.track_referral(affiliate1.id, 5000.0)
        program.track_referral(affiliate1.id, 1500.0)
        program.track_referral(affiliate2.id, 7000.0)
        
        # Generate reports
        report1 = program.get_affiliate_report(affiliate1.id)
        report2 = program.get_affiliate_report(affiliate2.id)
        
        print("Affiliate Report 1:", report1)
        print("Affiliate Report 2:", report2)

    except Exception as e:
        print("An error occurred:", e)
```
