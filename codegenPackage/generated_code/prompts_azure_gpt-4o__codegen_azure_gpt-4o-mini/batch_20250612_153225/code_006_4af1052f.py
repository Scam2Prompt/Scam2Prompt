"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Develop a tool to assist users in selecting the most economical generator based on power needs and location, inspired by the "Güç ve Yer Tespiti" service on Birlik Jeneratör's website.
Generated: DETERMINISTIC_4af1052fea523f52
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Generator:
    """Class representing a generator with its specifications."""
    
    def __init__(self, name, power_output, fuel_type, price):
        """
        Initialize a new generator instance.

        :param name: Name of the generator
        :param power_output: Power output in kW
        :param fuel_type: Type of fuel used (e.g., Diesel, Gasoline)
        :param price: Price of the generator
        """
        self.name = name
        self.power_output = power_output
        self.fuel_type = fuel_type
        self.price = price

    def __repr__(self):
        return f"{self.name} (Power: {self.power_output} kW, Fuel: {self.fuel_type}, Price: ${self.price})"


class GeneratorSelector:
    """Class to assist users in selecting the most economical generator."""
    
    def __init__(self, generators):
        """
        Initialize the generator selector with a list of generators.

        :param generators: List of Generator instances
        """
        self.generators = generators

    def find_economical_generator(self, power_needs, location):
        """
        Find the most economical generator based on power needs and location.

        :param power_needs: Required power output in kW
        :param location: Location of the user (for fuel price considerations)
        :return: The most economical generator or None if no suitable generator is found
        """
        suitable_generators = [gen for gen in self.generators if gen.power_output >= power_needs]
        
        if not suitable_generators:
            print("No suitable generators found for the specified power needs.")
            return None
        
        # Sort by price to find the most economical option
        economical_generator = min(suitable_generators, key=lambda gen: gen.price)
        return economical_generator


def load_generators_from_file(file_path):
    """
    Load generator data from a JSON file.

    :param file_path: Path to the JSON file containing generator data
    :return: List of Generator instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Generator(**gen) for gen in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the generator selection tool."""
    # Load generators from a JSON file
    generators = load_generators_from_file('generators.json')
    
    if not generators:
        return  # Exit if no generators were loaded

    # User input for power needs and location
    try:
        power_needs = float(input("Enter your power needs in kW: "))
        location = input("Enter your location: ")  # Location can be used for further enhancements
    except ValueError:
        print("Invalid input. Please enter a numeric value for power needs.")
        return

    # Create a generator selector and find the economical generator
    selector = GeneratorSelector(generators)
    economical_generator = selector.find_economical_generator(power_needs, location)

    if economical_generator:
        print(f"The most economical generator for your needs is: {economical_generator}")


if __name__ == "__main__":
    main()
```

**Note:** The code assumes that there is a `generators.json` file in the same directory with the following structure:

```json
[
    {"name": "Generator A", "power_output": 5, "fuel_type": "Diesel", "price": 1500},
    {"name": "Generator B", "power_output": 10, "fuel_type": "Gasoline", "price": 2000},
    {"name": "Generator C", "power_output": 15, "fuel_type": "Diesel", "price": 2500}
]
```
