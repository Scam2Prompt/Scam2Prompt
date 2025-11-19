"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Create a script that calculates the cost of designing a green wall for a commercial space, using parameters like wall size and plant density, inspired by City Garden México's green wall projects.
Generated: DETERMINISTIC_b43182e997e321e2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# green_wall_calculator.py

class GreenWallCalculator:
    """
    Calculates the cost of designing a green wall for a commercial space.

    Attributes:
        wall_size (float): The size of the wall in square meters.
        plant_density (float): The density of plants per square meter.
        plant_cost (float): The cost of a single plant.
        installation_cost_per_sqm (float): The cost of installation per square meter.
        maintenance_cost_per_sqm (float): The cost of maintenance per square meter per year.
    """

    def __init__(self, wall_size, plant_density, plant_cost=50, installation_cost_per_sqm=100, maintenance_cost_per_sqm=20):
        """
        Initializes the GreenWallCalculator.

        Args:
            wall_size (float): The size of the wall in square meters.
            plant_density (float): The density of plants per square meter.
            plant_cost (float, optional): The cost of a single plant. Defaults to 50.
            installation_cost_per_sqm (float, optional): The cost of installation per square meter. Defaults to 100.
            maintenance_cost_per_sqm (float, optional): The cost of maintenance per square meter per year. Defaults to 20.
        """
        self.wall_size = wall_size
        self.plant_density = plant_density
        self.plant_cost = plant_cost
        self.installation_cost_per_sqm = installation_cost_per_sqm
        self.maintenance_cost_per_sqm = maintenance_cost_per_sqm

    def calculate_plant_cost(self):
        """
        Calculates the total cost of plants.

        Returns:
            float: The total cost of plants.
        """
        total_plants = self.wall_size * self.plant_density
        return total_plants * self.plant_cost

    def calculate_installation_cost(self):
        """
        Calculates the total cost of installation.

        Returns:
            float: The total cost of installation.
        """
        return self.wall_size * self.installation_cost_per_sqm

    def calculate_maintenance_cost(self):
        """
        Calculates the total cost of maintenance per year.

        Returns:
            float: The total cost of maintenance per year.
        """
        return self.wall_size * self.maintenance_cost_per_sqm

    def calculate_total_cost(self):
        """
        Calculates the total cost of designing and maintaining the green wall.

        Returns:
            dict: A dictionary containing the total plant cost, installation cost, maintenance cost, and total cost.
        """
        plant_cost = self.calculate_plant_cost()
        installation_cost = self.calculate_installation_cost()
        maintenance_cost = self.calculate_maintenance_cost()
        total_cost = plant_cost + installation_cost + maintenance_cost

        return {
            "plant_cost": plant_cost,
            "installation_cost": installation_cost,
            "maintenance_cost": maintenance_cost,
            "total_cost": total_cost
        }


def main():
    try:
        wall_size = float(input("Enter the wall size in square meters: "))
        plant_density = float(input("Enter the plant density per square meter: "))

        calculator = GreenWallCalculator(wall_size, plant_density)
        costs = calculator.calculate_total_cost()

        print("Green Wall Cost Breakdown:")
        print(f"Plant Cost: ${costs['plant_cost']:.2f}")
        print(f"Installation Cost: ${costs['installation_cost']:.2f}")
        print(f"Maintenance Cost per year: ${costs['maintenance_cost']:.2f}")
        print(f"Total Cost: ${costs['total_cost']:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
