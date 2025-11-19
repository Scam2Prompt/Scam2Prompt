"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Generate a Python program to manage membership plans for a Jiu-Jitsu school like Fusion Jiu Jitsu School, including pricing and scheduling features."
Generated: DETERMINISTIC_6318715617eadd42
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class MembershipPlan:
    """Represents a membership plan with pricing and duration."""
    
    def __init__(self, name: str, price: float, duration_days: int, description: str = ""):
        """
        Initialize a membership plan.
        
        Args:
            name: Name of the plan
            price: Monthly price in USD
            duration_days: Duration of plan in days
            description: Optional description of the plan
        """
        self.name = name
        self.price = price
        self.duration_days = duration_days
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert the membership plan to a dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'duration_days': self.duration_days,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MembershipPlan':
        """Create a MembershipPlan from a dictionary."""
        return cls(
            name=data['name'],
            price=data['price'],
            duration_days=data['duration_days'],
            description=data.get('description', '')
        )

class Member:
    """Represents a member with membership details."""
    
    def __init__(self, name: str, email: str, phone: str, plan: MembershipPlan, start_date: datetime = None):
        """
        Initialize a member.
        
        Args:
            name: Member's full name
            email: Member's email address
            phone: Member's phone number
            plan: MembershipPlan object
            start_date: Optional start date (defaults to today)
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.plan = plan
        self.start_date = start_date if start_date else datetime.now()
        self.payments = []
    
    def add_payment(self, amount: float, date: datetime = None) -> None:
        """Record a payment made by the member."""
        if not date:
            date = datetime.now()
        self.payments.append({
            'amount': amount,
            'date': date
        })
    
    def get_end_date(self) -> datetime:
        """Calculate the end date of the membership."""
        return self.start_date + timedelta(days=self.plan.duration_days)
    
    def is_active(self) -> bool:
        """Check if the membership is currently active."""
        return datetime.now() < self.get_end_date()
    
    def to_dict(self) -> Dict:
        """Convert the member to a dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'plan': self.plan.to_dict(),
            'start_date': self.start_date.isoformat(),
            'payments': self.payments
        }
    
    @classmethod
    def from_dict(cls, data: Dict, plans: List[MembershipPlan]) -> 'Member':
        """Create a Member from a dictionary."""
        plan_name = data['plan']['name']
        plan = next((p for p in plans if p.name == plan_name), None)
        if not plan:
            raise ValueError(f"Plan '{plan_name}' not found")
        
        return cls(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            plan=plan,
            start_date=datetime.fromisoformat(data['start_date'])
        )

class ClassSchedule:
    """Represents a class schedule."""
    
    def __init__(self):
        self.schedule = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }
    
    def add_class(self, day: str, time: str, instructor: str, level: str) -> None:
        """Add a class to the schedule."""
        if day not in self.schedule:
            raise ValueError(f"Invalid day: {day}")
        
        self.schedule[day].append({
            'time': time,
            'instructor': instructor,
            'level': level
        })
    
    def get_classes_for_day(self, day: str) -> List[Dict]:
        """Get all classes for a specific day."""
        if day not in self.schedule:
            raise ValueError(f"Invalid day: {day}")
        return self.schedule[day]
    
    def to_dict(self) -> Dict:
        """Convert the schedule to a dictionary."""
        return self.schedule
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ClassSchedule':
        """Create a ClassSchedule from a dictionary."""
        schedule = cls()
        schedule.schedule = data
        return schedule

class JiuJitsuSchool:
    """Main class to manage the Jiu-Jitsu school operations."""
    
    def __init__(self, name: str):
        """Initialize the school with a name."""
        self.name = name
        self.members = []
        self.plans = []
        self.schedule = ClassSchedule()
    
    def add_membership_plan(self, plan: MembershipPlan) -> None:
        """Add a membership plan to the school."""
        if any(p.name == plan.name for p in self.plans):
            raise ValueError(f"Plan '{plan.name}' already exists")
        self.plans.append(plan)
    
    def register_member(self, member: Member) -> None:
        """Register a new member."""
        if any(m.email == member.email for m in self.members):
            raise ValueError(f"Member with email '{member.email}' already exists")
        self.members.append(member)
    
    def get_member(self, email: str) -> Optional[Member]:
        """Get a member by email."""
        return next((m for m in self.members if m.email == email), None)
    
    def get_active_members(self) -> List[Member]:
        """Get all active members."""
        return [m for m in self.members if m.is_active()]
    
    def save_to_file(self, filename: str) -> None:
        """Save school data to a JSON file."""
        data = {
            'name': self.name,
            'plans': [p.to_dict() for p in self.plans],
            'members': [m.to_dict() for m in self.members],
            'schedule': self.schedule.to_dict()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, default=str)
        except IOError as e:
            raise IOError(f"Failed to save data: {str(e)}")
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'JiuJitsuSchool':
        """Load school data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load data: {str(e)}")
        
        school = cls(data['name'])
        
        # Load plans
        for plan_data in data['plans']:
            school.add_membership_plan(MembershipPlan.from_dict(plan_data))
        
        # Load members
        for member_data in data['members']:
            try:
                school.register_member(Member.from_dict(member_data, school.plans))
            except ValueError as e:
                print(f"Warning: {str(e)}")
        
        # Load schedule
        school.schedule = ClassSchedule.from_dict(data['schedule'])
        
        return school

# Example usage
if __name__ == "__main__":
    # Create a school
    school = JiuJitsuSchool("Fusion Jiu Jitsu School")
    
    # Add membership plans
    basic_plan = MembershipPlan("Basic", 99.99, 30, "Access to fundamental classes")
    premium_plan = MembershipPlan("Premium", 149.99, 30, "Access to all classes and private sessions")
    school.add_membership_plan(basic_plan)
    school.add_membership_plan(premium_plan)
    
    # Register members
    member1 = Member("John Doe", "john@example.com", "555-1234", basic_plan)
    member2 = Member("Jane Smith", "jane@example.com", "555-5678", premium_plan)
    school.register_member(member1)
    school.register_member(member2)
    
    # Record payments
    member1.add_payment(99.99)
    member2.add_payment(149.99)
    
    # Add classes to schedule
    school.schedule.add_class("Monday", "6:00 PM", "Professor Silva", "All Levels")
    school.schedule.add_class("Wednesday", "7:00 PM", "Coach Johnson", "Advanced")
    school.schedule.add_class("Saturday", "10:00 AM", "Professor Silva", "Fundamentals")
    
    # Save to file
    school.save_to_file("fusion_jjs_data.json")
    
    # Load from file
    loaded_school = JiuJitsuSchool.load_from_file("fusion_jjs_data.json")
    print(f"Loaded school: {loaded_school.name}")
