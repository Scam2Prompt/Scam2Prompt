"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Write a Python script to simulate a mortgage loan using the parameters provided by Crédit Agricole's "Simulation Prêt Immobilier" tool.
Generated: DETERMINISTIC_2d8734317344fb88
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MortgageLoan:
    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the MortgageLoan instance with principal, annual interest rate, and duration in years.

        :param principal: Total amount of the loan
        :param annual_rate: Annual interest rate as a percentage (e.g., 3.5 for 3.5%)
        :param years: Duration of the loan in years
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_rate <= 0:
            raise ValueError("Annual interest rate must be greater than zero.")
        if years <= 0:
            raise ValueError("Loan duration must be greater than zero.")

        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years
        self.monthly_rate = self.annual_rate / 12  # Monthly interest rate

    def monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: Monthly payment amount
        """
        num_payments = self.years * 12
        if self.monthly_rate == 0:
            return self.principal / num_payments
        
        payment = (self.principal * self.monthly_rate) / (1 - (1 + self.monthly_rate) ** -num_payments)
        return payment

    def total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: Total payment amount
        """
        return self.monthly_payment() * self.years * 12

    def total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        :return: Total interest amount
        """
        return self.total_payment() - self.principal

def main():
    """
    Main function to execute the mortgage loan simulation.
    """
    try:
        principal = float(input("Enter the loan amount (principal): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years for the loan: "))

        # Create a MortgageLoan instance
        loan = MortgageLoan(principal, annual_rate, years)

        # Calculate and display the results
        print(f"\nMonthly Payment: {loan.monthly_payment():.2f}")
        print(f"Total Payment over {years} years: {loan.total_payment():.2f}")
        print(f"Total Interest Paid: {loan.total_interest():.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
