"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Generate code to validate the authenticity of temporary registration documents in Adygea, considering the warnings provided on the website about fraudulent registrations.
Generated: DETERMINISTIC_446652991ba617bc
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_registration_document(doc_number: str, issued_date: str, expiration_date: str) -> bool:
    """
    Validates the authenticity of a temporary registration document in Adygea.
    
    Parameters:
    - doc_number (str): Registration document number (should follow specific pattern, e.g., AA-123456).
    - issued_date (str): The date the document was issued (expected format: YYYY-MM-DD).
    - expiration_date (str): The date the document expires (expected format: YYYY-MM-DD).
    
    Returns:
    - bool: True if the document passes validation, False otherwise.
    """
    try:
        # Validate document number format using regex
        doc_pattern = r"^[A-Z]{2}-\d{6}$"
        if not re.match(doc_pattern, doc_number):
            print("Error: Invalid document number format.")
            return False

        # Validate date formats
        issued_date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        expiration_date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(issued_date_pattern, issued_date) or not re.match(expiration_date_pattern, expiration_date):
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return False

        # Ensure issued_date is before expiration_date
        from datetime import datetime
        issued_date_obj = datetime.strptime(issued_date, '%Y-%m-%d')
        expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d')
        if issued_date_obj >= expiration_date_obj:
            print("Error: Issued date must be earlier than the expiration date.")
            return False

        # Validate against known fraudulent patterns (this is an example and should be replaced with real data)
        fraudulent_patterns = ["XX-000000", "ZZ-123456"]  # Example fraudulent document numbers
        if doc_number in fraudulent_patterns:
            print("Warning: Document matches known fraudulent patterns.")
            return False

        # Validation passed
        print("Document is valid.")
        return True

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred during validation: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Example data for testing
    doc_num = "AA-123456"
    issued = "2023-01-01"
    expiration = "2023-12-31"

    # Validate a document
    is_valid = validate_registration_document(doc_num, issued, expiration)
    print("Validation result:", is_valid)
```
