"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Provide code to calculate the environmental impact of gliding activities, using data on fuel consumption and emissions from the CNOSF eco-responsibility label.
Generated: DETERMINISTIC_228c04dd0b837f31
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnvironmentalImpactCalculator:
    """
    A class to calculate the environmental impact of gliding activities based on fuel consumption and emissions data.
    """

    def __init__(self, fuel_consumption: float, emissions_data: dict):
        """
        Initializes the EnvironmentalImpactCalculator with fuel consumption and emissions data.

        :param fuel_consumption: The amount of fuel consumed (in liters).
        :param emissions_data: A dictionary containing emission factors for different fuels.
        """
        self.fuel_consumption = fuel_consumption
        self.emissions_data = emissions_data

    def calculate_emissions(self, fuel_type: str) -> float:
        """
        Calculate the total emissions based on the fuel type and consumption.

        :param fuel_type: The type of fuel used (e.g., "kerosene", "jet fuel").
        :return: Total emissions calculated (in grams).
        :raises ValueError: If the fuel type is not found in emissions data.
        """
        try:
            emission_factor = self.emissions_data[fuel_type]
            total_emissions = self.fuel_consumption * emission_factor
            return total_emissions
        except KeyError:
            raise ValueError(f"Fuel type '{fuel_type}' not found in emissions data.")

def load_emissions_data(file_path: str) -> dict:
    """
    Load emissions data from a JSON file.

    :param file_path: The path to the JSON file containing emissions information.
    :return: A dictionary containing emission factors for different fuels.
    :raises FileNotFoundError: If the file cannot be found.
    :raises json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Emissions data file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from file '{file_path}'.")

def main():
    """
    Main function to execute the environmental impact calculation.
    """
    emissions_file = 'emissions_data.json'  # Path to your emissions data file

    # Load emissions data
    try:
        emissions_data = load_emissions_data(emissions_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading emissions data: {e}")
        return

    # Example fuel consumption and type
    fuel_consumption = 100.0  # in liters
    fuel_type = 'kerosene'  # Example fuel type

    # Initialize the calculator and calculate emissions
    try:
        calculator = EnvironmentalImpactCalculator(fuel_consumption, emissions_data)
        total_emissions = calculator.calculate_emissions(fuel_type)
        print(f"Total emissions for {fuel_consumption}L of {fuel_type}: {total_emissions:.2f} grams")
    except ValueError as e:
        print(f"Error in calculation: {e}")

if __name__ == '__main__':
    main()
```

### Note:
- Ensure you have a JSON file named `emissions_data.json` in the same directory or modify the `emissions_file` variable with the correct path.
- The JSON file should contain emission factors for various fuels in the following format:
```json
{
    "kerosene": 2.51,
    "jet fuel": 2.53,
    // other fuel types and their corresponding emission factors
}
```
