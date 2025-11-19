"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: Write code for a comprehensive partner system to enhance marketing and sales efforts, integrating innovative solutions for scaling businesses, as described by Investment Brokers.
Generated: DETERMINISTIC_0aea2e1c7d84772d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partner_system.py

from enum import Enum
from typing import List, Dict

class PartnerStatus(str, Enum):
    """Partner status enumeration"""
    ACTIVE = "active"
    INACTIVE = "inactive"

class Partner:
    """Partner class"""
    def __init__(self, id: int, name: str, email: str, status: PartnerStatus = PartnerStatus.ACTIVE):
        """
        Initialize a Partner object.

        Args:
        id (int): Unique partner ID
        name (str): Partner name
        email (str): Partner email
        status (PartnerStatus): Partner status (default: active)
        """
        self.id = id
        self.name = name
        self.email = email
        self.status = status
        self.campaigns: List[str] = []  # List of campaigns associated with the partner

    def add_campaign(self, campaign: str):
        """Add a campaign to the partner's list of campaigns"""
        self.campaigns.append(campaign)

    def remove_campaign(self, campaign: str):
        """Remove a campaign from the partner's list of campaigns"""
        if campaign in self.campaigns:
            self.campaigns.remove(campaign)

    def update_status(self, status: PartnerStatus):
        """Update the partner's status"""
        self.status = status

class PartnerSystem:
    """Partner system class"""
    def __init__(self):
        self.partners: Dict[int, Partner] = {}  # Dictionary of partners

    def add_partner(self, partner: Partner):
        """Add a partner to the system"""
        self.partners[partner.id] = partner

    def remove_partner(self, partner_id: int):
        """Remove a partner from the system"""
        if partner_id in self.partners:
            del self.partners[partner_id]

    def get_partner(self, partner_id: int) -> Partner:
        """Get a partner by ID"""
        return self.partners.get(partner_id)

    def update_partner_status(self, partner_id: int, status: PartnerStatus):
        """Update a partner's status"""
        partner = self.get_partner(partner_id)
        if partner:
            partner.update_status(status)

    def assign_campaign(self, partner_id: int, campaign: str):
        """Assign a campaign to a partner"""
        partner = self.get_partner(partner_id)
        if partner:
            partner.add_campaign(campaign)

    def unassign_campaign(self, partner_id: int, campaign: str):
        """Unassign a campaign from a partner"""
        partner = self.get_partner(partner_id)
        if partner:
            partner.remove_campaign(campaign)

def main():
    # Create a partner system
    partner_system = PartnerSystem()

    # Create partners
    partner1 = Partner(1, "John Doe", "john.doe@example.com")
    partner2 = Partner(2, "Jane Smith", "jane.smith@example.com")

    # Add partners to the system
    partner_system.add_partner(partner1)
    partner_system.add_partner(partner2)

    # Assign campaigns
    partner_system.assign_campaign(1, "Campaign 1")
    partner_system.assign_campaign(2, "Campaign 2")

    # Print partner information
    for partner_id, partner in partner_system.partners.items():
        print(f"Partner ID: {partner_id}")
        print(f"Name: {partner.name}")
        print(f"Email: {partner.email}")
        print(f"Status: {partner.status}")
        print(f"Campaigns: {partner.campaigns}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
