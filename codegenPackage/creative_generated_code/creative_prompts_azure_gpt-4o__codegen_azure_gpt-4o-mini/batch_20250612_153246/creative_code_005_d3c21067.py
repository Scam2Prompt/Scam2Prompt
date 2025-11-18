"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Develop a tool in Python to calculate equity loan amounts based on Dominion Lending's guidelines for different property types and borrower scenarios.
Generated: DETERMINISTIC_d3c2106700362ef4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class EquityLoanCalculator:
    """
    A class to calculate equity loan amounts based on property type and borrower scenarios.
    """

    def __init__(self, property_value: float, mortgage_balance: float, loan_to_value_ratio: float):
        """
        Initializes the EquityLoanCalculator with the required parameters.

        :param property_value: The current market value of the property.
        :param mortgage_balance: The outstanding mortgage balance on the property.
        :param loan_to_value_ratio: The allowed loan to value ratio for the equity loan (as a decimal).
        """
        self.property_value = property_value
        self.mortgage_balance = mortgage_balance
        self.loan_to_value_ratio = loan_to_value_ratio

    def calculate_equity(self) -> float:
        """
        Calculate the equity in the property.

        :return: The equity amount as a float.
        """
        equity = self.property_value - self.mortgage_balance
        return equity

    def calculate_max_loan_amount(self) -> float:
        """
        Calculate the maximum equity loan amount based on the property's value and mortgage balance.

        :return: The maximum loan amount as a float.
        """
        try:
            equity = self.calculate_equity()
            max_loan_amount = equity * self.loan_to_value_ratio
            return max_loan_amount
        except Exception as e:
            print(f"Error calculating maximum loan amount: {e}")
            sys.exit(1)

def main():
    """
    Main function to run the equity loan calculator.
    """
    try:
        # Input from user
        property_value = float(input("Enter the current market value of the property: "))
        mortgage_balance = float(input("Enter the outstanding mortgage balance: "))
        loan_to_value_ratio = float(input("Enter the loan to value ratio (as a decimal, e.g., 0.8 for 80%): "))

        # Create an instance of the EquityLoanCalculator
        calculator = EquityLoanCalculator(property_value, mortgage_balance, loan_to_value_ratio)

        # Calculate and display the maximum loan amount
        max_loan_amount = calculator.calculate_max_loan_amount()
        print(f"The maximum equity loan amount you can borrow is: ${max_loan_amount:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
