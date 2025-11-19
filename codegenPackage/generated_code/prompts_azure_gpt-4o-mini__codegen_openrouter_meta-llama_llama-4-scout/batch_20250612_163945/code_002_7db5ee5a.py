"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: Write a function that validates user input for a telephone quote request form, ensuring all fields are filled correctly.
Generated: DETERMINISTIC_7db5ee5acb6b37c5
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_quote_request(
    first_name: str, 
    last_name: str, 
    email: str, 
    phone_number: str, 
    company: str, 
    description: str
) -> dict:
    """
    Validates user input for a telephone quote request form.

    Args:
    - first_name (str): The user's first name.
    - last_name (str): The user's last name.
    - email (str): The user's email address.
    - phone_number (str): The user's phone number.
    - company (str): The user's company name.
    - description (str): A brief description of the request.

    Returns:
    - dict: A dictionary containing validation results and error messages.
    """

    # Initialize validation results
    validation_results = {
        "is_valid": True,
        "errors": {}
    }

    # Validate first name
    if not first_name.strip():
        validation_results["errors"]["first_name"] = "First name is required."
        validation_results["is_valid"] = False

    # Validate last name
    if not last_name.strip():
        validation_results["errors"]["last_name"] = "Last name is required."
        validation_results["is_valid"] = False

    # Validate email
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, email):
        validation_results["errors"]["email"] = "Invalid email address."
        validation_results["is_valid"] = False

    # Validate phone number
    phone_pattern = r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
    if not re.match(phone_pattern, phone_number):
        validation_results["errors"]["phone_number"] = "Invalid phone number."
        validation_results["is_valid"] = False

    # Validate company
    if not company.strip():
        validation_results["errors"]["company"] = "Company name is required."
        validation_results["is_valid"] = False

    # Validate description
    if not description.strip():
        validation_results["errors"]["description"] = "Description is required."
        validation_results["is_valid"] = False

    return validation_results


def main():
    try:
        first_name = "John"
        last_name = "Doe"
        email = "john.doe@example.com"
        phone_number = "(123) 456-7890"
        company = "Example Inc."
        description = "This is a test request."

        validation_results = validate_quote_request(
            first_name, 
            last_name, 
            email, 
            phone_number, 
            company, 
            description
        )

        print("Validation Results:")
        print(f"Is Valid: {validation_results['is_valid']}")
        print("Errors:")
        for field, error in validation_results["errors"].items():
            print(f"- {field}: {error}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
