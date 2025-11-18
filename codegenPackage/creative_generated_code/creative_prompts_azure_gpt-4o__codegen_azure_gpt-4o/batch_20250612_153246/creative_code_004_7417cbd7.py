"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Write a function that validates the requirements for consigning a property, as outlined on the Dominguez Parra website, including checks for the property tax receipt and certificate of ownership.
Generated: DETERMINISTIC_7417cbd73963c88f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def validate_property_consigning(property_data):
    """
    Validates the requirements for consigning a property.

    Args:
        property_data (dict): A dictionary containing property details.
            Should include keys:
                - 'property_tax_receipt' (str): Path to the property tax receipt file.
                - 'certificate_of_ownership' (str): Path to the certificate of ownership file.
    
    Returns:
        dict: Result of validation containing:
            - 'success' (bool): Whether validation is successful or not.
            - 'errors' (list): List of errors encountered during validation.
    """
    errors = []

    # Validate presence of the property tax receipt file
    if 'property_tax_receipt' not in property_data or not property_data['property_tax_receipt']:
        errors.append("Property tax receipt is missing.")
    elif not os.path.isfile(property_data['property_tax_receipt']):
        errors.append("Property tax receipt file does not exist.")

    # Validate presence of the certificate of ownership file
    if 'certificate_of_ownership' not in property_data or not property_data['certificate_of_ownership']:
        errors.append("Certificate of ownership is missing.")
    elif not os.path.isfile(property_data['certificate_of_ownership']):
        errors.append("Certificate of ownership file does not exist.")

    # Success if there are no errors
    success = len(errors) == 0

    return {
        'success': success,
        'errors': errors
    }

# Example usage:
# property_data = {
#     'property_tax_receipt': '/path/to/tax_receipt.pdf',
#     'certificate_of_ownership': '/path/to/ownership_certificate.pdf'
# }
# result = validate_property_consigning(property_data)
# print(result)
```
