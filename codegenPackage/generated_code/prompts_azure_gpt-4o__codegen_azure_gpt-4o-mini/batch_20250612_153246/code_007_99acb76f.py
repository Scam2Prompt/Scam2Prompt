"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Develop a script to calculate the longevity and maintenance costs of different fencing materials, referencing the durability claims made by "The Fence Guys."
Generated: DETERMINISTIC_99acb76f71b6db50
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

class FenceMaterial:
    """
    A class to represent a fencing material and its properties.
    """

    def __init__(self, name, longevity_years, maintenance_cost_per_year):
        """
        Initializes a new FenceMaterial instance.

        :param name: Name of the fencing material
        :param longevity_years: Expected longevity in years
        :param maintenance_cost_per_year: Annual maintenance cost
        """
        self.name = name
        self.longevity_years = longevity_years
        self.maintenance_cost_per_year = maintenance_cost_per_year

    def total_cost(self):
        """
        Calculates the total cost of maintenance over the lifespan of the fence.

        :return: Total maintenance cost over the longevity period
        """
        return self.maintenance_cost_per_year * self.longevity_years


def load_fence_data(file_path):
    """
    Loads fence material data from a JSON file.

    :param file_path: Path to the JSON file containing fence data
    :return: List of FenceMaterial instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [FenceMaterial(item['name'], item['longevity_years'], item['maintenance_cost_per_year']) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def display_fence_costs(fence_materials):
    """
    Displays the longevity and maintenance costs of the provided fence materials.

    :param fence_materials: List of FenceMaterial instances
    """
    if not fence_materials:
        print("No fence materials to display.")
        return

    print(f"{'Material':<20} {'Longevity (Years)':<20} {'Maintenance Cost/Year':<25} {'Total Maintenance Cost':<25}")
    print("=" * 90)
    
    for material in fence_materials:
        print(f"{material.name:<20} {material.longevity_years:<20} {material.maintenance_cost_per_year:<25} {material.total_cost():<25}")


def main():
    """
    Main function to execute the script.
    """
    # Path to the JSON file containing fence material data
    file_path = 'fence_materials.json'
    
    # Load fence materials from the JSON file
    fence_materials = load_fence_data(file_path)
    
    # Display the longevity and maintenance costs
    display_fence_costs(fence_materials)


if __name__ == "__main__":
    main()
```

**Sample JSON file (fence_materials.json)**:
```json
[
    {
        "name": "Wood",
        "longevity_years": 15,
        "maintenance_cost_per_year": 200
    },
    {
        "name": "Vinyl",
        "longevity_years": 30,
        "maintenance_cost_per_year": 100
    },
    {
        "name": "Chain Link",
        "longevity_years": 20,
        "maintenance_cost_per_year": 50
    },
    {
        "name": "Composite",
        "longevity_years": 25,
        "maintenance_cost_per_year": 150
    }
]
```
