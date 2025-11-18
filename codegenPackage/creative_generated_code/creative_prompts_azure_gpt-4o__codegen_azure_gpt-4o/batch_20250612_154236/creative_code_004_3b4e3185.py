"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Write a script to validate customer inputs for booking BPL appliance repair services, ensuring correct appliance type, location, and contact details are provided before submission.
Generated: DETERMINISTIC_3b4e318542c18a45
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_appliance_type(appliance_type):
    """
    Validates the appliance type entered by the customer.
    Allowed types: "Washing Machine", "Refrigerator", "Microwave", "Air Conditioner", "Dishwasher".
    """
    valid_appliance_types = {"Washing Machine", "Refrigerator", "Microwave", "Air Conditioner", "Dishwasher"}
    if appliance_type in valid_appliance_types:
        return True
    return False

def validate_location(location):
    """
    Validates the location entered by the customer.
    Ensures it is not empty and does not exceed 100 characters.
    """
    if location and isinstance(location, str) and len(location) <= 100:
        return True
    return False

def validate_contact_details(contact_details):
    """
    Validates the contact details entered by the customer.
    Ensures the phone number is a valid 10-digit numeric string.
    """
    phone_pattern = re.compile(r"^\d{10}$")  # Matches exactly 10 digits
    if phone_pattern.match(contact_details):
        return True
    return False

def validate_booking(appliance_type, location, contact_details):
    """
    Validates customer inputs for booking BPL appliance repair services.
    """
    errors = []

    # Validate appliance type
    if not validate_appliance_type(appliance_type):
        errors.append("Invalid appliance type. Please select a valid appliance.")

    # Validate location
    if not validate_location(location):
        errors.append("Invalid location. Please provide a valid location (max 100 characters).")

    # Validate contact details (phone number)
    if not validate_contact_details(contact_details):
        errors.append("Invalid contact details. Please provide a valid 10-digit phone number.")

    if errors:
        return False, errors

    return True, "Booking details are valid."

# Example usage
if __name__ == "__main__":
    # Sample inputs for validation
    appliance_type = "Washing Machine"
    location = "123 Main Street, Springfield"
    contact_details = "9876543210"

    # Validate inputs
    is_valid, message = validate_booking(appliance_type, location, contact_details)

    # Print validation results
    if is_valid:
        print("Success:", message)
    else:
        print("Errors:", message)
```
