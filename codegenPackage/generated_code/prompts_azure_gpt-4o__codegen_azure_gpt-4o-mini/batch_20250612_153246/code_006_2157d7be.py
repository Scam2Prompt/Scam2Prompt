"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: Create a script to automate the generation of vehicle price quotes based on user input, as seen in the "Cotizar Vehículo" feature on Cid Autos.
Generated: DETERMINISTIC_2157d7be3d560053
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class VehicleQuote:
    def __init__(self, make, model, year, mileage, condition):
        """
        Initialize the VehicleQuote object with vehicle details.

        :param make: str - The make of the vehicle
        :param model: str - The model of the vehicle
        :param year: int - The year of manufacture
        :param mileage: int - The mileage of the vehicle
        :param condition: str - The condition of the vehicle (e.g., 'new', 'used', 'certified')
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.base_price = self.get_base_price()

    def get_base_price(self):
        """
        Retrieve the base price for the vehicle based on its make, model, and year.

        :return: float - The base price of the vehicle
        """
        # In a real application, this data might come from a database or an API
        price_data = {
            "Toyota": {"Camry": {2020: 24000, 2021: 25000}},
            "Honda": {"Civic": {2020: 22000, 2021: 23000}},
        }
        
        try:
            return price_data[self.make][self.model][self.year]
        except KeyError:
            raise ValueError("Price data not available for the specified vehicle.")

    def calculate_quote(self):
        """
        Calculate the final quote for the vehicle based on its condition and mileage.

        :return: float - The final price quote for the vehicle
        """
        depreciation_rate = self.get_depreciation_rate()
        final_price = self.base_price * (1 - depreciation_rate)
        return round(final_price, 2)

    def get_depreciation_rate(self):
        """
        Determine the depreciation rate based on the vehicle's condition and mileage.

        :return: float - The depreciation rate as a decimal
        """
        if self.condition == 'new':
            return 0.0
        elif self.condition == 'used':
            return min(0.2 + (self.mileage / 100000) * 0.1, 0.5)  # Max 50% depreciation
        elif self.condition == 'certified':
            return 0.1
        else:
            raise ValueError("Invalid condition specified.")

def main():
    """
    Main function to execute the vehicle quote generation.
    """
    try:
        # User input for vehicle details
        make = input("Enter the vehicle make (e.g., Toyota, Honda): ")
        model = input("Enter the vehicle model (e.g., Camry, Civic): ")
        year = int(input("Enter the vehicle year (e.g., 2020): "))
        mileage = int(input("Enter the vehicle mileage (e.g., 30000): "))
        condition = input("Enter the vehicle condition (new, used, certified): ").lower()

        # Create a VehicleQuote instance
        quote = VehicleQuote(make, model, year, mileage, condition)

        # Calculate and display the quote
        final_quote = quote.calculate_quote()
        print(f"The estimated price quote for your vehicle is: ${final_quote}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
