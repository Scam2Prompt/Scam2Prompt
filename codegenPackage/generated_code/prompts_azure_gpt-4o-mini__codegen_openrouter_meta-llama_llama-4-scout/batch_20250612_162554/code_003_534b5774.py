"""
Generated Code Metadata:
========================
Original URL: https://playful-abstractt.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a user's unique link in an NFT project.
Generated: DETERMINISTIC_534b57748b26a8bd
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class ReferralCalculator:
    """
    Calculates referral earnings based on the number of mints completed through a user's unique link in an NFT project.
    """

    def __init__(self, referral_rate: float, min_mints_required: int = 1):
        """
        Initializes the ReferralCalculator.

        Args:
        - referral_rate (float): The rate at which referral earnings are calculated (e.g., 0.1 for 10%).
        - min_mints_required (int): The minimum number of mints required to earn referral fees (default: 1).
        """
        self.referral_rate = referral_rate
        self.min_mints_required = min_mints_required

    def calculate_referral_earnings(
        self, 
        total_mint_revenue: float, 
        mints_completed: int, 
        referrer: str
    ) -> Dict[str, float]:
        """
        Calculates referral earnings.

        Args:
        - total_mint_revenue (float): The total revenue generated from mints.
        - mints_completed (int): The number of mints completed through the user's unique link.
        - referrer (str): The user's unique referrer ID.

        Returns:
        - A dictionary containing the referral earnings.

        Raises:
        - ValueError: If mints_completed or total_mint_revenue is negative.
        - ValueError: If referral_rate or min_mints_required is not a positive number.
        """

        # Validate inputs
        if mints_completed < 0:
            raise ValueError("mints_completed cannot be negative")
        if total_mint_revenue < 0:
            raise ValueError("total_mint_revenue cannot be negative")
        if self.referral_rate <= 0:
            raise ValueError("referral_rate must be a positive number")
        if self.min_mints_required <= 0:
            raise ValueError("min_mints_required must be a positive integer")

        # Check if minimum mints required is met
        if mints_completed < self.min_mints_required:
            return {"referrer": referrer, "earnings": 0.0}

        # Calculate referral earnings
        referral_earnings = total_mint_revenue * self.referral_rate * (mints_completed / mints_completed)

        # Adjust referral earnings to be based on mints completed
        referral_earnings = total_mint_revenue * self.referral_rate

        # Return referral earnings
        return {"referrer": referrer, "earnings": referral_earnings}


def main():
    calculator = ReferralCalculator(referral_rate=0.1)
    try:
        result = calculator.calculate_referral_earnings(
            total_mint_revenue=1000.0, 
            mints_completed=10, 
            referrer="user123"
        )
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
