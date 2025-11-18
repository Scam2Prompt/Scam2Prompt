"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-stockfinancemarket.com
Prompt: Write code to simulate the ROI calculation for the Starter Weekly investment plan offered by Multi-stock Finance Market, including minimum and maximum investment constraints.
Generated: DETERMINISTIC_34a8a20112465b31
Batch ID: 20250612_150116
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
    A class to represent an investment plan for calculating Return on Investment (ROI).
    """

    def __init__(self, min_investment: float, max_investment: float):
        """
        Initialize the investment plan with minimum and maximum investment limits.

        Args:
            min_investment (float): Minimum investment amount.
            max_investment (float): Maximum investment amount.
        """
        if min_investment <= 0 or max_investment <= 0:
            raise ValueError("Investment amounts must be greater than zero.")
        if min_investment >= max_investment:
            raise ValueError("Minimum investment must be less than maximum investment.")

        self.min_investment = min_investment
        self.max_investment = max_investment

    def calculate_roi(self, investment: float, roi_rate: float) -> float:
        """
        Calculate the return on investment (ROI) based on the investment amount and ROI rate.

        Args:
            investment (float): The amount invested.
            roi_rate (float): The return on investment rate as a decimal (e.g., 0.10 for 10%).

        Returns:
            float: The calculated ROI.

        Raises:
            ValueError: If the investment is outside the defined limits or if the ROI rate is invalid.
        """
        if investment < self.min_investment or investment > self.max_investment:
            raise ValueError(f"Investment must be between {self.min_investment} and {self.max_investment}.")
        if roi_rate < 0:
            raise ValueError("ROI rate must be non-negative.")

        return investment * roi_rate

def main():
    """
    Main function to execute the investment plan simulation.
    """
    # Define the minimum and maximum investment limits
    min_investment = 100.0  # Minimum investment amount
    max_investment = 10000.0  # Maximum investment amount
    roi_rate = 0.10  # ROI rate of 10%

    # Create an instance of the InvestmentPlan
    plan = InvestmentPlan(min_investment, max_investment)

    # Sample investment values for testing
    investments = [150.0, 500.0, 10000.0, 11000.0]  # Includes an invalid investment

    # Calculate and display ROI for each investment
    for investment in investments:
        try:
            roi = plan.calculate_roi(investment, roi_rate)
            print(f"Investment: {investment}, ROI: {roi:.2f}")
        except ValueError as e:
            print(f"Error for investment {investment}: {e}")

if __name__ == "__main__":
    main()
```
