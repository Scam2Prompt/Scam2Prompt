"""
Generated Code Metadata:
========================
Original URL: https://puroworldclub.com
Prompt: Write a Python script to manage membership plans for a cigar club like Puro World Club, including premium and private membership options.
Generated: DETERMINISTIC_26d8f38ef64f8d83
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
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class MembershipPlan:
    """Represents a membership plan for the cigar club."""
    
    def __init__(self, name: str, price: float, duration_days: int, benefits: List[str]):
        """
        Initialize a membership plan.
        
        Args:
            name: Name of the membership plan
            price: Price of the membership
            duration_days: Duration in days
            benefits: List of benefits included
        """
        self.name = name
        self.price = price
        self.duration_days = duration_days
        self.benefits = benefits
    
    def to_dict(self) -> Dict:
        """Convert membership plan to dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'duration_days': self.duration_days,
            'benefits': self.benefits
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MembershipPlan':
        """Create membership plan from dictionary."""
        return cls(
            name=data['name'],
            price=data['price'],
            duration_days=data['duration_days'],
            benefits=data['benefits']
        )

class Member:
    """Represents a club member."""
    
    def __init__(self, member_id: str, name: str, email: str, phone: str, 
                 membership_plan: Optional[MembershipPlan] = None, 
                 join_date: Optional[datetime] = None,
                 expiry_date: Optional[datetime] = None):
        """
        Initialize a member.
        
        Args:
            member_id: Unique member ID
            name: Member's full name
            email: Member's email
            phone: Member's phone number
            membership_plan: Current membership plan
            join_date: Date when member joined
            expiry_date: Date when membership expires
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_plan = membership_plan
        self.join_date = join_date or datetime.now()
        self.expiry_date = expiry_date
    
    def renew_membership(self, plan: MembershipPlan) -> None:
        """Renew or upgrade the member's membership plan."""
        self.membership_plan = plan
        self.expiry_date = datetime.now() + timedelta(days=plan.duration_days)
    
    def is_active(self) -> bool:
        """Check if membership is still active."""
        if self.expiry_date is None:
            return False
        return datetime.now() < self.expiry_date
    
    def to_dict(self) -> Dict:
        """Convert member to dictionary."""
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'membership_plan': self.membership_plan.to_dict() if self.membership_plan else None,
            'join_date': self.join_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Member':
        """Create member from dictionary."""
        membership_plan = None
        if data['membership_plan']:
            membership_plan = MembershipPlan.from_dict(data['membership_plan'])
        
        join_date = datetime.fromisoformat(data['join_date'])
        
        expiry_date = None
        if data['expiry_date']:
            expiry_date = datetime.fromisoformat(data['expiry_date'])
        
        return cls(
            member_id=data['member_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            membership_plan=membership_plan,
            join_date=join_date,
            expiry_date=expiry_date
        )

class CigarClubManager:
    """Manages cigar club memberships."""
    
    def __init__(self, data_file: str = 'cigar_club_data.json'):
        """
        Initialize the club manager.
        
        Args:
            data_file: Path to JSON file for data persistence
        """
        self.data_file = data_file
        self.members: Dict[str, Member] = {}
        self.plans: Dict[str, MembershipPlan] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from JSON file."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.plans = {
                    name: MembershipPlan.from_dict(plan_data) 
                    for name, plan_data in data.get('plans', {}).items()
                }
                self.members = {
                    member_id: Member.from_dict(member_data) 
                    for member_id, member_data in data.get('members', {}).items()
                }
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save data to JSON file."""
        data = {
            'plans': {name: plan.to_dict() for name, plan in self.plans.items()},
            'members': {member_id: member.to_dict() for member_id, member in self.members.items()}
        }
        
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_membership_plan(self, plan: MembershipPlan) -> None:
        """Add a new membership plan."""
        if plan.name in self.plans:
            raise ValueError(f"Plan '{plan.name}' already exists")
        self.plans[plan.name] = plan
        self._save_data()
    
    def get_membership_plan(self, name: str) -> Optional[MembershipPlan]:
        """Get a membership plan by name."""
        return self.plans.get(name)
    
    def list_membership_plans(self) -> List[MembershipPlan]:
        """List all available membership plans."""
        return list(self.plans.values())
    
    def register_member(self, name: str, email: str, phone: str, 
                       plan_name: Optional[str] = None) -> Member:
        """
        Register a new member.
        
        Args:
            name: Member's full name
            email: Member's email
            phone: Member's phone number
            plan_name: Optional membership plan name to enroll in
        
        Returns:
            The newly created member
        """
        member_id = f"M{len(self.members) + 1:04d}"
        membership_plan = None
        expiry_date = None
        
        if plan_name:
            membership_plan = self.get_membership_plan(plan_name)
            if not membership_plan:
                raise ValueError(f"Plan '{plan_name}' not found")
            expiry_date = datetime.now() + timedelta(days=membership_plan.duration_days)
        
        member = Member(
            member_id=member_id,
            name=name,
            email=email,
            phone=phone,
            membership_plan=membership_plan,
            expiry_date=expiry_date
        )
        
        self.members[member_id] = member
        self._save_data()
        return member
    
    def renew_member(self, member_id: str, plan_name: str) -> Member:
        """
        Renew or upgrade a member's membership.
        
        Args:
            member_id: ID of member to renew
            plan_name: Name of plan to renew with
        
        Returns:
            The updated member
        """
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"Member '{member_id}' not found")
        
        plan = self.get_membership_plan(plan_name)
        if not plan:
            raise ValueError(f"Plan '{plan_name}' not found")
        
        member.renew_membership(plan)
        self._save_data()
        return member
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """Get a member by ID."""
        return self.members.get(member_id)
    
    def list_members(self, active_only: bool = False) -> List[Member]:
        """List all members, optionally filtering by active status."""
        members = list(self.members.values())
        if active_only:
            members = [m for m in members if m.is_active()]
        return members
    
    def remove_member(self, member_id: str) -> None:
        """Remove a member from the club."""
        if member_id not in self.members:
            raise ValueError(f"Member '{member_id}' not found")
        del self.members[member_id]
        self._save_data()

def main():
    """Example usage of the CigarClubManager."""
    manager = CigarClubManager()
    
    # Add some membership plans
    premium_plan = MembershipPlan(
        name="Premium",
        price=299.99,
        duration_days=365,
        benefits=["Access to premium cigars", "Monthly tastings", "Priority
