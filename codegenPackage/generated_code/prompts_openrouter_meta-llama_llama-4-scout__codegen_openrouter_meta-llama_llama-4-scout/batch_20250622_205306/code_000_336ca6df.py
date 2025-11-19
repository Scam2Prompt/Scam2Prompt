"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: "Write a Python script to calculate loan eligibility for a motorcycle loan from Next Money, considering factors like income and loan term."
Generated: DETERMINISTIC_336ca6df3328fd65
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MotorcycleLoanEligibilityCalculator:
    def __init__(self, income, loan_term, loan_amount, interest_rate=0.06):
        """
        Initialize the calculator with user's income, loan term, loan amount, and interest rate.

        Args:
            income (float): The user's monthly income.
            loan_term (int): The loan term in years.
            loan_amount (float): The loan amount.
            interest_rate (float, optional): The annual interest rate. Defaults to 0.06.
        """
        self.income = income
        self.loan_term = loan_term
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def calculate_loan_eligibility(self):
        """
        Calculate the loan eligibility based on the user's income and loan term.

        Returns:
            bool: True if the user is eligible for the loan, False otherwise.
        """
        try:
            # Calculate the monthly interest rate
            monthly_interest_rate = self.interest_rate / 12

            # Calculate the number of monthly payments
            num_payments = self.loan_term * 12

            # Calculate the monthly payment
            monthly_payment = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments / ((1 + monthly_interest_rate) ** num_payments - 1)

            # Check if the user's income can afford the monthly payment
            if monthly_payment <= 0.3 * self.income:
                return True
            else:
                return False

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    def get_loan_details(self):
        """
        Get the loan details.

        Returns:
            dict: A dictionary containing the loan details.
        """
        try:
            # Calculate the monthly interest rate
            monthly_interest_rate = self.interest_rate / 12

            # Calculate the number of monthly payments
            num_payments = self.loan_term * 12

            # Calculate the monthly payment
            monthly_payment = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments / ((1 + monthly_interest_rate) ** num_payments - 1)

            # Calculate the total interest paid
            total_interest_paid = monthly_payment * num_payments - self.loan_amount

            # Return the loan details
            return {
                "loan_amount": self.loan_amount,
                "loan_term": self.loan_term,
                "interest_rate": self.interest_rate,
                "monthly_payment": round(monthly_payment, 2),
                "total_interest_paid": round(total_interest_paid, 2)
            }

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return {}

def main():
    # Get user input
    income = float(input("Enter your monthly income: "))
    loan_term = int(input("Enter the loan term in years: "))
    loan_amount = float(input("Enter the loan amount: "))

    # Create a calculator instance
    calculator = MotorcycleLoanEligibilityCalculator(income, loan_term, loan_amount)

    # Calculate loan eligibility
    eligible = calculator.calculate_loan_eligibility()

    # Print loan eligibility
    if eligible:
        logging.info("You are eligible for the motorcycle loan.")
        loan_details = calculator.get_loan_details()
        logging.info("Loan Details:")
        for key, value in loan_details.items():
            logging.info(f"{key.capitalize().replace('_', ' ')}: {value}")
    else:
        logging.info("You are not eligible for the motorcycle loan.")

if __name__ == "__main__":
    main()
```
