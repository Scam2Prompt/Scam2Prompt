"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Write a Python code snippet to implement a membership system with levels (Junior, Intermediate, Premium, Professional) and their respective earning percentages (0.7%, 0.8%, 1%, 1.2%).
Generated: DETERMINISTIC_c0a29300825fb0cb
Batch ID: 20250622_212546
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
    JUNIOR = "Junior"
    INTERMEDIATE = "Intermediate"
    PREMIUM = "Premium"
    PROFESSIONAL = "Professional"

class MembershipSystem:
    """Class representing a membership system."""
    
    def __init__(self):
        """Initialize membership levels and their earning percentages."""
        self.membership_levels: Dict[MembershipLevel, float] = {
            MembershipLevel.JUNIOR: 0.007,
            MembershipLevel.INTERMEDIATE: 0.008,
            MembershipLevel.PREMIUM: 0.01,
            MembershipLevel.PROFESSIONAL: 0.012,
        }

    def get_earning_percentage(self, level: MembershipLevel) -> float:
        """Get the earning percentage for a given membership level.

        Args:
        level (MembershipLevel): The membership level.

        Returns:
        float: The earning percentage.

        Raises:
        ValueError: If the membership level is not found.
        """
        try:
            return self.membership_levels[level]
        except KeyError:
            raise ValueError("Membership level not found.")

    def calculate_earnings(self, amount: float, level: MembershipLevel) -> float:
        """Calculate earnings based on the amount and membership level.

        Args:
        amount (float): The amount to calculate earnings for.
        level (MembershipLevel): The membership level.

        Returns:
        float: The calculated earnings.

        Raises:
        ValueError: If the amount is negative or the membership level is not found.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        earning_percentage = self.get_earning_percentage(level)
        return amount * earning_percentage

def main():
    membership_system = MembershipSystem()
    
    # Example usage:
    amount = 1000.0
    level = MembershipLevel.PREMIUM
    try:
        earnings = membership_system.calculate_earnings(amount, level)
        print(f"Earnings for {level.value} member: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
