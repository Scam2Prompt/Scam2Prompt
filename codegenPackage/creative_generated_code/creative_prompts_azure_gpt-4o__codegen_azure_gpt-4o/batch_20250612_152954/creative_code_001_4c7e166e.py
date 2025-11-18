"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vantardxyz.web.app
Prompt: Generate code to calculate the surge tax for Vantard token redemptions based on the pricing model described, where the tax starts at 0% and increases to a maximum of 50% during high demand.
Generated: DETERMINISTIC_4c7e166ec7f09b44
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# surge_tax_calculator.py

class SurgeTaxCalculator:
    """
    A class to calculate surge tax for Vantard token redemptions based on demand.
    Tax starts at 0% and increases linearly to a maximum of 50% at peak demand.
    """

    def __init__(self, max_demand: float, max_tax_rate: float = 0.5):
        """
        Initialize the surge tax calculator.

        :param max_demand: The maximum demand level (e.g., 100% utilization).
        :param max_tax_rate: The maximum tax rate (default: 50% or 0.5 as a fraction).
        """
        if max_demand <= 0:
            raise ValueError("max_demand must be greater than 0.")
        if not (0 <= max_tax_rate <= 1):
            raise ValueError("max_tax_rate must be a fraction between 0 and 1.")
        
        self.max_demand = max_demand
        self.max_tax_rate = max_tax_rate

    def calculate_surge_tax(self, current_demand: float) -> float:
        """
        Calculate the surge tax rate based on current demand.

        :param current_demand: The current demand level.
        :return: The surge tax rate as a fraction (0 to max_tax_rate).
        """
        if current_demand < 0:
            raise ValueError("current_demand cannot be negative.")
        
        # Cap the demand to the maximum demand to avoid unrealistic tax rates
        capped_demand = min(current_demand, self.max_demand)

        # Calculate the tax rate as a linear proportion of demand
        tax_rate = (capped_demand / self.max_demand) * self.max_tax_rate
        return round(tax_rate, 4)  # Round to 4 decimal places for precision


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with maximum demand at 100 and max tax rate of 50%
        calculator = SurgeTaxCalculator(max_demand=100, max_tax_rate=0.5)

        # Define some example demands to test
        example_demands = [0, 25, 50, 75, 100, 125]

        # Calculate and display the surge tax for each example demand
        print("Demand Level | Surge Tax Rate")
        print("----------------------------")
        for demand in example_demands:
            tax_rate = calculator.calculate_surge_tax(demand)
            print(f"{demand:<13} | {tax_rate*100:.2f}%")

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error: {e}")
```
