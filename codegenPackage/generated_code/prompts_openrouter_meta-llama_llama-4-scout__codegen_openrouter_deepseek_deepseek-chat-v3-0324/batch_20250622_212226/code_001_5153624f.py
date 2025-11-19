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

# Predefined list of valid audition cities and their corresponding states
VALID_AUDITION_CITIES = {
    "Mumbai": "Maharashtra",
    "Delhi": "Delhi",
    "Bangalore": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal"
}

def validate_date_of_birth(dob_str):
    """
    Validate date of birth format (DD-MM-YYYY) and ensure age is between 13 and 19.
    
    Args:
        dob_str (str): Date of birth string in DD-MM-YYYY format
        
    Returns:
        tuple: (bool, str) where bool indicates validity and str contains error message
    """
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
    except ValueError:
        return False, "Invalid date format. Please use DD-MM-YYYY."
    
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    if age < 13:
        return False, "You must be at least 13 years old to participate."
    if age > 19:
        return False, "You must be 19 years old or younger to participate."
    
    return True, ""

def validate_phone_number(number):
    """
    Validate Indian phone number format (10 digits starting with 6-9).
    
    Args:
        number (str): Phone number to validate
        
    Returns:
        tuple: (bool, str) where bool indicates validity and str contains error message
    """
    if not re.match(r'^[6-9]\d{9}$', number):
        return False, "Invalid Indian phone number. Must be 10 digits starting with 6-9."
    return True, ""

def validate_whatsapp_number(number):
    """
    Validate WhatsApp number format (same as phone number but with optional +91 prefix).
    
    Args:
        number (str): WhatsApp number to validate
        
    Returns:
        tuple: (bool, str) where bool indicates validity and str contains error message
    """
    if not re.match(r'^(\+91)?[6-9]\d{9}$', number):
        return False, "Invalid WhatsApp number. Must be 10 digits starting with 6-9, optionally prefixed with +91."
    return True, ""

def validate_audition_location(city, state):
    """
    Validate that the selected city and state combination is valid.
    
    Args:
        city (str): Selected audition city
        state (str): Selected audition state
        
    Returns:
        tuple: (bool, str) where bool indicates validity and str contains error message
    """
    if city not in VALID_AUDITION_CITIES:
        return False, "Invalid audition city selected."
    
    if VALID_AUDITION_CITIES[city] != state:
        return False, f"{city} is not in {state}. Please select the correct state."
    
    return True, ""

def validate_registration_details(dob, phone, whatsapp, city, state):
    """
    Validate all registration details for Star Miss Teen India 2025.
    
    Args:
        dob (str): Date of birth in DD-MM-YYYY format
        phone (str): Mobile phone number
        whatsapp (str): WhatsApp number
        city (str): Selected audition city
        state (str): Selected audition state
        
    Returns:
        dict: Dictionary containing validation results with success flag and error messages
    """
    errors = []
    
    # Validate date of birth
    dob_valid, dob_error = validate_date_of_birth(dob)
    if not dob_valid:
        errors.append(dob_error)
    
    # Validate phone number
    phone_valid, phone_error = validate_phone_number(phone)
    if not phone_valid:
        errors.append(phone_error)
    
    # Validate WhatsApp number
    whatsapp_valid, whatsapp_error = validate_whatsapp_number(whatsapp)
    if not whatsapp_valid:
        errors.append(whatsapp_error)
    
    # Validate audition location
    location_valid, location_error = validate_audition_location(city, state)
    if not location_valid:
        errors.append(location_error)
    
    return {
        "success": len(errors) == 0,
        "errors": errors
    }

# Example usage:
if __name__ == "__main__":
    # Test data
    test_data = {
        "dob": "15-08-2006",
        "phone": "9876543210",
        "whatsapp": "+919876543210",
        "city": "Mumbai",
        "state": "Maharashtra"
    }
    
    # Validate the test data
    result = validate_registration_details(
        test_data["dob"],
        test_data["phone"],
        test_data["whatsapp"],
        test_data["city"],
        test_data["state"]
    )
    
    # Print results
    if result["success"]:
        print("All registration details are valid!")
    else:
        print("Validation errors found:")
        for error in result["errors"]:
            print(f"- {error}")
```
