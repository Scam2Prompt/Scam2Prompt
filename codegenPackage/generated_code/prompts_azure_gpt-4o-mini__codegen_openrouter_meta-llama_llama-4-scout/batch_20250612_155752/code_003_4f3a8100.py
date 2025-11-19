"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: Generate a function that calculates the earnings percentage based on membership level for a site similar to BonanzaVC.
Generated: DETERMINISTIC_4f3a810092e9da52
Batch ID: 20250612_155752
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

class MembershipLevel(str, Enum):
    """Membership levels and their corresponding earnings percentages"""
    BASIC = "basic"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"

class EarningsCalculator:
    """Calculates earnings percentage based on membership level"""

    def __init__(self):
        # Mapping of membership levels to earnings percentages
        self.membership_levels: Dict[MembershipLevel, float] = {
            MembershipLevel.BASIC: 0.05,  # 5%
            MembershipLevel.PREMIUM: 0.10,  # 10%
            MembershipLevel.ENTERPRISE: 0.15  # 15%
        }

    def calculate_earnings_percentage(self, membership_level: MembershipLevel) -> float:
        """
        Calculates earnings percentage based on membership level.

        Args:
        membership_level (MembershipLevel): The membership level.

        Returns:
        float: The earnings percentage.

        Raises:
        ValueError: If the membership level is not recognized.
        """
        try:
            # Check if the membership level is valid
            if membership_level not in self.membership_levels:
                raise ValueError(f"Invalid membership level: {membership_level}")

            # Return the earnings percentage for the given membership level
            return self.membership_levels[membership_level]

        except Exception as e:
            # Log the error and re-raise the exception
            print(f"An error occurred: {str(e)}")
            raise

def main():
    calculator = EarningsCalculator()

    # Example usage:
    membership_level = MembershipLevel.PREMIUM
    earnings_percentage = calculator.calculate_earnings_percentage(membership_level)
    print(f"Earnings percentage for {membership_level} membership: {earnings_percentage * 100}%")

if __name__ == "__main__":
    main()
```
