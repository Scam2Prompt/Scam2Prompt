"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: Write a Python script to calculate the loan amount for a motorcycle title loan based on the information provided by Next Money.
Generated: DETERMINISTIC_1c91d00429332f58
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class LoanCalculator:
    """
    A class to calculate the loan amount for a motorcycle title loan.
    """

    def __init__(self, motorcycle_value, loan_to_value_ratio):
        """
        Initializes the LoanCalculator with the motorcycle value and loan-to-value ratio.

        :param motorcycle_value: The current market value of the motorcycle.
        :param loan_to_value_ratio: The maximum loan-to-value ratio (as a decimal).
        """
        self.motorcycle_value = motorcycle_value
        self.loan_to_value_ratio = loan_to_value_ratio

    def calculate_loan_amount(self):
        """
        Calculates the maximum loan amount based on the motorcycle value and loan-to-value ratio.

        :return: The maximum loan amount.
        """
        if self.motorcycle_value < 0 or not (0 <= self.loan_to_value_ratio <= 1):
            raise ValueError("Invalid input: motorcycle value must be non-negative and loan-to-value ratio must be between 0 and 1.")

        loan_amount = self.motorcycle_value * self.loan_to_value_ratio
        return loan_amount


def main():
    """
    Main function to execute the loan calculation based on user input.
    """
    try:
        # User input for motorcycle value and loan-to-value ratio
        motorcycle_value = float(input("Enter the current market value of the motorcycle: "))
        loan_to_value_ratio = float(input("Enter the loan-to-value ratio (as a decimal, e.g., 0.75 for 75%): "))

        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(motorcycle_value, loan_to_value_ratio)

        # Calculate the loan amount
        loan_amount = loan_calculator.calculate_loan_amount()

        # Output the result
        print(f"The maximum loan amount you can receive is: ${loan_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
