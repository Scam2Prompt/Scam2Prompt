"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Write a script to parse the DEPED Cash Assistance application form from the PRC Board website and validate the required fields, such as "Mobile Phone Number" and "Email."
Generated: DETERMINISTIC_db2b161621d41a6b
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_form(data):
    """
    Function to validate DEPED Cash Assistance application form fields.
    
    Parameters:
        data (dict): Dictionary containing form fields and their values.
        
    Returns:
        dict: Dictionary with validation results for each field.
    """
    validation_results = {}
    
    # Validate Mobile Phone Number
    mobile_number = data.get("Mobile Phone Number", "")
    # Philippine mobile numbers typically start with +63 or 09 and have 10 digits after the prefix
    mobile_pattern = r"^(?:\+63|0)(\d{10})$"
    if re.match(mobile_pattern, mobile_number):
        validation_results["Mobile Phone Number"] = "Valid"
    else:
        validation_results["Mobile Phone Number"] = "Invalid. Must start with +63 or 09 and contain 10 digits."
    
    # Validate Email
    email = data.get("Email", "")
    # Basic email validation regex pattern
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(email_pattern, email):
        validation_results["Email"] = "Valid"
    else:
        validation_results["Email"] = "Invalid. Ensure the email is in the proper format (e.g., user@example.com)."
    
    return validation_results


if __name__ == "__main__":
    # Example usage
    form_data = {
        "Mobile Phone Number": "+639123456789",  # Replace with actual input
        "Email": "user@example.com"  # Replace with actual input
    }

    try:
        # Validate form fields
        results = validate_form(form_data)
        
        # Print validation results
        for field, result in results.items():
            print(f"{field}: {result}")
    
    except Exception as e:
        print(f"An error occurred while validating the form: {e}")
```
