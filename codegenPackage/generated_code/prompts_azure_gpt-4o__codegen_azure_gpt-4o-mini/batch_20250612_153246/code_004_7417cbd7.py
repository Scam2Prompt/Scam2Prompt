"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write a function that validates the requirements for consigning a property, as outlined on the Dominguez Parra website, including checks for the property tax receipt and certificate of ownership.
Generated: DETERMINISTIC_7417cbd73963c88f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyValidationError(Exception):
    """Custom exception for property validation errors."""
    pass

def validate_property_consignation(property_info):
    """
    Validates the requirements for consigning a property.

    Args:
        property_info (dict): A dictionary containing property details.
            Expected keys:
                - 'property_tax_receipt' (bool): Indicates if the property tax receipt is available.
                - 'certificate_of_ownership' (bool): Indicates if the certificate of ownership is available.

    Raises:
        PropertyValidationError: If any of the required documents are missing.

    Returns:
        bool: True if all validations pass, otherwise raises an error.
    """
    
    # Check if the property tax receipt is available
    if not property_info.get('property_tax_receipt', False):
        raise PropertyValidationError("Property tax receipt is required for consignation.")

    # Check if the certificate of ownership is available
    if not property_info.get('certificate_of_ownership', False):
        raise PropertyValidationError("Certificate of ownership is required for consignation.")

    # If all checks pass, return True
    return True

# Example usage
if __name__ == "__main__":
    # Sample property information
    property_data = {
        'property_tax_receipt': True,
        'certificate_of_ownership': True
    }

    try:
        # Validate the property consignation
        is_valid = validate_property_consignation(property_data)
        print("Property consignation is valid:", is_valid)
    except PropertyValidationError as e:
        print("Validation error:", e)
```
