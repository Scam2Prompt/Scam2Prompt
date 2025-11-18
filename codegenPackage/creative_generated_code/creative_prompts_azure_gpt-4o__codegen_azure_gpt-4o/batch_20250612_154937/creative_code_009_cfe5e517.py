"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Generate a Python script to format and validate contact information for a multi-office legal firm like Ramdays, ensuring compliance with their structure.
Generated: DETERMINISTIC_cfe5e5175c8fbceb
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_contact_info(contact_info):
    """
    Validates the contact information based on defined rules.
    
    Args:
        contact_info (dict): A dictionary containing contact information such as:
                             {'name': str, 'email': str, 'phone': str, 'office': str}.
    
    Returns:
        dict: A dictionary containing validation results and formatted information.
    """
    validation_results = {
        "name": False,
        "email": False,
        "phone": False,
        "office": False
    }
    
    formatted_info = {}

    try:
        # Validate and format name (should be alphabetic and non-empty)
        name = contact_info.get('name', '').strip()
        if name and re.match(r'^[a-zA-Z\s]+$', name):
            validation_results['name'] = True
            formatted_info['name'] = name.title()
        else:
            formatted_info['name'] = "Invalid Name"

        # Validate and format email
        email = contact_info.get('email', '').strip()
        if email and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            validation_results['email'] = True
            formatted_info['email'] = email.lower()
        else:
            formatted_info['email'] = "Invalid Email"

        # Validate and format phone (should be 10 digits)
        phone = contact_info.get('phone', '').strip()
        if phone and re.match(r'^\d{10}$', phone):
            validation_results['phone'] = True
            formatted_info['phone'] = phone
        else:
            formatted_info['phone'] = "Invalid Phone"

        # Validate office (should be one of predefined office locations)
        office_locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
        office = contact_info.get('office', '').strip()
        if office in office_locations:
            validation_results['office'] = True
            formatted_info['office'] = office
        else:
            formatted_info['office'] = "Invalid Office"
    except Exception as e:
        # Catch unexpected errors
        return {"error": str(e), "validation_results": validation_results}

    return {"validation_results": validation_results, "formatted_info": formatted_info}


def main():
    """
    Entry point for the script. 
    Collects and validates contact information for the legal firm.
    """
    print("Welcome to Ramdays Legal Firm Contact Validator")

    # Example data for validation
    contact_list = [
        {"name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890", "office": "New York"},
        {"name": "Jane Smith", "email": "jane.smith@ramdays.com", "phone": "0987654321", "office": "Los Angeles"},
        {"name": "Invalid User", "email": "invalid.email", "phone": "55555", "office": "Unknown Office"}
    ]

    for contact in contact_list:
        result = validate_contact_info(contact)
        print(f"Input: {contact}")
        print(f"Validation Results: {result['validation_results']}")
        print(f"Formatted Info: {result['formatted_info']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
```
