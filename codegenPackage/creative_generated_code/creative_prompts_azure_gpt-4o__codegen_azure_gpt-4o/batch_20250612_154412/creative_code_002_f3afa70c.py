"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Generate code to validate form inputs for a telephony quote request system, ensuring fields like name, email, and phone number are correctly formatted.
Generated: DETERMINISTIC_f3afa70caf61ae26
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_form_inputs(name, email, phone):
    """
    Validates form inputs for a telephony quote request system.

    :param name: str - The name of the user (must contain only alphabetic characters and spaces).
    :param email: str - The email address (must follow standard email format).
    :param phone: str - The phone number (must be numeric and between 7-15 digits).
    :return: dict - Dictionary containing validation results for each field.
    """
    validation_results = {
        "name_valid": False,
        "email_valid": False,
        "phone_valid": False,
        "errors": []
    }

    # Validate name: must only contain alphabetic characters and spaces
    if name and re.match(r"^[a-zA-Z\s]+$", name):
        validation_results["name_valid"] = True
    else:
        validation_results["errors"].append("Invalid name. Name should contain only alphabetic characters and spaces.")

    # Validate email: must follow standard email format
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if email and re.match(email_regex, email):
        validation_results["email_valid"] = True
    else:
        validation_results["errors"].append("Invalid email format.")

    # Validate phone number: must be numeric and between 7-15 digits
    if phone and re.match(r"^\d{7,15}$", phone):
        validation_results["phone_valid"] = True
    else:
        validation_results["errors"].append("Invalid phone number. Phone number should be numeric and contain 7-15 digits.")

    return validation_results


if __name__ == "__main__":
    # Example usage
    # Replace these example inputs with actual user-provided data
    user_name = "John Doe"
    user_email = "john.doe@example.com"
    user_phone = "1234567890"

    # Validate the form inputs
    results = validate_form_inputs(user_name, user_email, user_phone)

    print("Validation Results:")
    print(results)

    if not all([results["name_valid"], results["email_valid"], results["phone_valid"]]):
        print("Errors:")
        for error in results["errors"]:
            print(f"- {error}")
    else:
        print("Form inputs are valid!")
```
