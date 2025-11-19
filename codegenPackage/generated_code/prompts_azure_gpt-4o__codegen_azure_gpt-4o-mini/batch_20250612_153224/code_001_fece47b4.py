"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Create a Python function to validate the required fields for Apostille document processing, including passport copies, valid IDs, and authorization letters, as outlined in the Schengen Apostille process.
Generated: DETERMINISTIC_fece47b4bd94980b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_apostille_documents(documents: Dict[str, Any]) -> List[str]:
    """
    Validate the required fields for Apostille document processing.

    Args:
        documents (Dict[str, Any]): A dictionary containing document information.
            Expected keys are:
            - 'passport_copies': List of passport copy file paths
            - 'valid_ids': List of valid ID file paths
            - 'authorization_letters': List of authorization letter file paths

    Returns:
        List[str]: A list of validation error messages. If no errors, returns an empty list.

    Raises:
        ValidationError: If the documents dictionary is missing required fields.
    """
    required_fields = ['passport_copies', 'valid_ids', 'authorization_letters']
    errors = []

    # Check for missing required fields
    for field in required_fields:
        if field not in documents:
            errors.append(f"Missing required field: {field}")

    # Validate passport copies
    if 'passport_copies' in documents:
        if not isinstance(documents['passport_copies'], list) or not documents['passport_copies']:
            errors.append("Passport copies must be a non-empty list.")

    # Validate valid IDs
    if 'valid_ids' in documents:
        if not isinstance(documents['valid_ids'], list) or not documents['valid_ids']:
            errors.append("Valid IDs must be a non-empty list.")

    # Validate authorization letters
    if 'authorization_letters' in documents:
        if not isinstance(documents['authorization_letters'], list) or not documents['authorization_letters']:
            errors.append("Authorization letters must be a non-empty list.")

    # Raise an exception if there are validation errors
    if errors:
        raise ValidationError("Validation errors occurred: " + "; ".join(errors))

    return errors

# Example usage
if __name__ == "__main__":
    try:
        documents_to_validate = {
            'passport_copies': ['passport_copy1.pdf', 'passport_copy2.pdf'],
            'valid_ids': ['id_card1.pdf'],
            'authorization_letters': ['auth_letter1.pdf']
        }
        validation_errors = validate_apostille_documents(documents_to_validate)
        if not validation_errors:
            print("All documents are valid.")
        else:
            print("Validation errors:", validation_errors)
    except ValidationError as e:
        print(e)
```
