"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Create a script to calculate the environmental impact of sourcing FSC-certified wood for cleaning tools, as described by PDC Brush's sustainability initiatives.
Generated: DETERMINISTIC_b6b1e5c0b573efc0
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FSCWoodImpactCalculator:
    """
    A class to calculate the environmental impact of sourcing FSC-certified wood
    for cleaning tools, based on sustainability initiatives.
    """

    def __init__(self, wood_data):
        """
        Initialize the calculator with wood data.

        :param wood_data: List of wood items with their weights and sustainability metrics
        """
        self.wood_data = wood_data

    def calculate_impact(self):
        """
        Calculate the total environmental impact based on FSC-certification metrics.

        :return: A dictionary containing the total carbon footprint saved
                 and trees preserved.
        """
        total_carbon_saved = 0.0
        total_trees_preserved = 0

        # Process each wood item
        for wood in self.wood_data:
            try:
                weight_kg = wood["weight_kg"]
                certification_factor = wood["certification_factor"]  # Multiplier for FSC benefits
                carbon_saved_per_kg = wood["carbon_saved_per_kg"]
                trees_preserved_per_kg = wood["trees_preserved_per_kg"]

                # Calculate impact for the current wood item
                total_carbon_saved += weight_kg * carbon_saved_per_kg * certification_factor
                total_trees_preserved += int(weight_kg * trees_preserved_per_kg * certification_factor)

            except KeyError as e:
                print(f"Missing data for wood item: {e}")
            except Exception as e:
                print(f"Error processing wood item: {e}")

        # Return the aggregated impact
        return {
            "total_carbon_saved_kg": round(total_carbon_saved, 2),
            "total_trees_preserved": total_trees_preserved
        }


def load_wood_data(filepath):
    """
    Load wood data from a JSON file.

    :param filepath: Path to the JSON file containing wood data
    :return: List of wood data
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {filepath}")
        return []


def main():
    """
    Main function to execute the FSC wood impact calculation.
    """
    # Path to the JSON data file
    wood_data_file = 'wood_data.json'

    # Load wood data from file
    wood_data = load_wood_data(wood_data_file)

    if not wood_data:
        print("No wood data available. Exiting program.")
        return

    # Initialize the calculator
    calculator = FSCWoodImpactCalculator(wood_data)

    # Calculate environmental impact
    impact = calculator.calculate_impact()

    # Display results
    print("Environmental Impact of FSC-Certified Wood:")
    print(f"Total Carbon Saved: {impact['total_carbon_saved_kg']} kg")
    print(f"Total Trees Preserved: {impact['total_trees_preserved']}")


if __name__ == "__main__":
    main()
```

### Expected JSON File Format (`wood_data.json`)
```json
[
    {
        "weight_kg": 150,
        "certification_factor": 1.2,
        "carbon_saved_per_kg": 2.5,
        "trees_preserved_per_kg": 0.01
    },
    {
        "weight_kg": 200,
        "certification_factor": 1.5,
        "carbon_saved_per_kg": 3.0,
        "trees_preserved_per_kg": 0.02
    }
]
```
