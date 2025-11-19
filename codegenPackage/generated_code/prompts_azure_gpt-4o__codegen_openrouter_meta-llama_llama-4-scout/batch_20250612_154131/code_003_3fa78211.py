"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a program to calculate the cost of automatic garage door installations and repairs, incorporating Trimatic's approach of offering free studies and budgets.
Generated: DETERMINISTIC_3fa7821143ef9c8d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# garage_door_calculator.py

class GarageDoorInstallation:
    def __init__(self, door_type, size, material, labor_cost_per_hour, labor_hours):
        """
        Initialize the GarageDoorInstallation class.

        Args:
            door_type (str): Type of garage door (e.g., sectional, roll-up).
            size (str): Size of the garage door (e.g., 9x7, 10x10).
            material (str): Material of the garage door (e.g., steel, wood).
            labor_cost_per_hour (float): Labor cost per hour.
            labor_hours (float): Number of labor hours.
        """
        self.door_type = door_type
        self.size = size
        self.material = material
        self.labor_cost_per_hour = labor_cost_per_hour
        self.labor_hours = labor_hours

    def calculate_door_cost(self):
        """
        Calculate the cost of the garage door based on type, size, and material.

        Returns:
            float: Cost of the garage door.
        """
        door_costs = {
            "sectional": {
                "steel": {"9x7": 800, "10x10": 1200},
                "wood": {"9x7": 1200, "10x10": 1800}
            },
            "roll-up": {
                "steel": {"9x7": 600, "10x10": 1000},
                "wood": {"9x7": 1000, "10x10": 1500}
            }
        }

        try:
            return door_costs[self.door_type][self.material][self.size]
        except KeyError:
            raise ValueError("Invalid door type, size, or material")

    def calculate_labor_cost(self):
        """
        Calculate the labor cost.

        Returns:
            float: Labor cost.
        """
        return self.labor_cost_per_hour * self.labor_hours

    def calculate_total_cost(self):
        """
        Calculate the total cost of the garage door installation.

        Returns:
            float: Total cost.
        """
        door_cost = self.calculate_door_cost()
        labor_cost = self.calculate_labor_cost()
        return door_cost + labor_cost


class GarageDoorRepair:
    def __init__(self, repair_type, labor_cost_per_hour, labor_hours, parts_cost):
        """
        Initialize the GarageDoorRepair class.

        Args:
            repair_type (str): Type of repair (e.g., spring replacement, cable repair).
            labor_cost_per_hour (float): Labor cost per hour.
            labor_hours (float): Number of labor hours.
            parts_cost (float): Cost of parts.
        """
        self.repair_type = repair_type
        self.labor_cost_per_hour = labor_cost_per_hour
        self.labor_hours = labor_hours
        self.parts_cost = parts_cost

    def calculate_labor_cost(self):
        """
        Calculate the labor cost.

        Returns:
            float: Labor cost.
        """
        return self.labor_cost_per_hour * self.labor_hours

    def calculate_total_cost(self):
        """
        Calculate the total cost of the garage door repair.

        Returns:
            float: Total cost.
        """
        labor_cost = self.calculate_labor_cost()
        return labor_cost + self.parts_cost


class TrimaticEstimator:
    def __init__(self):
        pass

    def offer_free_study_and_budget(self):
        """
        Offer a free study and budget.

        Returns:
            str: Message indicating a free study and budget are offered.
        """
        return "Trimatic offers a free study and budget for your garage door installation or repair needs."


def main():
    estimator = TrimaticEstimator()
    print(estimator.offer_free_study_and_budget())

    installation = GarageDoorInstallation(
        door_type="sectional",
        size="9x7",
        material="steel",
        labor_cost_per_hour=50,
        labor_hours=2
    )

    print(f"Garage Door Installation Cost: ${installation.calculate_total_cost():.2f}")

    repair = GarageDoorRepair(
        repair_type="spring replacement",
        labor_cost_per_hour=50,
        labor_hours=1,
        parts_cost=200
    )

    print(f"Garage Door Repair Cost: ${repair.calculate_total_cost():.2f}")


if __name__ == "__main__":
    main()
```
