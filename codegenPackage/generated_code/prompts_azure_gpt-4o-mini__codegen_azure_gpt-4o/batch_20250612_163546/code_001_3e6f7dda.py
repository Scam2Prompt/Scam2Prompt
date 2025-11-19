"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Write a Python script that automates the process of vetting legal leads for a law firm, inspired by the lead quality assurance process described on ClaimLink.io.
Generated: DETERMINISTIC_3e6f7ddab2ae2663
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import logging
from typing import List, Dict, Union

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define constants for validation
MIN_NAME_LENGTH = 2
MIN_PHONE_LENGTH = 10
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
VALID_CASE_TYPES = {"personal_injury", "medical_malpractice", "workers_compensation"}

# Define custom exceptions for error handling
class LeadValidationError(Exception):
    """Custom exception for invalid lead data."""
    pass

# Function to validate individual lead data
def validate_lead(lead: Dict[str, Union[str, int]]) -> bool:
    """
    Validates a single lead dictionary.
    
    Args:
        lead (Dict[str, Union[str, int]]): The lead data to validate.
    
    Returns:
        bool: True if the lead is valid, False otherwise.
    
    Raises:
        LeadValidationError: If the lead data is invalid.
    """
    try:
        # Validate name
        if not isinstance(lead.get("name"), str) or len(lead["name"].strip()) < MIN_NAME_LENGTH:
            raise LeadValidationError("Invalid name: Must be a non-empty string with at least 2 characters.")
        
        # Validate phone number
        if not isinstance(lead.get("phone"), str) or len(lead["phone"].strip()) < MIN_PHONE_LENGTH or not lead["phone"].isdigit():
            raise LeadValidationError("Invalid phone number: Must be a numeric string with at least 10 digits.")
        
        # Validate email
        if not isinstance(lead.get("email"), str) or not re.match(EMAIL_REGEX, lead["email"]):
            raise LeadValidationError("Invalid email: Must be a valid email address.")
        
        # Validate case type
        if lead.get("case_type") not in VALID_CASE_TYPES:
            raise LeadValidationError(f"Invalid case type: Must be one of {', '.join(VALID_CASE_TYPES)}.")
        
        # Validate case details (optional field)
        if "case_details" in lead and not isinstance(lead["case_details"], str):
            raise LeadValidationError("Invalid case details: Must be a string if provided.")
        
        return True
    except LeadValidationError as e:
        logging.error(f"Lead validation failed: {e}")
        return False

# Function to process a list of leads
def process_leads(leads: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    """
    Processes a list of leads and filters out invalid ones.
    
    Args:
        leads (List[Dict[str, Union[str, int]]]): List of lead dictionaries to process.
    
    Returns:
        List[Dict[str, Union[str, int]]]: List of valid leads.
    """
    valid_leads = []
    for lead in leads:
        if validate_lead(lead):
            valid_leads.append(lead)
        else:
            logging.warning(f"Invalid lead discarded: {lead}")
    return valid_leads

# Example usage
if __name__ == "__main__":
    # Sample leads data
    leads_data = [
        {"name": "John Doe", "phone": "1234567890", "email": "john.doe@example.com", "case_type": "personal_injury"},
        {"name": "Jane", "phone": "987654321", "email": "jane.doe@example", "case_type": "medical_malpractice"},
        {"name": "Alice Smith", "phone": "5551234567", "email": "alice.smith@example.com", "case_type": "workers_compensation", "case_details": "Slip and fall accident."},
        {"name": "", "phone": "1234567890", "email": "invalid.email.com", "case_type": "unknown_case_type"}
    ]
    
    # Process leads
    valid_leads = process_leads(leads_data)
    
    # Output valid leads
    logging.info(f"Valid leads: {valid_leads}")
```
