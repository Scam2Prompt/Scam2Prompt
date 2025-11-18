"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a script to calculate rush charges for environmental testing based on A & B Labs' turnaround time (TAT) policy, including surcharges for 1-day, 2-day, and 3-day testing.
Generated: DETERMINISTIC_0fe2f0665d1adb29
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class RushChargeCalculator:
    """
    A class to calculate rush charges for environmental testing based on turnaround time (TAT) policy.

    Attributes:
        base_charge (float): The base charge for the testing service.
        rush_charges (dict): A dictionary containing the surcharge percentages for different TATs.
    """

    def __init__(self, base_charge: float):
        """
        Initializes the RushChargeCalculator with a base charge and predefined rush charges.

        Args:
            base_charge (float): The base charge for the testing service.

        Raises:
            ValueError: If base_charge is negative.
        """
        if base_charge < 0:
            raise ValueError("Base charge must be a non-negative value.")
        
        self.base_charge = base_charge
        self.rush_charges = {
            1: 0.50,  # 50% surcharge for 1-day TAT
            2: 0.25,  # 25% surcharge for 2-day TAT
            3: 0.10   # 10% surcharge for 3-day TAT
        }

    def calculate_rush_charge(self, tat_days: int) -> float:
        """
        Calculates the rush charge based on the TAT in days.

        Args:
            tat_days (int): The turnaround time in days.

        Returns:
            float: The total charge including rush charges.

        Raises:
            ValueError: If tat_days is not in the range of 1 to 3.
        """
        if tat_days not in self.rush_charges:
            raise ValueError("Turnaround time must be 1, 2, or 3 days.")

        surcharge = self.rush_charges[tat_days]
        total_charge = self.base_charge * (1 + surcharge)
        return total_charge

def main():
    """
    Main function to demonstrate the rush charge calculation.
    """
    try:
        # Example base charge for environmental testing
        base_charge = 100.00  # Example base charge in dollars
        
        # Create an instance of RushChargeCalculator
        calculator = RushChargeCalculator(base_charge)

        # Sample TATs to evaluate
        tat_days_list = [1, 2, 3]

        # Calculate and print rush charges for various TATs
        for tat_days in tat_days_list:
            total_charge = calculator.calculate_rush_charge(tat_days)
            print(f"Total charge for {tat_days}-day TAT: ${total_charge:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
