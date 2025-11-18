"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstmemes.com
Prompt: Develop a Python program that calculates the potential ROI of investing in "good vibes," as humorously discussed in Wall Street Memes' article on outperforming blue-chip stocks.
Generated: DETERMINISTIC_fc804693ddf7326e
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GoodVibesInvestment:
    """
    A class to represent an investment in 'good vibes'.
    This investment simulates potential returns based on a randomized model.
    """

    def __init__(self, initial_investment: float, years: int):
        """
        Initializes the GoodVibesInvestment with the initial amount and investment duration.

        :param initial_investment: The initial amount of money to invest in good vibes.
        :param years: The number of years the investment will be held.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if years <= 0:
            raise ValueError("Investment duration must be a positive integer.")

        self.initial_investment = initial_investment
        self.years = years

    def simulate_roi(self) -> float:
        """
        Simulates the ROI for 'good vibes' investment.

        :return: The final value of the investment after the specified number of years.
        """
        # Simulate annual growth rate as a random percentage between 5% and 20%
        annual_growth_rate = random.uniform(0.05, 0.20)
        final_value = self.initial_investment * ((1 + annual_growth_rate) ** self.years)
        return final_value

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI) percentage.

        :return: The ROI as a percentage of the initial investment.
        """
        final_value = self.simulate_roi()
        roi = ((final_value - self.initial_investment) / self.initial_investment) * 100
        return roi


def main():
    """
    Main function to execute the Good Vibes Investment simulation.
    It gathers user input and displays the potential ROI from investing in 'good vibes'.
    """
    try:
        initial_investment = float(input("Enter your initial investment amount in 'good vibes': "))
        years = int(input("Enter the number of years you plan to invest: "))

        # Create an investment instance
        investment = GoodVibesInvestment(initial_investment, years)
        
        # Calculate ROI
        roi = investment.calculate_roi()
        
        # Display the result
        print(f"After {years} years of investing in 'good vibes', your ROI is approximately {roi:.2f}%.")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
```
