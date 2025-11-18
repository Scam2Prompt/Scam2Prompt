"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Recommend a Python library or framework to implement an EMI calculator for Jiomart Digital's financing options, and write a sample function for calculating monthly payments.
Generated: DETERMINISTIC_d268e3438d92f470
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class EMICalculator:
    """
    A class to calculate the Equated Monthly Installment (EMI) 
    for loans based on principal, interest rate, and loan tenure.
    """

    def __init__(self, principal: float, annual_interest_rate: float, tenure_months: int):
        """
        Initializes the EMI Calculator with principal, annual interest rate, and loan tenure.

        :param principal: The total loan amount (principal).
        :param annual_interest_rate: The annual interest rate (in percentage).
        :param tenure_months: The loan tenure in months.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be greater than zero.")
        if tenure_months <= 0:
            raise ValueError("Tenure must be a positive integer.")

        self.principal = principal
        self.monthly_interest_rate = (annual_interest_rate / 100) / 12
        self.tenure_months = tenure_months

    def calculate_emi(self) -> float:
        """
        Calculates the EMI based on the principal, monthly interest rate, and tenure.

        :return: The calculated EMI value.
        """
        # EMI formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        numerator = self.principal * self.monthly_interest_rate * math.pow(1 + self.monthly_interest_rate, self.tenure_months)
        denominator = math.pow(1 + self.monthly_interest_rate, self.tenure_months) - 1

        if denominator == 0:
            raise ValueError("Denominator in EMI calculation cannot be zero.")

        emi = numerator / denominator
        return emi

if __name__ == "__main__":
    # Example usage of the EMICalculator
    try:
        principal = 500000  # Loan amount
        annual_interest_rate = 12  # Annual interest rate in percentage
        tenure_months = 60  # Tenure in months

        emi_calculator = EMICalculator(principal, annual_interest_rate, tenure_months)
        emi = emi_calculator.calculate_emi()
        print(f"The calculated EMI is: {emi:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
