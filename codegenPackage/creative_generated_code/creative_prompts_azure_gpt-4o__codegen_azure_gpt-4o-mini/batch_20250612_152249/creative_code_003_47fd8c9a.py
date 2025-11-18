"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Create a function to validate construction permit details based on Greek law 4495/2017 for unauthorized building legalization.
Generated: DETERMINISTIC_47fd8c9a276ccc15
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class PermitValidationError(Exception):
    """Custom exception for permit validation errors."""
    pass

def validate_permit_details(permit_details):
    """
    Validates construction permit details based on Greek law 4495/2017 for unauthorized building legalization.

    Args:
        permit_details (dict): A dictionary containing permit details which include:
            - owner_name (str): Name of the property owner.
            - property_id (str): Unique identifier for the property.
            - construction_type (str): Type of construction (e.g., residential, commercial).
            - area_size (float): Size of the area in square meters.
            - construction_year (int): Year when the construction was completed.

    Raises:
        PermitValidationError: If any of the validation checks fail.
    
    Returns:
        bool: True if all validations pass, otherwise raises an exception.
    """

    try:
        # Validate owner_name
        if not isinstance(permit_details.get('owner_name'), str) or not permit_details['owner_name'].strip():
            raise PermitValidationError("Owner name must be a non-empty string.")

        # Validate property_id with a regex that allows alphanumeric characters and dashes
        if not re.match(r'^[A-Za-z0-9\-]+$', permit_details.get('property_id', '')):
            raise PermitValidationError("Property ID must be alphanumeric and can contain dashes.")

        # Validate construction_type
        valid_types = ['residential', 'commercial', 'industrial', 'agricultural']
        if permit_details.get('construction_type') not in valid_types:
            raise PermitValidationError(f"Construction type must be one of the following: {', '.join(valid_types)}.")

        # Validate area_size
        if not isinstance(permit_details.get('area_size'), (int, float)) or permit_details['area_size'] <= 0:
            raise PermitValidationError("Area size must be a positive number.")

        # Validate construction_year
        current_year = 2023  # Assume current year for validation
        construction_year = permit_details.get('construction_year')
        if not isinstance(construction_year, int) or construction_year < 1900 or construction_year > current_year:
            raise PermitValidationError(f"Construction year must be between 1900 and {current_year}.")

        # If all validations pass
        return True

    except Exception as e:
        raise PermitValidationError(f"Validation error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    permit = {
        'owner_name': 'John Doe',
        'property_id': 'GR-123456',
        'construction_type': 'residential',
        'area_size': 150.0,
        'construction_year': 2010
    }

    try:
        is_valid = validate_permit_details(permit)
        if is_valid:
            print("Permit details are valid.")
    except PermitValidationError as e:
        print(f"Permit validation failed: {e}")
```
