"""
Generated Code Metadata:
========================
Original URL: https://sherafight.nl
Prompt: Write a Python script to manage membership and pricing for a martial arts school like Shera Fight, with different rates for children, junior, and adults.
Generated: DETERMINISTIC_b6f5591df400a818
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import os

class MembershipTier(Enum):
    CHILD = "Child"
    JUNIOR = "Junior"
    ADULT = "Adult"

@dataclass
class Member:
    name: str
    email: str
    phone: str
    tier: MembershipTier
    join_date: str
    active: bool = True
    membership_id: Optional[str] = None

@dataclass
class Pricing:
    child: float
    junior: float
    adult: float

class MartialArtsSchool:
    def __init__(self, name: str, pricing: Pricing):
        self.name = name
        self.pricing = pricing
        self.members: Dict[str, Member] = {}
        self.data_file = "members_data.json"
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for member_id, member_data in data.items():
                    member_data['tier'] = MembershipTier(member_data['tier'])
                    self.members[member_id] = Member(**member_data)

    def _save_data(self):
        data = {mid: asdict(member) for mid, member in self.members.items()}
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def _generate_membership_id(self) -> str:
        return f"{self.name[:3].upper()}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def add_member(self, name: str, email: str, phone: str, tier: MembershipTier) -> str:
        """Add a new member to the school."""
        if not all([name, email, phone]):
            raise ValueError("Name, email, and phone are required fields")
        
        membership_id = self._generate_membership_id()
        join_date = datetime.now().strftime("%Y-%m-%d")
        
        new_member = Member(
            name=name,
            email=email,
            phone=phone,
            tier=tier,
            join_date=join_date,
            membership_id=membership_id
        )
        
        self.members[membership_id] = new_member
        self._save_data()
        return membership_id

    def get_member(self, membership_id: str) -> Optional[Member]:
        """Retrieve a member by their membership ID."""
        return self.members.get(membership_id)

    def update_member(self, membership_id: str, **kwargs) -> bool:
        """Update member information."""
        member = self.members.get(membership_id)
        if not member:
            return False
        
        for key, value in kwargs.items():
            if key == 'tier' and isinstance(value, str):
                value = MembershipTier(value)
            setattr(member, key, value)
        
        self._save_data()
        return True

    def deactivate_member(self, membership_id: str) -> bool:
        """Deactivate a member's account."""
        member = self.members.get(membership_id)
        if not member:
            return False
        
        member.active = False
        self._save_data()
        return True

    def get_membership_fee(self, membership_id: str) -> Optional[float]:
        """Get the membership fee for a member."""
        member = self.members.get(membership_id)
        if not member or not member.active:
            return None
        
        if member.tier == MembershipTier.CHILD:
            return self.pricing.child
        elif member.tier == MembershipTier.JUNIOR:
            return self.pricing.junior
        elif member.tier == MembershipTier.ADULT:
            return self.pricing.adult
        return None

    def list_members(self, active_only: bool = True) -> List[Member]:
        """List all members, optionally filtering by active status."""
        members = list(self.members.values())
        if active_only:
            return [m for m in members if m.active]
        return members

    def get_members_by_tier(self, tier: MembershipTier) -> List[Member]:
        """Get all members of a specific tier."""
        return [m for m in self.members.values() if m.tier == tier and m.active]

# Example usage
if __name__ == "__main__":
    # Initialize the school with pricing
    pricing = Pricing(child=50.0, junior=75.0, adult=100.0)
    school = MartialArtsSchool("Shera Fight", pricing)

    # Add some members
    child_id = school.add_member(
        "Alice Johnson", "alice@example.com", "555-1234", MembershipTier.CHILD
    )
    adult_id = school.add_member(
        "Bob Smith", "bob@example.com", "555-5678", MembershipTier.ADULT
    )

    # Get membership fee
    print(f"Child membership fee: ${school.get_membership_fee(child_id)}")
    print(f"Adult membership fee: ${school.get_membership_fee(adult_id)}")

    # List all active members
    print("\nActive Members:")
    for member in school.list_members():
        print(f"{member.name} ({member.tier.value}) - {member.membership_id}")
```
