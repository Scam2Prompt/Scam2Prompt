"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Write Python code to simulate a legal advisory system that structures lending transactions in both local currency and foreign denominations, as described in Ramdays' advisory services.
Generated: DETERMINISTIC_ff3cbd7c3fbb2ce0
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class LoanTransaction:
    """
    A class to simulate a lending transaction in both local and foreign currencies.
    """

    def __init__(self, borrower_name, loan_amount, currency, interest_rate, loan_duration):
        """
        Initialize a LoanTransaction object.

        :param borrower_name: Name of the borrower (string)
        :param loan_amount: Amount of loan (float)
        :param currency: Currency type (string, e.g., "USD", "INR")
        :param interest_rate: Annual interest rate in percentage (float, e.g., 5.0 for 5%)
        :param loan_duration: Loan duration in months (integer)
        """
        self.borrower_name = borrower_name
        self.loan_amount = loan_amount
        self.currency = currency
        self.interest_rate = interest_rate
        self.loan_duration = loan_duration
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=loan_duration * 30)
        self.is_local_currency = self.currency.upper() == "INR"

    def calculate_total_repayment(self):
        """
        Calculate the total repayment amount including interest.

        :return: Total repayment amount (float)
        """
        try:
            # Simple interest formula: Total = Principal + (Principal * Rate * Time)
            total_interest = (self.loan_amount * (self.interest_rate / 100) * (self.loan_duration / 12))
            total_repayment = self.loan_amount + total_interest
            return round(total_repayment, 2)
        except Exception as e:
            raise ValueError(f"Error while calculating repayment: {e}")

    def transaction_summary(self):
        """
        Generate a summary of the lending transaction.

        :return: Summary dictionary
        """
        try:
            summary = {
                "Borrower Name": self.borrower_name,
                "Loan Amount": f"{self.loan_amount} {self.currency}",
                "Interest Rate": f"{self.interest_rate}%",
                "Loan Duration": f"{self.loan_duration} months",
                "Start Date": self.start_date.strftime("%Y-%m-%d"),
                "End Date": self.end_date.strftime("%Y-%m-%d"),
                "Total Repayment": f"{self.calculate_total_repayment()} {self.currency}",
                "Local Currency Transaction": self.is_local_currency,
            }
            return summary
        except Exception as e:
            raise ValueError(f"Error generating transaction summary: {e}")


def simulate_loan_advisory():
    """
    Main function to simulate loan advisory system and interact with the user.
    """
    print("Welcome to Ramdays' Legal Advisory Lending System!")
    try:
        # Gather input from the user
        borrower_name = input("Enter the borrower's name: ").strip()
        loan_amount = float(input("Enter the loan amount: "))
        currency = input("Enter the currency type (e.g., USD, INR): ").strip().upper()
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_duration = int(input("Enter the loan duration (in months): "))

        # Create a loan transaction object
        transaction = LoanTransaction(borrower_name, loan_amount, currency, interest_rate, loan_duration)

        # Generate and display transaction summary
        summary = transaction.transaction_summary()
        print("\nTransaction Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    simulate_loan_advisory()
```
