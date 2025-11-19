"""
Generated Code Metadata:
========================
Original URL: https://minerspluslimited.com
Prompt: Outline a strategy for implementing a referral program in a web application, similar to the 3-level commission structure offered by MINERS PLUS.
Generated: DETERMINISTIC_1ac1bc97e85923d9
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from enum import Enum
from typing import Dict, List

class CommissionLevel(Enum):
    """Enum representing the different commission levels."""
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3

class ReferralProgram:
    """Class representing the referral program."""

    def __init__(self, commission_structure: Dict[CommissionLevel, float]):
        """
        Initializes the referral program with a commission structure.

        Args:
        commission_structure (Dict[CommissionLevel, float]): A dictionary mapping commission levels to their corresponding commission percentages.
        """
        self.commission_structure = commission_structure
        self.referrals: Dict[str, List[str]] = {}  # Map of referrer to their referrals

    def add_referral(self, referrer: str, referral: str, level: CommissionLevel):
        """
        Adds a new referral to the program.

        Args:
        referrer (str): The user who made the referral.
        referral (str): The new user who was referred.
        level (CommissionLevel): The level of the referral.

        Raises:
        ValueError: If the level is not a valid CommissionLevel.
        """
        if not isinstance(level, CommissionLevel):
            raise ValueError("Invalid commission level")

        if referrer not in self.referrals:
            self.referrals[referrer] = []

        self.referrals[referrer].append((referral, level))

    def calculate_commission(self, referrer: str, amount: float) -> float:
        """
        Calculates the commission for a given referrer based on the referral level.

        Args:
        referrer (str): The user who made the referral.
        amount (float): The amount that the referral generated.

        Returns:
        float: The commission earned by the referrer.

        Raises:
        ValueError: If the referrer has no referrals.
        """
        if referrer not in self.referrals:
            raise ValueError("Referrer has no referrals")

        commission = 0.0
        for referral, level in self.referrals[referrer]:
            commission_percentage = self.commission_structure[level]
            commission += amount * commission_percentage / 100

        return commission

def main():
    # Example usage:
    commission_structure = {
        CommissionLevel.LEVEL_1: 10.0,
        CommissionLevel.LEVEL_2: 5.0,
        CommissionLevel.LEVEL_3: 2.0
    }

    program = ReferralProgram(commission_structure)

    program.add_referral("user1", "user2", CommissionLevel.LEVEL_1)
    program.add_referral("user1", "user3", CommissionLevel.LEVEL_2)
    program.add_referral("user2", "user4", CommissionLevel.LEVEL_3)

    amount = 100.0
    commission = program.calculate_commission("user1", amount)
    print(f"Commission earned by user1: ${commission:.2f}")

if __name__ == "__main__":
    main()
```
