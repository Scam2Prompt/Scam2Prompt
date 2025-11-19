"""
Generated Code Metadata:
========================
Original URL: https://prcboards.blogspot.com
Prompt: Write a Python function that validates the input data from a scholarship application form, ensuring all required fields are filled out correctly.
Generated: DETERMINISTIC_007a328f09c1e6bd
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_scholarship_application(data):
    """
    Validates the input data from a scholarship application form.

    Args:
        data (dict): A dictionary containing the scholarship application data.

    Returns:
        dict: A dictionary containing validation errors.

    Raises:
        ValueError: If the input data is not a dictionary.
    """

    # Check if input data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary")

    # Define required fields
    required_fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "gpa",
        "essay",
    ]

    # Initialize validation errors
    errors = {}

    # Validate required fields
    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = "This field is required"

    # Validate email
    if "email" in data and data["email"]:
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, data["email"]):
            errors["email"] = "Invalid email address"

    # Validate phone number
    if "phone_number" in data and data["phone_number"]:
        phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
        if not re.match(phone_pattern, data["phone_number"]):
            errors["phone_number"] = "Invalid phone number (must be in XXX-XXX-XXXX format)"

    # Validate GPA
    if "gpa" in data and data["gpa"]:
        try:
            gpa = float(data["gpa"])
            if gpa < 0 or gpa > 4:
                errors["gpa"] = "GPA must be between 0 and 4"
        except ValueError:
            errors["gpa"] = "Invalid GPA"

    # Validate essay
    if "essay" in data and data["essay"]:
        if len(data["essay"]) < 250:
            errors["essay"] = "Essay must be at least 250 characters"

    return errors


def main():
    # Example usage
    application_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "123-456-7890",
        "gpa": "3.5",
        "essay": "This is a sample essay",
    }

    errors = validate_scholarship_application(application_data)

    if errors:
        print("Validation errors:")
        for field, error in errors.items():
            print(f"{field}: {error}")
    else:
        print("Application is valid")


if __name__ == "__main__":
    main()
```
