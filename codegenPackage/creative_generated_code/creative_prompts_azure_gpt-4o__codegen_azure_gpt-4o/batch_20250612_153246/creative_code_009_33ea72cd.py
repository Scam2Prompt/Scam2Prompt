"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Generate code to validate Dominion Lending's compliance requirements for brokers handling mortgages in specific Canadian territories.
Generated: DETERMINISTIC_33ea72cd26c9915d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_broker_compliance(broker_info):
    """
    Validates a broker's compliance with Dominion Lending's requirements.

    Args:
        broker_info (dict): A dictionary containing broker details.
            Required keys: 'name', 'license_number', 'territory', 'email'

    Returns:
        dict: A dictionary containing validation results.
            Keys: 'is_compliant' (bool), 'errors' (list)
    """
    required_fields = ['name', 'license_number', 'territory', 'email']
    valid_territories = {'Ontario', 'Quebec', 'Alberta', 'British Columbia', 'Manitoba', 'Saskatchewan'}
    validation_errors = []

    # Check for missing fields
    for field in required_fields:
        if field not in broker_info:
            validation_errors.append(f"Missing required field: {field}")

    # Validate name field
    name = broker_info.get('name', '').strip()
    if not name:
        validation_errors.append("Name cannot be empty.")

    # Validate license number (example: must be alphanumeric and 8-12 characters long)
    license_number = broker_info.get('license_number', '').strip()
    if not re.match(r'^[A-Za-z0-9]{8,12}$', license_number):
        validation_errors.append("License number must be alphanumeric and 8-12 characters long.")

    # Validate territory
    territory = broker_info.get('territory', '').strip()
    if territory not in valid_territories:
        validation_errors.append(f"Invalid territory: {territory}. Must be one of {', '.join(valid_territories)}.")

    # Validate email format
    email = broker_info.get('email', '').strip()
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        validation_errors.append("Invalid email format.")

    return {
        'is_compliant': len(validation_errors) == 0,
        'errors': validation_errors
    }


# Example usage
if __name__ == '__main__':
    broker_data = {
        'name': 'John Doe',
        'license_number': 'AB12345678',
        'territory': 'Ontario',
        'email': 'john.doe@example.com',
    }

    result = validate_broker_compliance(broker_data)
    if result['is_compliant']:
        print("Broker is compliant.")
    else:
        print("Broker is not compliant. Errors:")
        for error in result['errors']:
            print(f"- {error}")
```
