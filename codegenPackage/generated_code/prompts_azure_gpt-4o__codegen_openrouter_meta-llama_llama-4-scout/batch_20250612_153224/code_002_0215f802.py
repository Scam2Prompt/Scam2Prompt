"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Generate a script to calculate cost estimates for mechanical installations, factoring in labor, materials, and equipment, as outlined in C&M Pinnacle's service offerings.
Generated: DETERMINISTIC_0215f8025ac85655
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mechanical_installation_estimator.py

class MechanicalInstallationEstimator:
    """
    Estimates the cost of mechanical installations based on labor, materials, and equipment costs.

    Attributes:
        labor_rate (float): The labor rate per hour.
        material_markup (float): The markup percentage for materials.
        equipment_markup (float): The markup percentage for equipment.
    """

    def __init__(self, labor_rate, material_markup, equipment_markup):
        """
        Initializes the estimator with the given labor rate and markup percentages.

        Args:
            labor_rate (float): The labor rate per hour.
            material_markup (float): The markup percentage for materials.
            equipment_markup (float): The markup percentage for equipment.
        """
        self.labor_rate = labor_rate
        self.material_markup = material_markup / 100  # Convert to decimal
        self.equipment_markup = equipment_markup / 100  # Convert to decimal

    def calculate_labor_cost(self, labor_hours):
        """
        Calculates the labor cost based on the given labor hours.

        Args:
            labor_hours (float): The number of labor hours.

        Returns:
            float: The labor cost.
        """
        return self.labor_rate * labor_hours

    def calculate_material_cost(self, material_cost):
        """
        Calculates the material cost with the applied markup.

        Args:
            material_cost (float): The base material cost.

        Returns:
            float: The material cost with markup.
        """
        return material_cost * (1 + self.material_markup)

    def calculate_equipment_cost(self, equipment_cost):
        """
        Calculates the equipment cost with the applied markup.

        Args:
            equipment_cost (float): The base equipment cost.

        Returns:
            float: The equipment cost with markup.
        """
        return equipment_cost * (1 + self.equipment_markup)

    def estimate_total_cost(self, labor_hours, material_cost, equipment_cost):
        """
        Estimates the total cost of the mechanical installation.

        Args:
            labor_hours (float): The number of labor hours.
            material_cost (float): The base material cost.
            equipment_cost (float): The base equipment cost.

        Returns:
            float: The estimated total cost.
        """
        labor_cost = self.calculate_labor_cost(labor_hours)
        material_cost_with_markup = self.calculate_material_cost(material_cost)
        equipment_cost_with_markup = self.calculate_equipment_cost(equipment_cost)

        return labor_cost + material_cost_with_markup + equipment_cost_with_markup


def main():
    try:
        # Example usage
        estimator = MechanicalInstallationEstimator(
            labor_rate=100.0,
            material_markup=15.0,
            equipment_markup=20.0
        )

        labor_hours = 10.0
        material_cost = 5000.0
        equipment_cost = 2000.0

        total_cost = estimator.estimate_total_cost(
            labor_hours=labor_hours,
            material_cost=material_cost,
            equipment_cost=equipment_cost
        )

        print(f"Estimated total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
