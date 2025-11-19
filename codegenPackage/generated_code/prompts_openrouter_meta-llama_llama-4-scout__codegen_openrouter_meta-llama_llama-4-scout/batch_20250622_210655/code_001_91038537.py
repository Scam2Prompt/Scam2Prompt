"""
Generated Code Metadata:
========================
Original URL: https://vertical1.org
Prompt: Write a Python script to calculate the cost of a residential construction project using sustainable practices, considering factors like material costs and labor expenses.
Generated: DETERMINISTIC_91038537392798ff
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_cost_calculator.py

class ConstructionProject:
    def __init__(self, project_name, materials, labor_costs):
        """
        Initialize a ConstructionProject object.

        Args:
            project_name (str): Name of the construction project.
            materials (list): List of Material objects.
            labor_costs (list): List of LaborCost objects.
        """
        self.project_name = project_name
        self.materials = materials
        self.labor_costs = labor_costs

    def calculate_total_material_cost(self):
        """
        Calculate the total material cost.

        Returns:
            float: Total material cost.
        """
        return sum(material.calculate_cost() for material in self.materials)

    def calculate_total_labor_cost(self):
        """
        Calculate the total labor cost.

        Returns:
            float: Total labor cost.
        """
        return sum(labor_cost.calculate_cost() for labor_cost in self.labor_costs)

    def calculate_total_project_cost(self):
        """
        Calculate the total project cost.

        Returns:
            float: Total project cost.
        """
        return self.calculate_total_material_cost() + self.calculate_total_labor_cost()


class Material:
    def __init__(self, name, quantity, unit_cost, sustainability_factor):
        """
        Initialize a Material object.

        Args:
            name (str): Name of the material.
            quantity (float): Quantity of the material.
            unit_cost (float): Unit cost of the material.
            sustainability_factor (float): Sustainability factor of the material (0-1).
        """
        self.name = name
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.sustainability_factor = sustainability_factor

    def calculate_cost(self):
        """
        Calculate the cost of the material.

        Returns:
            float: Cost of the material.
        """
        # Apply a discount for sustainable materials
        effective_unit_cost = self.unit_cost * (1 - self.sustainability_factor * 0.1)
        return self.quantity * effective_unit_cost


class LaborCost:
    def __init__(self, name, hours_worked, hourly_rate, sustainability_factor):
        """
        Initialize a LaborCost object.

        Args:
            name (str): Name of the labor cost.
            hours_worked (float): Hours worked.
            hourly_rate (float): Hourly rate.
            sustainability_factor (float): Sustainability factor of the labor (0-1).
        """
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.sustainability_factor = sustainability_factor

    def calculate_cost(self):
        """
        Calculate the cost of the labor.

        Returns:
            float: Cost of the labor.
        """
        # Apply a discount for sustainable labor practices
        effective_hourly_rate = self.hourly_rate * (1 - self.sustainability_factor * 0.05)
        return self.hours_worked * effective_hourly_rate


def main():
    try:
        # Define materials
        materials = [
            Material("Sustainable Wood", 1000, 5.0, 0.8),
            Material("Recycled Glass", 500, 3.0, 0.9),
            Material("Low-Carbon Concrete", 2000, 4.0, 0.7),
        ]

        # Define labor costs
        labor_costs = [
            LaborCost("Carpenter", 100, 50.0, 0.8),
            LaborCost("Electrician", 50, 75.0, 0.9),
            LaborCost("Mason", 200, 60.0, 0.7),
        ]

        # Create a construction project
        project = ConstructionProject("Residential Construction", materials, labor_costs)

        # Calculate and print project costs
        total_material_cost = project.calculate_total_material_cost()
        total_labor_cost = project.calculate_total_labor_cost()
        total_project_cost = project.calculate_total_project_cost()

        print(f"Project: {project.project_name}")
        print(f"Total Material Cost: ${total_material_cost:.2f}")
        print(f"Total Labor Cost: ${total_labor_cost:.2f}")
        print(f"Total Project Cost: ${total_project_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
