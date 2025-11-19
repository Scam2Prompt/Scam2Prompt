"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-zanyat.online
Prompt: Compare the interest rates and terms of microloans offered by Lime-zaim, еКапуста, and Срочно Деньги, and write a Python script to calculate the total repayment amount for a 30-day loan of 10,000 rubles from each provider.
Generated: DETERMINISTIC_9d8d4346dbf015cc
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# microloan_comparison.py

class MicroloanProvider:
    def __init__(self, name, interest_rate, term, fee=0):
        """
        Initialize a microloan provider.

        Args:
            name (str): Provider name.
            interest_rate (float): Interest rate as a decimal.
            term (int): Loan term in days.
            fee (float, optional): Additional fee. Defaults to 0.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.term = term
        self.fee = fee

    def calculate_repayment(self, loan_amount):
        """
        Calculate the total repayment amount.

        Args:
            loan_amount (float): Initial loan amount.

        Returns:
            float: Total repayment amount.
        """
        interest = loan_amount * self.interest_rate * (self.term / 365)
        return loan_amount + interest + self.fee


def main():
    # Define microloan providers
    providers = [
        MicroloanProvider("Lime-zaim", 0.365, 30),  # 36.5% interest rate for 30 days
        MicroloanProvider("еКапуста", 0.405, 30),  # 40.5% interest rate for 30 days
        MicroloanProvider("Срочно Деньги", 0.45, 30),  # 45% interest rate for 30 days
    ]

    # Define loan parameters
    loan_amount = 10000  # 10,000 rubles
    loan_term = 30  # 30-day loan

    # Calculate and compare repayment amounts
    print("Microloan Repayment Comparison")
    print("--------------------------------")
    for provider in providers:
        repayment_amount = provider.calculate_repayment(loan_amount)
        print(f"{provider.name}: {repayment_amount:.2f} rubles")

    # Check for errors
    try:
        # Simulate error handling for invalid input
        invalid_loan_amount = -1000
        repayment_amount = providers[0].calculate_repayment(invalid_loan_amount)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
