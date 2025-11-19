"""
Generated Code Metadata:
========================
Original URL: https://starmissteenindia.com
Prompt: "Write a Python script to validate the registration details for 'Star Miss Teen India 2025', including checking the correct format for date of birth, WhatsApp number, and mobile number, and ensuring the selected audition city and state are valid."
Generated: DETERMINISTIC_5153624f9ac235da
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime

# List of valid audition cities and states
VALID_CITIES = {
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Bangalore": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Hyderabad": "Telangana",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat"
}

def validate_date_of_birth(dob):
    """
    Validates the date of birth format (DD-MM-YYYY) and checks if the age is between 13 and 19.
    """
    try:
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        if 13 <= age <= 19:
            return True
        else:
            return False
    except ValueError:
        return False

def validate_mobile_number(number):
    """
    Validates the mobile number format (10 digits, starts with 6-9).
    """
    return bool(re.fullmatch(r"[6-9]\d{9}", number))

def validate_whatsapp_number(number):
    """
    Validates the WhatsApp number format (10 digits, starts with 6-9).
    """
    return validate_mobile_number(number)

def validate_audition_city_and_state(city, state):
    """
    Validates if the selected audition city and state are valid and match.
    """
    return VALID_CITIES.get(city) == state

def validate_registration_details(details):
    """
    Validates the registration details for 'Star Miss Teen India 2025'.
    :param details: Dictionary containing registration details.
    :return: Tuple (is_valid, errors) where is_valid is a boolean and errors is a list of error messages.
    """
    errors = []

    # Validate date of birth
    if not validate_date_of_birth(details.get("date_of_birth", "")):
        errors.append("Invalid date of birth. Ensure the format is DD-MM-YYYY and age is between 13 and 19.")

    # Validate mobile number
    if not validate_mobile_number(details.get("mobile_number", "")):
        errors.append("Invalid mobile number. It should be 10 digits and start with 6-9.")

    # Validate WhatsApp number
    if not validate_whatsapp_number(details.get("whatsapp_number", "")):
        errors.append("Invalid WhatsApp number. It should be 10 digits and start with 6-9.")

    # Validate audition city and state
    city = details.get("audition_city", "")
    state = details.get("audition_state", "")
    if not validate_audition_city_and_state(city, state):
        errors.append(f"Invalid audition city and state. Ensure the city '{city}' matches the state '{state}'.")

    return len(errors) == 0, errors

# Example usage
if __name__ == "__main__":
    # Sample registration details
    registration_details = {
        "date_of_birth": "15-08-2008",  # DD-MM-YYYY
        "mobile_number": "9876543210",
        "whatsapp_number": "9876543210",
        "audition_city": "Mumbai",
        "audition_state": "Maharashtra"
    }

    # Validate the details
    is_valid, validation_errors = validate_registration_details(registration_details)

    if is_valid:
        print("Registration details are valid.")
    else:
        print("Registration details are invalid. Errors:")
        for error in validation_errors:
            print(f"- {error}")
```
