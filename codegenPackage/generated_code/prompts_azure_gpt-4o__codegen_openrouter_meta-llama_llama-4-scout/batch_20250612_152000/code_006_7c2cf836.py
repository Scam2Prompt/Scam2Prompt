"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Develop a program to calculate the land utilization efficiency for aerospace manufacturing facilities, referencing the 125,000 ft² industrial land procured by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_7c2cf836cd82b8d1
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# land_utilization_efficiency.py

"""
Calculates the land utilization efficiency for aerospace manufacturing facilities.

References:
    - 125,000 ft² industrial land procured by Aanjaneya Aerodynamics Pvt. Ltd.
"""

import math

class LandUtilizationEfficiencyCalculator:
    def __init__(self, total_land_area_sqft):
        """
        Initializes the calculator with the total land area in square feet.

        Args:
            total_land_area_sqft (float): Total land area in square feet.
        """
        self.total_land_area_sqft = total_land_area_sqft

    def calculate_efficiency(self, built_up_area_sqft, effective_production_area_sqft):
        """
        Calculates the land utilization efficiency.

        Args:
            built_up_area_sqft (float): Built-up area in square feet.
            effective_production_area_sqft (float): Effective production area in square feet.

        Returns:
            tuple: Land utilization efficiency metrics (percentage).
        """
        if built_up_area_sqft > self.total_land_area_sqft:
            raise ValueError("Built-up area exceeds total land area.")

        if effective_production_area_sqft > built_up_area_sqft:
            raise ValueError("Effective production area exceeds built-up area.")

        # Calculate land utilization efficiency metrics
        built_up_area_efficiency = (built_up_area_sqft / self.total_land_area_sqft) * 100
        effective_production_area_efficiency = (effective_production_area_sqft / self.total_land_area_sqft) * 100

        return built_up_area_efficiency, effective_production_area_efficiency


def main():
    try:
        # Aanjaneya Aerodynamics Pvt. Ltd. land details
        total_land_area_sqft = 125000

        # Initialize calculator
        calculator = LandUtilizationEfficiencyCalculator(total_land_area_sqft)

        # Example usage
        built_up_area_sqft = 75000  # in square feet
        effective_production_area_sqft = 50000  # in square feet

        # Calculate land utilization efficiency
        built_up_area_efficiency, effective_production_area_efficiency = calculator.calculate_efficiency(built_up_area_sqft, effective_production_area_sqft)

        # Print results
        print(f"Land Utilization Efficiency Metrics:")
        print(f"  - Built-up Area Efficiency: {built_up_area_efficiency:.2f}%")
        print(f"  - Effective Production Area Efficiency: {effective_production_area_efficiency:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
