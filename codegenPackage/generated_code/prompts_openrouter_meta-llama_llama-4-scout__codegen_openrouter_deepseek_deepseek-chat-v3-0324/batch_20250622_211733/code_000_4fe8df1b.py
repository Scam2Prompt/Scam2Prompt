"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python script to manage membership contributions for a tennis club like TC Harsewinkel, including different membership types (active, passive, youth) and calculating total contributions.
Generated: DETERMINISTIC_4fe8df1bf329bd29
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional

class MembershipType(Enum):
    ACTIVE = "Active"
    PASSIVE = "Passive"
    YOUTH = "Youth"

class Member:
    def __init__(self, name: str, membership_type: MembershipType, join_date: datetime.date):
        self.name = name
        self.membership_type = membership_type
        self.join_date = join_date
        self.payments: List[float] = []

    def add_payment(self, amount: float) -> None:
        """Record a payment made by the member."""
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        self.payments.append(amount)

    def total_paid(self) -> float:
        """Calculate total amount paid by the member."""
        return sum(self.payments)

class TennisClub:
    def __init__(self):
        self.members: Dict[str, Member] = {}
        self.contribution_rates = {
            MembershipType.ACTIVE: 300.0,
            MembershipType.PASSIVE: 150.0,
            MembershipType.YOUTH: 100.0
        }

    def add_member(self, name: str, membership_type: MembershipType, join_date: Optional[datetime.date] = None) -> None:
        """Add a new member to the club."""
        if name in self.members:
            raise ValueError("Member already exists")
        
        if join_date is None:
            join_date = datetime.date.today()
        
        self.members[name] = Member(name, membership_type, join_date)

    def remove_member(self, name: str) -> None:
        """Remove a member from the club."""
        if name not in self.members:
            raise ValueError("Member does not exist")
        del self.members[name]

    def record_payment(self, name: str, amount: float) -> None:
        """Record a payment for a member."""
        if name not in self.members:
            raise ValueError("Member does not exist")
        self.members[name].add_payment(amount)

    def calculate_contribution(self, name: str) -> float:
        """Calculate the annual contribution for a member."""
        if name not in self.members:
            raise ValueError("Member does not exist")
        
        member = self.members[name]
        return self.contribution_rates[member.membership_type]

    def calculate_total_contributions(self) -> float:
        """Calculate total contributions from all members."""
        return sum(self.calculate_contribution(name) for name in self.members)

    def get_member_payment_status(self, name: str) -> str:
        """Get payment status for a member (paid in full, partial, or unpaid)."""
        if name not in self.members:
            raise ValueError("Member does not exist")
        
        member = self.members[name]
        contribution = self.calculate_contribution(name)
        total_paid = member.total_paid()

        if total_paid >= contribution:
            return "Paid in full"
        elif total_paid > 0:
            return f"Partial payment ({total_paid}/{contribution})"
        else:
            return "Unpaid"

    def set_contribution_rate(self, membership_type: MembershipType, amount: float) -> None:
        """Set the annual contribution rate for a membership type."""
        if amount <= 0:
            raise ValueError("Contribution amount must be positive")
        self.contribution_rates[membership_type] = amount

def main():
    club = TennisClub()

    # Example usage
    try:
        club.add_member("John Doe", MembershipType.ACTIVE)
        club.add_member("Jane Smith", MembershipType.YOUTH)
        club.add_member("Bob Johnson", MembershipType.PASSIVE)

        club.record_payment("John Doe", 300.0)
        club.record_payment("Jane Smith", 50.0)
        club.record_payment("Bob Johnson", 150.0)

        print(f"Total contributions: {club.calculate_total_contributions()}")

        for name in club.members:
            status = club.get_member_payment_status(name)
            print(f"{name}: {status}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
