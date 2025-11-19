"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Write a code snippet to calculate the cost of a construction project based on the number of workers, materials, and equipment, using SSTCO's pricing strategy as a reference.
Generated: DETERMINISTIC_52bf3e31d3c61ba2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_cost_calculator.py

class ConstructionProject:
    def __init__(self, num_workers, materials_cost, equipment_cost):
        """
        Initialize a construction project with the given parameters.

        Args:
            num_workers (int): The number of workers for the project.
            materials_cost (float): The total cost of materials for the project.
            equipment_cost (float): The total cost of equipment for the project.
        """
        self.num_workers = num_workers
        self.materials_cost = materials_cost
        self.equipment_cost = equipment_cost

    def calculate_labor_cost(self, labor_rate):
        """
        Calculate the total labor cost for the project.

        Args:
            labor_rate (float): The labor rate per worker per hour.

        Returns:
            float: The total labor cost for the project.
        """
        # Assuming a standard 8-hour workday
        hours_per_day = 8
        days_per_project = 1  # This can be adjusted based on project duration

        total_labor_hours = self.num_workers * hours_per_day * days_per_project
        total_labor_cost = total_labor_hours * labor_rate
        return total_labor_cost

    def calculate_total_cost(self, labor_rate):
        """
        Calculate the total cost of the construction project.

        Args:
            labor_rate (float): The labor rate per worker per hour.

        Returns:
            float: The total cost of the construction project.
        """
        labor_cost = self.calculate_labor_cost(labor_rate)
        total_cost = labor_cost + self.materials_cost + self.equipment_cost
        return total_cost


class SSTCOPricingStrategy:
    def __init__(self, base_labor_rate, material_markup, equipment_markup):
        """
        Initialize the SSTCO pricing strategy with the given parameters.

        Args:
            base_labor_rate (float): The base labor rate per worker per hour.
            material_markup (float): The markup percentage for materials.
            equipment_markup (float): The markup percentage for equipment.
        """
        self.base_labor_rate = base_labor_rate
        self.material_markup = material_markup / 100  # Convert to decimal
        self.equipment_markup = equipment_markup / 100  # Convert to decimal

    def calculate_total_cost(self, project):
        """
        Calculate the total cost of a construction project using SSTCO's pricing strategy.

        Args:
            project (ConstructionProject): The construction project.

        Returns:
            float: The total cost of the construction project.
        """
        labor_cost = project.calculate_labor_cost(self.base_labor_rate)
        materials_cost_with_markup = project.materials_cost * (1 + self.material_markup)
        equipment_cost_with_markup = project.equipment_cost * (1 + self.equipment_markup)
        total_cost = labor_cost + materials_cost_with_markup + equipment_cost_with_markup
        return total_cost


def main():
    try:
        # Example usage
        project = ConstructionProject(num_workers=10, materials_cost=10000, equipment_cost=5000)
        sstco_pricing_strategy = SSTCOPricingStrategy(base_labor_rate=50, material_markup=10, equipment_markup=5)
        total_cost = sstco_pricing_strategy.calculate_total_cost(project)
        print(f"Total cost of the construction project: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
