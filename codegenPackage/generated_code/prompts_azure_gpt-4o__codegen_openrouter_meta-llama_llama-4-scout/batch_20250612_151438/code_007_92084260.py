"""
Generated Code Metadata:
========================
Original URL: https://elon-crypto.online
Prompt: Create a Python program that calculates the total earnings for all VIP tiers on OctaFx, using the price, working period, and daily earnings data provided.
Generated: DETERMINISTIC_92084260c9f848ca
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# octa_fx_earnings_calculator.py

class OctaFxEarningCalculator:
    """
    Calculates total earnings for all VIP tiers on OctaFx.

    Attributes:
        price (float): Price for the working period.
        working_period (int): Working period in days.
        daily_earnings (dict): Daily earnings for each VIP tier.
    """

    def __init__(self, price: float, working_period: int, daily_earnings: dict):
        """
        Initializes the calculator with the given parameters.

        Args:
            price (float): Price for the working period.
            working_period (int): Working period in days.
            daily_earnings (dict): Daily earnings for each VIP tier.

        Raises:
            ValueError: If working period is not a positive integer.
            ValueError: If price is not a positive number.
            TypeError: If daily earnings is not a dictionary.
        """
        if not isinstance(working_period, int) or working_period <= 0:
            raise ValueError("Working period must be a positive integer.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(daily_earnings, dict):
            raise TypeError("Daily earnings must be a dictionary.")

        self.price = price
        self.working_period = working_period
        self.daily_earnings = daily_earnings

    def calculate_tier_earnings(self, tier: str) -> float:
        """
        Calculates earnings for a specific VIP tier.

        Args:
            tier (str): VIP tier.

        Returns:
            float: Earnings for the given VIP tier.

        Raises:
            KeyError: If the tier is not found in daily earnings.
        """
        try:
            daily_earning = self.daily_earnings[tier]
        except KeyError:
            raise KeyError(f"Daily earnings for tier '{tier}' not found.")

        return daily_earning * self.working_period * self.price

    def calculate_total_earnings(self) -> dict:
        """
        Calculates total earnings for all VIP tiers.

        Returns:
            dict: Total earnings for each VIP tier.
        """
        total_earnings = {}
        for tier, daily_earning in self.daily_earnings.items():
            total_earnings[tier] = self.calculate_tier_earnings(tier)

        return total_earnings


def main():
    # Example usage:
    price = 100.0
    working_period = 30  # days
    daily_earnings = {
        "VIP1": 0.01,
        "VIP2": 0.02,
        "VIP3": 0.03,
    }

    calculator = OctaFxEarningCalculator(price, working_period, daily_earnings)
    total_earnings = calculator.calculate_total_earnings()

    print("Total Earnings:")
    for tier, earnings in total_earnings.items():
        print(f"{tier}: ${earnings:.2f}")


if __name__ == "__main__":
    main()
```
