"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Create a script to calculate the cost of leasing SCOUT tractors based on user inputs like duration, equipment type, and budget, similar to the leasing options provided on SCOUT.kz.
Generated: DETERMINISTIC_719172b676a34003
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TractorLeaseCalculator:
    """
    A class to calculate the cost of leasing SCOUT tractors based on user inputs.
    """

    def __init__(self):
        # Define base costs for different equipment types (in currency units)
        self.equipment_costs = {
            'standard': 1000,  # Base cost for standard tractor
            'premium': 1500,   # Base cost for premium tractor
            'heavy': 2000      # Base cost for heavy-duty tractor
        }

    def calculate_lease_cost(self, equipment_type, duration_months):
        """
        Calculate the total lease cost based on equipment type and duration.

        :param equipment_type: Type of equipment to lease (standard, premium, heavy)
        :param duration_months: Duration of lease in months
        :return: Total lease cost
        :raises ValueError: If equipment type is invalid or duration is not positive
        """
        if equipment_type not in self.equipment_costs:
            raise ValueError(f"Invalid equipment type: {equipment_type}. Choose from {list(self.equipment_costs.keys())}.")
        
        if duration_months <= 0:
            raise ValueError("Duration must be a positive integer.")

        # Calculate total cost
        base_cost = self.equipment_costs[equipment_type]
        total_cost = base_cost * duration_months
        return total_cost

    def get_user_input(self):
        """
        Get user input for equipment type and duration.

        :return: Tuple containing equipment type and duration
        """
        equipment_type = input("Enter equipment type (standard, premium, heavy): ").strip().lower()
        duration_months = int(input("Enter lease duration in months: ").strip())
        return equipment_type, duration_months

    def run(self):
        """
        Run the lease calculator, handling user input and displaying results.
        """
        try:
            equipment_type, duration_months = self.get_user_input()
            total_cost = self.calculate_lease_cost(equipment_type, duration_months)
            print(f"The total lease cost for {duration_months} months of {equipment_type} tractor is: {total_cost} currency units.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Create an instance of the calculator and run it
    calculator = TractorLeaseCalculator()
    calculator.run()
```
