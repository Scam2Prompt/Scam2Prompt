"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Create a Python program that validates user input for investment amounts based on the minimum and maximum limits specified in Steadfast Asset Innovation's investment plans.
Generated: DETERMINISTIC_4a1758eebed55d2f
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to validate user input for investment amounts
# based on minimum and maximum limits specified in investment plans.

def validate_investment_amount(amount, min_limit, max_limit):
    """
    Validates the given investment amount against specified limits.

    :param amount: Investment amount to validate
    :param min_limit: Minimum allowable investment amount
    :param max_limit: Maximum allowable investment amount
    :return: A boolean indicating whether the amount is valid
    """
    if amount < min_limit:
        return f"Invalid: The amount is below the minimum limit of ${min_limit}."
    elif amount > max_limit:
        return f"Invalid: The amount exceeds the maximum limit of ${max_limit}."
    else:
        return "Valid: The investment amount is within the acceptable range."


def main():
    """
    Main function to handle user input and validate investment amounts.
    """
    # Example limits specified by Steadfast Asset Innovation
    MIN_INVESTMENT = 1000  # Minimum investment amount in dollars
    MAX_INVESTMENT = 50000  # Maximum investment amount in dollars

    print("Welcome to Steadfast Asset Innovation's Investment Validator.")
    print(f"Please enter an amount between ${MIN_INVESTMENT} and ${MAX_INVESTMENT}.")

    try:
        # Accept user input
        user_input = input("Enter your investment amount: ").strip()

        # Convert input to a float to handle decimal values
        investment_amount = float(user_input)

        # Validate the investment amount
        validation_result = validate_investment_amount(
            investment_amount, MIN_INVESTMENT, MAX_INVESTMENT
        )

        # Print the result of the validation
        print(validation_result)

    except ValueError:
        # Handle non-numeric input errors
        print("Error: Please enter a valid numeric value for the investment amount.")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
