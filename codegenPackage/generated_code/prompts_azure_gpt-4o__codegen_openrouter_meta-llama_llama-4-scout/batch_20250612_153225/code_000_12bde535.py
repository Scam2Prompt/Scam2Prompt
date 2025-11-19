"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Write a Python script to calculate the monthly renting cost for a vehicle based on the principles described by Innova Renting, including maintenance, insurance, and other expenses.
Generated: DETERMINISTIC_12bde535107da4b0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_renting_cost_calculator.py

class Vehicle:
    def __init__(self, purchase_price, annual_maintenance, annual_insurance, annual_other_expenses, depreciation_rate, years_owned):
        """
        Initialize a Vehicle object.

        Args:
        - purchase_price (float): The initial purchase price of the vehicle.
        - annual_maintenance (float): The annual maintenance cost of the vehicle.
        - annual_insurance (float): The annual insurance cost of the vehicle.
        - annual_other_expenses (float): The annual other expenses (e.g., fuel, tolls) of the vehicle.
        - depreciation_rate (float): The annual depreciation rate of the vehicle (as a decimal).
        - years_owned (int): The number of years the vehicle is owned.
        """
        self.purchase_price = purchase_price
        self.annual_maintenance = annual_maintenance
        self.annual_insurance = annual_insurance
        self.annual_other_expenses = annual_other_expenses
        self.depreciation_rate = depreciation_rate
        self.years_owned = years_owned

    def calculate_depreciation(self):
        """
        Calculate the vehicle's depreciation over the ownership period.

        Returns:
        - float: The vehicle's depreciation.
        """
        return self.purchase_price * (1 - (1 - self.depreciation_rate) ** self.years_owned)

    def calculate_annual_expenses(self):
        """
        Calculate the vehicle's annual expenses.

        Returns:
        - float: The vehicle's annual expenses.
        """
        return self.annual_maintenance + self.annual_insurance + self.annual_other_expenses

    def calculate_monthly_renting_cost(self):
        """
        Calculate the monthly renting cost for the vehicle.

        Returns:
        - float: The monthly renting cost.
        """
        depreciation = self.calculate_depreciation()
        annual_expenses = self.calculate_annual_expenses()
        total_cost = depreciation + (annual_expenses * self.years_owned)
        monthly_cost = total_cost / (self.years_owned * 12)
        return round(monthly_cost, 2)


def main():
    try:
        purchase_price = float(input("Enter the vehicle's purchase price: "))
        annual_maintenance = float(input("Enter the vehicle's annual maintenance cost: "))
        annual_insurance = float(input("Enter the vehicle's annual insurance cost: "))
        annual_other_expenses = float(input("Enter the vehicle's annual other expenses: "))
        depreciation_rate = float(input("Enter the vehicle's annual depreciation rate (as a decimal): "))
        years_owned = int(input("Enter the number of years the vehicle is owned: "))

        vehicle = Vehicle(purchase_price, annual_maintenance, annual_insurance, annual_other_expenses, depreciation_rate, years_owned)
        monthly_renting_cost = vehicle.calculate_monthly_renting_cost()

        print(f"The monthly renting cost for the vehicle is: ${monthly_renting_cost}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
