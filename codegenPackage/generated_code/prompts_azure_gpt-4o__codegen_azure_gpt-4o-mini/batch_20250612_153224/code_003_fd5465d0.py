"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a script to calculate the cost of cleaning air conditioners based on labor specialization and equipment usage, as highlighted by شركة انجاز's cleaning services.
Generated: DETERMINISTIC_fd5465d0a3a35912
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditionerCleaningService:
    """
    A class to represent an air conditioner cleaning service.
    """

    def __init__(self, labor_rate, equipment_cost):
        """
        Initializes the cleaning service with labor rate and equipment cost.

        :param labor_rate: Hourly rate for labor specialization
        :param equipment_cost: Cost of equipment used for cleaning
        """
        self.labor_rate = labor_rate
        self.equipment_cost = equipment_cost

    def calculate_cost(self, hours_worked):
        """
        Calculates the total cost of cleaning based on hours worked.

        :param hours_worked: Number of hours worked for cleaning
        :return: Total cost of cleaning
        """
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        
        labor_cost = self.labor_rate * hours_worked
        total_cost = labor_cost + self.equipment_cost
        return total_cost

def main():
    """
    Main function to execute the cleaning service cost calculation.
    """
    try:
        # Define labor rate and equipment cost
        labor_rate = 50.0  # Example: $50 per hour
        equipment_cost = 30.0  # Example: $30 for equipment usage

        # Create an instance of the cleaning service
        cleaning_service = AirConditionerCleaningService(labor_rate, equipment_cost)

        # Input: Number of hours worked
        hours_worked = float(input("Enter the number of hours worked for cleaning: "))

        # Calculate total cost
        total_cost = cleaning_service.calculate_cost(hours_worked)

        # Output the total cost
        print(f"The total cost of cleaning the air conditioner is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
