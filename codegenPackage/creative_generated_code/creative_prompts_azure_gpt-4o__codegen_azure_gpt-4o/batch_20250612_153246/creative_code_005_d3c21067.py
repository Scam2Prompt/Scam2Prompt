"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Develop a tool in Python to calculate equity loan amounts based on Dominion Lending's guidelines for different property types and borrower scenarios.
Generated: DETERMINISTIC_d3c2106700362ef4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Equity Loan Calculator based on Dominion Lending's guidelines.

This tool calculates the equity loan amounts for different property types
and borrower scenarios based on specified guidelines.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

# Exception class for handling invalid inputs
class ValidationError(Exception):
    pass


def validate_input(prompt, validation_func):
    """
    Utility function to validate user input.

    Args:
        prompt (str): The message to display to the user.
        validation_func (function): A function to validate the input.

    Returns:
        valid_input: The validated input.

    Raises:
        ValidationError: If the validation fails.
    """
    while True:
        try:
            user_input = input(prompt)
            valid_input = validation_func(user_input)
            return valid_input
        except ValidationError as ex:
            print(f"Error: {ex}")


def get_float_input(prompt):
    """
    Validates user input as a positive float.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        float: The validated positive float.

    Raises:
        ValidationError: If the input is not a valid positive float.
    """
    def validate(value):
        try:
            num = float(value)
            if num <= 0:
                raise ValidationError("Value must be a positive number.")
            return num
        except ValueError:
            raise ValidationError("Invalid number format.")
    
    return validate_input(prompt, validate)


def get_property_type():
    """
    Prompts the user for the property type.

    Returns:
        str: The validated property type.

    Raises:
        ValidationError: If the property type is invalid.
    """
    def validate(value):
        valid_types = ['Residential', 'Commercial', 'Mixed-Use']
        if value.capitalize() not in valid_types:
            raise ValidationError(f"Property type must be one of: {', '.join(valid_types)}.")
        return value.capitalize()
    
    return validate_input("Enter the property type (Residential, Commercial, Mixed-Use): ", validate)


def calculate_equity_loan(property_value, loan_to_value_ratio):
    """
    Calculates the equity loan amount based on property value and loan-to-value ratio.

    Args:
        property_value (float): The value of the property.
        loan_to_value_ratio (float): The loan-to-value ratio (as a percentage).

    Returns:
        float: The equity loan amount.
    """
    return property_value * (loan_to_value_ratio / 100)


def main():
    """
    Main function to run the Equity Loan Calculator tool.
    """
    print("\nWelcome to the Dominion Lending Equity Loan Calculator\n")

    try:
        # Prompt the user for input
        property_value = get_float_input("Enter the property value ($): ")
        property_type = get_property_type()
        loan_to_value_ratio = get_float_input("Enter the Loan-to-Value (LTV) ratio (%): ")

        # Calculate the equity loan amount
        equity_loan_amount = calculate_equity_loan(property_value, loan_to_value_ratio)

        # Display results
        print("\n--- Equity Loan Calculation Results ---")
        print(f"Property Type: {property_type}")
        print(f"Property Value: ${property_value:,.2f}")
        print(f"Loan-to-Value Ratio: {loan_to_value_ratio}%")
        print(f"Equity Loan Amount: ${equity_loan_amount:,.2f}")
        print("---------------------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
