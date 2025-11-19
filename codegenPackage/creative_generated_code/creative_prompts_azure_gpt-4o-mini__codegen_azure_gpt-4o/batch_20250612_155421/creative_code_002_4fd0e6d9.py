"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Create a script that automates the process of selecting the right drive flange based on the specifications provided by Metal Fab Pro Race Shop.
Generated: DETERMINISTIC_4fd0e6d9b68159a0
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DriveFlangeSelector:
    def __init__(self, flange_data_file):
        """
        Initialize the DriveFlangeSelector with the data file containing flange specifications.

        :param flange_data_file: Path to the JSON file containing drive flange specifications.
        """
        self.flange_data_file = flange_data_file
        self.flange_specs = []
        self.load_flange_data()

    def load_flange_data(self):
        """
        Load drive flange specifications from a JSON file.
        """
        try:
            with open(self.flange_data_file, 'r') as file:
                self.flange_specs = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{self.flange_data_file}' not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from file '{self.flange_data_file}'.")
            raise

    def find_matching_flange(self, specifications):
        """
        Find the best matching drive flange based on provided specifications.

        :param specifications: A dictionary containing specifications to match against.
        :return: A dictionary representing the matched flange or None if no match is found.
        """
        matching_flange = None

        for flange in self.flange_specs:
            if all(flange.get(key) == value for key, value in specifications.items()):
                matching_flange = flange
                break

        return matching_flange

    def run(self):
        """
        Run the flange selection process interactively.
        """
        print("Welcome to the Drive Flange Selector!")
        print("Please provide the specifications to find the matching drive flange.")

        # Collect specifications from the user
        specifications = {}
        while True:
            key = input("Enter specification name (or 'done' to finish): ").strip()
            if key.lower() == 'done':
                break
            value = input(f"Enter value for '{key}': ").strip()
            specifications[key] = value

        # Find the matching flange
        matching_flange = self.find_matching_flange(specifications)

        if matching_flange:
            print("Matching Drive Flange found:")
            print(json.dumps(matching_flange, indent=4))
        else:
            print("No matching Drive Flange found for the provided specifications.")


if __name__ == "__main__":
    # Path to the JSON file containing flange specifications
    flange_data_file = "flange_data.json"

    try:
        selector = DriveFlangeSelector(flange_data_file)
        selector.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Notes:
1. Ensure the `flange_data.json` file exists in the working directory and has valid JSON data.
2. An example `flange_data.json` file format might look like:
```json
[
    {
        "material": "steel",
        "diameter": "5",
        "bolt_pattern": "6-bolt",
        "brand": "ProRace"
    },
    {
        "material": "aluminum",
        "diameter": "6",
        "bolt_pattern": "4-bolt",
        "brand": "SpeedFab"
    }
]
```
