"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: "Write a Python script to calculate the cost of construction for a new building in Russia, considering factors such as materials, labor, and location, as per ExpertStroy's services."
Generated: DETERMINISTIC_d553b6f0723ea293
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_cost_calculator.py

class ConstructionCostCalculator:
    """
    Calculates the cost of construction for a new building in Russia.

    Attributes:
        materials_cost (float): Cost of materials per square meter.
        labor_cost (float): Cost of labor per square meter.
        location_coefficients (dict): Location-based cost coefficients.
    """

    def __init__(self):
        # Base costs per square meter (in RUB)
        self.materials_cost = 0
        self.labor_cost = 0

        # Location-based cost coefficients
        self.location_coefficients = {
            'Moscow': 1.2,
            'St. Petersburg': 1.1,
            'Other regions': 1.0
        }

    def calculate_construction_cost(self, area, location, materials_type, labor_type):
        """
        Calculates the total construction cost.

        Args:
            area (float): Building area in square meters.
            location (str): Location of the building.
            materials_type (str): Type of materials (e.g., 'basic', 'premium').
            labor_type (str): Type of labor (e.g., 'skilled', 'unskilled').

        Returns:
            float: Total construction cost in RUB.

        Raises:
            ValueError: If location, materials type, or labor type is invalid.
        """

        # Validate input parameters
        if location not in self.location_coefficients:
            raise ValueError(f"Invalid location: {location}")

        # Materials cost per square meter based on type
        materials_costs = {
            'basic': 5000,
            'premium': 10000
        }
        if materials_type not in materials_costs:
            raise ValueError(f"Invalid materials type: {materials_type}")
        self.materials_cost = materials_costs[materials_type]

        # Labor cost per square meter based on type
        labor_costs = {
            'skilled': 3000,
            'unskilled': 2000
        }
        if labor_type not in labor_costs:
            raise ValueError(f"Invalid labor type: {labor_type}")
        self.labor_cost = labor_costs[labor_type]

        # Calculate total construction cost
        location_coefficient = self.location_coefficients[location]
        total_cost = (self.materials_cost + self.labor_cost) * area * location_coefficient

        return total_cost


def main():
    calculator = ConstructionCostCalculator()

    try:
        area = float(input("Enter building area (in square meters): "))
        location = input("Enter location (Moscow, St. Petersburg, or Other regions): ")
        materials_type = input("Enter materials type (basic or premium): ")
        labor_type = input("Enter labor type (skilled or unskilled): ")

        total_cost = calculator.calculate_construction_cost(area, location, materials_type, labor_type)
        print(f"Total construction cost: {total_cost:.2f} RUB")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
