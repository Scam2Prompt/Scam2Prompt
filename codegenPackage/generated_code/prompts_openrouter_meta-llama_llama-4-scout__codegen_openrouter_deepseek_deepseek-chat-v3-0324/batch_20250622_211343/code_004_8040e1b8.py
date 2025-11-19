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
from typing import Optional

class MembershipLevel(Enum):
    """Enumeration of membership levels and their earning percentages."""
    JUNIOR = 0.05      # 5% earning
    INTERMEDIATE = 0.1 # 10% earning
    PREMIUM = 0.15     # 15% earning
    PROFESSIONAL = 0.2 # 20% earning

class Member:
    """Represents a member in the membership system."""

    def __init__(self, name: str, level: MembershipLevel = MembershipLevel.JUNIOR):
        """
        Initialize a member with a name and membership level.
        
        Args:
            name: The name of the member.
            level: The membership level (default: JUNIOR).
        """
        self.name = name
        self.level = level
        self.total_earnings: float = 0.0

    def calculate_earnings(self, amount: float) -> float:
        """
        Calculate earnings based on the member's level percentage.
        
        Args:
            amount: The base amount to calculate earnings from.
            
        Returns:
            The calculated earnings.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        earnings = amount * self.level.value
        self.total_earnings += earnings
        return earnings

    def upgrade_membership(self, new_level: MembershipLevel) -> None:
        """
        Upgrade the member's membership level.
        
        Args:
            new_level: The new membership level.
        """
        self.level = new_level

    def __str__(self) -> str:
        """Return a string representation of the member."""
        return f"Member(name={self.name}, level={self.level.name}, total_earnings={self.total_earnings:.2f})"

# Example usage
if __name__ == "__main__":
    try:
        member = Member("Alice")
        print(member)
        
        earnings = member.calculate_earnings(1000)
        print(f"Earned: ${earnings:.2f}")
        print(member)
        
        member.upgrade_membership(MembershipLevel.PREMIUM)
        earnings = member.calculate_earnings(1000)
        print(f"Earned: ${earnings:.2f}")
        print(member)
        
    except ValueError as e:
        print(f"Error: {e}")
```
