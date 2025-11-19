"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: "Design a simple membership level system with 4 levels (Junior, Intermediate, Premium, Professional) with increasing earning percentages (0.7%, 0.8%, 1%, 1.2%)."
Generated: DETERMINISTIC_e140908d0bd56b2a
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
    JUNIOR = "Junior"
    INTERMEDIATE = "Intermediate"
    PREMIUM = "Premium"
    PROFESSIONAL = "Professional"

class MembershipSystem:
    """Class representing a simple membership level system."""
    
    def __init__(self):
        """Initialize membership levels with their respective earning percentages."""
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
            raise ValueError(f"Membership level '{level}' not found.")

    def calculate_earnings(self, level: MembershipLevel, amount: float) -> float:
        """Calculate earnings based on the membership level and amount.

        Args:
        level (MembershipLevel): The membership level.
        amount (float): The amount to calculate earnings for.

        Returns:
        float: The calculated earnings.

        Raises:
        ValueError: If the membership level is not found or if the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        earning_percentage = self.get_earning_percentage(level)
        return amount * earning_percentage

def main():
    membership_system = MembershipSystem()

    # Example usage:
    levels = [MembershipLevel.JUNIOR, MembershipLevel.INTERMEDIATE, MembershipLevel.PREMIUM, MembershipLevel.PROFESSIONAL]
    amount = 1000.0

    for level in levels:
        try:
            earning_percentage = membership_system.get_earning_percentage(level)
            earnings = membership_system.calculate_earnings(level, amount)
            print(f"Membership Level: {level.value}, Earning Percentage: {earning_percentage*100:.2f}%, Earnings: ${earnings:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
