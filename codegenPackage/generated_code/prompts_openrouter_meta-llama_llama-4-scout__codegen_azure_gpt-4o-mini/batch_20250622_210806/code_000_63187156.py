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
import datetime
from typing import List, Dict, Optional

class MembershipPlan:
    """Class to represent a membership plan for the Jiu-Jitsu school."""
    
    def __init__(self, name: str, price: float, duration_months: int):
        """
        Initialize a new membership plan.

        :param name: Name of the membership plan
        :param price: Price of the membership plan
        :param duration_months: Duration of the membership in months
        """
        self.name = name
        self.price = price
        self.duration_months = duration_months

    def __str__(self):
        return f"{self.name}: ${self.price} for {self.duration_months} months"


class Member:
    """Class to represent a member of the Jiu-Jitsu school."""
    
    def __init__(self, name: str, membership_plan: MembershipPlan):
        """
        Initialize a new member.

        :param name: Name of the member
        :param membership_plan: Membership plan associated with the member
        """
        self.name = name
        self.membership_plan = membership_plan
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30 * membership_plan.duration_months)

    def is_active(self) -> bool:
        """Check if the membership is currently active."""
        return datetime.date.today() <= self.end_date

    def __str__(self):
        status = "Active" if self.is_active() else "Inactive"
        return f"{self.name} - {self.membership_plan} (Status: {status})"


class JiuJitsuSchool:
    """Class to manage the Jiu-Jitsu school membership plans and members."""
    
    def __init__(self):
        """Initialize the Jiu-Jitsu school with an empty list of membership plans and members."""
        self.membership_plans: List[MembershipPlan] = []
        self.members: List[Member] = []

    def add_membership_plan(self, plan: MembershipPlan):
        """Add a new membership plan to the school."""
        self.membership_plans.append(plan)

    def register_member(self, name: str, plan_name: str) -> Optional[Member]:
        """
        Register a new member with a specified membership plan.

        :param name: Name of the member
        :param plan_name: Name of the membership plan
        :return: The newly created Member object or None if the plan does not exist
        """
        plan = next((p for p in self.membership_plans if p.name == plan_name), None)
        if plan is None:
            print(f"Error: Membership plan '{plan_name}' does not exist.")
            return None
        
        new_member = Member(name, plan)
        self.members.append(new_member)
        return new_member

    def list_members(self) -> List[str]:
        """List all members and their membership status."""
        return [str(member) for member in self.members]

    def list_membership_plans(self) -> List[str]:
        """List all available membership plans."""
        return [str(plan) for plan in self.membership_plans]


# Example usage
if __name__ == "__main__":
    school = JiuJitsuSchool()

    # Adding membership plans
    school.add_membership_plan(MembershipPlan("Basic", 50.0, 1))
    school.add_membership_plan(MembershipPlan("Standard", 140.0, 3))
    school.add_membership_plan(MembershipPlan("Premium", 500.0, 12))

    # Registering members
    member1 = school.register_member("Alice", "Basic")
    member2 = school.register_member("Bob", "Standard")
    member3 = school.register_member("Charlie", "Nonexistent Plan")  # This will show an error

    # Listing members
    print("Members:")
    for member in school.list_members():
        print(member)

    # Listing membership plans
    print("\nMembership Plans:")
    for plan in school.list_membership_plans():
        print(plan)
```
