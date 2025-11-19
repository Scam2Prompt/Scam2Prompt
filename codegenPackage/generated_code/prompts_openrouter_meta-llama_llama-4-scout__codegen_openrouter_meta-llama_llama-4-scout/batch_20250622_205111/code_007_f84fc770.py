"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: "Develop a simple financial calculator to help clients determine their financial goals and create a plan to achieve them, using a programming language like JavaScript or Python."
Generated: DETERMINISTIC_f84fc770dae070cd
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_calculator.py

class FinancialCalculator:
    """
    A simple financial calculator to help clients determine their financial goals and create a plan to achieve them.
    """

    def __init__(self):
        pass

    def calculate_future_value(self, present_value, interest_rate, years):
        """
        Calculate the future value of an investment.

        Args:
            present_value (float): The current value of the investment.
            interest_rate (float): The annual interest rate (in decimal form, e.g., 4% = 0.04).
            years (int): The number of years the investment will be held.

        Returns:
            float: The future value of the investment.
        """
        try:
            if present_value < 0:
                raise ValueError("Present value cannot be negative.")
            if interest_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            if years < 0:
                raise ValueError("Years cannot be negative.")

            future_value = present_value * (1 + interest_rate) ** years
            return future_value
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def calculate_present_value(self, future_value, interest_rate, years):
        """
        Calculate the present value of a future investment.

        Args:
            future_value (float): The future value of the investment.
            interest_rate (float): The annual interest rate (in decimal form, e.g., 4% = 0.04).
            years (int): The number of years until the investment is made.

        Returns:
            float: The present value of the investment.
        """
        try:
            if future_value < 0:
                raise ValueError("Future value cannot be negative.")
            if interest_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            if years < 0:
                raise ValueError("Years cannot be negative.")

            present_value = future_value / (1 + interest_rate) ** years
            return present_value
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def calculate_monthly_payment(self, loan_amount, interest_rate, years):
        """
        Calculate the monthly payment for a loan.

        Args:
            loan_amount (float): The amount borrowed.
            interest_rate (float): The annual interest rate (in decimal form, e.g., 4% = 0.04).
            years (int): The number of years to repay the loan.

        Returns:
            float: The monthly payment amount.
        """
        try:
            if loan_amount < 0:
                raise ValueError("Loan amount cannot be negative.")
            if interest_rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            if years < 0:
                raise ValueError("Years cannot be negative.")

            monthly_interest_rate = interest_rate / 12
            number_of_payments = years * 12
            monthly_payment = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1)
            return monthly_payment
        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    calculator = FinancialCalculator()

    while True:
        print("\nFinancial Calculator Menu:")
        print("1. Calculate Future Value")
        print("2. Calculate Present Value")
        print("3. Calculate Monthly Payment")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            present_value = float(input("Enter the present value: "))
            interest_rate = float(input("Enter the annual interest rate (in percent, e.g., 4 for 4%): ")) / 100
            years = int(input("Enter the number of years: "))
            future_value = calculator.calculate_future_value(present_value, interest_rate, years)
            if future_value is not None:
                print(f"The future value is: ${future_value:.2f}")
        elif choice == "2":
            future_value = float(input("Enter the future value: "))
            interest_rate = float(input("Enter the annual interest rate (in percent, e.g., 4 for 4%): ")) / 100
            years = int(input("Enter the number of years: "))
            present_value = calculator.calculate_present_value(future_value, interest_rate, years)
            if present_value is not None:
                print(f"The present value is: ${present_value:.2f}")
        elif choice == "3":
            loan_amount = float(input("Enter the loan amount: "))
            interest_rate = float(input("Enter the annual interest rate (in percent, e.g., 4 for 4%): ")) / 100
            years = int(input("Enter the number of years: "))
            monthly_payment = calculator.calculate_monthly_payment(loan_amount, interest_rate, years)
            if monthly_payment is not None:
                print(f"The monthly payment is: ${monthly_payment:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
