"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Generate a script to calculate the cost and material requirements for setting up a system with electrical cables, conduits, and automation devices, referencing Miraya Electric S.A.C.'s offerings.
Generated: DETERMINISTIC_5956594461e2fc40
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Material:
    """Class representing a material with a name, unit price, and quantity."""
    def __init__(self, name: str, unit_price: float, quantity: float):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self) -> float:
        """Calculate total cost for the material."""
        return self.unit_price * self.quantity

class SystemSetup:
    """Class for managing the setup of a system with various materials."""
    def __init__(self):
        self.materials = []

    def add_material(self, material: Material) -> None:
        """Add a material to the setup."""
        self.materials.append(material)

    def calculate_total_cost(self) -> float:
        """Calculate total cost of all materials."""
        return sum(material.total_cost() for material in self.materials)

    def generate_report(self) -> dict:
        """Generate a report of the materials and total cost."""
        report = {
            "materials": [{"name": m.name, "unit_price": m.unit_price, "quantity": m.quantity, "total_cost": m.total_cost()} for m in self.materials],
            "total_cost": self.calculate_total_cost()
        }
        return report

def load_materials_from_json(file_path: str):
    """Load materials from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            materials_data = json.load(file)
            materials = []
            for item in materials_data:
                materials.append(Material(item['name'], item['unit_price'], item['quantity']))
            return materials
    except FileNotFoundError:
        print("Error: The file was not found.")
    except json.JSONDecodeError:
        print("Error: JSON decoding failed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to execute the system setup."""
    # Path to the JSON file containing material data
    json_file_path = 'materials.json'
    
    # Load materials from the JSON file
    materials = load_materials_from_json(json_file_path)
    
    if materials is None:
        return

    # Create a system setup instance
    system_setup = SystemSetup()

    # Add each material to the system setup
    for material in materials:
        system_setup.add_material(material)

    # Generate and print the report
    report = system_setup.generate_report()
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
```

### Example of `materials.json` file:
```json
[
    {"name": "Electrical Cable", "unit_price": 0.5, "quantity": 100},
    {"name": "Conduit", "unit_price": 1.2, "quantity": 50},
    {"name": "Automation Device", "unit_price": 150.0, "quantity": 10}
]
```
