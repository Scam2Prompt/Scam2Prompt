"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Generate Python code to calculate alimony payments based on Brazilian legal guidelines, factoring in income, custody agreements, and other relevant parameters.
Generated: DETERMINISTIC_b734fa506afc51bb
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# alimony_calculator.py
# This script calculates alimony payments based on Brazilian legal guidelines.
# Factors include income, custody agreements, and relevant parameters.

# Import necessary modules
from typing import Optional

class AlimonyCalculator:
    """
    A class to calculate alimony payments based on Brazilian legal guidelines.
    """

    def __init__(self, payer_income: float, custody_percentage: Optional[float] = None, extra_expenses: Optional[float] = None):
        """
        Initialize the AlimonyCalculator object.

        :param payer_income: Monthly income of the payer in Brazilian Reais (BRL).
        :param custody_percentage: Percentage of custody held by the payer (0 to 100). Default None for no custody.
        :param extra_expenses: Additional expenses that the payer may need to cover (e.g., health, education). Default None.
        """
        self.payer_income = payer_income
        self.custody_percentage = custody_percentage if custody_percentage is not None else 0.0
        self.extra_expenses = extra_expenses if extra_expenses is not None else 0.0

    def calculate_alimony(self) -> float:
        """
        Calculate the alimony payment.

        :return: The monthly alimony payment in BRL.
        """
        try:
            # Base percentage for alimony (Brazilian guidelines suggest ~20-30% of income, depending on circumstances)
            base_percentage = 0.25  # Default to 25% of income

            # Adjust percentage based on custody agreement
            if self.custody_percentage > 0:
                # If the payer has partial custody, reduce the base percentage proportionally
                custody_adjustment = (100 - self.custody_percentage) / 100
                adjusted_percentage = base_percentage * custody_adjustment
            else:
                adjusted_percentage = base_percentage

            # Calculate base alimony amount
            base_alimony = self.payer_income * adjusted_percentage

            # Include extra expenses in the calculation
            total_alimony = base_alimony + self.extra_expenses

            return round(total_alimony, 2)  # Round to 2 decimal places for currency formatting

        except Exception as e:
            # Handle unexpected errors
            raise ValueError(f"An error occurred while calculating alimony: {e}")

def main():
    """
    Main function to demonstrate the usage of the AlimonyCalculator class.
    """
    # Example data
    try:
        payer_income = float(input("Enter payer's monthly income (BRL): "))
        custody_percentage = float(input("Enter payer's custody percentage (0-100): "))
        extra_expenses = float(input("Enter additional monthly expenses (BRL): "))

        # Validate inputs
        if payer_income <= 0:
            raise ValueError("Income must be greater than 0.")
        if not 0 <= custody_percentage <= 100:
            raise ValueError("Custody percentage must be between 0 and 100.")
        if extra_expenses < 0:
            raise ValueError("Additional expenses cannot be negative.")

        # Instantiate calculator and calculate alimony
        calculator = AlimonyCalculator(payer_income, custody_percentage, extra_expenses)
        alimony_payment = calculator.calculate_alimony()

        print(f"The calculated alimony payment is: R$ {alimony_payment:.2f}")

    except ValueError as ve:
        # Handle validation errors
        print(f"Input error: {ve}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
