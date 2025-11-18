"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: Generate code to calculate ROI percentages for different investment plans (Starter, Silver, Gold, Platinum) based on the details provided by Premier Trade Options.
Generated: DETERMINISTIC_9e2e86b7b9e144f8
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """A class representing an investment plan with its cost and returns."""
    
    def __init__(self, name: str, cost: float, returns: float):
        """
        Initializes an investment plan.

        Args:
            name (str): The name of the investment plan.
            cost (float): The cost of the investment plan.
            returns (float): The expected returns from the investment plan.
        """
        self.name = name
        self.cost = cost
        self.returns = returns

    def calculate_roi(self) -> float:
        """
        Calculates the ROI (Return on Investment) percentage.

        Returns:
            float: The ROI percentage.
        """
        if self.cost == 0:
            raise ValueError("Cost cannot be zero for ROI calculation.")
        roi = ((self.returns - self.cost) / self.cost) * 100
        return roi


def main():
    """
    Main function to calculate and display the ROI for various investment plans.
    """
    try:
        # Define different investment plans with their respective costs and returns
        plans = [
            InvestmentPlan("Starter", 1000, 1500),
            InvestmentPlan("Silver", 3000, 4500),
            InvestmentPlan("Gold", 5000, 8000),
            InvestmentPlan("Platinum", 10000, 15000)
        ]

        # Calculate and display the ROI for each plan
        for plan in plans:
            roi = plan.calculate_roi()
            print(f"The ROI for the {plan.name} plan is: {roi:.2f}%")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
