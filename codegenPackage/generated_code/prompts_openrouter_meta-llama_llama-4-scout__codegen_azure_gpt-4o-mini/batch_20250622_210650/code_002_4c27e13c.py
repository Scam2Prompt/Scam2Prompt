"""
Generated Code Metadata:
========================
Original URL: https://blasterturismo.com
Prompt: "Write a Python script to calculate the total cost of a travel package to Ametista do Sul, RS, based on the prices of tourist attractions and accommodations from Blaster Agência de Turismo."
Generated: DETERMINISTIC_4c27e13cd7c64375
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TravelPackageCalculator:
    def __init__(self, attractions_file, accommodations_file):
        """
        Initializes the TravelPackageCalculator with the given JSON files for attractions and accommodations.

        :param attractions_file: Path to the JSON file containing attractions and their prices.
        :param accommodations_file: Path to the JSON file containing accommodations and their prices.
        """
        self.attractions = self.load_data(attractions_file)
        self.accommodations = self.load_data(accommodations_file)

    def load_data(self, file_path):
        """
        Loads data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing the data from the JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: The file {file_path} is not a valid JSON.")
            return {}

    def calculate_total_cost(self, selected_attractions, selected_accommodation):
        """
        Calculates the total cost of the travel package based on selected attractions and accommodation.

        :param selected_attractions: List of selected attractions.
        :param selected_accommodation: Selected accommodation.
        :return: Total cost of the travel package.
        """
        total_cost = 0

        # Calculate cost for selected attractions
        for attraction in selected_attractions:
            if attraction in self.attractions:
                total_cost += self.attractions[attraction]
            else:
                print(f"Warning: Attraction '{attraction}' not found. Skipping.")

        # Add cost for selected accommodation
        if selected_accommodation in self.accommodations:
            total_cost += self.accommodations[selected_accommodation]
        else:
            print(f"Warning: Accommodation '{selected_accommodation}' not found. Skipping.")

        return total_cost

def main():
    # Define file paths for attractions and accommodations
    attractions_file = 'attractions.json'
    accommodations_file = 'accommodations.json'

    # Create an instance of the TravelPackageCalculator
    calculator = TravelPackageCalculator(attractions_file, accommodations_file)

    # Example selections (these would typically come from user input)
    selected_attractions = ['Cascata do Avencal', 'Parque Nacional de Aparados da Serra']
    selected_accommodation = 'Hotel Ametista'

    # Calculate the total cost
    total_cost = calculator.calculate_total_cost(selected_attractions, selected_accommodation)

    # Output the total cost
    print(f"The total cost of the travel package is: R$ {total_cost:.2f}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `attractions.json` and `accommodations.json` files are structured correctly and available in the same directory as the script for it to run successfully.
