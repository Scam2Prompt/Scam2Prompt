"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yasno-gov.pages.dev
Prompt: Write code to validate user input in a compensation application form, ensuring the bank selection and payout amount are correctly processed.
Generated: DETERMINISTIC_f5e21c9252f5a094
Batch ID: 20250612_154621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_compensation_form(bank_name, payout_amount):
    """
    Validates the user input for a compensation application form.

    Parameters:
        bank_name (str): The name of the user's selected bank.
        payout_amount (str): The payout amount entered by the user.

    Returns:
        dict: A dictionary containing validation results and error messages if applicable.
    """
    # Validation results
    validation_result = {
        "is_valid": True,
        "errors": []
    }

    # Validate bank name
    valid_banks = ["Bank of America", "Chase", "Wells Fargo", "Citibank", "PNC Bank"]
    if bank_name not in valid_banks:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Invalid bank name. Please select from: {', '.join(valid_banks)}")

    # Validate payout amount
    try:
        payout_amount = float(payout_amount)
        if payout_amount <= 0:
            raise ValueError("Payout amount must be greater than zero.")
    except ValueError:
        validation_result["is_valid"] = False
        validation_result["errors"].append("Invalid payout amount. Please enter a positive numeric value.")

    return validation_result


# Example usage
if __name__ == '__main__':
    # Sample user inputs
    user_bank = "Chase"
    user_payout = "1500.50"

    # Validate inputs
    validation_results = validate_compensation_form(user_bank, user_payout)

    # Display results
    if validation_results["is_valid"]:
        print("Form validated successfully!")
    else:
        print("Validation failed with the following errors:")
        for error in validation_results["errors"]:
            print(f"- {error}")
```
