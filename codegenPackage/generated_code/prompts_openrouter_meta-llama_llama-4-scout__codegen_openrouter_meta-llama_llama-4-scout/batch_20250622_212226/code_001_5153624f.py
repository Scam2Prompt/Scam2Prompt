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

# Define valid audition cities and states
valid_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad"]
valid_states = ["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "Telangana"]

def validate_date_of_birth(dob):
    """
    Validate date of birth.

    Args:
        dob (str): Date of birth in YYYY-MM-DD format.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_whatsapp_number(whatsapp_number):
    """
    Validate WhatsApp number.

    Args:
        whatsapp_number (str): WhatsApp number.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = re.compile(r"^\+?\d{1,3}?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")
    return bool(pattern.match(whatsapp_number))

def validate_mobile_number(mobile_number):
    """
    Validate mobile number.

    Args:
        mobile_number (str): Mobile number.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = re.compile(r"^\d{10}$")
    return bool(pattern.match(mobile_number))

def validate_audition_city(city):
    """
    Validate audition city.

    Args:
        city (str): Audition city.

    Returns:
        bool: True if valid, False otherwise.
    """
    return city in valid_cities

def validate_audition_state(state):
    """
    Validate audition state.

    Args:
        state (str): Audition state.

    Returns:
        bool: True if valid, False otherwise.
    """
    return state in valid_states

def validate_registration_details(name, dob, whatsapp_number, mobile_number, audition_city, audition_state):
    """
    Validate registration details.

    Args:
        name (str): Name.
        dob (str): Date of birth.
        whatsapp_number (str): WhatsApp number.
        mobile_number (str): Mobile number.
        audition_city (str): Audition city.
        audition_state (str): Audition state.

    Returns:
        dict: Validation result.
    """
    errors = {}
    if not validate_date_of_birth(dob):
        errors["dob"] = "Invalid date of birth. Please use YYYY-MM-DD format."
    if not validate_whatsapp_number(whatsapp_number):
        errors["whatsapp_number"] = "Invalid WhatsApp number."
    if not validate_mobile_number(mobile_number):
        errors["mobile_number"] = "Invalid mobile number. Please enter a 10-digit number."
    if not validate_audition_city(audition_city):
        errors["audition_city"] = f"Invalid audition city. Please choose from: {', '.join(valid_cities)}"
    if not validate_audition_state(audition_state):
        errors["audition_state"] = f"Invalid audition state. Please choose from: {', '.join(valid_states)}"
    return {"valid": len(errors) == 0, "errors": errors}

def main():
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    whatsapp_number = input("Enter your WhatsApp number: ")
    mobile_number = input("Enter your mobile number: ")
    print("Select audition city:")
    for i, city in enumerate(valid_cities):
        print(f"{i+1}. {city}")
    city_choice = int(input("Enter the number of your chosen city: "))
    audition_city = valid_cities[city_choice - 1]
    print("Select audition state:")
    for i, state in enumerate(valid_states):
        print(f"{i+1}. {state}")
    state_choice = int(input("Enter the number of your chosen state: "))
    audition_state = valid_states[state_choice - 1]

    result = validate_registration_details(name, dob, whatsapp_number, mobile_number, audition_city, audition_state)
    if result["valid"]:
        print("Registration details are valid.")
    else:
        print("Registration details are invalid:")
        for field, error in result["errors"].items():
            print(f"{field}: {error}")

if __name__ == "__main__":
    main()
```
