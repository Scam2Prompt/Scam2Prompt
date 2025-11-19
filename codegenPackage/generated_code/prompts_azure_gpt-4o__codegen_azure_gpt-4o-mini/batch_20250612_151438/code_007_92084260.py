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
class VIPTierEarningsCalculator:
    """
    A class to calculate total earnings for all VIP tiers on OctaFx.
    """

    def __init__(self, price_per_unit, working_period_days, daily_earnings):
        """
        Initializes the calculator with the price per unit, working period, and daily earnings.

        :param price_per_unit: float, the price for each unit of currency
        :param working_period_days: int, the number of days worked
        :param daily_earnings: list of floats, daily earnings for each VIP tier
        """
        self.price_per_unit = price_per_unit
        self.working_period_days = working_period_days
        self.daily_earnings = daily_earnings

    def calculate_total_earnings(self):
        """
        Calculates the total earnings for all VIP tiers.

        :return: float, total earnings across all tiers
        """
        if not self.daily_earnings:
            raise ValueError("Daily earnings list cannot be empty.")

        total_earnings = 0.0

        for earnings in self.daily_earnings:
            if earnings < 0:
                raise ValueError("Daily earnings cannot be negative.")
            total_earnings += earnings * self.working_period_days

        return total_earnings * self.price_per_unit

def main():
    """
    Main function to execute the earnings calculation.
    """
    try:
        # Example input values
        price_per_unit = 1.5  # Price per unit in currency
        working_period_days = 30  # Total working days
        daily_earnings = [100.0, 150.0, 200.0]  # Daily earnings for each VIP tier

        # Create an instance of the calculator
        calculator = VIPTierEarningsCalculator(price_per_unit, working_period_days, daily_earnings)

        # Calculate total earnings
        total_earnings = calculator.calculate_total_earnings()

        # Output the result
        print(f"Total earnings for all VIP tiers: {total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
