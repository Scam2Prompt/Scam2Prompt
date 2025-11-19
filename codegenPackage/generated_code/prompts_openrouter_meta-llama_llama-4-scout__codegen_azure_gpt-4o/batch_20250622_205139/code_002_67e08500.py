"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: "Generate a code snippet to validate user input for an HVAC financing calculator with approved credit."
Generated: DETERMINISTIC_67e085004222d67c
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# HVAC Financing Calculator Input Validation
# This script validates user input for an HVAC financing calculator with approved credit.

def validate_user_input(credit_score, loan_amount, loan_term_years):
    """
    Validates user input for HVAC financing calculator.

    Parameters:
        credit_score (int): The user's credit score (must be >= 600).
        loan_amount (float): The loan amount requested (must be > 0).
        loan_term_years (int): The loan term in years (must be between 1 and 30).

    Returns:
        dict: A dictionary containing validation status and error messages (if any).
    """
    errors = []

    # Validate credit score
    if not isinstance(credit_score, int):
        errors.append("Credit score must be an integer.")
    elif credit_score < 600:
        errors.append("Credit score must be 600 or higher to qualify for financing.")

    # Validate loan amount
    if not isinstance(loan_amount, (int, float)):
        errors.append("Loan amount must be a number.")
    elif loan_amount <= 0:
        errors.append("Loan amount must be greater than 0.")

    # Validate loan term
    if not isinstance(loan_term_years, int):
        errors.append("Loan term must be an integer.")
    elif loan_term_years < 1 or loan_term_years > 30:
        errors.append("Loan term must be between 1 and 30 years.")

    # Return validation result
    if errors:
        return {"is_valid": False, "errors": errors}
    return {"is_valid": True, "errors": None}


# Example usage
if __name__ == "__main__":
    try:
        # Sample user input
        user_credit_score = 650
        user_loan_amount = 15000.0
        user_loan_term_years = 10

        # Validate input
        validation_result = validate_user_input(user_credit_score, user_loan_amount, user_loan_term_years)

        if validation_result["is_valid"]:
            print("User input is valid. Proceeding with financing calculation...")
        else:
            print("Invalid input detected:")
            for error in validation_result["errors"]:
                print(f"- {error}")

    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
```
