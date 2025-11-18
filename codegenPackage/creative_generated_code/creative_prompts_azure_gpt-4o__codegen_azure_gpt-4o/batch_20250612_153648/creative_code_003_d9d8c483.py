"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Develop a script to calculate the cost-effectiveness of architectural designs, incorporating the economic and competitive principles emphasized by Remas Engineering Consultants.
Generated: DETERMINISTIC_d9d8c483f211afcc
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class ArchitecturalDesign:
    """
    Represents an architectural design with various cost and benefit attributes.
    """

    def __init__(self, name, construction_cost, maintenance_cost, expected_lifetime, competitive_rating):
        """
        Initialize an architectural design instance.

        :param name: Name of the design
        :param construction_cost: Initial construction cost
        :param maintenance_cost: Annual maintenance cost
        :param expected_lifetime: Expected lifetime in years
        :param competitive_rating: Competitive rating (scale 1-10, with 10 being highly competitive)
        """
        self.name = name
        self.construction_cost = construction_cost
        self.maintenance_cost = maintenance_cost
        self.expected_lifetime = expected_lifetime
        self.competitive_rating = competitive_rating

    def calculate_total_cost(self):
        """
        Calculate the total cost over the design's lifetime.

        :return: Total cost in monetary units
        """
        return self.construction_cost + (self.maintenance_cost * self.expected_lifetime)

    def calculate_cost_effectiveness(self):
        """
        Calculate cost-effectiveness based on competitive principles.

        Cost-effectiveness = Competitive rating / Total cost
        Higher value indicates better cost-effectiveness.

        :return: Cost-effectiveness score
        """
        total_cost = self.calculate_total_cost()
        if total_cost == 0:
            raise ValueError("Total cost cannot be zero.")
        return self.competitive_rating / total_cost


def load_designs_from_file(file_path):
    """
    Load architectural designs from a JSON file.

    :param file_path: Path to the JSON file containing design data
    :return: List of ArchitecturalDesign objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            designs = [
                ArchitecturalDesign(
                    name=item['name'],
                    construction_cost=item['construction_cost'],
                    maintenance_cost=item['maintenance_cost'],
                    expected_lifetime=item['expected_lifetime'],
                    competitive_rating=item['competitive_rating']
                )
                for item in data
            ]
            return designs
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}")
        return []
    except KeyError as e:
        print(f"Error: Missing required field in design data: {e}")
        return []


def main():
    """
    Main function to calculate and display cost-effectiveness of architectural designs.
    """
    file_path = "designs.json"  # Example file path

    # Load designs from file
    designs = load_designs_from_file(file_path)

    if not designs:
        print("No designs available to process.")
        return

    print("Cost-Effectiveness of Architectural Designs:")
    print("-" * 50)

    for design in designs:
        try:
            cost_effectiveness = design.calculate_cost_effectiveness()
            print(f"Design: {design.name}")
            print(f"  Total Cost: {design.calculate_total_cost():,.2f}")
            print(f"  Cost-Effectiveness Score: {cost_effectiveness:.6f}")
        except ValueError as e:
            print(f"Error processing design '{design.name}': {e}")


if __name__ == "__main__":
    main()
```
