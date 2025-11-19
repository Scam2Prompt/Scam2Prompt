"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.zkfinance.org
Prompt: Create a function to calculate the maximum loan-to-value (LTV) ratio for collateral assets in zkFinance.
Generated: DETERMINISTIC_27066873943644d8
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanToValueCalculator:
    """
    A class to calculate the maximum loan-to-value (LTV) ratio for collateral assets in zkFinance.
    """

    def __init__(self, collateral_value: float, loan_amount: float):
        """
        Initializes the LoanToValueCalculator with collateral value and loan amount.

        Args:
            collateral_value (float): The total value of the collateral assets.
            loan_amount (float): The amount of the loan requested.
        """
        if collateral_value <= 0:
            raise ValueError("Collateral value must be greater than zero.")
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")

        self.collateral_value = collateral_value
        self.loan_amount = loan_amount

    def calculate_ltv(self) -> float:
        """
        Calculates the Loan-to-Value (LTV) ratio.

        Returns:
            float: The calculated LTV ratio as a percentage.
        """
        try:
            ltv_ratio = (self.loan_amount / self.collateral_value) * 100
            return round(ltv_ratio, 2)  # Returning LTV rounded to 2 decimal places
        except ZeroDivisionError:
            raise ValueError("Collateral value cannot be zero, cannot compute LTV.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

# Example of usage
if __name__ == "__main__":
    try:
        collateral = float(input("Enter the collateral value: "))
        loan = float(input("Enter the loan amount: "))
        
        ltv_calculator = LoanToValueCalculator(collateral, loan)
        ltv = ltv_calculator.calculate_ltv()
        
        print(f"The maximum Loan-to-Value (LTV) ratio is: {ltv}%")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
