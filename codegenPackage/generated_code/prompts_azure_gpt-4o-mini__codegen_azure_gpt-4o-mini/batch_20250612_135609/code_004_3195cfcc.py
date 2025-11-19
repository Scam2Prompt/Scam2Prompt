"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: What are the key features to include in a financial application that provides motorcycle title loans, based on Next Money's service descriptions?
Generated: DETERMINISTIC_3195cfcca4cb7ed5
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class MotorcycleTitleLoan:
    """
    A class to represent a motorcycle title loan application.
    """

    def __init__(self, customer_name: str, motorcycle_value: float, loan_amount: float):
        """
        Initializes the MotorcycleTitleLoan instance.

        :param customer_name: Name of the customer applying for the loan
        :param motorcycle_value: Estimated value of the motorcycle
        :param loan_amount: Amount of loan requested
        """
        self.customer_name = customer_name
        self.motorcycle_value = motorcycle_value
        self.loan_amount = loan_amount
        self.approved = False

    def validate_loan(self) -> bool:
        """
        Validates the loan application based on motorcycle value and requested loan amount.

        :return: True if the loan is valid, False otherwise
        """
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        if self.loan_amount > self.motorcycle_value * 0.75:  # Loan should not exceed 75% of motorcycle value
            raise ValueError("Loan amount exceeds 75% of motorcycle value.")
        return True

    def approve_loan(self) -> None:
        """
        Approves the loan if it is valid.

        :raises ValueError: If the loan is not valid
        """
        if self.validate_loan():
            self.approved = True
            print(f"Loan approved for {self.customer_name}.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the loan application to a dictionary format.

        :return: Dictionary representation of the loan application
        """
        return {
            "customer_name": self.customer_name,
            "motorcycle_value": self.motorcycle_value,
            "loan_amount": self.loan_amount,
            "approved": self.approved
        }

def save_loan_application(loan: MotorcycleTitleLoan, filename: str) -> None:
    """
    Saves the loan application to a JSON file.

    :param loan: The MotorcycleTitleLoan instance to save
    :param filename: The name of the file to save the application to
    """
    try:
        with open(filename, 'w') as file:
            json.dump(loan.to_dict(), file)
            print(f"Loan application saved to {filename}.")
    except IOError as e:
        print(f"Error saving loan application: {e}")

def main() -> None:
    """
    Main function to execute the loan application process.
    """
    try:
        # Example data for loan application
        customer_name = "John Doe"
        motorcycle_value = 5000.00
        loan_amount = 3500.00

        # Create a loan application
        loan = MotorcycleTitleLoan(customer_name, motorcycle_value, loan_amount)

        # Approve the loan
        loan.approve_loan()

        # Save the loan application
        save_loan_application(loan, "loan_application.json")

    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
