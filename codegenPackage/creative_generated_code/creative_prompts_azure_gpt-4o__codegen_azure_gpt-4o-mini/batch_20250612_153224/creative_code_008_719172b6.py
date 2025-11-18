"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a script to calculate the cost of leasing SCOUT tractors based on user inputs like duration, equipment type, and budget, similar to the leasing options provided on SCOUT.kz.
Generated: DETERMINISTIC_719172b676a34003
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TractorLeasingCalculator:
    def __init__(self):
        # Define leasing options with estimated monthly costs for each equipment type
        self.equipment_costs = {
            "SCOUT_1": 500,
            "SCOUT_2": 700,
            "SCOUT_3": 900
        }

    def calculate_leasing_cost(self, equipment_type, duration_months):
        """
        Calculate the total leasing cost based on equipment type and duration.

        :param equipment_type: str, type of equipment to lease
        :param duration_months: int, duration of the lease in months
        :return: float, total leasing cost
        """
        if equipment_type not in self.equipment_costs:
            raise ValueError("Invalid equipment type selected.")
        
        monthly_cost = self.equipment_costs[equipment_type]
        total_cost = monthly_cost * duration_months
        return total_cost

    def check_budget(self, total_cost, budget):
        """
        Check if the total cost is within the user's budget.

        :param total_cost: float, total cost of the lease
        :param budget: float, user's budget
        :return: bool, True if within budget, otherwise False
        """
        return total_cost <= budget

def main():
    calculator = TractorLeasingCalculator()
    
    try:
        # User inputs
        equipment_type = input("Enter the equipment type (SCOUT_1, SCOUT_2, SCOUT_3): ")
        duration_months = int(input("Enter the duration of leasing in months: "))
        budget = float(input("Enter your budget: "))

        # Calculate leasing cost
        total_cost = calculator.calculate_leasing_cost(equipment_type, duration_months)
        print(f"Total leasing cost for {duration_months} months: ${total_cost:.2f}")

        # Check if within budget
        if calculator.check_budget(total_cost, budget):
            print("The total leasing cost is within your budget.")
        else:
            print("The total leasing cost exceeds your budget.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
