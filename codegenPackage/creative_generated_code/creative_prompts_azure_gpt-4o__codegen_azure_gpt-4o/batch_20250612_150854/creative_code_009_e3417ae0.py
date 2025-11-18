"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Build a tool that evaluates mortgage eligibility for users with bad credit, incorporating the actionable tips provided in ImmediateGains' guide on getting approved for a mortgage.
Generated: DETERMINISTIC_e3417ae0d069b1e1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def evaluate_mortgage_eligibility(credit_score, annual_income, down_payment, existing_debt, loan_amount):
    """
    Evaluates mortgage eligibility based on user input and actionable tips from ImmediateGains' guide.

    Args:
        credit_score (int): User's credit score.
        annual_income (float): User's annual income in USD.
        down_payment (float): Down payment the user can make in USD.
        existing_debt (float): Total existing debt in USD.
        loan_amount (float): Desired loan amount in USD.

    Returns:
        dict: A dictionary containing eligibility status and actionable tips.
    """
    try:
        # Basic validation for inputs
        if credit_score < 0 or annual_income < 0 or down_payment < 0 or existing_debt < 0 or loan_amount < 0:
            raise ValueError("Input values must be non-negative.")

        # Actionable tips for improving chances
        tips = [
            "Consider improving your credit score by paying bills on time and reducing credit usage.",
            "Increase your down payment to reduce the lender's risk.",
            "Pay off existing debts to reduce your debt-to-income ratio.",
            "Explore FHA loans or other programs designed for bad credit borrowers.",
            "Get pre-approved before house hunting to understand your borrowing limit."
        ]

        # Eligibility criteria
        eligibility = {
            "eligible": False,
            "reason": None,
            "actionable_tips": tips
        }

        # Rule 1: Minimum credit score requirement
        MIN_CREDIT_SCORE = 500
        if credit_score < MIN_CREDIT_SCORE:
            eligibility["reason"] = f"Credit score below the minimum requirement of {MIN_CREDIT_SCORE}."
            return eligibility

        # Rule 2: Debt-to-income ratio
        DEBT_TO_INCOME_THRESHOLD = 0.43
        debt_to_income_ratio = existing_debt / annual_income
        if debt_to_income_ratio > DEBT_TO_INCOME_THRESHOLD:
            eligibility["reason"] = f"Debt-to-income ratio ({debt_to_income_ratio:.2f}) exceeds the threshold of {DEBT_TO_INCOME_THRESHOLD}."
            return eligibility

        # Rule 3: Down payment percentage
        DOWN_PAYMENT_PERCENTAGE = 0.10
        required_down_payment = loan_amount * DOWN_PAYMENT_PERCENTAGE
        if down_payment < required_down_payment:
            eligibility["reason"] = f"Down payment is less than the required 10% of loan amount (${required_down_payment:.2f})."
            return eligibility

        # If all criteria are met, the user is eligible
        eligibility["eligible"] = True
        eligibility["reason"] = "You meet all eligibility criteria for a mortgage."

        return eligibility

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

def main():
    """
    Main function to interact with the mortgage eligibility tool.
    """
    try:
        print("Welcome to the Mortgage Eligibility Evaluator")
        print("Please provide the following details to evaluate your eligibility.\n")

        # Collecting user inputs
        credit_score = int(input("Enter your credit score: "))
        annual_income = float(input("Enter your annual income (USD): "))
        down_payment = float(input("Enter your down payment (USD): "))
        existing_debt = float(input("Enter your total existing debt (USD): "))
        loan_amount = float(input("Enter your desired loan amount (USD): "))

        # Evaluate eligibility
        result = evaluate_mortgage_eligibility(credit_score, annual_income, down_payment, existing_debt, loan_amount)

        # Display results
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\nMortgage Eligibility Result:")
            print(f"Eligible: {'Yes' if result['eligible'] else 'No'}")
            print(f"Reason: {result['reason']}")
            if not result['eligible']:
                print("\nActionable Tips to Improve Eligibility:")
                for tip in result["actionable_tips"]:
                    print(f"- {tip}")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
