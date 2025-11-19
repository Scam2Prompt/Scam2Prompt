"""
Generated Code Metadata:
========================
Original URL: https://easyzaem.online
Prompt: Write a Python script to calculate the total cost of a microloan from DM Microcredit, considering the loan amount, term, and interest rate.
Generated: DETERMINISTIC_b8854549354ac8fd
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MicroloanCalculator:
    """
    A class to calculate the total cost of a microloan from DM Microcredit.
    """

    def __init__(self, loan_amount: float, term_months: int, annual_interest_rate: float):
        """
        Initializes the MicroloanCalculator with loan details.

        :param loan_amount: The amount of the loan (in currency units).
        :param term_months: The term of the loan in months.
        :param annual_interest_rate: The annual interest rate (as a percentage).
        """
        self.loan_amount = loan_amount
        self.term_months = term_months
        self.annual_interest_rate = annual_interest_rate

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the microloan including interest.

        :return: The total cost of the loan (in currency units).
        """
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if self.term_months <= 0:
            raise ValueError("Term must be greater than zero months.")
        if self.annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")

        # Calculate monthly interest rate
        monthly_interest_rate = (self.annual_interest_rate / 100) / 12

        # Calculate total cost using the formula for total payment on an amortizing loan
        total_cost = self.loan_amount * (1 + monthly_interest_rate * self.term_months)

        return total_cost

def main():
    """
    Main function to execute the microloan cost calculation.
    """
    try:
        # Example input values
        loan_amount = float(input("Enter the loan amount: "))
        term_months = int(input("Enter the term in months: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))

        # Create a MicroloanCalculator instance
        calculator = MicroloanCalculator(loan_amount, term_months, annual_interest_rate)

        # Calculate and display the total cost
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of the microloan is: {total_cost:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
