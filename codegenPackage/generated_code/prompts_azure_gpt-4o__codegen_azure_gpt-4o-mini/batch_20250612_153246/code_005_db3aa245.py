"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Write code to model energy efficiency improvements for cleaner energy solutions in construction projects, as described in the sustainability services section of Bismillah Traders.
Generated: DETERMINISTIC_db3aa2456cf87941
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class EnergyEfficiencyImprovement:
    """
    A class to model energy efficiency improvements for construction projects.
    """

    def __init__(self, name: str, cost: float, energy_savings: float, carbon_reduction: float):
        """
        Initializes an EnergyEfficiencyImprovement instance.

        :param name: Name of the energy efficiency improvement.
        :param cost: Cost of the improvement.
        :param energy_savings: Estimated energy savings (in kWh).
        :param carbon_reduction: Estimated carbon reduction (in kg CO2).
        """
        self.name = name
        self.cost = cost
        self.energy_savings = energy_savings
        self.carbon_reduction = carbon_reduction

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the instance to a dictionary for easy serialization.

        :return: A dictionary representation of the instance.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "energy_savings": self.energy_savings,
            "carbon_reduction": self.carbon_reduction
        }

class ConstructionProject:
    """
    A class to model a construction project with energy efficiency improvements.
    """

    def __init__(self, project_name: str):
        """
        Initializes a ConstructionProject instance.

        :param project_name: Name of the construction project.
        """
        self.project_name = project_name
        self.improvements: List[EnergyEfficiencyImprovement] = []

    def add_improvement(self, improvement: EnergyEfficiencyImprovement):
        """
        Adds an energy efficiency improvement to the project.

        :param improvement: An instance of EnergyEfficiencyImprovement.
        """
        self.improvements.append(improvement)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of all improvements.

        :return: Total cost of improvements.
        """
        return sum(improvement.cost for improvement in self.improvements)

    def calculate_total_energy_savings(self) -> float:
        """
        Calculates the total energy savings from all improvements.

        :return: Total energy savings in kWh.
        """
        return sum(improvement.energy_savings for improvement in self.improvements)

    def calculate_total_carbon_reduction(self) -> float:
        """
        Calculates the total carbon reduction from all improvements.

        :return: Total carbon reduction in kg CO2.
        """
        return sum(improvement.carbon_reduction for improvement in self.improvements)

    def to_json(self) -> str:
        """
        Serializes the project and its improvements to a JSON string.

        :return: JSON string representation of the project.
        """
        project_data = {
            "project_name": self.project_name,
            "improvements": [improvement.to_dict() for improvement in self.improvements]
        }
        return json.dumps(project_data, indent=4)

def main():
    """
    Main function to demonstrate the functionality of the classes.
    """
    try:
        # Create a construction project
        project = ConstructionProject("Green Building Project")

        # Add energy efficiency improvements
        project.add_improvement(EnergyEfficiencyImprovement("Solar Panels", 15000, 12000, 9000))
        project.add_improvement(EnergyEfficiencyImprovement("High-Efficiency HVAC", 8000, 8000, 6000))
        project.add_improvement(EnergyEfficiencyImprovement("Insulation Upgrade", 5000, 5000, 4000))

        # Calculate totals
        total_cost = project.calculate_total_cost()
        total_energy_savings = project.calculate_total_energy_savings()
        total_carbon_reduction = project.calculate_total_carbon_reduction()

        # Print results
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Energy Savings: {total_energy_savings} kWh")
        print(f"Total Carbon Reduction: {total_carbon_reduction} kg CO2")

        # Print project details in JSON format
        print("\nProject Details:")
        print(project.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
