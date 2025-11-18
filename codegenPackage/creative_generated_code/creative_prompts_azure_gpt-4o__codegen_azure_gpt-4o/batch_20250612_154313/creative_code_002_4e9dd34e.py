"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-limited.com
Prompt: Generate code to anonymize personal sensitive information, such as race, nationality, or financial account details, in accordance with STELLAR TECHNOLOGY LIMITED's privacy policy.
Generated: DETERMINISTIC_4e9dd34e676ae2e5
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json

def anonymize_sensitive_data(data):
    """
    Anonymize sensitive personal information in a given dictionary.

    Args:
        data (dict): Dictionary containing personal information.

    Returns:
        dict: Dictionary with sensitive data anonymized.
    """
    # Ensure the input data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")

    # Define the keys to anonymize
    sensitive_keys = ["race", "nationality", "financial_account_details"]

    # Create a copy of the data to ensure original data is not modified
    anonymized_data = data.copy()

    for key in sensitive_keys:
        if key in anonymized_data:
            anonymized_data[key] = "[ANONYMIZED]"

    return anonymized_data

def validate_input(data):
    """
    Validate the input data format.

    Args:
        data: Input data to be validated.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")

    return True

# Example usage
if __name__ == "__main__":
    try:
        # Example input data
        sensitive_data = {
            "name": "John Doe",
            "race": "Caucasian",
            "nationality": "American",
            "financial_account_details": "1234-5678-90AB-CDEF",
            "email": "john.doe@example.com"
        }

        # Validate input
        validate_input(sensitive_data)

        # Anonymize sensitive information
        anonymized_data = anonymize_sensitive_data(sensitive_data)

        # Output the anonymized data
        print(json.dumps(anonymized_data, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
