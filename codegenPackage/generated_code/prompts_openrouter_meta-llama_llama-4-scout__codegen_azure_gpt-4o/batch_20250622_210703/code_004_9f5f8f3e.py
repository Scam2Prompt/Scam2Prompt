"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Compare the features and benefits of using Olyna filament versus traditional materials in outdoor furniture production, focusing on durability, maintenance, and environmental impact."
Generated: DETERMINISTIC_9f5f8f3e95cc73d2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent material properties
class Material:
    def __init__(self, name, durability, maintenance, environmental_impact):
        """
        Initialize a Material object.

        :param name: Name of the material
        :param durability: Durability score (1-10)
        :param maintenance: Maintenance score (1-10, lower is better)
        :param environmental_impact: Environmental impact score (1-10, lower is better)
        """
        self.name = name
        self.durability = durability
        self.maintenance = maintenance
        self.environmental_impact = environmental_impact

    def to_dict(self):
        """
        Convert the Material object to a dictionary.

        :return: Dictionary representation of the Material object
        """
        return {
            "name": self.name,
            "durability": self.durability,
            "maintenance": self.maintenance,
            "environmental_impact": self.environmental_impact,
        }

# Function to compare two materials
def compare_materials(material1, material2):
    """
    Compare two materials based on durability, maintenance, and environmental impact.

    :param material1: First Material object
    :param material2: Second Material object
    :return: Comparison results as a dictionary
    """
    comparison = {
        "durability": f"{material1.name} is {'better' if material1.durability > material2.durability else 'worse'} than {material2.name}",
        "maintenance": f"{material1.name} requires {'less' if material1.maintenance < material2.maintenance else 'more'} maintenance than {material2.name}",
        "environmental_impact": f"{material1.name} has {'lower' if material1.environmental_impact < material2.environmental_impact else 'higher'} environmental impact than {material2.name}",
    }
    return comparison

# Main function
def main():
    """
    Main function to compare Olyna filament with traditional materials.
    """
    try:
        # Define materials
        olyna_filament = Material(name="Olyna Filament", durability=9, maintenance=3, environmental_impact=2)
        traditional_material = Material(name="Traditional Material", durability=7, maintenance=5, environmental_impact=6)

        # Compare materials
        comparison_results = compare_materials(olyna_filament, traditional_material)

        # Print results
        print("Comparison Results:")
        print(json.dumps(comparison_results, indent=4))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
