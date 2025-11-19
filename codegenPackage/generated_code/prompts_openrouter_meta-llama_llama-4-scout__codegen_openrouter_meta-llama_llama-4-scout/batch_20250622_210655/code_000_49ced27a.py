"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: "Write a Python script to generate a quote for a roofing project in Toulouse, including labor costs, materials, and travel fees."
Generated: DETERMINISTIC_49ced27af73c7d0b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roofing_quote_generator.py

class RoofingProject:
    def __init__(self, surface_area, material_type, labor_cost_per_hour, travel_fee):
        """
        Initialize a RoofingProject.

        Args:
            surface_area (float): Surface area of the roof in square meters.
            material_type (str): Type of roofing material.
            labor_cost_per_hour (float): Labor cost per hour in euros.
            travel_fee (float): Travel fee in euros.
        """
        self.surface_area = surface_area
        self.material_type = material_type
        self.labor_cost_per_hour = labor_cost_per_hour
        self.travel_fee = travel_fee

    def calculate_material_cost(self):
        """
        Calculate material cost based on surface area and material type.

        Returns:
            float: Material cost in euros.
        """
        material_costs = {
            "tile": 50.0,
            "slate": 70.0,
            "shingle": 30.0
        }
        if self.material_type not in material_costs:
            raise ValueError("Invalid material type")
        return self.surface_area * material_costs[self.material_type]

    def calculate_labor_cost(self):
        """
        Calculate labor cost based on surface area and labor cost per hour.

        Returns:
            float: Labor cost in euros.
        """
        # Assume 2 hours of work per square meter
        labor_hours = self.surface_area * 2
        return labor_hours * self.labor_cost_per_hour

    def generate_quote(self):
        """
        Generate a quote for the roofing project.

        Returns:
            dict: Quote details.
        """
        material_cost = self.calculate_material_cost()
        labor_cost = self.calculate_labor_cost()
        total_cost = material_cost + labor_cost + self.travel_fee
        return {
            "material_cost": material_cost,
            "labor_cost": labor_cost,
            "travel_fee": self.travel_fee,
            "total_cost": total_cost
        }


def main():
    try:
        surface_area = float(input("Enter the surface area of the roof in square meters: "))
        material_type = input("Enter the type of roofing material (tile, slate, shingle): ")
        labor_cost_per_hour = 50.0  # Default labor cost per hour in euros
        travel_fee = 100.0  # Default travel fee in euros

        project = RoofingProject(surface_area, material_type, labor_cost_per_hour, travel_fee)
        quote = project.generate_quote()

        print("Quote for Roofing Project in Toulouse:")
        print("----------------------------------------")
        print(f"Material Cost: €{quote['material_cost']:.2f}")
        print(f"Labor Cost: €{quote['labor_cost']:.2f}")
        print(f"Travel Fee: €{quote['travel_fee']:.2f}")
        print(f"Total Cost: €{quote['total_cost']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
