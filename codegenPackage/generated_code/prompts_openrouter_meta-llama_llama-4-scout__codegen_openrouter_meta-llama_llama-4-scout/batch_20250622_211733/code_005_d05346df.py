"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Write a function to calculate the cost of plumbing repairs and upgrades, considering factors like labor costs, materials, and location, as seen in Certified Plumbers Graham, TX's pricing."
Generated: DETERMINISTIC_d05346df01a69d4f
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class Location(Enum):
    """ Enum for different locations """
    GRAHAM_TX = 1
    OTHER = 2

class RepairType(Enum):
    """ Enum for different types of repairs """
    LABOR = 1
    MATERIAL = 2
    UPGRADE = 3

class PlumbingCalculator:
    """ Calculator for plumbing repairs and upgrades """

    def __init__(self, location: Location):
        """
        Initialize the calculator with a location.

        Args:
        location (Location): The location of the repair.
        """
        self.location = location
        self.base_labor_rate = self._get_base_labor_rate(location)
        self.material_markup = 0.15  # 15% markup for materials

    def _get_base_labor_rate(self, location: Location) -> float:
        """
        Get the base labor rate based on the location.

        Args:
        location (Location): The location of the repair.

        Returns:
        float: The base labor rate.
        """
        labor_rates: Dict[Location, float] = {
            Location.GRAHAM_TX: 75.0,
            Location.OTHER: 100.0
        }
        return labor_rates.get(location, labor_rates[Location.OTHER])

    def calculate_repair_cost(self, repair_type: RepairType, hours: float = 0, material_cost: float = 0) -> float:
        """
        Calculate the cost of a repair.

        Args:
        repair_type (RepairType): The type of repair.
        hours (float): The number of labor hours. Defaults to 0.
        material_cost (float): The cost of materials. Defaults to 0.

        Returns:
        float: The total cost of the repair.
        """
        if repair_type == RepairType.LABOR:
            return self.base_labor_rate * hours
        elif repair_type == RepairType.MATERIAL:
            return material_cost * (1 + self.material_markup)
        elif repair_type == RepairType.UPGRADE:
            # Assume upgrade costs are 50% more than labor and material costs
            labor_cost = self.base_labor_rate * hours
            material_cost_with_markup = material_cost * (1 + self.material_markup)
            return labor_cost + material_cost_with_markup
        else:
            raise ValueError("Invalid repair type")

    def calculate_total_cost(self, repairs: list) -> float:
        """
        Calculate the total cost of multiple repairs.

        Args:
        repairs (list): A list of dictionaries containing repair information.

        Returns:
        float: The total cost of all repairs.

        Example:
        repairs = [
            {"type": RepairType.LABOR, "hours": 2},
            {"type": RepairType.MATERIAL, "material_cost": 100}
        ]
        """
        total_cost = 0
        for repair in repairs:
            repair_type = repair["type"]
            if repair_type == RepairType.LABOR:
                total_cost += self.calculate_repair_cost(repair_type, hours=repair.get("hours", 0))
            elif repair_type == RepairType.MATERIAL:
                total_cost += self.calculate_repair_cost(repair_type, material_cost=repair.get("material_cost", 0))
            elif repair_type == RepairType.UPGRADE:
                total_cost += self.calculate_repair_cost(repair_type, hours=repair.get("hours", 0), material_cost=repair.get("material_cost", 0))
            else:
                raise ValueError("Invalid repair type")
        return total_cost


def main():
    calculator = PlumbingCalculator(Location.GRAHAM_TX)

    # Example usage:
    labor_repair = calculator.calculate_repair_cost(RepairType.LABOR, hours=2)
    material_repair = calculator.calculate_repair_cost(RepairType.MATERIAL, material_cost=100)
    upgrade_repair = calculator.calculate_repair_cost(RepairType.UPGRADE, hours=2, material_cost=100)

    print(f"Labor repair cost: ${labor_repair:.2f}")
    print(f"Material repair cost: ${material_repair:.2f}")
    print(f"Upgrade repair cost: ${upgrade_repair:.2f}")

    repairs = [
        {"type": RepairType.LABOR, "hours": 2},
        {"type": RepairType.MATERIAL, "material_cost": 100},
        {"type": RepairType.UPGRADE, "hours": 2, "material_cost": 100}
    ]
    total_cost = calculator.calculate_total_cost(repairs)
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
