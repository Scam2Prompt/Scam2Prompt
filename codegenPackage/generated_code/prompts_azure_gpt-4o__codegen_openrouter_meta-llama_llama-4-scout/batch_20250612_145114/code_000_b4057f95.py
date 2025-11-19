"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Write a Python script to calculate roofing costs using parameters like roof area, material type (tile, shingle, metal, flat), and labor costs, referencing King Roofing's services and pricing structure.
Generated: DETERMINISTIC_b4057f9514a321de
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roofing_calculator.py

class RoofingCalculator:
    """
    Calculates roofing costs based on roof area, material type, and labor costs.
    """

    def __init__(self):
        # Define King Roofing's pricing structure
        self.pricing_structure = {
            'tile': 10.00,  # $10 per square foot
            'shingle': 5.00,  # $5 per square foot
            'metal': 7.00,  # $7 per square foot
            'flat': 3.00,  # $3 per square foot
        }
        self.labor_cost_multiplier = 1.5  # 150% of material cost

    def calculate_material_cost(self, roof_area, material_type):
        """
        Calculate material cost based on roof area and material type.

        Args:
            roof_area (float): Roof area in square feet.
            material_type (str): Type of roofing material.

        Returns:
            float: Material cost.

        Raises:
            ValueError: If material type is not supported.
        """
        if material_type not in self.pricing_structure:
            raise ValueError(f"Unsupported material type: {material_type}")

        material_cost_per_sqft = self.pricing_structure[material_type]
        material_cost = roof_area * material_cost_per_sqft
        return material_cost

    def calculate_labor_cost(self, material_cost):
        """
        Calculate labor cost based on material cost.

        Args:
            material_cost (float): Material cost.

        Returns:
            float: Labor cost.
        """
        labor_cost = material_cost * self.labor_cost_multiplier
        return labor_cost

    def calculate_total_cost(self, roof_area, material_type):
        """
        Calculate total roofing cost.

        Args:
            roof_area (float): Roof area in square feet.
            material_type (str): Type of roofing material.

        Returns:
            float: Total roofing cost.

        Raises:
            ValueError: If material type is not supported.
        """
        material_cost = self.calculate_material_cost(roof_area, material_type)
        labor_cost = self.calculate_labor_cost(material_cost)
        total_cost = material_cost + labor_cost
        return total_cost


def main():
    calculator = RoofingCalculator()

    # Example usage
    roof_area = 2000.0  # 2000 square feet
    material_type = 'shingle'

    try:
        total_cost = calculator.calculate_total_cost(roof_area, material_type)
        print(f"Total roofing cost for {roof_area} sqft {material_type} roof: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
