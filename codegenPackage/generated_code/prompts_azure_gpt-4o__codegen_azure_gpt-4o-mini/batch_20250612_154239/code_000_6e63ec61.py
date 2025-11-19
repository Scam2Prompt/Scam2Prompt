"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Write a Python script to simulate a cashback calculation for a casino platform, including user loyalty tiers and bonus percentages as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_6e63ec61c0a39ddc
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoyaltyTier:
    """Class representing a loyalty tier in the casino platform."""
    
    def __init__(self, name, min_spend, cashback_percentage):
        """
        Initialize a loyalty tier.

        :param name: Name of the loyalty tier.
        :param min_spend: Minimum spend required to qualify for this tier.
        :param cashback_percentage: Cashback percentage for this tier.
        """
        self.name = name
        self.min_spend = min_spend
        self.cashback_percentage = cashback_percentage


class CashbackCalculator:
    """Class to calculate cashback based on user spend and loyalty tier."""
    
    def __init__(self, tiers):
        """
        Initialize the cashback calculator with loyalty tiers.

        :param tiers: List of LoyaltyTier objects.
        """
        self.tiers = tiers

    def get_loyalty_tier(self, total_spend):
        """
        Determine the user's loyalty tier based on total spend.

        :param total_spend: Total amount spent by the user.
        :return: The user's loyalty tier.
        """
        for tier in sorted(self.tiers, key=lambda x: x.min_spend):
            if total_spend >= tier.min_spend:
                return tier
        return None

    def calculate_cashback(self, total_spend):
        """
        Calculate the cashback amount based on total spend.

        :param total_spend: Total amount spent by the user.
        :return: Cashback amount.
        """
        tier = self.get_loyalty_tier(total_spend)
        if tier:
            cashback = total_spend * (tier.cashback_percentage / 100)
            return cashback
        else:
            return 0.0  # No cashback if no tier is applicable


def main():
    """Main function to run the cashback calculation."""
    # Define loyalty tiers
    tiers = [
        LoyaltyTier("Bronze", 0, 1.0),  # 1% cashback for spending $0+
        LoyaltyTier("Silver", 1000, 2.0),  # 2% cashback for spending $1000+
        LoyaltyTier("Gold", 5000, 3.0),  # 3% cashback for spending $5000+
        LoyaltyTier("Platinum", 10000, 5.0)  # 5% cashback for spending $10000+
    ]

    # Create a cashback calculator instance
    calculator = CashbackCalculator(tiers)

    # Example user spend
    user_spend = 7500  # Example total spend

    try:
        # Calculate cashback
        cashback = calculator.calculate_cashback(user_spend)
        print(f"Total spend: ${user_spend:.2f}")
        print(f"Cashback earned: ${cashback:.2f}")
    except Exception as e:
        print(f"An error occurred during cashback calculation: {e}")


if __name__ == "__main__":
    main()
```
