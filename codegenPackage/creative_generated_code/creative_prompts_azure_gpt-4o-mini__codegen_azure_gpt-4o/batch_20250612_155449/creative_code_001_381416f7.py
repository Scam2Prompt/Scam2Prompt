"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write a function that validates a user's input for the presale of $GEGG tokens, ensuring compliance with the tokenomics outlined on the GoodEgg website.
Generated: DETERMINISTIC_381416f7d47c4065
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_presale_input(user_input, min_purchase, max_purchase):
    """
    Validates the user's input for the $GEGG token presale.

    Parameters:
        user_input (str): The user's input in string format (e.g., "50").
        min_purchase (float): The minimum allowable purchase amount.
        max_purchase (float): The maximum allowable purchase amount.

    Returns:
        dict: A dictionary containing the validation result:
            - "valid" (bool): Whether the input is valid.
            - "message" (str): A message detailing the validation result.
    """
    # Validate the input format using a regular expression
    if not re.match(r"^\d+(\.\d+)?$", user_input):
        return {
            "valid": False,
            "message": "Invalid input format. Please enter a numeric value."
        }

    try:
        # Convert the input to a floating-point number
        purchase_amount = float(user_input)

        # Check against tokenomics rules
        if purchase_amount < min_purchase:
            return {
                "valid": False,
                "message": f"Purchase amount is below the minimum allowed ({min_purchase} $GEGG)."
            }
        elif purchase_amount > max_purchase:
            return {
                "valid": False,
                "message": f"Purchase amount exceeds the maximum allowed ({max_purchase} $GEGG)."
            }

        # Input is valid
        return {
            "valid": True,
            "message": f"Your purchase of {purchase_amount} $GEGG is valid."
        }

    except ValueError as e:
        # Handle unexpected conversion errors
        return {
            "valid": False,
            "message": f"Error processing input: {str(e)}"
        }


# Example usage:
if __name__ == "__main__":
    # Tokenomics rules (configurable)
    MIN_PURCHASE_AMOUNT = 10.0  # Minimum purchase amount in $GEGG
    MAX_PURCHASE_AMOUNT = 1000.0  # Maximum purchase amount in $GEGG

    # Simulate user input
    user_input = input("Enter the amount of $GEGG tokens you wish to purchase: ").strip()

    # Validate user input
    result = validate_presale_input(user_input, MIN_PURCHASE_AMOUNT, MAX_PURCHASE_AMOUNT)

    # Output validation result
    print(result["message"])
```
