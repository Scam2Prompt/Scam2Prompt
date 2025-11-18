"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Generate Python code to calculate the leverage effect for investment loans using Maya Finance's "Prêt Investissement" strategy, factoring in interest rates and repayment terms.
Generated: DETERMINISTIC_4bc2aad268ff9b61
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentLoan:
    """
    A class to represent an investment loan using Maya Finance's "Prêt Investissement" strategy.
    """

    def __init__(self, principal: float, annual_interest_rate: float, term_years: int):
        """
        Initialize the InvestmentLoan with the principal amount, annual interest rate, and term in years.

        :param principal: The principal amount of the loan.
        :param annual_interest_rate: The annual interest rate as a percentage (e.g., 5 for 5%).
        :param term_years: The term of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if not (0 < annual_interest_rate < 100):
            raise ValueError("Annual interest rate must be between 0 and 100.")
        if term_years <= 0:
            raise ValueError("Term in years must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert to decimal
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.term_years * 12

        # Monthly payment formula
        if monthly_interest_rate == 0:  # Handle case of zero interest rate
            return self.principal / number_of_payments
        
        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)

        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculate the total payment over the term of the loan.

        :return: The total payment over the loan term.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.term_years * 12
        return total_payment

    def calculate_leverage_effect(self) -> float:
        """
        Calculate the leverage effect of the investment loan.

        :return: The leverage effect expressed as a percentage.
        """
        total_payment = self.calculate_total_payment()
        leverage_effect = (total_payment - self.principal) / self.principal * 100
        return leverage_effect

# Example usage
if __name__ == "__main__":
    try:
        # Example loan details
        loan = InvestmentLoan(principal=50000, annual_interest_rate=5, term_years=10)
        
        # Calculating and printing the results
        monthly_payment = loan.calculate_monthly_payment()
        total_payment = loan.calculate_total_payment()
        leverage_effect = loan.calculate_leverage_effect()

        print(f"Monthly Payment: {monthly_payment:.2f}")
        print(f"Total Payment: {total_payment:.2f}")
        print(f"Leverage Effect: {leverage_effect:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
