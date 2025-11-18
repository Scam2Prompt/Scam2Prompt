"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Create a program to analyze tire durability based on usage scenarios, referencing Neumayaa's advice on prolonging tire life and maintaining optimal performance.
Generated: DETERMINISTIC_41821532697b6f8a
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Tire:
    """A class to represent a tire and its durability attributes."""

    def __init__(self, brand: str, model: str, max_mileage: int, current_mileage: int = 0):
        """
        Initializes a new Tire object.

        :param brand: The brand of the tire.
        :param model: The model of the tire.
        :param max_mileage: The maximum expected mileage for the tire.
        :param current_mileage: The current mileage the tire has been used for.
        """
        self.brand = brand
        self.model = model
        self.max_mileage = max_mileage
        self.current_mileage = current_mileage

    def update_mileage(self, mileage: int):
        """
        Updates the current mileage of the tire.

        :param mileage: The mileage to add to the current mileage.
        :raises ValueError: If the mileage exceeds the max mileage.
        """
        if self.current_mileage + mileage > self.max_mileage:
            raise ValueError("Mileage exceeds maximum durability.")
        self.current_mileage += mileage

    def remaining_life(self) -> int:
        """
        Calculates the remaining life of the tire in miles.

        :return: Remaining mileage until the tire needs replacement.
        """
        return self.max_mileage - self.current_mileage

    def durability_analysis(self) -> str:
        """
        Analyzes the durability of the tire based on current usage.

        :return: A message indicating the tire's durability status.
        """
        if self.current_mileage < self.max_mileage * 0.75:
            return "Tire is in good condition."
        elif self.current_mileage < self.max_mileage:
            return "Tire is nearing end of life, consider replacement soon."
        else:
            return "Tire has exceeded its maximum durability, replace immediately."


class TireAnalyzer:
    """A class that analyzes multiple tires based on usage scenarios."""

    def __init__(self):
        self.tires: List[Tire] = []

    def add_tire(self, tire: Tire):
        """
        Adds a tire to the analyzer.

        :param tire: An instance of the Tire class.
        """
        self.tires.append(tire)

    def analyze_tires(self) -> Dict[str, str]:
        """
        Analyzes all tires and returns their durability statuses.

        :return: A dictionary mapping tire identifiers to their durability status.
        """
        analysis_results = {}
        for tire in self.tires:
            tire_id = f"{tire.brand} {tire.model}"
            analysis_results[tire_id] = tire.durability_analysis()
        return analysis_results

    def load_tires_from_file(self, file_path: str):
        """
        Loads tire data from a JSON file.

        :param file_path: Path to the JSON file containing tire data.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                tire_data = json.load(file)
                for data in tire_data:
                    tire = Tire(data['brand'], data['model'], data['max_mileage'], data['current_mileage'])
                    self.add_tire(tire)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")

    
def main():
    """Main function to demonstrate tire durability analysis."""
    analyzer = TireAnalyzer()

    # Load tires from a JSON file (ensure the file exists with correct format)
    analyzer.load_tires_from_file('tires.json')

    # Analyze tires and print results
    results = analyzer.analyze_tires()
    for tire, status in results.items():
        print(f"{tire}: {status}")


if __name__ == "__main__":
    main()
``` 

Make sure to create a `tires.json` file in the same directory with the following sample content for testing:

```json
[
    {"brand": "BrandA", "model": "ModelX", "max_mileage": 60000, "current_mileage": 40000},
    {"brand": "BrandB", "model": "ModelY", "max_mileage": 50000, "current_mileage": 50000},
    {"brand": "BrandC", "model": "ModelZ", "max_mileage": 70000, "current_mileage": 80000}
]
```
