"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a Python script to calculate roofing costs using parameters like roof area, material type (tile, shingle, metal, flat), and labor costs, referencing King Roofing's services and pricing structure.
Generated: DETERMINISTIC_b4057f9514a321de
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class RoofingCostCalculator:
    """
    A class to calculate the total cost of roofing based on area, material type, and labor costs.
    """

    MATERIAL_COSTS = {
        'tile': 5.00,  # Cost per square foot
        'shingle': 3.50,
        'metal': 7.00,
        'flat': 4.00
    }

    LABOR_COST_PER_SQFT = 1.50  # Labor cost per square foot

    def __init__(self, roof_area, material_type):
        """
        Initializes the RoofingCostCalculator with the roof area and material type.

        :param roof_area: Total area of the roof in square feet.
        :param material_type: Type of roofing material selected.
        """
        self.roof_area = roof_area
        self.material_type = material_type.lower()

    def validate_parameters(self):
        """
        Validates the roof area and material type parameters.
        Raises:
            ValueError: If any parameter is invalid.
        """
        if self.roof_area <= 0:
            raise ValueError("Roof area must be greater than zero.")
        if self.material_type not in self.MATERIAL_COSTS:
            raise ValueError(f"Invalid material type. Choose from: {', '.join(self.MATERIAL_COSTS.keys())}")

    def calculate_material_cost(self):
        """
        Calculates the material cost based on the roof area and material type.

        :return: The total material cost.
        """
        material_cost = self.MATERIAL_COSTS[self.material_type]
        return self.roof_area * material_cost

    def calculate_labor_cost(self):
        """
        Calculates the labor cost based on the roof area.

        :return: The total labor cost.
        """
        return self.roof_area * self.LABOR_COST_PER_SQFT

    def calculate_total_cost(self):
        """
        Calculates the total cost of the roofing project including material and labor costs.

        :return: The total cost of the roofing project.
        """
        self.validate_parameters()
        material_cost = self.calculate_material_cost()
        labor_cost = self.calculate_labor_cost()
        total_cost = material_cost + labor_cost
        return total_cost


def main():
    """
    Main function to execute the roofing cost calculator.
    """
    try:
        # Example inputs, you can modify as needed or take input from user
        roof_area = float(input("Enter the roof area in square feet: "))
        material_type = input("Enter the roofing material type (tile, shingle, metal, flat): ")

        calculator = RoofingCostCalculator(roof_area, material_type)
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of roofing is: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
