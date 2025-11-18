"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate code to validate user input for a claim submission form based on the requirements outlined by Financial Recovery Solutions Ltd, ensuring eligibility for PPI or packaged bank account claims.
Generated: DETERMINISTIC_31dd2c05a262591c
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_claim_submission(data):
    """
    Validate user input for a claim submission form.

    Args:
        data (dict): A dictionary containing the user's input.

    Returns:
        dict: A dictionary with validation results and error messages (if any).
    """
    # Initialize result dictionary
    validation_result = {
        "is_valid": True,
        "errors": []
    }
    
    # Define validation rules
    required_fields = ["name", "email", "phone", "claim_type", "account_number"]
    claim_types = ["PPI", "Packaged Bank Account"]
    
    # Check for missing required fields
    for field in required_fields:
        if field not in data or not data[field].strip():
            validation_result["is_valid"] = False
            validation_result["errors"].append(f"{field} is required.")
    
    # Validate name (should be alphabetic and have at least two characters)
    if "name" in data and data["name"].strip():
        if not re.match(r"^[a-zA-Z\s]{2,}$", data["name"].strip()):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Name should contain only letters and be at least two characters long.")
    
    # Validate email (basic email format matching)
    if "email" in data and data["email"].strip():
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, data["email"].strip()):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Invalid email format.")
    
    # Validate phone number (basic UK phone number format)
    if "phone" in data and data["phone"].strip():
        phone_regex = r"^\+?44?\d{10}$"
        if not re.match(phone_regex, data["phone"].strip()):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Phone number must be a valid UK number.")
    
    # Validate claim type (must be one of the predefined types)
    if "claim_type" in data and data["claim_type"].strip():
        if data["claim_type"].strip() not in claim_types:
            validation_result["is_valid"] = False
            validation_result["errors"].append("Claim type must be either 'PPI' or 'Packaged Bank Account'.")
    
    # Validate account number (simple numeric validation, must be 8-10 digits)
    if "account_number" in data and data["account_number"].strip():
        if not re.match(r"^\d{8,10}$", data["account_number"].strip()):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Account number must be 8 to 10 digits long.")
    
    return validation_result


# Example usage
if __name__ == "__main__":
    # Sample user input
    user_input = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "07123456789",
        "claim_type": "PPI",
        "account_number": "12345678"
    }
    
    result = validate_claim_submission(user_input)
    if result["is_valid"]:
        print("Validation successful. Ready for submission.")
    else:
        print("Validation failed:")
        for error in result["errors"]:
            print(f"- {error}")
```
