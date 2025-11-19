"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Write a Python script to calculate the cost of owning a hot tub, including maintenance and energy costs, for a customer in El Paso County.
Generated: DETERMINISTIC_b0a7009df02811a3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class HotTubCostCalculator:
    """
    A class to calculate the total cost of owning a hot tub, including
    maintenance and energy costs.
    """

    def __init__(self, purchase_price, maintenance_cost, energy_cost, usage_hours_per_week):
        """
        Initializes the HotTubCostCalculator with the given parameters.

        :param purchase_price: Initial purchase price of the hot tub
        :param maintenance_cost: Annual maintenance cost
        :param energy_cost: Monthly energy cost
        :param usage_hours_per_week: Average hours of usage per week
        """
        self.purchase_price = purchase_price
        self.maintenance_cost = maintenance_cost
        self.energy_cost = energy_cost
        self.usage_hours_per_week = usage_hours_per_week

    def calculate_annual_cost(self):
        """
        Calculates the total annual cost of owning the hot tub.

        :return: Total annual cost
        """
        try:
            # Calculate annual energy cost
            annual_energy_cost = self.energy_cost * 12
            
            # Total annual cost includes maintenance and energy costs
            total_annual_cost = self.maintenance_cost + annual_energy_cost
            
            return total_annual_cost
        except Exception as e:
            print(f"Error calculating annual cost: {e}")
            sys.exit(1)

    def calculate_total_cost(self, years):
        """
        Calculates the total cost of owning the hot tub over a specified number of years.

        :param years: Number of years to calculate the total cost for
        :return: Total cost over the specified number of years
        """
        try:
            if years < 0:
                raise ValueError("Number of years cannot be negative.")
            
            annual_cost = self.calculate_annual_cost()
            total_cost = self.purchase_price + (annual_cost * years)
            
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            sys.exit(1)

def main():
    """
    Main function to execute the hot tub cost calculator.
    """
    try:
        # Example values for the hot tub costs
        purchase_price = float(input("Enter the purchase price of the hot tub: "))
        maintenance_cost = float(input("Enter the annual maintenance cost: "))
        energy_cost = float(input("Enter the monthly energy cost: "))
        usage_hours_per_week = float(input("Enter the average hours of usage per week: "))
        years = int(input("Enter the number of years to calculate the total cost: "))

        # Create an instance of the HotTubCostCalculator
        calculator = HotTubCostCalculator(purchase_price, maintenance_cost, energy_cost, usage_hours_per_week)

        # Calculate and display the total cost
        total_cost = calculator.calculate_total_cost(years)
        print(f"The total cost of owning the hot tub for {years} years is: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
