"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-crypto.online
Prompt: Create a Python program that calculates the total earnings for all VIP tiers on OctaFx, using the price, working period, and daily earnings data provided.
Generated: DETERMINISTIC_92084260c9f848ca
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

class VIPTierEarningsCalculator:
    """
    A class to calculate total earnings for all VIP tiers on OctaFx.
    """

    def __init__(self, price: float, working_period_days: int, daily_earnings: Dict[str, float]):
        """
        Initialize the VIPTierEarningsCalculator with price, working period, and daily earnings.

        :param price: The price to be used for calculations.
        :param working_period_days: The total number of working days.
        :param daily_earnings: A dictionary containing daily earnings for each VIP tier.
        """
        self.price = price
        self.working_period_days = working_period_days
        self.daily_earnings = daily_earnings

    def calculate_total_earnings(self) -> Dict[str, float]:
        """
        Calculate total earnings for each VIP tier.

        :return: A dictionary with VIP tiers as keys and their corresponding total earnings as values.
        """
        total_earnings = {}
        try:
            for tier, daily_earning in self.daily_earnings.items():
                total_earnings[tier] = self.calculate_earnings(daily_earning)
        except Exception as e:
            print(f"An error occurred during the calculation: {e}")
        
        return total_earnings

    def calculate_earnings(self, daily_earning: float) -> float:
        """
        Calculate the total earnings based on daily earnings and working period.

        :param daily_earning: The daily earnings for a specific VIP tier.
        :return: The total earnings for the period.
        """
        if daily_earning < 0:
            raise ValueError("Daily earnings cannot be negative.")
        
        total = daily_earning * self.working_period_days
        return total

# Example usage
if __name__ == "__main__":
    # Define price, working period, and daily earnings for various VIP tiers
    price = 1000.0  # Example price
    working_period_days = 30  # Example working period in days
    daily_earnings = {
        'VIP1': 50.0,
        'VIP2': 100.0,
        'VIP3': 150.0
    }

    # Create an instance of the calculator
    calculator = VIPTierEarningsCalculator(price, working_period_days, daily_earnings)
    
    # Calculate total earnings
    earnings = calculator.calculate_total_earnings()
    
    # Display the results
    for tier, total in earnings.items():
        print(f"Total earnings for {tier}: ${total:.2f}")
```
