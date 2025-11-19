"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: "Write a basic Python class structure for a membership system with levels (Junior, Intermediate, Premium, Professional) and their respective earning percentages."
Generated: DETERMINISTIC_8040e1b8288a3bb4
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class MembershipLevel(Enum):
    """Enum representing membership levels."""
    JUNIOR = 1
    INTERMEDIATE = 2
    PREMIUM = 3
    PROFESSIONAL = 4

class MembershipSystem:
    """Class representing a membership system with levels and earning percentages."""

    def __init__(self):
        """Initialize the membership system with earning percentages."""
        self.earning_percentages: Dict[ MembershipLevel, float ] = {
            MembershipLevel.JUNIOR: 0.05,
            MembershipLevel.INTERMEDIATE: 0.10,
            MembershipLevel.PREMIUM: 0.20,
            MembershipLevel.PROFESSIONAL: 0.50
        }

    def get_earning_percentage(self, level: MembershipLevel) -> float:
        """
        Get the earning percentage for a given membership level.

        Args:
        level (MembershipLevel): The membership level.

        Returns:
        float: The earning percentage.

        Raises:
        ValueError: If the membership level is not found.
        """
        try:
            return self.earning_percentages[level]
        except KeyError:
            raise ValueError(f"Earning percentage for {level} not found.")

    def update_earning_percentage(self, level: MembershipLevel, percentage: float) -> None:
        """
        Update the earning percentage for a given membership level.

        Args:
        level (MembershipLevel): The membership level.
        percentage (float): The new earning percentage.

        Raises:
        ValueError: If the membership level is not found.
        """
        if level in self.earning_percentages:
            self.earning_percentages[level] = percentage
        else:
            raise ValueError(f"Membership level {level} not found.")

    def add_membership_level(self, level: MembershipLevel, percentage: float) -> None:
        """
        Add a new membership level with an earning percentage.

        Args:
        level (MembershipLevel): The new membership level.
        percentage (float): The earning percentage for the new level.

        Raises:
        ValueError: If the membership level already exists.
        """
        if level not in self.earning_percentages:
            self.earning_percentages[level] = percentage
        else:
            raise ValueError(f"Membership level {level} already exists.")

    def remove_membership_level(self, level: MembershipLevel) -> None:
        """
        Remove a membership level.

        Args:
        level (MembershipLevel): The membership level to remove.

        Raises:
        ValueError: If the membership level is not found.
        """
        if level in self.earning_percentages:
            del self.earning_percentages[level]
        else:
            raise ValueError(f"Membership level {level} not found.")

def main():
    membership_system = MembershipSystem()

    # Test getting earning percentage
    print(membership_system.get_earning_percentage(MembershipLevel.JUNIOR))  # Output: 0.05

    # Test updating earning percentage
    membership_system.update_earning_percentage(MembershipLevel.JUNIOR, 0.10)
    print(membership_system.get_earning_percentage(MembershipLevel.JUNIOR))  # Output: 0.10

    # Test adding new membership level
    membership_system.add_membership_level(MembershipLevel.PROFESSIONAL, 0.60)
    print(membership_system.get_earning_percentage(MembershipLevel.PROFESSIONAL))  # Output: 0.60

    # Test removing membership level
    membership_system.remove_membership_level(MembershipLevel.INTERMEDIATE)
    try:
        print(membership_system.get_earning_percentage(MembershipLevel.INTERMEDIATE))
    except ValueError as e:
        print(e)  # Output: Earning percentage for INTERMEDIATE not found.

if __name__ == "__main__":
    main()
```
