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
"""
This script calculates loan eligibility for personal and business loans based on
Genesis Investment Credit Union's criteria. The user provides input for loan type,
income, loan amount, credit score, and other relevant details. Eligibility is determined
based on predefined thresholds.
"""

def calculate_personal_loan_eligibility(income, loan_amount, credit_score, debt_to_income_ratio):
    """
    Function to calculate eligibility for personal loans.
    :param income: Monthly income of the applicant (float).
    :param loan_amount: Desired loan amount (float).
    :param credit_score: Credit score of the applicant (integer).
    :param debt_to_income_ratio: Current debt-to-income ratio as a percentage (float).
    :return: Eligibility status (boolean) and reason (string).
    """
    # Eligibility criteria
    MIN_CREDIT_SCORE = 650
    MAX_DEBT_TO_INCOME_RATIO = 40.0  # percentage
    MAX_LOAN_TO_INCOME_RATIO = 30.0  # percentage

    # Check credit score
    if credit_score < MIN_CREDIT_SCORE:
        return False, "Credit score below minimum threshold."

    # Check debt-to-income ratio
    if debt_to_income_ratio > MAX_DEBT_TO_INCOME_RATIO:
        return False, "Debt-to-income ratio exceeds allowed limit."

    # Check loan amount relative to income
    if (loan_amount / income) * 100 > MAX_LOAN_TO_INCOME_RATIO:
        return False, "Loan amount exceeds allowed percentage of monthly income."

    return True, "Eligible for a personal loan."


def calculate_business_loan_eligibility(business_revenue, loan_amount, credit_score, years_in_business):
    """
    Function to calculate eligibility for business loans.
    :param business_revenue: Annual revenue of the business (float).
    :param loan_amount: Desired loan amount (float).
    :param credit_score: Credit score of the business or business owner (integer).
    :param years_in_business: Number of years the business has been operational (integer).
    :return: Eligibility status (boolean) and reason (string).
    """
    # Eligibility criteria
    MIN_CREDIT_SCORE = 700
    MIN_YEARS_IN_BUSINESS = 2
    MAX_LOAN_TO_REVENUE_RATIO = 25.0  # percentage

    # Check credit score
    if credit_score < MIN_CREDIT_SCORE:
        return False, "Credit score below minimum threshold."

    # Check years in business
    if years_in_business < MIN_YEARS_IN_BUSINESS:
        return False, "Business has not been operational for the minimum required years."

    # Check loan amount relative to revenue
    if (loan_amount / business_revenue) * 100 > MAX_LOAN_TO_REVENUE_RATIO:
        return False, "Loan amount exceeds allowed percentage of annual revenue."

    return True, "Eligible for a business loan."


def main():
    """
    Main function to execute the loan eligibility calculator.
    """
    print("Welcome to Genesis Investment Credit Union Loan Eligibility Calculator.")
    try:
        # Gather loan type
        loan_type = input("Enter loan type (personal/business): ").strip().lower()

        if loan_type == "personal":
            # Gather personal loan details
            income = float(input("Enter your monthly income: "))
            loan_amount = float(input("Enter the desired loan amount: "))
            credit_score = int(input("Enter your credit score: "))
            debt_to_income_ratio = float(input("Enter your current debt-to-income ratio (%): "))

            # Calculate personal loan eligibility
            eligible, reason = calculate_personal_loan_eligibility(income, loan_amount, credit_score, debt_to_income_ratio)
            print(f"Eligibility Status: {'Eligible' if eligible else 'Not Eligible'}")
            print(f"Reason: {reason}")

        elif loan_type == "business":
            # Gather business loan details
            business_revenue = float(input("Enter your annual business revenue: "))
            loan_amount = float(input("Enter the desired loan amount: "))
            credit_score = int(input("Enter your credit score: "))
            years_in_business = int(input("Enter the number of years your business has been operational: "))

            # Calculate business loan eligibility
            eligible, reason = calculate_business_loan_eligibility(business_revenue, loan_amount, credit_score, years_in_business)
            print(f"Eligibility Status: {'Eligible' if eligible else 'Not Eligible'}")
            print(f"Reason: {reason}")

        else:
            print("Invalid loan type. Please enter 'personal' or 'business'.")
    except ValueError as e:
        print(f"Input Error: {e}. Please provide valid numerical values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
