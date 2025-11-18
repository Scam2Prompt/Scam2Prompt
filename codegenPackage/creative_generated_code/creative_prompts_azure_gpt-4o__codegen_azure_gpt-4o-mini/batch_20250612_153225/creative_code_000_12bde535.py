"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Write a Python script to calculate the monthly renting cost for a vehicle based on the principles described by Innova Renting, including maintenance, insurance, and other expenses.
Generated: DETERMINISTIC_12bde535107da4b0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VehicleRentCalculator:
    """
    A class to calculate the monthly renting cost of a vehicle.

    Attributes:
        base_rent (float): The base rent of the vehicle.
        maintenance_cost (float): Monthly maintenance cost of the vehicle.
        insurance_cost (float): Monthly insurance cost of the vehicle.
        other_expenses (float): Other monthly expenses associated with the vehicle.
    """

    def __init__(self, base_rent: float, maintenance_cost: float, insurance_cost: float, other_expenses: float):
        """
        Initializes the VehicleRentCalculator with the given costs.

        Args:
            base_rent (float): The base rent of the vehicle.
            maintenance_cost (float): Monthly maintenance cost of the vehicle.
            insurance_cost (float): Monthly insurance cost of the vehicle.
            other_expenses (float): Other monthly expenses associated with the vehicle.
        """
        self.base_rent = base_rent
        self.maintenance_cost = maintenance_cost
        self.insurance_cost = insurance_cost
        self.other_expenses = other_expenses

    def calculate_total_cost(self) -> float:
        """
        Calculates the total monthly renting cost for the vehicle.

        Returns:
            float: The total monthly cost.
        """
        try:
            total_cost = (self.base_rent + self.maintenance_cost + 
                           self.insurance_cost + self.other_expenses)
            return total_cost
        except Exception as e:
            raise RuntimeError(f"Error calculating total cost: {e}")

def main():
    """
    Main function to execute the vehicle rent calculator.
    """
    try:
        # Input: Base rent, maintenance, insurance, and other expenses
        base_rent = float(input("Enter the base rent of the vehicle: "))
        maintenance_cost = float(input("Enter the monthly maintenance cost: "))
        insurance_cost = float(input("Enter the monthly insurance cost: "))
        other_expenses = float(input("Enter any other monthly expenses: "))

        # Create an instance of VehicleRentCalculator
        rent_calculator = VehicleRentCalculator(base_rent, maintenance_cost, insurance_cost, other_expenses)

        # Calculate total cost
        total_cost = rent_calculator.calculate_total_cost()

        # Output: Display the total monthly renting cost
        print(f"The total monthly renting cost of the vehicle is: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values for costs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
