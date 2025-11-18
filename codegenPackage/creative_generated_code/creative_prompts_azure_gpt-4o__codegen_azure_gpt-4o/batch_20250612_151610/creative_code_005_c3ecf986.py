"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Develop a program to compare Cummins engine specifications (e.g., horsepower, transmission type) with other diesel engines, based on the solutions offered by Indusur.
Generated: DETERMINISTIC_c3ecf986805d5def
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


class Engine:
    """
    Represents a diesel engine with specifications such as engine name, horsepower, and transmission type.
    """

    def __init__(self, name, horsepower, transmission_type):
        """
        Initializes an Engine object.

        :param name: Name of the engine (string)
        :param horsepower: Horsepower of the engine (integer)
        :param transmission_type: Transmission type of the engine (string)
        """
        self.name = name
        self.horsepower = horsepower
        self.transmission_type = transmission_type

    def __str__(self):
        """
        Returns a formatted string representation of the engine.

        :return: Engine details as a string
        """
        return f"{self.name} - Horsepower: {self.horsepower}, Transmission Type: {self.transmission_type}"


def load_indusur_engines(file_path):
    """
    Loads diesel engine specifications from an Indusur-provided JSON file.

    :param file_path: Path to the JSON file containing engine specifications
    :return: List of Engine objects
    """
    try:
        with open(file_path, 'r') as file:
            engines_data = json.load(file)
            engines = [
                Engine(data['name'], data['horsepower'], data['transmission_type'])
                for data in engines_data
            ]
            return engines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please verify the file path.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file {file_path}. Ensure the file contains valid JSON.")
    except KeyError as e:
        print(f"Error: Missing required field in the JSON data - {e}.")
    return []


def compare_engines(cummins_engine, other_engines):
    """
    Compares a Cummins engine with a list of other diesel engines based on horsepower
    and transmission type.

    :param cummins_engine: Cummins engine to compare (Engine object)
    :param other_engines: List of other engines to compare against (list of Engine objects)
    :return: None
    """
    print(f"Comparison Results for Cummins Engine: {cummins_engine}\n")

    for engine in other_engines:
        print(f"Comparing with: {engine}")
        horsepower_diff = cummins_engine.horsepower - engine.horsepower
        transmission_match = cummins_engine.transmission_type == engine.transmission_type

        print(f"  Horsepower Difference: {horsepower_diff}")
        print(f"  Transmission Match: {'Yes' if transmission_match else 'No'}\n")


def main():
    """
    Main function to demonstrate engine comparison.

    :return: None
    """
    # Example Cummins engine specifications
    cummins_engine = Engine(name="Cummins ISX15", horsepower=400, transmission_type="Automatic")

    # Load other engines from Indusur-provided JSON file
    file_path = "indusur_engines.json"  # Update this path to the actual file location
    other_engines = load_indusur_engines(file_path)

    # Perform comparison if engines were loaded successfully
    if other_engines:
        compare_engines(cummins_engine, other_engines)


if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure the `indusur_engines.json` file exists and has valid data. Example JSON structure:
   ```json
   [
       {"name": "Engine A", "horsepower": 350, "transmission_type": "Manual"},
       {"name": "Engine B", "horsepower": 450, "transmission_type": "Automatic"}
   ]
   ```
2. Update the JSON file path (`file_path`) in the `main()` function as needed.
