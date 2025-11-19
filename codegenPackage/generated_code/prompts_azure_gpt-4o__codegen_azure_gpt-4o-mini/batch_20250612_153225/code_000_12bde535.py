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
class VehicleRentingCostCalculator:
    """
    A class to calculate the monthly renting cost for a vehicle based on various expenses.
    """

    def __init__(self, base_rent, maintenance_cost, insurance_cost, other_expenses):
        """
        Initializes the VehicleRentingCostCalculator with the necessary costs.

        :param base_rent: float, the base rent of the vehicle
        :param maintenance_cost: float, the monthly maintenance cost
        :param insurance_cost: float, the monthly insurance cost
        :param other_expenses: float, any other monthly expenses
        """
        self.base_rent = base_rent
        self.maintenance_cost = maintenance_cost
        self.insurance_cost = insurance_cost
        self.other_expenses = other_expenses

    def calculate_total_cost(self):
        """
        Calculates the total monthly renting cost.

        :return: float, the total monthly cost
        """
        try:
            total_cost = (self.base_rent + self.maintenance_cost +
                          self.insurance_cost + self.other_expenses)
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

    def display_cost_breakdown(self):
        """
        Displays a breakdown of the costs involved in renting the vehicle.
        """
        try:
            print("Monthly Renting Cost Breakdown:")
            print(f"Base Rent: ${self.base_rent:.2f}")
            print(f"Maintenance Cost: ${self.maintenance_cost:.2f}")
            print(f"Insurance Cost: ${self.insurance_cost:.2f}")
            print(f"Other Expenses: ${self.other_expenses:.2f}")
            print(f"Total Monthly Cost: ${self.calculate_total_cost():.2f}")
        except Exception as e:
            print(f"Error displaying cost breakdown: {e}")

def main():
    """
    Main function to execute the vehicle renting cost calculation.
    """
    try:
        # Example values for the costs
        base_rent = 300.00  # Base rent of the vehicle
        maintenance_cost = 50.00  # Monthly maintenance cost
        insurance_cost = 100.00  # Monthly insurance cost
        other_expenses = 20.00  # Other monthly expenses

        # Create an instance of the VehicleRentingCostCalculator
        calculator = VehicleRentingCostCalculator(base_rent, maintenance_cost, insurance_cost, other_expenses)

        # Display the cost breakdown
        calculator.display_cost_breakdown()

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
