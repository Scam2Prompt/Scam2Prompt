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
# scout_tractor_leasing_calculator.py

class ScoutTractorLeasingCalculator:
    """
    Calculates the cost of leasing SCOUT tractors based on user inputs.

    Attributes:
        equipment_types (dict): Dictionary of equipment types with their respective prices.
        durations (list): List of available leasing durations in months.
    """

    def __init__(self):
        self.equipment_types = {
            "Scout 20": 50000,
            "Scout 30": 70000,
            "Scout 40": 90000
        }
        self.durations = [12, 24, 36]

    def calculate_leasing_cost(self, equipment_type, duration, budget):
        """
        Calculates the leasing cost based on the equipment type, duration, and budget.

        Args:
            equipment_type (str): Type of equipment.
            duration (int): Leasing duration in months.
            budget (float): User's budget.

        Returns:
            float: The calculated leasing cost.

        Raises:
            ValueError: If the equipment type or duration is invalid.
        """
        if equipment_type not in self.equipment_types:
            raise ValueError("Invalid equipment type")

        if duration not in self.durations:
            raise ValueError("Invalid leasing duration")

        equipment_price = self.equipment_types[equipment_type]
        monthly_interest_rate = 0.05 / 12  # 5% annual interest rate
        monthly_payment = equipment_price * monthly_interest_rate * (1 + monthly_interest_rate) ** duration / ((1 + monthly_interest_rate) ** duration - 1)

        if monthly_payment > budget:
            raise ValueError("Leasing cost exceeds your budget")

        return monthly_payment

    def get_equipment_types(self):
        """
        Returns a list of available equipment types.

        Returns:
            list: List of equipment types.
        """
        return list(self.equipment_types.keys())

    def get_durations(self):
        """
        Returns a list of available leasing durations.

        Returns:
            list: List of leasing durations in months.
        """
        return self.durations


def main():
    calculator = ScoutTractorLeasingCalculator()

    print("Available equipment types:")
    for i, equipment_type in enumerate(calculator.get_equipment_types()):
        print(f"{i+1}. {equipment_type}")

    equipment_type_choice = int(input("Enter the number of your chosen equipment type: "))
    equipment_type = calculator.get_equipment_types()[equipment_type_choice - 1]

    print("\nAvailable leasing durations:")
    for i, duration in enumerate(calculator.get_durations()):
        print(f"{i+1}. {duration} months")

    duration_choice = int(input("Enter the number of your chosen leasing duration: "))
    duration = calculator.get_durations()[duration_choice - 1]

    budget = float(input("Enter your budget: "))

    try:
        leasing_cost = calculator.calculate_leasing_cost(equipment_type, duration, budget)
        print(f"\nThe leasing cost for {equipment_type} for {duration} months is: ${leasing_cost:.2f} per month")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
