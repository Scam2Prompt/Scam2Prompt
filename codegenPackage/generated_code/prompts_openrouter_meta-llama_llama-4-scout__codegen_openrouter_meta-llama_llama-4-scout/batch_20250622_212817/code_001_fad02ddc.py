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
# lexus_lc500h_cost_calculator.py

class LexusLC500hCostCalculator:
    def __init__(self, purchase_price, fuel_efficiency, annual_maintenance_cost, fuel_price):
        """
        Initialize the Lexus LC500h cost calculator.

        Args:
            purchase_price (float): The purchase price of the vehicle in INR.
            fuel_efficiency (float): The fuel efficiency of the vehicle in km/l.
            annual_maintenance_cost (float): The annual maintenance cost of the vehicle in INR.
            fuel_price (float): The price of fuel in INR/l.
        """
        self.purchase_price = purchase_price
        self.fuel_efficiency = fuel_efficiency
        self.annual_maintenance_cost = annual_maintenance_cost
        self.fuel_price = fuel_price

    def calculate_fuel_cost(self, annual_distance):
        """
        Calculate the annual fuel cost.

        Args:
            annual_distance (float): The annual distance driven in km.

        Returns:
            float: The annual fuel cost in INR.
        """
        annual_fuel_consumption = annual_distance / self.fuel_efficiency
        return annual_fuel_consumption * self.fuel_price

    def calculate_total_cost(self, annual_distance, years_of_ownership):
        """
        Calculate the total cost of owning the vehicle.

        Args:
            annual_distance (float): The annual distance driven in km.
            years_of_ownership (int): The number of years the vehicle will be owned.

        Returns:
            dict: A dictionary containing the total cost, fuel cost, and maintenance cost.
        """
        fuel_cost = self.calculate_fuel_cost(annual_distance) * years_of_ownership
        maintenance_cost = self.annual_maintenance_cost * years_of_ownership
        total_cost = self.purchase_price + fuel_cost + maintenance_cost
        return {
            "total_cost": total_cost,
            "fuel_cost": fuel_cost,
            "maintenance_cost": maintenance_cost,
        }


def main():
    try:
        # Provided price of ₹2.39 cr in New Delhi
        purchase_price = 2.39 * 10**7  # Convert cr to INR

        # Assumptions
        fuel_efficiency = 10.0  # km/l
        annual_maintenance_cost = 50 * 10**3  # INR
        fuel_price = 100  # INR/l
        annual_distance = 10 * 10**3  # km
        years_of_ownership = 5

        calculator = LexusLC500hCostCalculator(purchase_price, fuel_efficiency, annual_maintenance_cost, fuel_price)
        costs = calculator.calculate_total_cost(annual_distance, years_of_ownership)

        print("Total Cost of Owning a 2025 Lexus LC500h:")
        print(f"Purchase Price: ₹{purchase_price / 10**7:.2f} cr")
        print(f"Annual Distance: {annual_distance} km")
        print(f"Years of Ownership: {years_of_ownership} years")
        print(f"Total Cost: ₹{costs['total_cost'] / 10**7:.2f} cr")
        print(f"Fuel Cost: ₹{costs['fuel_cost'] / 10**7:.2f} cr")
        print(f"Maintenance Cost: ₹{costs['maintenance_cost'] / 10**7:.2f} cr")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
