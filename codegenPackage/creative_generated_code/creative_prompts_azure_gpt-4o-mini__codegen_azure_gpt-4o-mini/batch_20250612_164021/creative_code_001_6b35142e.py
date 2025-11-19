"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Write a Python script that calculates loan eligibility based on the criteria provided by Genesis Investment Credit Union for personal and business loans.
Generated: DETERMINISTIC_6b35142ee90e55c3
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# loan_eligibility.py

class LoanEligibility:
    """
    A class to calculate loan eligibility for personal and business loans.
    """

    def __init__(self, annual_income, credit_score, existing_debt):
        """
        Initialize the LoanEligibility class with user financial information.

        :param annual_income: float - The user's annual income.
        :param credit_score: int - The user's credit score (0-850).
        :param existing_debt: float - The total existing debt of the user.
        """
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.existing_debt = existing_debt

    def is_eligible_for_personal_loan(self):
        """
        Determine eligibility for a personal loan based on criteria.

        :return: bool - True if eligible, False otherwise.
        """
        try:
            # Eligibility Criteria for Personal Loan
            if self.credit_score < 650:
                return False  # Credit score too low
            if self.annual_income < 30000:
                return False  # Income too low
            if self.existing_debt / self.annual_income > 0.5:
                return False  # Debt-to-income ratio too high
            return True
        except ZeroDivisionError:
            print("Error: Annual income cannot be zero.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def is_eligible_for_business_loan(self):
        """
        Determine eligibility for a business loan based on criteria.

        :return: bool - True if eligible, False otherwise.
        """
        try:
            # Eligibility Criteria for Business Loan
            if self.credit_score < 700:
                return False  # Credit score too low
            if self.annual_income < 50000:
                return False  # Income too low
            if self.existing_debt / self.annual_income > 0.6:
                return False  # Debt-to-income ratio too high
            return True
        except ZeroDivisionError:
            print("Error: Annual income cannot be zero.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


def main():
    """
    Main function to execute loan eligibility checks.
    """
    # User input for financial information
    try:
        annual_income = float(input("Enter your annual income: "))
        credit_score = int(input("Enter your credit score (0-850): "))
        existing_debt = float(input("Enter your existing debt: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Create an instance of LoanEligibility
    loan_eligibility = LoanEligibility(annual_income, credit_score, existing_debt)

    # Check eligibility for personal and business loans
    personal_loan_eligibility = loan_eligibility.is_eligible_for_personal_loan()
    business_loan_eligibility = loan_eligibility.is_eligible_for_business_loan()

    # Displaying results
    print(f"Eligible for Personal Loan: {'Yes' if personal_loan_eligibility else 'No'}")
    print(f"Eligible for Business Loan: {'Yes' if business_loan_eligibility else 'No'}")


if __name__ == "__main__":
    main()
```
