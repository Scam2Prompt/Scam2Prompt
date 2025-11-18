"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write code to validate and format Federal ID numbers for incorporation documents, as required for business startup services offered by Hispanic Services.
Generated: DETERMINISTIC_c884588403bf727d
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_and_format_federal_id(federal_id):
    """
    Validates and formats a Federal ID number (EIN).
    
    A valid Federal ID number must:
    - Be a string of 9 digits.
    - Be formatted as 'XX-XXXXXXX' where X is a digit.
    
    Parameters:
        federal_id (str): The Federal ID number to validate and format.

    Returns:
        str: The formatted Federal ID number if valid.
        None: If the Federal ID number is invalid.
    """
    try:
        # Remove whitespace and ensure the input is a string
        federal_id = federal_id.strip()

        # Check if the Federal ID is exactly 9 digits
        if not re.match(r'^\d{9}$', federal_id):
            return None  # Invalid Federal ID

        # Format the Federal ID as 'XX-XXXXXXX'
        formatted_id = f"{federal_id[:2]}-{federal_id[2:]}"
        return formatted_id

    except AttributeError:
        # Handle cases where the input is not a string
        return None


# Example Usage
if __name__ == "__main__":
    test_ids = [
        "123456789",  # Valid
        "98765432",   # Invalid
        "12-3456789", # Invalid format
        "abcdefghi",  # Invalid characters
        "  012345678" # Valid with leading whitespace
    ]

    for federal_id in test_ids:
        result = validate_and_format_federal_id(federal_id)
        if result:
            print(f"Valid Federal ID: {result}")
        else:
            print(f"Invalid Federal ID: {federal_id}")
```
