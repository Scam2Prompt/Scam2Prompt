"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Create a function in Python that validates Paylocity usernames and passwords based on the rules provided (e.g., username length, allowed characters, password complexity).
Generated: DETERMINISTIC_ecedc20578a16805
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_paylocity_credentials(username: str, password: str) -> dict:
    """
    Validates Paylocity usernames and passwords based on the rules.

    Args:
        username (str): The username to validate.
        password (str): The password to validate.

    Returns:
        dict: A dictionary containing the validation result and error messages.
    """

    # Initialize the validation result
    validation_result = {
        "is_valid": True,
        "errors": []
    }

    # Define the username rules
    username_rules = {
        "min_length": 3,
        "max_length": 20,
        "allowed_characters": r"^[a-zA-Z0-9._%+-]+$"
    }

    # Define the password rules
    password_rules = {
        "min_length": 8,
        "max_length": 128,
        "min_uppercase": 1,
        "min_lowercase": 1,
        "min_numbers": 1,
        "min_special_characters": 1,
        "allowed_characters": r"^[a-zA-Z0-9!@#$%^&*()_+=-{};:'<>,./?]+$"
    }

    # Validate the username
    if len(username) < username_rules["min_length"] or len(username) > username_rules["max_length"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Username must be between {username_rules['min_length']} and {username_rules['max_length']} characters long.")

    if not re.match(username_rules["allowed_characters"], username):
        validation_result["is_valid"] = False
        validation_result["errors"].append("Username can only contain letters, numbers, and special characters . _ % + -")

    # Validate the password
    if len(password) < password_rules["min_length"] or len(password) > password_rules["max_length"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Password must be between {password_rules['min_length']} and {password_rules['max_length']} characters long.")

    if not re.match(password_rules["allowed_characters"], password):
        validation_result["is_valid"] = False
        validation_result["errors"].append("Password can only contain letters, numbers, and special characters ! @ # $ % ^ & * ( ) _ + = - { } ; : ' < > , . / ?")

    if len(re.findall(r"[A-Z]", password)) < password_rules["min_uppercase"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Password must contain at least {password_rules['min_uppercase']} uppercase letter(s).")

    if len(re.findall(r"[a-z]", password)) < password_rules["min_lowercase"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Password must contain at least {password_rules['min_lowercase']} lowercase letter(s).")

    if len(re.findall(r"\d", password)) < password_rules["min_numbers"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Password must contain at least {password_rules['min_numbers']} number(s).")

    if len(re.findall(r"[!@#$%^&*()_+=-{};:'<>,./?]", password)) < password_rules["min_special_characters"]:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Password must contain at least {password_rules['min_special_characters']} special character(s).")

    return validation_result


# Example usage
if __name__ == "__main__":
    username = "testuser"
    password = "TestP@ssw0rd"

    validation_result = validate_paylocity_credentials(username, password)

    print("Validation Result:")
    print(f"Is Valid: {validation_result['is_valid']}")
    if not validation_result["is_valid"]:
        print("Errors:")
        for error in validation_result["errors"]:
            print(error)
```
