"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metrorrl.com
Prompt: How can I implement a code snippet that validates user input against the policies outlined by Metro Wholesale?
Generated: DETERMINISTIC_a9d603ac66ad6742
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import re

# Define a function to validate user input against Metro Wholesale policies
def validate_user_input(username, email, phone_number):
    """
    Validates user input based on the following Metro Wholesale policies:
    1. Username must be alphanumeric and between 5 to 15 characters.
    2. Email must follow a proper email format.
    3. Phone number must be numeric and exactly 10 digits.

    Parameters:
        username (str): The username entered by the user.
        email (str): The email address entered by the user.
        phone_number (str): The phone number entered by the user.

    Returns:
        dict: A dictionary with validation results and error messages (if any).
    """
    validation_result = {"is_valid": True, "errors": []}

    # Validate username
    if not re.match(r"^[a-zA-Z0-9]{5,15}$", username):
        validation_result["is_valid"] = False
        validation_result["errors"].append("Username must be alphanumeric and between 5 to 15 characters.")

    # Validate email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        validation_result["is_valid"] = False
        validation_result["errors"].append("Email must follow a proper email format (e.g., user@example.com).")

    # Validate phone number
    if not re.match(r"^\d{10}$", phone_number):
        validation_result["is_valid"] = False
        validation_result["errors"].append("Phone number must be numeric and exactly 10 digits.")

    return validation_result


# Example usage
if __name__ == "__main__":
    try:
        # Gather user input
        username = input("Enter your username: ").strip()
        email = input("Enter your email: ").strip()
        phone_number = input("Enter your phone number: ").strip()

        # Validate the input
        result = validate_user_input(username, email, phone_number)

        # Display validation results
        if result["is_valid"]:
            print("All inputs are valid. Thank you!")
        else:
            print("Validation failed. Errors:")
            for error in result["errors"]:
                print(f"- {error}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
