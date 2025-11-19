"""
Generated Code Metadata:
========================
Original URL: https://premiertradeoptions.com
Prompt: Can you provide an example of how to calculate the return on investment (ROI) for different trading plans offered by Premier Trade Options?
Generated: DETERMINISTIC_37d2e6797e1aa2e4
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingPlan:
    """
    A class to represent a trading plan and calculate its return on investment (ROI).
    """

    def __init__(self, initial_investment: float, final_value: float):
        """
        Initializes the TradingPlan with initial investment and final value.

        :param initial_investment: The amount of money initially invested.
        :param final_value: The value of the investment at the end of the trading period.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if final_value < 0:
            raise ValueError("Final value cannot be negative.")

        self.initial_investment = initial_investment
        self.final_value = final_value

    def calculate_roi(self) -> float:
        """
        Calculates the return on investment (ROI).

        :return: The ROI as a percentage.
        """
        roi = ((self.final_value - self.initial_investment) / self.initial_investment) * 100
        return roi

def main():
    """
    Main function to demonstrate the ROI calculation for different trading plans.
    """
    try:
        # Example trading plans with initial investments and final values
        plans = [
            TradingPlan(initial_investment=1000, final_value=1500),
            TradingPlan(initial_investment=2000, final_value=2500),
            TradingPlan(initial_investment=1500, final_value=1200),  # This will show a loss
        ]

        # Calculate and display ROI for each trading plan
        for index, plan in enumerate(plans):
            roi = plan.calculate_roi()
            print(f"Trading Plan {index + 1}: ROI = {roi:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
