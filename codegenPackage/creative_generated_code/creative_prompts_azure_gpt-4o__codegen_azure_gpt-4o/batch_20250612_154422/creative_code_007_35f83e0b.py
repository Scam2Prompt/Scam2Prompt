"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Provide a solution for implementing a "积分返利商城直销系统" (points rebate e-commerce direct selling system) with features like bonus distribution and member tracking, as outlined by JieyaSoft.
Generated: DETERMINISTIC_35f83e0b60643d92
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready implementation in Python. The system includes core features like member management, points rebate logic, and bonus distribution. It uses an object-oriented approach and includes proper error handling, documentation, and follows Python best practices.

```python
import uuid
from typing import List, Dict

class Member:
    """
    Represents a member in the system.
    Attributes:
        member_id (str): Unique identifier for the member.
        name (str): Member's name.
        points (float): Points accumulated by the member.
        bonuses (float): Bonuses distributed to the member.
        referrals (List[str]): List of referral member IDs.
    """
    def __init__(self, name: str):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.points = 0.0
        self.bonuses = 0.0
        self.referrals = []

    def add_points(self, amount: float):
        """Adds points to the member's account."""
        if amount < 0:
            raise ValueError("Points amount cannot be negative.")
        self.points += amount

    def add_bonus(self, amount: float):
        """Adds a bonus to the member's account."""
        if amount < 0:
            raise ValueError("Bonus amount cannot be negative.")
        self.bonuses += amount

    def add_referral(self, referral_id: str):
        """Adds a referred member ID to the list of referrals."""
        self.referrals.append(referral_id)

    def get_summary(self) -> Dict[str, float]:
        """Returns a summary of the member's points and bonuses."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "points": self.points,
            "bonuses": self.bonuses,
            "referrals": self.referrals,
        }


class PointsRebateSystem:
    """
    Points rebate direct selling system for managing members, points, and bonuses.
    Attributes:
        members (Dict[str, Member]): Dictionary of members (key: member_id, value: Member object).
    """
    def __init__(self):
        self.members = {}

    def register_member(self, name: str) -> str:
        """
        Registers a new member in the system.
        Args:
            name (str): Name of the member.
        Returns:
            str: The newly created member's ID.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        member = Member(name)
        self.members[member.member_id] = member
        return member.member_id

    def distribute_points(self, member_id: str, amount: float):
        """
        Distributes points to a specific member.
        Args:
            member_id (str): ID of the member.
            amount (float): Amount of points to distribute.
        """
        member = self.members.get(member_id)
        if not member:
            raise ValueError("Invalid member ID.")
        member.add_points(amount)

    def distribute_bonus(self, member_id: str, amount: float):
        """
        Distributes bonuses to a specific member.
        Args:
            member_id (str): ID of the member.
            amount (float): Amount of bonuses to distribute.
        """
        member = self.members.get(member_id)
        if not member:
            raise ValueError("Invalid member ID.")
        member.add_bonus(amount)

    def add_referral(self, referrer_id: str, referred_name: str) -> str:
        """
        Adds a referral relationship between two members.
        Args:
            referrer_id (str): ID of the referrer.
            referred_name (str): Name of the referred member.
        Returns:
            str: The referred member's ID.
        """
        referrer = self.members.get(referrer_id)
        if not referrer:
            raise ValueError("Invalid referrer ID.")
        referred_id = self.register_member(referred_name)
        referrer.add_referral(referred_id)
        return referred_id

    def get_member_summary(self, member_id: str) -> Dict[str, float]:
        """
        Retrieves the summary information for a specific member.
        Args:
            member_id (str): ID of the member.
        Returns:
            Dict[str, float]: Summary data of the member.
        """
        member = self.members.get(member_id)
        if not member:
            raise ValueError("Invalid member ID.")
        return member.get_summary()

    def get_all_members(self) -> List[Dict[str, float]]:
        """
        Retrieves summaries for all members in the system.
        Returns:
            List[Dict[str, float]]: List of summary dictionaries for all members.
        """
        return [member.get_summary() for member in self.members.values()]


# Example usage (commented out for production-ready code):
# if __name__ == "__main__":
#     system = PointsRebateSystem()
#     member_id = system.register_member("Alice")
#     system.distribute_points(member_id, 100.0)
#     system.distribute_bonus(member_id, 20.0)
#     referred_id = system.add_referral(member_id, "Bob")
#     print(system.get_member_summary(member_id))
#     print(system.get_member_summary(referred_id))
```

This code is structured to be expanded easily for new features, such as transaction history or complex bonus distribution rules. It also includes appropriate error handling and validation.
