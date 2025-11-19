"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Write a Python script to calculate the cost of owning a 2025 Lexus LC 500h, including fuel costs and maintenance expenses, based on the provided price of ₹ 2.39 cr in New Delhi.
Generated: DETERMINISTIC_fad02ddc8b80a036
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CarOwnershipCostCalculator:
    def __init__(self, purchase_price, fuel_efficiency, fuel_price, annual_mileage, maintenance_cost):
        """
        Initializes the CarOwnershipCostCalculator with the necessary parameters.

        :param purchase_price: The purchase price of the car (in INR).
        :param fuel_efficiency: The fuel efficiency of the car (in km/l).
        :param fuel_price: The price of fuel (in INR/l).
        :param annual_mileage: The estimated annual mileage (in km).
        :param maintenance_cost: The annual maintenance cost (in INR).
        """
        self.purchase_price = purchase_price
        self.fuel_efficiency = fuel_efficiency
        self.fuel_price = fuel_price
        self.annual_mileage = annual_mileage
        self.maintenance_cost = maintenance_cost

    def calculate_fuel_cost(self):
        """
        Calculates the annual fuel cost based on the fuel efficiency and annual mileage.

        :return: Annual fuel cost (in INR).
        """
        try:
            fuel_needed = self.annual_mileage / self.fuel_efficiency
            fuel_cost = fuel_needed * self.fuel_price
            return fuel_cost
        except ZeroDivisionError:
            raise ValueError("Fuel efficiency cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating fuel cost: {e}")

    def calculate_total_ownership_cost(self, years):
        """
        Calculates the total cost of ownership over a specified number of years.

        :param years: The number of years to calculate the total cost for.
        :return: Total cost of ownership (in INR).
        """
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")
        
        try:
            total_fuel_cost = self.calculate_fuel_cost() * years
            total_maintenance_cost = self.maintenance_cost * years
            total_cost = self.purchase_price + total_fuel_cost + total_maintenance_cost
            return total_cost
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating total ownership cost: {e}")

def main():
    # Constants for the Lexus LC 500h
    PURCHASE_PRICE = 23900000  # in INR
    FUEL_EFFICIENCY = 15  # in km/l (example value)
    FUEL_PRICE = 100  # in INR/l (example value)
    ANNUAL_MILEAGE = 15000  # in km (example value)
    MAINTENANCE_COST = 50000  # in INR (example value)

    # Create an instance of the calculator
    calculator = CarOwnershipCostCalculator(
        purchase_price=PURCHASE_PRICE,
        fuel_efficiency=FUEL_EFFICIENCY,
        fuel_price=FUEL_PRICE,
        annual_mileage=ANNUAL_MILEAGE,
        maintenance_cost=MAINTENANCE_COST
    )

    # Calculate total ownership cost for a specified number of years
    years = 5  # Example: Calculate for 5 years
    try:
        total_cost = calculator.calculate_total_ownership_cost(years)
        print(f"Total cost of owning the Lexus LC 500h for {years} years: ₹ {total_cost:,.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
