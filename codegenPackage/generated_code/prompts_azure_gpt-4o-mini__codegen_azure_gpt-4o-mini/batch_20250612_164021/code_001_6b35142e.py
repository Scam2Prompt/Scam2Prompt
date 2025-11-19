"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Write a Python script that calculates loan eligibility based on the criteria provided by Genesis Investment Credit Union for personal and business loans.
Generated: DETERMINISTIC_6b35142ee90e55c3
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoanEligibilityCalculator:
    """
    A class to calculate loan eligibility based on specific criteria for personal and business loans.
    """

    def __init__(self, income, credit_score, existing_debts, loan_amount, loan_type):
        """
        Initializes the LoanEligibilityCalculator with the necessary parameters.

        :param income: Monthly income of the applicant
        :param credit_score: Credit score of the applicant
        :param existing_debts: Total existing monthly debts of the applicant
        :param loan_amount: Desired loan amount
        :param loan_type: Type of loan ('personal' or 'business')
        """
        self.income = income
        self.credit_score = credit_score
        self.existing_debts = existing_debts
        self.loan_amount = loan_amount
        self.loan_type = loan_type

    def calculate_debt_to_income_ratio(self):
        """
        Calculates the debt-to-income ratio.

        :return: Debt-to-income ratio as a percentage
        """
        try:
            dti_ratio = (self.existing_debts / self.income) * 100
            return dti_ratio
        except ZeroDivisionError:
            raise ValueError("Income cannot be zero when calculating DTI ratio.")

    def is_credit_score_acceptable(self):
        """
        Checks if the credit score meets the minimum requirement.

        :return: True if credit score is acceptable, False otherwise
        """
        return self.credit_score >= 650  # Minimum acceptable credit score

    def is_loan_amount_acceptable(self):
        """
        Checks if the loan amount is within acceptable limits based on income.

        :return: True if loan amount is acceptable, False otherwise
        """
        max_loan_amount = self.income * 5  # Example: Maximum loan amount is 5 times the monthly income
        return self.loan_amount <= max_loan_amount

    def is_eligible_for_loan(self):
        """
        Determines if the applicant is eligible for a loan based on the criteria.

        :return: Eligibility status as a string
        """
        try:
            dti_ratio = self.calculate_debt_to_income_ratio()
            if dti_ratio > 40:
                return "Not eligible: Debt-to-Income ratio exceeds 40%."
            if not self.is_credit_score_acceptable():
                return "Not eligible: Credit score is below the acceptable threshold."
            if not self.is_loan_amount_acceptable():
                return "Not eligible: Loan amount exceeds acceptable limits."

            return "Eligible for loan."
        except ValueError as e:
            return str(e)

def main():
    """
    Main function to execute the loan eligibility calculation.
    """
    # Example input values
    income = 5000  # Monthly income
    credit_score = 700  # Credit score
    existing_debts = 1500  # Existing monthly debts
    loan_amount = 20000  # Desired loan amount
    loan_type = 'personal'  # Type of loan

    # Create an instance of LoanEligibilityCalculator
    calculator = LoanEligibilityCalculator(income, credit_score, existing_debts, loan_amount, loan_type)

    # Calculate and print loan eligibility
    eligibility_status = calculator.is_eligible_for_loan()
    print(eligibility_status)

if __name__ == "__main__":
    main()
```
