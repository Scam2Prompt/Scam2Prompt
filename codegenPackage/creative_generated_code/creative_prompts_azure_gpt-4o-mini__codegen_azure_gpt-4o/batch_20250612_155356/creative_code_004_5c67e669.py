"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cma.or.ke
Prompt: Illustrate how to implement a financial calculator using the guidelines provided by the Capital Markets Authority for investor education.
Generated: DETERMINISTIC_5c67e66985782de9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# financial_calculator.py

import math

class FinancialCalculator:
    """
    A class to implement a financial calculator for investor education.
    Adheres to guidelines provided by the Capital Markets Authority.
    """

    @staticmethod
    def compound_interest(principal: float, rate: float, years: int, compounds_per_year: int = 1) -> float:
        """
        Calculate compound interest.

        Formula: A = P * (1 + r/n)^(n*t)
        
        Args:
            principal (float): Initial investment amount (P).
            rate (float): Annual interest rate in decimal (r).
            years (int): Time in years (t).
            compounds_per_year (int): Number of times interest is compounded per year (n).

        Returns:
            float: Total amount after applying compound interest (A).
        """
        if principal <= 0 or rate < 0 or years < 0 or compounds_per_year <= 0:
            raise ValueError("Invalid input values. Ensure principal > 0, rate >= 0, years >= 0, and compounds_per_year > 0.")
        return principal * math.pow(1 + rate / compounds_per_year, compounds_per_year * years)

    @staticmethod
    def loan_emi(principal: float, annual_rate: float, years: int) -> float:
        """
        Calculate Equated Monthly Installment (EMI) for a loan.

        Formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        
        Args:
            principal (float): Loan amount (P).
            annual_rate (float): Annual interest rate in decimal.
            years (int): Loan tenure in years.

        Returns:
            float: Monthly EMI payment.
        """
        if principal <= 0 or annual_rate < 0 or years <= 0:
            raise ValueError("Invalid input values. Ensure principal > 0, annual_rate >= 0, and years > 0.")
        
        monthly_rate = annual_rate / 12  # Convert annual rate to monthly rate
        months = years * 12  # Convert years to months

        if monthly_rate == 0:  # Handle zero interest rate separately
            return principal / months
        
        numerator = principal * monthly_rate * math.pow(1 + monthly_rate, months)
        denominator = math.pow(1 + monthly_rate, months) - 1
        return numerator / denominator

    @staticmethod
    def future_value(principal: float, rate: float, years: int, periodic_contribution: float = 0) -> float:
        """
        Calculate the future value of an investment with periodic contributions.

        Formula: FV = P * (1 + r)^t + PMT * [((1 + r)^t - 1) / r]
        
        Args:
            principal (float): Initial investment amount (P).
            rate (float): Annual interest rate in decimal (r).
            years (int): Time in years (t).
            periodic_contribution (float): Periodic contributions (PMT).

        Returns:
            float: Future value of the investment (FV).
        """
        if principal < 0 or rate < 0 or years < 0 or periodic_contribution < 0:
            raise ValueError("Invalid input values. Ensure values are non-negative.")
        
        fv_principal = principal * math.pow(1 + rate, years)
        
        if rate == 0:  # Handle zero interest rate separately
            fv_contributions = periodic_contribution * years
        else:
            fv_contributions = periodic_contribution * ((math.pow(1 + rate, years) - 1) / rate)
        
        return fv_principal + fv_contributions

# Example usage
if __name__ == "__main__":
    # Tests for the Financial Calculator
    try:
        principal = 10000
        rate = 0.05
        years = 10
        compounds_per_year = 4

        print("Compound Interest Calculation:")
        print(FinancialCalculator.compound_interest(principal, rate, years, compounds_per_year))

        loan_amount = 500000
        annual_rate = 0.07
        loan_years = 15

        print("\nLoan EMI Calculation:")
        print(FinancialCalculator.loan_emi(loan_amount, annual_rate, loan_years))

        periodic_contribution = 2000

        print("\nFuture Value Calculation:")
        print(FinancialCalculator.future_value(principal, rate, years, periodic_contribution))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```

This code provides a financial calculator with methods for calculating compound interest, loan EMI, and future value. Each method is carefully validated for input and includes error handling for invalid values. Feel free to run the script and test different inputs.
