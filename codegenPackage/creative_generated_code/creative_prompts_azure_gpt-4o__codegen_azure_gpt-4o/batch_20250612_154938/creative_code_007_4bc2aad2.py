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
# Import necessary libraries
import math

def calculate_leverage_effect(investment_amount, loan_amount, interest_rate, repayment_term, annual_growth_rate):
    """
    Calculate the leverage effect for investment loans.

    Parameters:
    investment_amount (float): The initial amount of money invested.
    loan_amount (float): The amount of money borrowed for the investment.
    interest_rate (float): Annual interest rate for the loan (in percentage).
    repayment_term (int): Duration of the loan repayment (in years).
    annual_growth_rate (float): Expected annual growth rate of the investment (in percentage).

    Returns:
    float: Leverage effect value.
    """
    try:
        # Validate input parameters
        if investment_amount <= 0 or loan_amount <= 0 or interest_rate < 0 or repayment_term <= 0 or annual_growth_rate < 0:
            raise ValueError("All numeric inputs must be positive, and interest rates/growth rates must be non-negative.")

        # Calculate annual loan repayment amount
        annual_interest_rate = interest_rate / 100  # Convert percentage to decimal
        annual_growth_rate = annual_growth_rate / 100  # Convert percentage to decimal

        # Formula for annual installment (fixed repayment based on loan term, simple annuity formula)
        # P = (r * L) / (1 - (1 + r)^-n)
        if annual_interest_rate == 0:  # Handle edge case for zero interest
            annual_repayment = loan_amount / repayment_term
        else:
            annual_repayment = (annual_interest_rate * loan_amount) / (1 - math.pow(1 + annual_interest_rate, -repayment_term))

        # Calculate total cost of loan repayment over the term
        total_repayment_cost = annual_repayment * repayment_term

        # Calculate future value of investment after repayment term
        # Future Value = Investment Amount * (1 + Annual Growth Rate)^Repayment Term
        future_investment_value = investment_amount * math.pow(1 + annual_growth_rate, repayment_term)

        # Calculate leverage effect
        leverage_effect = future_investment_value - total_repayment_cost

        return leverage_effect

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # User input
    investment_amount = 50000  # Initial investment amount in currency
    loan_amount = 20000        # Loan amount taken for investment
    interest_rate = 5          # Annual interest rate (percentage)
    repayment_term = 10        # Repayment term (in years)
    annual_growth_rate = 8     # Expected annual growth rate of the investment (percentage)

    leverage_result = calculate_leverage_effect(investment_amount, loan_amount, interest_rate, repayment_term, annual_growth_rate)

    if leverage_result is not None:
        print(f"The leverage effect of your investment loan strategy is: {leverage_result:.2f}")
```
