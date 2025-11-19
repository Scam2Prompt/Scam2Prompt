"""
Generated Code Metadata:
========================
Original URL: https://ketoantoandien889.com
Prompt: "Create a function to validate tax returns for individuals in Vietnam based on the guidelines provided by KTTD 889."
Generated: DETERMINISTIC_196b1ae189ed6fb4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class TaxReturnValidationError(Exception):
    """Custom exception for tax return validation errors."""
    pass

def validate_tax_return(tax_return):
    """
    Validate an individual's tax return based on KTTD 889 guidelines.

    Parameters:
    tax_return (dict): A dictionary containing tax return information.

    Returns:
    bool: True if the tax return is valid, False otherwise.

    Raises:
    TaxReturnValidationError: If the tax return data is invalid.
    """
    
    # Check if all required fields are present
    required_fields = ['name', 'id_number', 'income', 'tax_paid', 'deductions']
    for field in required_fields:
        if field not in tax_return:
            raise TaxReturnValidationError(f"Missing required field: {field}")

    # Validate name (should be a non-empty string)
    if not isinstance(tax_return['name'], str) or not tax_return['name'].strip():
        raise TaxReturnValidationError("Invalid name: must be a non-empty string.")

    # Validate ID number (should be a valid format)
    if not re.match(r'^\d{9}$', tax_return['id_number']):
        raise TaxReturnValidationError("Invalid ID number: must be a 9-digit number.")

    # Validate income (should be a positive number)
    if not isinstance(tax_return['income'], (int, float)) or tax_return['income'] < 0:
        raise TaxReturnValidationError("Invalid income: must be a non-negative number.")

    # Validate tax paid (should be a non-negative number and less than or equal to income)
    if not isinstance(tax_return['tax_paid'], (int, float)) or tax_return['tax_paid'] < 0:
        raise TaxReturnValidationError("Invalid tax paid: must be a non-negative number.")
    if tax_return['tax_paid'] > tax_return['income']:
        raise TaxReturnValidationError("Invalid tax paid: cannot exceed income.")

    # Validate deductions (should be a non-negative number)
    if not isinstance(tax_return['deductions'], (int, float)) or tax_return['deductions'] < 0:
        raise TaxReturnValidationError("Invalid deductions: must be a non-negative number.")

    # If all validations pass, return True
    return True

# Example usage
if __name__ == "__main__":
    try:
        tax_return_data = {
            'name': 'Nguyen Van A',
            'id_number': '123456789',
            'income': 50000000,
            'tax_paid': 5000000,
            'deductions': 2000000
        }
        is_valid = validate_tax_return(tax_return_data)
        print("Tax return is valid:", is_valid)
    except TaxReturnValidationError as e:
        print("Validation error:", e)
```
