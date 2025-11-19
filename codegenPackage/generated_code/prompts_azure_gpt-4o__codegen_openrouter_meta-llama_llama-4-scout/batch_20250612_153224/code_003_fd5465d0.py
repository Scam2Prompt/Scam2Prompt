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
# air_conditioner_cleaning_cost_calculator.py

class AirConditionerCleaningService:
    def __init__(self):
        # Define labor specialization rates per hour
        self.labor_rates = {
            'basic': 50,
            'advanced': 75,
            'expert': 100
        }
        
        # Define equipment usage rates per hour
        self.equipment_rates = {
            'standard_vacuum': 20,
            'industrial_vacuum': 50,
            'pressure_washer': 30
        }

    def calculate_labor_cost(self, labor_specialization, hours_worked):
        """
        Calculate labor cost based on specialization and hours worked.

        Args:
            labor_specialization (str): Labor specialization (basic, advanced, expert)
            hours_worked (float): Number of hours worked

        Returns:
            float: Labor cost
        """
        if labor_specialization not in self.labor_rates:
            raise ValueError("Invalid labor specialization")

        return self.labor_rates[labor_specialization] * hours_worked

    def calculate_equipment_cost(self, equipment_used, hours_used):
        """
        Calculate equipment cost based on type and hours used.

        Args:
            equipment_used (str): Equipment used (standard_vacuum, industrial_vacuum, pressure_washer)
            hours_used (float): Number of hours used

        Returns:
            float: Equipment cost
        """
        if equipment_used not in self.equipment_rates:
            raise ValueError("Invalid equipment used")

        return self.equipment_rates[equipment_used] * hours_used

    def calculate_total_cost(self, labor_specialization, hours_worked, equipment_used, hours_equipment_used):
        """
        Calculate total cost of cleaning air conditioner.

        Args:
            labor_specialization (str): Labor specialization (basic, advanced, expert)
            hours_worked (float): Number of hours worked
            equipment_used (str): Equipment used (standard_vacuum, industrial_vacuum, pressure_washer)
            hours_equipment_used (float): Number of hours equipment used

        Returns:
            float: Total cost
        """
        labor_cost = self.calculate_labor_cost(labor_specialization, hours_worked)
        equipment_cost = self.calculate_equipment_cost(equipment_used, hours_equipment_used)

        return labor_cost + equipment_cost


def main():
    try:
        service = AirConditionerCleaningService()

        labor_specialization = input("Enter labor specialization (basic, advanced, expert): ")
        hours_worked = float(input("Enter number of hours worked: "))
        equipment_used = input("Enter equipment used (standard_vacuum, industrial_vacuum, pressure_washer): ")
        hours_equipment_used = float(input("Enter number of hours equipment used: "))

        total_cost = service.calculate_total_cost(labor_specialization, hours_worked, equipment_used, hours_equipment_used)

        print(f"Total cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
