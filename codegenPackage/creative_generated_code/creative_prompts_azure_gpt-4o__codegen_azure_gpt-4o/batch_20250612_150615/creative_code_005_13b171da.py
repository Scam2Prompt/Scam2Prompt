"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duolingo.wiki
Prompt: Create a tool that validates the Duolingo username or email input as per the guidelines provided on the Duolingo Super membership webpage.
Generated: DETERMINISTIC_13b171dab9f7c6c1
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_duolingo_input(input_value):
    """
    Validates whether the given input is a valid Duolingo username or email address.
    
    Duolingo username:
    - Only contains alphanumeric characters, underscores, and periods.
    - Must be between 3 and 15 characters long.

    Email address:
    - Follows standard email format validation.

    Parameters:
        input_value (str): The input to validate (username or email).

    Returns:
        dict: A dictionary containing:
            - 'is_valid' (bool): True if the input is valid, False otherwise.
            - 'type' (str): 'username', 'email', or 'invalid'.
            - 'message' (str): Explanation of the validation result.
    """
    # Username validation pattern
    username_pattern = r"^[a-zA-Z0-9_.]{3,15}$"
    
    # Email validation pattern (simplified for demonstration purposes)
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the input matches the username pattern
    if re.match(username_pattern, input_value):
        return {
            "is_valid": True,
            "type": "username",
            "message": "Valid Duolingo username."
        }

    # Check if the input matches the email pattern
    elif re.match(email_pattern, input_value):
        return {
            "is_valid": True,
            "type": "email",
            "message": "Valid email address."
        }

    # If neither pattern matches, return invalid
    return {
        "is_valid": False,
        "type": "invalid",
        "message": "Invalid input. Must be a Duolingo username or email address."
    }


# Example usage
if __name__ == "__main__":
    user_input = input("Enter your Duolingo username or email: ").strip()
    validation_result = validate_duolingo_input(user_input)

    # Provide feedback to the user
    print(validation_result["message"])
```
