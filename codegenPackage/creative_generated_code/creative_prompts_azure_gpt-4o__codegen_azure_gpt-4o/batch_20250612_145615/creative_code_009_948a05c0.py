"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-7.webflow.io
Prompt: Develop a program to calculate the environmental impact of architectural materials used in projects like those described by Linea 7, emphasizing sustainability and livability.
Generated: DETERMINISTIC_948a05c00322f84c
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv


class Material:
    """
    Represents an architectural material with its environmental impact properties.
    """
    def __init__(self, name, carbon_footprint, recyclability, toxicity):
        """
        Initializes a material with provided attributes.
        :param name: Name of the material
        :param carbon_footprint: Carbon footprint of the material (kg CO2 per kg)
        :param recyclability: Recyclability percentage (0-100)
        :param toxicity: Toxicity score of the material (1-10, where 1 is least toxic)
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclability = recyclability
        self.toxicity = toxicity


class EnvironmentalImpactCalculator:
    """
    Calculates environmental impact scores for architectural materials in a project.
    """
    def __init__(self):
        """
        Initializes the calculator with an empty list of materials.
        """
        self.materials = []

    def add_material(self, material):
        """
        Adds a material to the materials list.
        :param material: An instance of the Material class
        """
        self.materials.append(material)

    def calculate_impact(self):
        """
        Calculates the overall environmental impact based on all materials.
        :return: A dictionary containing the calculated scores
        """
        if not self.materials:
            raise ValueError("No materials have been added for calculation.")

        total_carbon_footprint = sum(m.carbon_footprint for m in self.materials)
        average_recyclability = sum(m.recyclability for m in self.materials) / len(self.materials)
        average_toxicity = sum(m.toxicity for m in self.materials) / len(self.materials)

        return {
            "total_carbon_footprint": total_carbon_footprint,
            "average_recyclability": average_recyclability,
            "average_toxicity": average_toxicity
        }

    def load_materials_from_csv(self, file_path):
        """
        Loads material data from a CSV file and adds them to the materials list.
        The CSV file must have columns: name, carbon_footprint, recyclability, toxicity.
        :param file_path: Path to the CSV file
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        material = Material(
                            name=row['name'],
                            carbon_footprint=float(row['carbon_footprint']),
                            recyclability=float(row['recyclability']),
                            toxicity=float(row['toxicity'])
                        )
                        self.add_material(material)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid row in CSV: {row}. Error: {e}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")


def main():
    """
    Main function to demonstrate the environmental impact calculator.
    """
    # Initialize the calculator
    calculator = EnvironmentalImpactCalculator()

    # Load materials from a CSV file
    csv_file_path = "materials.csv"  # Replace with the actual path to your CSV file
    calculator.load_materials_from_csv(csv_file_path)

    # Perform the calculation
    try:
        impact = calculator.calculate_impact()
        print("Environmental Impact Report:")
        print(f"  Total Carbon Footprint: {impact['total_carbon_footprint']} kg CO2")
        print(f"  Average Recyclability: {impact['average_recyclability']}%")
        print(f"  Average Toxicity: {impact['average_toxicity']}")
    except ValueError as ve:
        print(f"Error: {ve}")


# Entry point
if __name__ == "__main__":
    main()
```
