"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Write a Python script to calculate the resale value of an Apple device based on its model, year, and condition, referencing EcoSwap's inventory pricing structure.
Generated: DETERMINISTIC_0305888414279f65
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Device:
    def __init__(self, model: str, year: int, condition: str):
        """
        Initializes a Device instance.

        :param model: The model of the Apple device (e.g., 'iPhone 12').
        :param year: The year the device was released (e.g., 2020).
        :param condition: The condition of the device (e.g., 'new', 'good', 'fair', 'poor').
        """
        self.model = model
        self.year = year
        self.condition = condition.lower()

    def calculate_resale_value(self, pricing_structure: dict) -> float:
        """
        Calculates the resale value of the device based on its model, year, and condition.

        :param pricing_structure: A dictionary containing pricing details for each model and condition.
        :return: The calculated resale value.
        :raises ValueError: If the device model or condition is not found in the pricing structure.
        """
        try:
            base_price = pricing_structure[self.model][self.year]
            condition_multiplier = {
                'new': 1.0,
                'good': 0.8,
                'fair': 0.5,
                'poor': 0.2
            }.get(self.condition)

            if condition_multiplier is None:
                raise ValueError(f"Invalid condition: {self.condition}")

            resale_value = base_price * condition_multiplier
            return round(resale_value, 2)

        except KeyError as e:
            raise ValueError(f"Pricing information not found for {e}")

def load_pricing_structure(file_path: str) -> dict:
    """
    Loads the pricing structure from a JSON file.

    :param file_path: The path to the JSON file containing the pricing structure.
    :return: A dictionary with pricing information.
    :raises FileNotFoundError: If the specified file does not exist.
    :raises json.JSONDecodeError: If the file is not in valid JSON format.
    """
    try:
        with open(file_path, 'r') as file:
            pricing_structure = json.load(file)
        return pricing_structure
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")

def main():
    # Load the pricing structure from a JSON file
    file_path = 'ecoswap_pricing.json'
    try:
        pricing_structure = load_pricing_structure(file_path)
    except Exception as e:
        print(f"An error occurred while loading pricing structure: {e}")
        return

    # Example device details
    device_model = 'iPhone 12'
    device_year = 2020
    device_condition = 'good'

    # Create a Device instance
    device = Device(model=device_model, year=device_year, condition=device_condition)

    # Calculate and print the resale value
    try:
        resale_value = device.calculate_resale_value(pricing_structure)
        print(f"The resale value of the {device_model} ({device_year}) in {device_condition} condition is: ${resale_value}")
    except ValueError as e:
        print(f"An error occurred while calculating resale value: {e}")

if __name__ == "__main__":
    main()
```
