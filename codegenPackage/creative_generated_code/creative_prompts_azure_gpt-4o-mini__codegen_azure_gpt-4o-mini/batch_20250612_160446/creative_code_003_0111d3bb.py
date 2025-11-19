"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Create a function that calculates potential ROI for the various investment plans offered by Aphatradespro, such as Spot Futures and Infinity Grid Bot.
Generated: DETERMINISTIC_0111d3bb7a5e14a8
Batch ID: 20250612_160446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class representing an investment plan with its specifics
    for calculating potential Return on Investment (ROI).
    """

    def __init__(self, name, initial_investment, expected_return_rate, duration_years):
        """
        Initializes the InvestmentPlan with necessary parameters.

        :param name: str - The name of the investment plan
        :param initial_investment: float - The initial amount invested
        :param expected_return_rate: float - The expected annual return rate (as a decimal)
        :param duration_years: int - The duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.expected_return_rate = expected_return_rate
        self.duration_years = duration_years

    def calculate_roi(self):
        """
        Calculates the potential ROI for the investment plan.

        :return: float - The potential return on investment
        :raises ValueError: If initial_investment or duration_years is negative
        """
        if self.initial_investment < 0:
            raise ValueError("Initial investment must be non-negative.")
        if self.duration_years < 0:
            raise ValueError("Duration in years must be non-negative.")
        
        # Calculate the future value of the investment using compound interest formula
        future_value = self.initial_investment * (1 + self.expected_return_rate) ** self.duration_years
        
        # Calculate the ROI as a percentage
        roi = (future_value - self.initial_investment) / self.initial_investment * 100
        
        return roi

def main():
    """
    Main function to demonstrate the ROI calculation for different investment plans.
    """
    # Sample investment plans
    plans = [
        InvestmentPlan("Spot Futures", 1000, 0.08, 5),  # 8% expected return over 5 years
        InvestmentPlan("Infinity Grid Bot", 2000, 0.1, 3)  # 10% expected return over 3 years
    ]

    # Calculate and display the ROI for each investment plan
    for plan in plans:
        try:
            roi = plan.calculate_roi()
            print(f"{plan.name} ROI: {roi:.2f}%")
        except ValueError as e:
            print(f"Error calculating ROI for {plan.name}: {e}")

if __name__ == "__main__":
    main()
```
