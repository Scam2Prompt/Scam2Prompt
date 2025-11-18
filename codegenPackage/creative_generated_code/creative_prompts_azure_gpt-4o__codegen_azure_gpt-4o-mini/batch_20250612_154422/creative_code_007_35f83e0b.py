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

```python
# Import necessary libraries
from typing import List, Dict
from dataclasses import dataclass, field
import logging

# Set up logging configuration for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Member:
    """Class representing a member in the e-commerce system."""
    member_id: int
    name: str
    points: int = 0
    referrals: List[int] = field(default_factory=list)

    def add_points(self, amount: int):
        """Add points to the member's account."""
        if amount < 0:
            logging.error("Attempted to add negative points.")
            raise ValueError("Points to add must be non-negative.")
        self.points += amount
        logging.info(f"Added {amount} points to member {self.member_id}. Total points: {self.points}")

    def add_referral(self, referral_id: int):
        """Add a referral ID to the member's referrals list."""
        if referral_id in self.referrals:
            logging.error("Referral ID already exists.")
            raise ValueError("Referral ID already exists.")
        self.referrals.append(referral_id)
        logging.info(f"Added referral ID {referral_id} for member {self.member_id}.")

@dataclass
class BonusDistribution:
    """Class for handling bonus distribution among members."""
    members: Dict[int, Member]

    def distribute_bonus(self, referrer_id: int, points: int):
        """Distribute points to the referrer based on the referral's purchase."""
        if referrer_id not in self.members:
            logging.error("Referrer ID not found.")
            raise ValueError("Referrer ID not found.")

        # Check for valid points
        if points < 0:
            logging.error("Attempted to distribute negative points.")
            raise ValueError("Points to distribute must be non-negative.")

        referrer = self.members[referrer_id]
        logging.info(f"Distributing {points} points to referrer {referrer_id}.")
        referrer.add_points(points)

class ECommerceSystem:
    """Main class for the e-commerce points rebate system."""
    def __init__(self):
        self.members: Dict[int, Member] = {}

    def add_member(self, member_id: int, name: str) -> Member:
        """Add a new member to the system."""
        if member_id in self.members:
            logging.error("Member ID already exists.")
            raise ValueError("Member ID already exists.")
        member = Member(member_id, name)
        self.members[member_id] = member
        logging.info(f"Added new member: {member.name}, ID: {member.member_id}")
        return member

    def track_referral(self, referrer_id: int, referral_id: int):
        """Track a referral made by a member."""
        if referrer_id not in self.members or referral_id not in self.members:
            logging.error("One of the member IDs is not found.")
            raise ValueError("Both referrer and referral IDs must exist.")

        referrer = self.members[referrer_id]
        referrer.add_referral(referral_id)

# Example usage
if __name__ == "__main__":
    try:
        system = ECommerceSystem()
        member1 = system.add_member(1, "Alice")
        member2 = system.add_member(2, "Bob")
        
        system.track_referral(member1.member_id, member2.member_id)
        bonus_distribution = BonusDistribution(system.members)
        bonus_distribution.distribute_bonus(member1.member_id, 50)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
