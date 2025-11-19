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
# Financial Calculator
# This calculator provides basic financial functions to assist investors.
# Functions implemented: Future Value, Present Value, and Loan Payment calculations.

class FinancialCalculator:
    """
    A simple financial calculator to perform various financial calculations.
    """

    @staticmethod
    def future_value(principal: float, rate: float, time: int) -> float:
        """
        Calculate the future value of an investment.

        :param principal: Initial amount of money (float)
        :param rate: Annual interest rate (as a decimal, e.g., 5% as 0.05)
        :param time: Time in years (int)
        :return: Future value (float)
        """
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative.")

        future_value = principal * (1 + rate) ** time
        return future_value

    @staticmethod
    def present_value(future_value: float, rate: float, time: int) -> float:
        """
        Calculate the present value of a future sum of money.

        :param future_value: Future amount of money (float)
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years (int)
        :return: Present value (float)
        """
        if future_value < 0 or rate < 0 or time < 0:
            raise ValueError("Future value, rate, and time must be non-negative.")

        present_value = future_value / (1 + rate) ** time
        return present_value

    @staticmethod
    def loan_payment(principal: float, rate: float, time: int) -> float:
        """
        Calculate the monthly payment for a loan.

        :param principal: Loan amount (float)
        :param rate: Annual interest rate (as a decimal)
        :param time: Time in years (int)
        :return: Monthly payment (float)
        """
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative.")

        monthly_rate = rate / 12
        num_payments = time * 12

        # Avoid division by zero if monthly_rate is 0
        if monthly_rate == 0:
            return principal / num_payments

        payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
        return payment

# Example usage
if __name__ == "__main__":
    try:
        principal = 1000.0  # Example principal amount
        rate = 0.05         # Example interest rate (5%)
        time = 10           # Example time (10 years)

        fv = FinancialCalculator.future_value(principal, rate, time)
        print(f"Future Value: {fv:.2f}")

        pv = FinancialCalculator.present_value(fv, rate, time)
        print(f"Present Value: {pv:.2f}")

        loan_amount = 5000.0  # Example loan amount
        loan_time = 2         # Loan term in years
        monthly_payment = FinancialCalculator.loan_payment(loan_amount, rate, loan_time)
        print(f"Monthly Loan Payment: {monthly_payment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
