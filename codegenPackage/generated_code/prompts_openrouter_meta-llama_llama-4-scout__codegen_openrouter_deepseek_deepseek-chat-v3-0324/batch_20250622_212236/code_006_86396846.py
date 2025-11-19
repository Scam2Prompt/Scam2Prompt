"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Write a code snippet to implement a basic loyalty program, like "The Star Club" at Treasury Brisbane Casino, that rewards members with exclusive offers and VIP benefits.
Generated: DETERMINISTIC_86396846e2f1056b
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import List, Dict, Optional


class MembershipTier(Enum):
    """Enum representing different membership tiers."""
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()
    VIP = auto()


class Member:
    """Class representing a loyalty program member."""
    
    def __init__(self, name: str, email: str, phone: str):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.points = 0
        self.tier = MembershipTier.BRONZE
        self.join_date = datetime.now()
        self.last_activity = datetime.now()
        self.vouchers: List[str] = []
        self.exclusive_offers: List[str] = []
    
    def add_points(self, points: int) -> None:
        """Add points to member's account."""
        if points <= 0:
            raise ValueError("Points must be positive")
        self.points += points
        self._update_tier()
        self.last_activity = datetime.now()
    
    def redeem_points(self, points: int) -> None:
        """Redeem points from member's account."""
        if points <= 0:
            raise ValueError("Points must be positive")
        if points > self.points:
            raise ValueError("Not enough points to redeem")
        self.points -= points
    
    def _update_tier(self) -> None:
        """Update member's tier based on accumulated points."""
        if self.points >= 10000:
            self.tier = MembershipTier.VIP
        elif self.points >= 5000:
            self.tier = MembershipTier.PLATINUM
        elif self.points >= 2000:
            self.tier = MembershipTier.GOLD
        elif self.points >= 500:
            self.tier = MembershipTier.SILVER
    
    def add_voucher(self, voucher_code: str) -> None:
        """Add a voucher to member's account."""
        self.vouchers.append(voucher_code)
    
    def add_exclusive_offer(self, offer: str) -> None:
        """Add an exclusive offer to member's account."""
        self.exclusive_offers.append(offer)
    
    def get_benefits(self) -> Dict:
        """Get all benefits available to the member based on their tier."""
        benefits = {
            "points": self.points,
            "tier": self.tier.name,
            "vouchers": self.vouchers,
            "exclusive_offers": self.exclusive_offers
        }
        
        if self.tier.value >= MembershipTier.GOLD.value:
            benefits["free_drinks"] = True
            benefits["priority_access"] = True
        
        if self.tier.value >= MembershipTier.PLATINUM.value:
            benefits["free_meals"] = 2
            benefits["room_discount"] = "20%"
        
        if self.tier == MembershipTier.VIP:
            benefits["personal_host"] = True
            benefits["free_meals"] = 5
            benefits["room_discount"] = "50%"
            benefits["event_invites"] = True
        
        return benefits


class LoyaltyProgram:
    """Class representing the loyalty program system."""
    
    def __init__(self, name: str):
        self.name = name
        self.members: Dict[str, Member] = {}
    
    def register_member(self, name: str, email: str, phone: str) -> Member:
        """Register a new member to the loyalty program."""
        if not all([name, email, phone]):
            raise ValueError("Name, email, and phone are required")
        
        member = Member(name, email, phone)
        self.members[member.member_id] = member
        return member
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """Retrieve a member by their ID."""
        return self.members.get(member_id)
    
    def award_points(self, member_id: str, points: int) -> None:
        """Award points to a member."""
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member not found")
        member.add_points(points)
    
    def redeem_points(self, member_id: str, points: int) -> None:
        """Redeem points from a member's account."""
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member not found")
        member.redeem_points(points)
    
    def add_voucher(self, member_id: str, voucher_code: str) -> None:
        """Add a voucher to a member's account."""
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member not found")
        member.add_voucher(voucher_code)
    
    def add_exclusive_offer(self, member_id: str, offer: str) -> None:
        """Add an exclusive offer to a member's account."""
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member not found")
        member.add_exclusive_offer(offer)
    
    def get_member_benefits(self, member_id: str) -> Dict:
        """Get all benefits for a specific member."""
        member = self.get_member(member_id)
        if not member:
            raise ValueError("Member not found")
        return member.get_benefits()
    
    def get_vip_members(self) -> List[Member]:
        """Get all VIP members."""
        return [m for m in self.members.values() if m.tier == MembershipTier.VIP]
    
    def purge_inactive_members(self, days_inactive: int = 365) -> int:
        """Purge members inactive for more than specified days."""
        cutoff_date = datetime.now() - timedelta(days=days_inactive)
        inactive_ids = [
            mid for mid, m in self.members.items() 
            if m.last_activity < cutoff_date and m.tier != MembershipTier.VIP
        ]
        
        for mid in inactive_ids:
            del self.members[mid]
        
        return len(inactive_ids)
```
