"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Create a script to calculate fuel savings for trucking companies using a fuel card program similar to the one offered by Summar Financial.
Generated: DETERMINISTIC_0979a0c89e7a1120
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FuelSavingsCalculator:
    """
    A class to calculate fuel savings for trucking companies using a fuel card program.
    """

    def __init__(self, fuel_data_file):
        """
        Initializes the FuelSavingsCalculator with fuel data from a JSON file.

        :param fuel_data_file: Path to the JSON file containing fuel data.
        """
        self.fuel_data_file = fuel_data_file
        self.fuel_data = self.load_fuel_data()

    def load_fuel_data(self):
        """
        Loads fuel data from a JSON file.

        :return: A dictionary containing fuel data.
        """
        try:
            with open(self.fuel_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Fuel data file '{self.fuel_data_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the fuel data file.")

    def calculate_savings(self, distance, fuel_efficiency, fuel_price):
        """
        Calculates the fuel savings based on distance, fuel efficiency, and fuel price.

        :param distance: Distance traveled in miles.
        :param fuel_efficiency: Fuel efficiency in miles per gallon (MPG).
        :param fuel_price: Price of fuel per gallon.
        :return: The total fuel cost and savings.
        """
        if distance <= 0 or fuel_efficiency <= 0 or fuel_price < 0:
            raise ValueError("Distance, fuel efficiency must be positive and fuel price cannot be negative.")

        # Calculate total fuel needed
        gallons_needed = distance / fuel_efficiency
        total_fuel_cost = gallons_needed * fuel_price

        # Calculate savings based on average fuel price from data
        average_fuel_price = self.get_average_fuel_price()
        savings = (average_fuel_price - fuel_price) * gallons_needed

        return total_fuel_cost, savings

    def get_average_fuel_price(self):
        """
        Calculates the average fuel price from the loaded fuel data.

        :return: The average fuel price.
        """
        prices = [entry['price'] for entry in self.fuel_data if 'price' in entry]
        if not prices:
            raise ValueError("No fuel price data available.")
        return sum(prices) / len(prices)

def main():
    """
    Main function to execute the fuel savings calculation.
    """
    fuel_data_file = 'fuel_data.json'  # Path to the fuel data JSON file
    calculator = FuelSavingsCalculator(fuel_data_file)

    # Example input values
    distance = 1000  # miles
    fuel_efficiency = 8  # MPG
    fuel_price = 3.50  # price per gallon

    try:
        total_cost, savings = calculator.calculate_savings(distance, fuel_efficiency, fuel_price)
        print(f"Total Fuel Cost: ${total_cost:.2f}")
        print(f"Estimated Savings: ${savings:.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `fuel_data.json` file exists in the same directory as the script and contains valid JSON data with a structure that includes a `price` key for each fuel entry.
