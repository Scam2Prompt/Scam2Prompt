"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Generate code to create a bonus system for an online gaming platform like Pelangi189, where users can claim rewards after specific milestones.
Generated: DETERMINISTIC_57efaa2c8332c4d3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_system.py

from enum import Enum
from typing import Dict, List

class MilestoneType(Enum):
    """Enum for milestone types."""
    DEPOSIT = 1
    WAGER = 2
    LOSS = 3

class Bonus:
    """Class representing a bonus."""
    def __init__(self, id: int, name: str, amount: float, milestone_type: MilestoneType, milestone_value: float):
        """
        Initialize a Bonus object.

        Args:
        id (int): Unique identifier for the bonus.
        name (str): Name of the bonus.
        amount (float): Amount of the bonus.
        milestone_type (MilestoneType): Type of milestone required to claim the bonus.
        milestone_value (float): Value of the milestone required to claim the bonus.
        """
        self.id = id
        self.name = name
        self.amount = amount
        self.milestone_type = milestone_type
        self.milestone_value = milestone_value

class User:
    """Class representing a user."""
    def __init__(self, id: int):
        """
        Initialize a User object.

        Args:
        id (int): Unique identifier for the user.
        """
        self.id = id
        self.milestones: Dict[MilestoneType, float] = {MilestoneType.DEPOSIT: 0.0, MilestoneType.WAGER: 0.0, MilestoneType.LOSS: 0.0}
        self.bonuses: List[Bonus] = []

    def update_milestone(self, milestone_type: MilestoneType, value: float):
        """
        Update a user's milestone.

        Args:
        milestone_type (MilestoneType): Type of milestone to update.
        value (float): Value to add to the milestone.
        """
        self.milestones[milestone_type] += value
        self.check_for_bonuses()

    def check_for_bonuses(self):
        """Check if the user is eligible for any bonuses."""
        for bonus in bonuses:
            if self.milestones[bonus.milestone_type] >= bonus.milestone_value and bonus not in self.bonuses:
                self.bonuses.append(bonus)
                print(f"User {self.id} is eligible for bonus {bonus.name} of {bonus.amount}")

class BonusSystem:
    """Class representing the bonus system."""
    def __init__(self):
        self.bonuses: List[Bonus] = []
        self.users: Dict[int, User] = {}

    def add_bonus(self, bonus: Bonus):
        """
        Add a bonus to the system.

        Args:
        bonus (Bonus): Bonus to add.
        """
        self.bonuses.append(bonus)

    def add_user(self, user: User):
        """
        Add a user to the system.

        Args:
        user (User): User to add.
        """
        self.users[user.id] = user

    def get_user(self, user_id: int) -> User:
        """
        Get a user from the system.

        Args:
        user_id (int): ID of the user to get.

        Returns:
        User: The user with the given ID, or None if not found.
        """
        return self.users.get(user_id)

# Initialize the bonus system
bonus_system = BonusSystem()

# Define bonuses
bonuses = [
    Bonus(1, "Welcome Bonus", 10.0, MilestoneType.DEPOSIT, 100.0),
    Bonus(2, "Wager Bonus", 20.0, MilestoneType.WAGER, 500.0),
    Bonus(3, "Loss Bonus", 5.0, MilestoneType.LOSS, 200.0)
]

# Add bonuses to the system
for bonus in bonuses:
    bonus_system.add_bonus(bonus)

# Create users
user1 = User(1)
user2 = User(2)

# Add users to the system
bonus_system.add_user(user1)
bonus_system.add_user(user2)

# Update user milestones
user1.update_milestone(MilestoneType.DEPOSIT, 150.0)
user2.update_milestone(MilestoneType.WAGER, 600.0)
user1.update_milestone(MilestoneType.LOSS, 250.0)

# Print user bonuses
print("User 1 bonuses:")
for bonus in user1.bonuses:
    print(bonus.name)

print("User 2 bonuses:")
for bonus in user2.bonuses:
    print(bonus.name)
```
