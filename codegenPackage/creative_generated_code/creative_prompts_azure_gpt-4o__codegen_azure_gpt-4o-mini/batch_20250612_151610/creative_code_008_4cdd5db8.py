"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Create a script to calculate the transportation safety index for packaging materials, incorporating the benefits of stretch films and corrugated cardboard as described on Cartonerías Andinas del Sur's website.
Generated: DETERMINISTIC_4cdd5db883b9cc10
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PackagingMaterial:
    def __init__(self, name, durability_score, protection_score):
        self.name = name
        self.durability_score = durability_score
        self.protection_score = protection_score

    def calculate_safety_index(self):
        """Calculate the transportation safety index."""
        try:
            safety_index = (self.durability_score + self.protection_score) / 2
            return round(safety_index, 2)
        except Exception as e:
            raise ValueError(f"Error calculating safety index for {self.name}: {str(e)}")


def load_material_data(file_path):
    """Load packaging material data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            materials = json.load(file)
            return materials
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON data from the file.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")


def main():
    """Main function to execute the safety index calculations."""
    # Define the path to the material data JSON file
    file_path = 'packaging_materials.json'

    try:
        materials_data = load_material_data(file_path)

        materials = []
        for item in materials_data:
            material = PackagingMaterial(
                name=item['name'],
                durability_score=item['durability_score'],
                protection_score=item['protection_score']
            )
            materials.append(material)

        # Calculate and print safety indexes
        print("Transportation Safety Index for Packaging Materials:")
        for material in materials:
            safety_index = material.calculate_safety_index()
            print(f"{material.name}: {safety_index}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
