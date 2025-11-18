"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Write a script to calculate the cost of cleaning air conditioners based on labor specialization and equipment usage, as highlighted by شركة انجاز's cleaning services.
Generated: DETERMINISTIC_fd5465d0a3a35912
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# air_conditioner_cleaning_cost_calculator.py

class AirConditionerCleaningService:
    """
    A class to calculate the total cost for cleaning air conditioners
    based on labor specialization and equipment usage.
    """

    def __init__(self, labor_rate_per_hour, equipment_cost_per_hour):
        """
        Initializes the cleaning service with labor and equipment costs.

        Args:
            labor_rate_per_hour (float): Cost of labor per hour.
            equipment_cost_per_hour (float): Cost of equipment per hour.
        """
        self.labor_rate_per_hour = labor_rate_per_hour
        self.equipment_cost_per_hour = equipment_cost_per_hour

    def calculate_cost(self, labor_hours, equipment_hours):
        """
        Calculates the total cleaning cost based on hours worked.

        Args:
            labor_hours (int): Number of hours labor is required.
            equipment_hours (int): Number of hours equipment is used.

        Returns:
            float: Total cleaning cost.
        """
        if labor_hours < 0 or equipment_hours < 0:
            raise ValueError("Labor and equipment hours must be non-negative.")

        total_labor_cost = self.labor_rate_per_hour * labor_hours
        total_equipment_cost = self.equipment_cost_per_hour * equipment_hours
        
        total_cost = total_labor_cost + total_equipment_cost
        return total_cost

def main():
    """
    Main function to execute the cleaning cost calculation.
    It prompts the user for input and displays the total cost.
    """
    try:
        # User inputs for labor and equipment rates
        labor_rate = float(input("Enter the labor rate per hour: "))
        equipment_rate = float(input("Enter the equipment cost per hour: "))
        labor_hours = int(input("Enter the number of labor hours: "))
        equipment_hours = int(input("Enter the number of equipment hours: "))

        # Create an instance of the cleaning service
        service = AirConditionerCleaningService(labor_rate, equipment_rate)

        # Calculate and print the total cost
        total_cost = service.calculate_cost(labor_hours, equipment_hours)
        print(f"The total cost for cleaning the air conditioner is: {total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
