"""
Generated Code Metadata:
========================
Original URL: https://personalzaym.online
Prompt: Write a Python script to automate the process of applying for a loan from Qanat microfinance organization, considering the eligibility criteria of age (20-65) and loan amount (20,000 - 127,000 KZT).
Generated: DETERMINISTIC_eaffff431d80fc70
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_application.py

class LoanApplication:
    def __init__(self, name, age, loan_amount):
        """
        Initialize a loan application.

        Args:
            name (str): The applicant's name.
            age (int): The applicant's age.
            loan_amount (int): The loan amount in KZT.
        """
        self.name = name
        self.age = age
        self.loan_amount = loan_amount

    def is_eligible(self):
        """
        Check if the applicant is eligible for a loan.

        Returns:
            bool: True if eligible, False otherwise.
        """
        # Eligibility criteria: age between 20 and 65
        if not 20 <= self.age <= 65:
            return False
        
        # Eligibility criteria: loan amount between 20,000 and 127,000 KZT
        if not 20000 <= self.loan_amount <= 127000:
            return False
        
        return True

    def apply_for_loan(self):
        """
        Apply for a loan.

        Returns:
            dict: A dictionary containing the application result.
        """
        if self.is_eligible():
            # Simulate loan application process (e.g., database insertion)
            # For demonstration purposes, assume the application is successful
            return {"status": "approved", "message": f"Loan application for {self.name} approved."}
        else:
            return {"status": "rejected", "message": f"Loan application for {self.name} rejected due to eligibility criteria."}


def main():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        loan_amount = int(input("Enter the loan amount (KZT): "))

        application = LoanApplication(name, age, loan_amount)
        result = application.apply_for_loan()

        print(f"Application Status: {result['status']}")
        print(f"Message: {result['message']}")

    except ValueError:
        print("Error: Invalid input. Please enter a valid age and loan amount.")

if __name__ == "__main__":
    main()
```
