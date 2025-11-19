"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Create a library function that calculates the estimated costs for building residential units, inspired by the construction practices of Construye RK.
Generated: DETERMINISTIC_18c0e5f65e6afd6e
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConstructionCostEstimator:
    """
    A class to estimate the construction costs for residential units.
    The estimation is inspired by the construction practices of Construye RK.
    """

    def __init__(self, base_cost_per_sqft, sqft_per_unit):
        """
        Initializes the estimator with the base cost per square foot and the square footage of each unit.

        Parameters:
        base_cost_per_sqft (float): The base cost of construction per square foot.
        sqft_per_unit (float): The average square footage of a residential unit.
        """
        self.base_cost_per_sqft = base_cost_per_sqft
        self.sqft_per_unit = sqft_per_unit

    def calculate_cost(self, number_of_units):
        """
        Calculates the estimated total cost for building a specified number of residential units.

        Parameters:
        number_of_units (int): The number of residential units to estimate the cost for.

        Returns:
        float: The estimated total cost.
        """
        if not isinstance(number_of_units, int) or number_of_units <= 0:
            raise ValueError("number_of_units must be a positive integer.")

        total_cost = self.base_cost_per_sqft * self.sqft_per_unit * number_of_units
        return total_cost

    def calculate_total_costs(self, number_of_units, contingency_percentage=0.1):
        """
        Calculates the total estimated costs including a contingency.

        Parameters:
        number_of_units (int): The number of residential units to estimate the cost for.
        contingency_percentage (float): The percentage of the total cost to reserve for contingencies.

        Returns:
        float: The total estimated cost including contingencies.
        """
        if not isinstance(contingency_percentage, (float, int)) or not (0 <= contingency_percentage <= 1):
            raise ValueError("contingency_percentage must be a float between 0 and 1.")

        base_cost = self.calculate_cost(number_of_units)
        contingency_cost = base_cost * contingency_percentage
        total_cost = base_cost + contingency_cost
        
        return total_cost

# Example usage
if __name__ == "__main__":
    try:
        estimator = ConstructionCostEstimator(base_cost_per_sqft=150.0, sqft_per_unit=1200.0)
        num_units = 10
        estimated_cost = estimator.calculate_cost(num_units)
        total_cost_with_contingency = estimator.calculate_total_costs(num_units, contingency_percentage=0.1)

        print(f"Estimated Cost for {num_units} units: ${estimated_cost:.2f}")
        print(f"Total Cost with Contingency: ${total_cost_with_contingency:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
