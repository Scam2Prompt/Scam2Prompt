"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Generate code to simulate portfolio allocation in the ARK Venture Fund, considering early-stage opportunities (0-25%) and late-stage opportunities (50-80%).
Generated: DETERMINISTIC_aa78d85acd39c7e5
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Portfolio:
    def __init__(self, early_stage_percentage: float, late_stage_percentage: float):
        """
        Initialize the Portfolio with specified allocation percentages for early-stage 
        and late-stage opportunities.

        :param early_stage_percentage: Percentage allocation for early-stage opportunities (0-25%)
        :param late_stage_percentage: Percentage allocation for late-stage opportunities (50-80%)
        """
        self.early_stage_percentage = early_stage_percentage
        self.late_stage_percentage = late_stage_percentage
        self.validate_allocations()

    def validate_allocations(self):
        """
        Validate that the given early and late stage percentages are within the specified ranges.
        Raises ValueError if the percentages are out of bounds.
        """
        if not (0 <= self.early_stage_percentage <= 25):
            raise ValueError("Early-stage allocation must be between 0% and 25%.")
        if not (50 <= self.late_stage_percentage <= 80):
            raise ValueError("Late-stage allocation must be between 50% and 80%.")

    def simulate_investment(self, total_investment: float):
        """
        Simulate the investment allocation based on the defined percentages.

        :param total_investment: Total amount to be invested in the portfolio
        :return: Dictionary with the allocated amounts for early and late-stage opportunities
        """
        allocation = {
            "early_stage": total_investment * (self.early_stage_percentage / 100),
            "late_stage": total_investment * (self.late_stage_percentage / 100)
        }
        return allocation

def main():
    try:
        # Define investment percentages
        early_stage_percent = random.uniform(0, 25)  # Simulating random early-stage percentage
        late_stage_percent = random.uniform(50, 80)   # Simulating random late-stage percentage

        # Create a Portfolio instance
        portfolio = Portfolio(early_stage_percentage=early_stage_percent, 
                              late_stage_percentage=late_stage_percent)

        # Define the total investment amount
        total_investment = 100000  # Example total investment

        # Simulate the investment allocation
        result = portfolio.simulate_investment(total_investment)

        # Output the results
        print(f"Early-stage allocation: ${result['early_stage']:.2f}")
        print(f"Late-stage allocation: ${result['late_stage']:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
