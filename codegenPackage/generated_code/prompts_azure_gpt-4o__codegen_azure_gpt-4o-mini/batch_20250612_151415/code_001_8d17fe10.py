"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Create a program that calculates monthly loan EMI based on principal, interest rate, and loan tenure, similar to the EMI Calculator tool provided on the IFSC Finder website.
Generated: DETERMINISTIC_8d17fe10c5447177
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoanEMICalculator:
    """
    A class to calculate the Equated Monthly Installment (EMI) for a loan.

    Attributes:
        principal (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate (in percentage).
        tenure_years (int): The tenure of the loan in years.
    """

    def __init__(self, principal: float, annual_interest_rate: float, tenure_years: int):
        """
        Initializes the LoanEMICalculator with principal, interest rate, and tenure.

        Args:
            principal (float): The principal amount of the loan.
            annual_interest_rate (float): The annual interest rate (in percentage).
            tenure_years (int): The tenure of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if tenure_years <= 0:
            raise ValueError("Tenure must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.tenure_years = tenure_years

    def calculate_emi(self) -> float:
        """
        Calculates the EMI for the loan.

        Returns:
            float: The calculated EMI amount.
        """
        # Convert annual interest rate to monthly and decimal
        monthly_interest_rate = self.annual_interest_rate / (12 * 100)
        # Total number of monthly payments
        total_payments = self.tenure_years * 12

        # EMI formula
        emi = (self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
              ((1 + monthly_interest_rate) ** total_payments - 1)

        return emi

def main():
    """
    Main function to execute the EMI calculation based on user input.
    """
    try:
        # User input for loan details
        principal = float(input("Enter the principal amount of the loan: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_years = int(input("Enter the tenure of the loan (in years): "))

        # Create an instance of LoanEMICalculator
        emi_calculator = LoanEMICalculator(principal, annual_interest_rate, tenure_years)

        # Calculate and display the EMI
        emi = emi_calculator.calculate_emi()
        print(f"The monthly EMI for the loan is: {emi:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
