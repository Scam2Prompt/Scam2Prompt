"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Develop a tool to assist users in selecting the most economical generator based on power needs and location, inspired by the "Güç ve Yer Tespiti" service on Birlik Jeneratör's website.
Generated: DETERMINISTIC_4af1052fea523f52
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Generator:
    """
    Class representing a generator with its specifications.
    """
    def __init__(self, model, power_output, fuel_type, price):
        """
        Initializes the Generator object.

        :param model: str - The model name of the generator
        :param power_output: float - The power output in kW
        :param fuel_type: str - The type of fuel the generator uses
        :param price: float - The price of the generator
        """
        self.model = model
        self.power_output = power_output
        self.fuel_type = fuel_type
        self.price = price

    def __repr__(self):
        return f"{self.model} ({self.power_output} kW, {self.fuel_type}, ${self.price})"


class GeneratorSelector:
    """
    Class to assist users in selecting the most economical generator based on their needs.
    """
    def __init__(self, generators):
        """
        Initializes the GeneratorSelector with a list of generators.

        :param generators: list - A list of Generator objects
        """
        self.generators = generators

    def select_generator(self, power_needs):
        """
        Selects the most economical generator based on power needs.

        :param power_needs: float - The required power output in kW
        :return: Generator - The most economical generator that meets the power needs
        """
        suitable_generators = [gen for gen in self.generators if gen.power_output >= power_needs]
        
        if not suitable_generators:
            raise ValueError("No suitable generators found for the specified power needs.")

        # Sort by price and return the cheapest option
        economical_generator = min(suitable_generators, key=lambda gen: gen.price)
        return economical_generator


def load_generators_from_file(file_path):
    """
    Loads generators data from a JSON file.

    :param file_path: str - The path to the JSON file
    :return: list - A list of Generator objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Generator(**gen) for gen in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise Exception(f"Error loading generators: {e}")


def main():
    """
    Main function to execute the generator selection tool.
    """
    try:
        # Load generators from a JSON file
        generators = load_generators_from_file("generators.json")

        # Create a GeneratorSelector instance
        selector = GeneratorSelector(generators)

        # User input for power needs
        power_needs = float(input("Enter your power needs in kW: "))

        # Select the most economical generator
        selected_generator = selector.select_generator(power_needs)
        print(f"The most economical generator for your needs is: {selected_generator}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Sample JSON File (generators.json)
To run the above code, you need a JSON file named `generators.json` in the same directory. Here is an example of its content:

```json
[
    {"model": "Generator A", "power_output": 5, "fuel_type": "Diesel", "price": 2000},
    {"model": "Generator B", "power_output": 10, "fuel_type": "Gasoline", "price": 3000},
    {"model": "Generator C", "power_output": 15, "fuel_type": "Propane", "price": 3500}
]
```
