"""
Generated Code Metadata:
========================
Original URL: https://maya-finance.com
Prompt: Generate Python code to calculate the leverage effect for investment loans using Maya Finance's "Prêt Investissement" strategy, factoring in interest rates and repayment terms.
Generated: DETERMINISTIC_4bc2aad268ff9b61
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentLoan:
    """
    A class to represent an investment loan and calculate the leverage effect
    using Maya Finance's "Prêt Investissement" strategy.
    """

    def __init__(self, principal: float, interest_rate: float, term_years: int):
        """
        Initializes the InvestmentLoan instance.

        :param principal: The total amount of the loan.
        :param interest_rate: The annual interest rate (as a decimal).
        :param term_years: The duration of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if not (0 < interest_rate < 1):
            raise ValueError("Interest rate must be between 0 and 1.")
        if term_years <= 0:
            raise ValueError("Term in years must be greater than zero.")

        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an annuity.

        :return: The monthly payment amount.
        """
        monthly_rate = self.interest_rate / 12
        number_of_payments = self.term_years * 12

        # Monthly payment formula
        monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.term_years * 12
        return total_payment

    def calculate_leverage_effect(self) -> float:
        """
        Calculates the leverage effect of the investment loan.

        :return: The leverage effect as a percentage.
        """
        total_payment = self.calculate_total_payment()
        leverage_effect = (total_payment - self.principal) / self.principal * 100
        return leverage_effect

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the investment loan with example values
        loan = InvestmentLoan(principal=100000, interest_rate=0.05, term_years=15)

        # Calculate and print the monthly payment
        monthly_payment = loan.calculate_monthly_payment()
        print(f"Monthly Payment: {monthly_payment:.2f}")

        # Calculate and print the total payment
        total_payment = loan.calculate_total_payment()
        print(f"Total Payment: {total_payment:.2f}")

        # Calculate and print the leverage effect
        leverage_effect = loan.calculate_leverage_effect()
        print(f"Leverage Effect: {leverage_effect:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
```
