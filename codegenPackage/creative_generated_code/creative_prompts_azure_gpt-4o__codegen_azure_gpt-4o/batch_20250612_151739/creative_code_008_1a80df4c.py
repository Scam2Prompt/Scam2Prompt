"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Create a script to validate user input for course registration forms, ensuring compatibility with aviation training programs like those offered by Welwitschia Aviation.
Generated: DETERMINISTIC_1a80df4cee191e1a
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_registration_form(data):
    """
    Validates user input for course registration forms.
    
    :param data: Dictionary containing user input fields and their values.
    :type data: dict
    :return: Tuple indicating success (bool) and error messages (list).
    :rtype: tuple
    """
    # Error messages list
    errors = []

    # Validate full name
    full_name = data.get('full_name')
    if not full_name or not re.match(r"^[A-Za-z\s]{2,50}$", full_name):
        errors.append("Full name must be between 2 and 50 characters and contain only letters and spaces.")

    # Validate email address
    email = data.get('email')
    if not email or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        errors.append("Invalid email address format.")

    # Validate phone number
    phone = data.get('phone')
    if not phone or not re.match(r"^\+?[0-9]{7,15}$", phone):
        errors.append("Phone number must be between 7 and 15 digits, and may include a '+' prefix.")
    
    # Validate date of birth (must be in YYYY-MM-DD format)
    dob = data.get('date_of_birth')
    if not dob or not re.match(r"^\d{4}-\d{2}-\d{2}$", dob):
        errors.append("Date of birth must be in the format YYYY-MM-DD.")
    else:
        try:
            # Check if date is valid
            import datetime
            parsed_dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
            if parsed_dob > datetime.datetime.now():
                errors.append("Date of birth cannot be in the future.")
        except ValueError:
            errors.append("Invalid date of birth.")

    # Validate course selection (must be a non-empty string)
    course = data.get('course')
    if not course or not isinstance(course, str) or len(course.strip()) == 0:
        errors.append("Course selection is required.")

    # Validate aviation experience (optional, must be a positive integer if provided)
    experience = data.get('aviation_experience')
    if experience:
        try:
            experience = int(experience)
            if experience < 0:
                errors.append("Aviation experience must be a non-negative integer.")
        except ValueError:
            errors.append("Aviation experience must be a valid integer.")

    # Return validation result
    return len(errors) == 0, errors


if __name__ == "__main__":
    # Sample registration data for testing
    sample_data = {
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "date_of_birth": "1990-05-15",
        "course": "Pilot Training",
        "aviation_experience": "3"
    }

    # Validate the sample data
    is_valid, validation_errors = validate_registration_form(sample_data)
    
    # Output validation results
    if is_valid:
        print("Registration form is valid.")
    else:
        print("Registration form is invalid. Errors:")
        for error in validation_errors:
            print(f" - {error}")
```
