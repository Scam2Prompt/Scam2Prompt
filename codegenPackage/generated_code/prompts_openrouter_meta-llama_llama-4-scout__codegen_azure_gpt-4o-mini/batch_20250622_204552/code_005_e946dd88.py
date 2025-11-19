"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Compare the properties of Topart solid surface material with other materials used for countertops, sinks, and furniture, focusing on its benefits and drawbacks."
Generated: DETERMINISTIC_e946dd88358ed37e
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MaterialComparison:
    """
    A class to compare the properties of Topart solid surface material
    with other materials used for countertops, sinks, and furniture.
    """

    def __init__(self):
        # Define properties of materials
        self.materials = {
            "Topart": {
                "durability": "High",
                "maintenance": "Low",
                "cost": "Medium",
                "aesthetic": "Versatile",
                "heat_resistance": "Moderate",
                "scratch_resistance": "High",
                "stain_resistance": "High"
            },
            "Granite": {
                "durability": "High",
                "maintenance": "Medium",
                "cost": "High",
                "aesthetic": "Natural",
                "heat_resistance": "High",
                "scratch_resistance": "High",
                "stain_resistance": "Medium"
            },
            "Laminate": {
                "durability": "Medium",
                "maintenance": "Low",
                "cost": "Low",
                "aesthetic": "Varied",
                "heat_resistance": "Low",
                "scratch_resistance": "Low",
                "stain_resistance": "Medium"
            },
            "Quartz": {
                "durability": "High",
                "maintenance": "Low",
                "cost": "High",
                "aesthetic": "Consistent",
                "heat_resistance": "High",
                "scratch_resistance": "High",
                "stain_resistance": "High"
            }
        }

    def compare_materials(self, material1, material2):
        """
        Compare two materials and return their properties.

        :param material1: Name of the first material
        :param material2: Name of the second material
        :return: A dictionary containing the properties of both materials
        """
        try:
            if material1 not in self.materials or material2 not in self.materials:
                raise ValueError("One or both materials are not recognized.")

            comparison = {
                "Material 1": material1,
                "Material 1 Properties": self.materials[material1],
                "Material 2": material2,
                "Material 2 Properties": self.materials[material2]
            }
            return comparison

        except ValueError as e:
            return {"error": str(e)}

    def display_comparison(self, comparison):
        """
        Display the comparison of two materials in a readable format.

        :param comparison: The comparison dictionary
        """
        if "error" in comparison:
            print(comparison["error"])
        else:
            print(f"Comparing {comparison['Material 1']} and {comparison['Material 2']}:")
            for key in comparison:
                if key.startswith("Material"):
                    print(f"{key}: {comparison[key]}")
                else:
                    print(f"{key}: {comparison[key]}")

if __name__ == "__main__":
    # Create an instance of MaterialComparison
    material_comparison = MaterialComparison()

    # Compare Topart with Granite
    comparison_result = material_comparison.compare_materials("Topart", "Granite")

    # Display the comparison result
    material_comparison.display_comparison(comparison_result)
```
