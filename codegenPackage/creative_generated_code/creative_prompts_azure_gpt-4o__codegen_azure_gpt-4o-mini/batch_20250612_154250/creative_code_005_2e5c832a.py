"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tari.ee
Prompt: Write a function to calculate construction costs based on the rational design principles highlighted on Tari.ee.
Generated: DETERMINISTIC_2e5c832ae35356bd
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConstructionCostCalculator:
    """
    A class to calculate construction costs based on various parameters.
    """

    def __init__(self, base_cost_per_sqft, inflation_rate, area, design_principle_factor):
        """
        Initializes the ConstructionCostCalculator with the necessary parameters.

        :param base_cost_per_sqft: Base cost per square foot for construction
        :param inflation_rate: Annual inflation rate as a percentage
        :param area: Total area of construction in square feet
        :param design_principle_factor: Adjustment factor based on rational design principles
        """
        self.base_cost_per_sqft = base_cost_per_sqft
        self.inflation_rate = inflation_rate / 100  # Convert percentage to decimal
        self.area = area
        self.design_principle_factor = design_principle_factor

    def calculate_total_cost(self, years=0):
        """
        Calculates the total construction cost accounting for inflation and design adjustments.

        :param years: Number of years to adjust for inflation, default is 0
        :return: Total construction cost
        :raises ValueError: If any input parameter is negative
        """
        # Validate inputs
        if any(param < 0 for param in [self.base_cost_per_sqft, self.area, self.design_principle_factor]):
            raise ValueError("Base cost, area, and design principle factor must be non-negative.")

        # Calculate the adjusted base cost after inflation
        adjusted_cost_per_sqft = self.base_cost_per_sqft * ((1 + self.inflation_rate) ** years)

        # Calculate total cost
        total_cost = adjusted_cost_per_sqft * self.area * self.design_principle_factor

        return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        # Define parameters
        base_cost = 150  # Base cost per square foot
        inflation = 3    # Annual inflation rate in percent
        area = 2000      # Area in square feet
        design_factor = 1.1  # Design principle factor (adjustment)

        # Create a calculator instance
        calculator = ConstructionCostCalculator(base_cost, inflation, area, design_factor)

        # Calculate total cost for 5 years of inflation
        total_cost = calculator.calculate_total_cost(years=5)
        
        print(f"Total Construction Cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
