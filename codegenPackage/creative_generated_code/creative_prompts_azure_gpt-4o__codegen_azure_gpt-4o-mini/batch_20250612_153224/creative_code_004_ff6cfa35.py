"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionic-money.web.app
Prompt: Create a Python script to calculate the multiplied Ionic Points earned for borrowing USDC and display the results in a user-friendly format.
Generated: DETERMINISTIC_ff6cfa35fc0d00c0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

class IonicPointsCalculator:
    """A class to calculate Ionic Points for borrowing USDC."""

    def __init__(self, borrowed_amount: float, interest_rate: float, duration: int):
        """
        Initialize the calculator with borrowed amount, interest rate, and duration.

        :param borrowed_amount: Amount of USDC borrowed
        :param interest_rate: Annual interest rate in percentage
        :param duration: Duration of the loan in days
        """
        self.borrowed_amount = borrowed_amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration = duration

    def calculate_ionic_points(self) -> float:
        """
        Calculate the Ionic Points based on borrowed amount, interest rate, and duration.

        :return: Calculated Ionic Points
        """
        if self.borrowed_amount <= 0 or self.interest_rate < 0 or self.duration <= 0:
            raise ValueError("Borrowed amount, interest rate, and duration must be positive.")

        # Simple Interest Calculation
        interest_earned = self.borrowed_amount * self.interest_rate * (self.duration / 365)
        ionic_points = interest_earned * 0.1  # Assuming 10% of interest earned becomes Ionic Points
        return ionic_points

    def display_results(self):
        """Display the results in a user-friendly format."""
        try:
            ionic_points = self.calculate_ionic_points()
            print(f"Borrowed Amount: ${self.borrowed_amount:.2f} USDC")
            print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
            print(f"Duration: {self.duration} days")
            print(f"Calculated Ionic Points Earned: {ionic_points:.2f} points")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """Main function to execute the Ionic Points Calculator."""
    try:
        # Input: borrowed amount, interest rate, and duration
        borrowed_amount = float(input("Enter the borrowed amount in USDC: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        duration = int(input("Enter the duration of the loan in days: "))

        # Create an instance of the IonicPointsCalculator
        calculator = IonicPointsCalculator(borrowed_amount, interest_rate, duration)

        # Display results
        calculator.display_results()
    except ValueError:
        print("Invalid input. Please enter numeric values for borrowed amount, interest rate, and duration.")

if __name__ == "__main__":
    main()
```
