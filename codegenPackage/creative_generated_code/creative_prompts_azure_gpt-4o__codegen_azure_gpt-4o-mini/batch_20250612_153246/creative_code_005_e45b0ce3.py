"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerafricasolar.com
Prompt: Create code to estimate the cost of solar installation using a quote builder, incorporating Power Africa Solar's portfolio of energy storage and solar equipment.
Generated: DETERMINISTIC_e45b0ce3889d6339
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

class SolarInstallationEstimator:
    def __init__(self, equipment_data_file):
        """
        Initialize the estimator with equipment data loaded from a JSON file.

        :param equipment_data_file: Path to the JSON file containing equipment and storage data.
        """
        self.equipment_data = self.load_equipment_data(equipment_data_file)

    def load_equipment_data(self, file_path):
        """
        Load equipment data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing equipment data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            raise Exception(f"Equipment data file not found: {file_path}")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON from the file: {file_path}")

    def estimate_cost(self, equipment_selection):
        """
        Estimate the total cost of solar installation based on selected equipment.

        :param equipment_selection: Dictionary containing selected equipment and their quantities.
        :return: Estimated total cost.
        """
        total_cost = 0.0

        for equipment_type, quantity in equipment_selection.items():
            if equipment_type in self.equipment_data:
                equipment_price = self.equipment_data[equipment_type]['price']
                total_cost += equipment_price * quantity
            else:
                raise ValueError(f"Invalid equipment type selected: {equipment_type}")

        return total_cost

def main():
    equipment_file = 'equipment_data.json'  # Path to the equipment data file
    estimator = SolarInstallationEstimator(equipment_file)

    # Example equipment selections (e.g., number of panels, batteries)
    equipment_selection = {
        "solar_panel": 10,  # Number of solar panels
        "battery_storage": 5  # Number of battery storage units
    }

    try:
        total_estimated_cost = estimator.estimate_cost(equipment_selection)
        print(f"Total estimated cost for solar installation: ${total_estimated_cost:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to have a `equipment_data.json` file structured like this:

```json
{
    "solar_panel": {
        "price": 200.00
    },
    "battery_storage": {
        "price": 500.00
    }
}
``` 

This code encapsulates the functionality to estimate solar installation costs based on user-selected equipment and handles errors for file operations and invalid selections.
