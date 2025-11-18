"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code for a system that calculates production timelines and cost estimates for custom cosmetic products, leveraging the production and logistics expertise highlighted by Fabricare Cosméticos.
Generated: DETERMINISTIC_cb0efa7ac7727bf9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CosmeticProductionEstimator:
    """
    A class to calculate production timelines and cost estimates for custom cosmetic products.
    """

    def __init__(self, base_cost_per_unit, daily_production_capacity):
        """
        Initialize the CosmeticProductionEstimator with production cost and capacity.

        Args:
            base_cost_per_unit (float): Base cost to produce one unit of the product.
            daily_production_capacity (int): Maximum number of units that can be produced in a day.
        """
        if base_cost_per_unit <= 0 or daily_production_capacity <= 0:
            raise ValueError("Base cost and production capacity must be positive numbers.")
        self.base_cost_per_unit = base_cost_per_unit
        self.daily_production_capacity = daily_production_capacity

    def calculate_cost(self, units, complexity_factor=1.0):
        """
        Calculate the production cost for the given number of units.

        Args:
            units (int): The number of units to produce.
            complexity_factor (float): A multiplier based on the product's complexity (default is 1.0).

        Returns:
            float: Total production cost.
        """
        if units <= 0:
            raise ValueError("Number of units must be a positive integer.")
        if complexity_factor <= 0:
            raise ValueError("Complexity factor must be a positive number.")
        return self.base_cost_per_unit * units * complexity_factor

    def calculate_timeline(self, units):
        """
        Calculate the production timeline based on the number of units.

        Args:
            units (int): The number of units to produce.

        Returns:
            datetime.timedelta: Estimated production timeline.
        """
        if units <= 0:
            raise ValueError("Number of units must be a positive integer.")
        days_required = -(-units // self.daily_production_capacity)  # Ceiling division
        return datetime.timedelta(days=days_required)

    def estimate(self, units, complexity_factor=1.0):
        """
        Provide a full estimate including cost and timeline.

        Args:
            units (int): The number of units to produce.
            complexity_factor (float): A multiplier based on the product's complexity (default is 1.0).

        Returns:
            dict: A dictionary with estimated cost and timeline.
        """
        production_cost = self.calculate_cost(units, complexity_factor)
        production_timeline = self.calculate_timeline(units)
        return {
            "Estimated Cost": production_cost,
            "Estimated Timeline": production_timeline
        }


def main():
    """
    Entry point for the program. Takes user input and calculates production estimates.
    """
    try:
        print("Welcome to Fabricare Cosméticos Production Estimator")
        base_cost_per_unit = float(input("Enter the base cost per unit ($): "))
        daily_production_capacity = int(input("Enter daily production capacity (units): "))

        estimator = CosmeticProductionEstimator(base_cost_per_unit, daily_production_capacity)

        units = int(input("Enter the number of units to produce: "))
        complexity_factor = float(input("Enter the product complexity factor (default is 1.0): ") or 1.0)

        estimate = estimator.estimate(units, complexity_factor)
        print("\nProduction Estimate:")
        print(f"Estimated Cost: ${estimate['Estimated Cost']:.2f}")
        print(f"Estimated Timeline: {estimate['Estimated Timeline'].days} days")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
