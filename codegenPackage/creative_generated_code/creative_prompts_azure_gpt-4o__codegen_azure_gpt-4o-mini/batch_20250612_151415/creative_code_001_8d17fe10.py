"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Create a program that calculates monthly loan EMI based on principal, interest rate, and loan tenure, similar to the EMI Calculator tool provided on the IFSC Finder website.
Generated: DETERMINISTIC_8d17fe10c5447177
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanEMICalculator:
    """
    A class to calculate the Equated Monthly Installment (EMI) for a loan.
    """

    def __init__(self, principal: float, annual_interest_rate: float, tenure_years: int):
        """
        Initializes the LoanEMICalculator with principal, interest rate, and tenure.

        :param principal: Total loan amount (principal)
        :param annual_interest_rate: Annual interest rate (as a percentage)
        :param tenure_years: Loan tenure in years
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if tenure_years <= 0:
            raise ValueError("Tenure must be greater than 0 years.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.tenure_years = tenure_years

    def calculate_emi(self) -> float:
        """
        Calculates the monthly EMI based on the principal, interest rate, and tenure.

        :return: The calculated monthly EMI.
        """
        monthly_interest_rate = self.annual_interest_rate / (12 * 100)  # converting annual rate to monthly and percentage to decimal
        number_of_months = self.tenure_years * 12  # converting years to months

        # Calculating EMI using the formula
        emi = (self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / \
              ((1 + monthly_interest_rate) ** number_of_months - 1)

        return emi

def main():
    """
    Main function to execute the EMI calculator.
    """
    try:
        # Input data for the loan
        principal = float(input("Enter the principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_years = int(input("Enter the loan tenure (in years): "))

        # Create a LoanEMICalculator object
        emi_calculator = LoanEMICalculator(principal, annual_interest_rate, tenure_years)

        # Calculate EMI
        emi = emi_calculator.calculate_emi()

        # Display the result
        print(f"The monthly EMI for the loan is: {emi:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
