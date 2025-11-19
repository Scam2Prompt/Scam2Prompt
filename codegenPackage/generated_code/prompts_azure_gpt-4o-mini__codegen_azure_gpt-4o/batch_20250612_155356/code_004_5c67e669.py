"""
Generated Code Metadata:
========================
Original URL: https://cma.or.ke
Prompt: Illustrate how to implement a financial calculator using the guidelines provided by the Capital Markets Authority for investor education.
Generated: DETERMINISTIC_5c67e66985782de9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Calculator for Investor Education
This script implements a financial calculator based on guidelines provided by the Capital Markets Authority.
It includes functionality for calculating compound interest, future value of investments, and loan repayment schedules.
"""

import math

class FinancialCalculator:
    """
    A class to perform various financial calculations.
    """

    @staticmethod
    def calculate_compound_interest(principal, rate, time, compounding_frequency=1):
        """
        Calculate compound interest.

        Formula: A = P * (1 + r/n)^(n*t)
        Where:
        A = Future value
        P = Principal amount
        r = Annual interest rate (decimal)
        n = Compounding frequency per year
        t = Time in years

        :param principal: Initial amount of money (float)
        :param rate: Annual interest rate in percentage (float)
        :param time: Time in years (float)
        :param compounding_frequency: Number of times interest is compounded per year (int, default=1)
        :return: Future value after interest (float)
        """
        try:
            # Convert rate from percentage to decimal
            rate_decimal = rate / 100
            # Calculate future value
            future_value = principal * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * time)
            return round(future_value, 2)
        except Exception as e:
            raise ValueError(f"Error calculating compound interest: {e}")

    @staticmethod
    def calculate_future_value(principal, rate, time):
        """
        Calculate future value of an investment with simple interest.

        Formula: FV = P * (1 + r * t)
        Where:
        FV = Future value
        P = Principal amount
        r = Annual interest rate (decimal)
        t = Time in years

        :param principal: Initial amount of money (float)
        :param rate: Annual interest rate in percentage (float)
        :param time: Time in years (float)
        :return: Future value (float)
        """
        try:
            # Convert rate from percentage to decimal
            rate_decimal = rate / 100
            # Calculate future value
            future_value = principal * (1 + rate_decimal * time)
            return round(future_value, 2)
        except Exception as e:
            raise ValueError(f"Error calculating future value: {e}")

    @staticmethod
    def calculate_loan_repayment(principal, annual_rate, years):
        """
        Calculate monthly loan repayment amount.

        Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        Where:
        M = Monthly payment
        P = Loan principal
        r = Monthly interest rate (decimal)
        n = Total number of payments (months)

        :param principal: Loan amount (float)
        :param annual_rate: Annual interest rate in percentage (float)
        :param years: Loan term in years (int)
        :return: Monthly repayment amount (float)
        """
        try:
            # Convert annual rate to monthly rate (decimal)
            monthly_rate = (annual_rate / 100) / 12
            # Total number of payments
            total_payments = years * 12
            # Calculate monthly payment
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / \
                              ((1 + monthly_rate) ** total_payments - 1)
            return round(monthly_payment, 2)
        except Exception as e:
            raise ValueError(f"Error calculating loan repayment: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Compound Interest Example
        principal = 10000  # Initial investment
        rate = 5  # Annual interest rate in percentage
        time = 10  # Time in years
        compounding_frequency = 4  # Quarterly compounding
        compound_interest = FinancialCalculator.calculate_compound_interest(principal, rate, time, compounding_frequency)
        print(f"Compound Interest Future Value: ${compound_interest}")

        # Future Value Example
        future_value = FinancialCalculator.calculate_future_value(principal, rate, time)
        print(f"Future Value with Simple Interest: ${future_value}")

        # Loan Repayment Example
        loan_principal = 50000  # Loan amount
        annual_rate = 7  # Annual interest rate in percentage
        loan_years = 15  # Loan term in years
        monthly_payment = FinancialCalculator.calculate_loan_repayment(loan_principal, annual_rate, loan_years)
        print(f"Monthly Loan Repayment: ${monthly_payment}")

    except ValueError as e:
        print(e)
```
