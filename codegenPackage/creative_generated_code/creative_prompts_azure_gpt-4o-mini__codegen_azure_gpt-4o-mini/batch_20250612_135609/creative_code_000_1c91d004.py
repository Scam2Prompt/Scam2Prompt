"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextmoney.co.th
Prompt: Write a Python script to calculate the loan amount for a motorcycle title loan based on the information provided by Next Money.
Generated: DETERMINISTIC_1c91d00429332f58
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LoanCalculator:
    """
    A class to calculate the loan amount for a motorcycle title loan.
    """

    def __init__(self, motorcycle_value: float, loan_to_value_ratio: float):
        """
        Initialize the LoanCalculator with motorcycle value and loan-to-value ratio.

        Args:
            motorcycle_value (float): The current value of the motorcycle.
            loan_to_value_ratio (float): The maximum percentage of the motorcycle value that can be loaned.
        """
        if motorcycle_value <= 0:
            raise ValueError("Motorcycle value must be greater than zero.")
        if not (0 < loan_to_value_ratio <= 1):
            raise ValueError("Loan to value ratio must be between 0 and 1.")

        self.motorcycle_value = motorcycle_value
        self.loan_to_value_ratio = loan_to_value_ratio

    def calculate_loan_amount(self) -> float:
        """
        Calculate the loan amount based on the motorcycle value and the loan-to-value ratio.

        Returns:
            float: The maximum loan amount that can be issued.
        """
        loan_amount = self.motorcycle_value * self.loan_to_value_ratio
        return round(loan_amount, 2)


def main():
    """
    The main function to execute the loan calculation.
    """
    try:
        # Input: Motorcycle value
        motorcycle_value = float(input("Enter the current value of the motorcycle: "))
        
        # Input: Loan to value ratio
        loan_to_value_ratio = float(input("Enter the loan-to-value ratio (as a decimal): "))

        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(motorcycle_value, loan_to_value_ratio)

        # Calculate loan amount
        loan_amount = loan_calculator.calculate_loan_amount()
        print(f"The maximum loan amount for the motorcycle is: ${loan_amount}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
