"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write Python code to calculate the optimal dimensions for a Caja China based on user input for meat capacity (in kg) and material type (e.g., acero inoxidable or madera laqueada), referencing the product specifications on Meat Master.
Generated: DETERMINISTIC_7836640838889378
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# caja_china_calculator.py

class CajaChinaCalculator:
    """
    Calculates the optimal dimensions for a Caja China based on user input.

    References:
    - Meat Master product specifications
    """

    def __init__(self):
        # Material properties (thickness in mm)
        self.material_properties = {
            "acero inoxidable": 1.5,
            "madera laqueada": 2.0
        }

        # Default dimensions (in cm) based on Meat Master specs
        self.default_dimensions = {
            "length": 100,
            "width": 60,
            "height": 20
        }

    def calculate_optimal_dimensions(self, meat_capacity_kg, material_type):
        """
        Calculates the optimal dimensions for a Caja China.

        Args:
            meat_capacity_kg (float): Meat capacity in kg.
            material_type (str): Material type (e.g., acero inoxidable, madera laqueada).

        Returns:
            dict: Optimal dimensions (length, width, height) in cm.
        """

        # Validate input
        if meat_capacity_kg <= 0:
            raise ValueError("Meat capacity must be greater than 0 kg")

        if material_type not in self.material_properties:
            raise ValueError(f"Invalid material type. Supported types: {list(self.material_properties.keys())}")

        # Calculate optimal dimensions based on meat capacity and material type
        # Assuming a base area of 0.06 m^2 (60x100 cm) for 10 kg of meat
        base_area = 0.06  # m^2
        meat_density = 0.8  # kg/m^3 (approximate density of meat)

        # Scale base area based on meat capacity
        scaled_area = base_area * (meat_capacity_kg / 10)

        # Adjust for material thickness
        material_thickness = self.material_properties[material_type] / 10  # convert mm to cm

        # Calculate optimal dimensions (length, width, height)
        optimal_length = self.default_dimensions["length"] * (scaled_area / self.default_dimensions["length"] * self.default_dimensions["width"]) ** 0.5
        optimal_width = self.default_dimensions["width"] * (scaled_area / self.default_dimensions["length"] * self.default_dimensions["width"]) ** 0.5
        optimal_height = self.default_dimensions["height"] + material_thickness

        return {
            "length": round(optimal_length, 2),
            "width": round(optimal_width, 2),
            "height": round(optimal_height, 2)
        }

def main():
    calculator = CajaChinaCalculator()

    try:
        meat_capacity_kg = float(input("Enter meat capacity (in kg): "))
        material_type = input("Enter material type (e.g., acero inoxidable, madera laqueada): ")

        optimal_dimensions = calculator.calculate_optimal_dimensions(meat_capacity_kg, material_type)

        print("Optimal dimensions:")
        print(f"  Length: {optimal_dimensions['length']} cm")
        print(f"  Width: {optimal_dimensions['width']} cm")
        print(f"  Height: {optimal_dimensions['height']} cm")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
