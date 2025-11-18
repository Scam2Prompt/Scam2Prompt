"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Develop a script to calculate the longevity and maintenance costs of different fencing materials, referencing the durability claims made by "The Fence Guys."
Generated: DETERMINISTIC_99acb76f71b6db50
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FencingMaterial:
    """
    A class to represent a fencing material.
    Attributes:
        name (str): The name of the fencing material.
        longevity (int): The expected longevity of the material in years.
        maintenance_cost (float): The annual maintenance cost in dollars.
    """

    def __init__(self, name, longevity, maintenance_cost):
        self.name = name
        self.longevity = longevity
        self.maintenance_cost = maintenance_cost

    def total_cost(self):
        """
        Calculate the total cost of the fencing material over its lifetime.
        Returns:
            float: Total cost including maintenance over the longevity period.
        """
        return self.longevity * self.maintenance_cost


class FenceCostCalculator:
    """
    A class to calculate and compare the longevity and maintenance costs of fencing materials.
    Attributes:
        materials (list): A list of FencingMaterial instances.
    """

    def __init__(self, materials):
        self.materials = materials

    def compare_costs(self):
        """
        Compare the total costs of all fencing materials over their lifespan.
        
        Returns:
            dict: A dictionary with material names as keys and their total costs as values.
        """
        cost_comparison = {}
        for material in self.materials:
            cost_comparison[material.name] = material.total_cost()
        return cost_comparison


def load_materials_from_json(file_path):
    """
    Load fencing materials from a given JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing fencing materials data.

    Returns:
        list: A list of FencingMaterial instances.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If the JSON file is not valid.
    """
    try:
        with open(file_path, 'r') as file:
            materials_data = json.load(file)
            materials = [
                FencingMaterial(
                    name=material['name'],
                    longevity=material['longevity'],
                    maintenance_cost=material['maintenance_cost']
                ) for material in materials_data
            ]
            return materials
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON from the file.")
        raise e


def main():
    """
    Main function to execute the fencing materials cost calculator.
    """
    file_path = 'fencing_materials.json'  # Path to the JSON file
    try:
        materials = load_materials_from_json(file_path)
        calculator = FenceCostCalculator(materials)
        costs = calculator.compare_costs()

        print("Total Costs of Fencing Materials Over Their Lifespan:")
        for material, cost in costs.items():
            print(f"{material}: ${cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

```json
// fencing_materials.json - Example Content
[
    {
        "name": "Wood",
        "longevity": 10,
        "maintenance_cost": 200
    },
    {
        "name": "Vinyl",
        "longevity": 25,
        "maintenance_cost": 100
    },
    {
        "name": "Chain Link",
        "longevity": 15,
        "maintenance_cost": 50
    },
    {
        "name": "Aluminum",
        "longevity": 20,
        "maintenance_cost": 70
    }
]
```
