"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-v-dolg.online
Prompt: Write code to calculate loan repayment amounts based on interest rates from 0% to 365% per annum, considering loan terms and sums from 2,000 to 100,000 rubles.
Generated: DETERMINISTIC_5fae08e74077b00c
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_loan_repayment(loan_sum, interest_rate, loan_term):
    """
    Calculate loan repayment amount based on interest rate, loan term, and loan sum.

    Args:
        loan_sum (float): Loan amount in rubles (2,000 to 100,000).
        interest_rate (float): Interest rate per annum (0% to 365%).
        loan_term (int): Loan term in years.

    Returns:
        float: Monthly loan repayment amount.

    Raises:
        ValueError: If loan sum, interest rate, or loan term is out of range.
    """
    if not (2000 <= loan_sum <= 100000):
        raise ValueError("Loan sum must be between 2,000 and 100,000 rubles")
    if not (0 <= interest_rate <= 365):
        raise ValueError("Interest rate must be between 0% and 365% per annum")
    if loan_term <= 0:
        raise ValueError("Loan term must be a positive integer")

    # Convert interest rate from per annum to per month
    monthly_interest_rate = (interest_rate / 100) / 12

    # Calculate monthly repayment amount using the formula for monthly payments (M) on a fixed-rate loan:
    # M = P[r(1+r)^n]/[(1+r)^n – 1]
    # Where:
    #   P = loan sum
    #   r = monthly interest rate
    #   n = number of payments (loan term in years * 12)
    number_of_payments = loan_term * 12
    monthly_repayment = loan_sum * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
            (1 + monthly_interest_rate) ** number_of_payments - 1)

    return round(monthly_repayment, 2)


def main():
    try:
        loan_sum = float(input("Enter loan sum (2,000 to 100,000 rubles): "))
        interest_rate = float(input("Enter interest rate per annum (0% to 365%): "))
        loan_term = int(input("Enter loan term in years: "))

        monthly_repayment = calculate_loan_repayment(loan_sum, interest_rate, loan_term)
        print(f"Monthly loan repayment amount: {monthly_repayment} rubles")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
