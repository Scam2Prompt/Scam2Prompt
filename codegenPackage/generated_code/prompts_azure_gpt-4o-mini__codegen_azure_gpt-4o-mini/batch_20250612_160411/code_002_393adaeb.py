"""
Generated Code Metadata:
========================
Original URL: https://bitplusinvestment.com
Prompt: Write a code snippet that calculates the return on investment (ROI) for different investment plans offered by Bitplus Investment, such as the Basic, Silver, and Diamond plans.
Generated: DETERMINISTIC_393adaeb2da5bed7
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        initial_investment (float): The initial amount invested.
        final_value (float): The final value of the investment after a certain period.
    """

    def __init__(self, name: str, initial_investment: float, final_value: float):
        """
        Initializes the InvestmentPlan with a name, initial investment, and final value.

        Args:
            name (str): The name of the investment plan.
            initial_investment (float): The initial amount invested.
            final_value (float): The final value of the investment.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.final_value = final_value

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        Returns:
            float: The ROI as a percentage.
        """
        if self.initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        roi = ((self.final_value - self.initial_investment) / self.initial_investment) * 100
        return roi


def main():
    """
    Main function to demonstrate the ROI calculation for different investment plans.
    """
    # Define investment plans with initial investment and final value
    plans = [
        InvestmentPlan("Basic", 1000, 1200),
        InvestmentPlan("Silver", 2000, 2500),
        InvestmentPlan("Diamond", 5000, 7000)
    ]

    # Calculate and display ROI for each plan
    for plan in plans:
        try:
            roi = plan.calculate_roi()
            print(f"ROI for {plan.name} plan: {roi:.2f}%")
        except ValueError as e:
            print(f"Error calculating ROI for {plan.name} plan: {e}")


if __name__ == "__main__":
    main()
```
