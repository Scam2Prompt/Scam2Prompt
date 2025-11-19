"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the expected reduction in fűtési energia (heating energy) loss after installing Rehau emelő-toló erkélyajtó (lift-slide balcony doors).
Generated: DETERMINISTIC_c0192ff71472346b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class HeatingEnergyCalculator:
    """
    A class to calculate the expected reduction in heating energy loss
    after installing Rehau lift-slide balcony doors.
    """

    def __init__(self, current_energy_loss, new_energy_loss):
        """
        Initializes the calculator with current and new energy loss values.

        :param current_energy_loss: Current heating energy loss (in kWh)
        :param new_energy_loss: Expected heating energy loss after installation (in kWh)
        """
        self.current_energy_loss = current_energy_loss
        self.new_energy_loss = new_energy_loss

    def calculate_reduction(self):
        """
        Calculates the expected reduction in heating energy loss.

        :return: Reduction in heating energy loss (in kWh)
        :raises ValueError: If current_energy_loss or new_energy_loss is negative
        """
        if self.current_energy_loss < 0 or self.new_energy_loss < 0:
            raise ValueError("Energy loss values must be non-negative.")

        reduction = self.current_energy_loss - self.new_energy_loss
        return max(reduction, 0)  # Ensure reduction is not negative

    def calculate_percentage_reduction(self):
        """
        Calculates the percentage reduction in heating energy loss.

        :return: Percentage reduction in heating energy loss
        :raises ValueError: If current_energy_loss is zero
        """
        if self.current_energy_loss == 0:
            raise ValueError("Current energy loss cannot be zero for percentage calculation.")

        reduction = self.calculate_reduction()
        percentage_reduction = (reduction / self.current_energy_loss) * 100
        return percentage_reduction

def main():
    """
    Main function to execute the heating energy loss calculation.
    """
    try:
        # Example values for current and new energy loss
        current_energy_loss = float(input("Enter current heating energy loss (kWh): "))
        new_energy_loss = float(input("Enter expected heating energy loss after installation (kWh): "))

        # Create an instance of the calculator
        calculator = HeatingEnergyCalculator(current_energy_loss, new_energy_loss)

        # Calculate reduction and percentage reduction
        reduction = calculator.calculate_reduction()
        percentage_reduction = calculator.calculate_percentage_reduction()

        # Display results
        print(f"Expected reduction in heating energy loss: {reduction:.2f} kWh")
        print(f"Percentage reduction in heating energy loss: {percentage_reduction:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
