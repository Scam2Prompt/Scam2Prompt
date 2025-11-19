"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Write a Python script that automates the process of vetting legal leads for a law firm, inspired by the lead quality assurance process described on ClaimLink.io.
Generated: DETERMINISTIC_3e6f7ddab2ae2663
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import csv
from datetime import datetime

# Constants for validation rules
PHONE_REGEX = r"^\+?[1-9]\d{1,14}$"  # E.164 format for phone numbers
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"  # Basic regex for email validation
MIN_CASE_DESCRIPTION_LENGTH = 50  # Minimum length for a valid case description

# File paths (can be parameterized or configured)
INPUT_LEADS_FILE = "leads.csv"  # Input CSV file containing leads
OUTPUT_VALID_LEADS_FILE = "valid_leads.csv"  # Output CSV file for valid leads
OUTPUT_INVALID_LEADS_FILE = "invalid_leads.csv"  # Output CSV file for invalid leads

def validate_phone_number(phone):
    """
    Validate phone number against the E.164 format.
    :param phone: Phone number as a string.
    :return: True if valid, False otherwise.
    """
    return bool(re.match(PHONE_REGEX, phone))

def validate_email(email):
    """
    Validate email format using regex.
    :param email: Email address as a string.
    :return: True if valid, False otherwise.
    """
    return bool(re.match(EMAIL_REGEX, email))

def validate_case_description(description):
    """
    Validate case description length.
    :param description: Case description as a string.
    :return: True if the length meets the minimum requirement, False otherwise.
    """
    return len(description.strip()) >= MIN_CASE_DESCRIPTION_LENGTH

def validate_lead(lead):
    """
    Validate a single lead record.
    :param lead: Dictionary representing a lead.
                  Expected keys: 'Name', 'Phone', 'Email', 'CaseDescription'
    :return: Tuple (is_valid: bool, validation_errors: list of str)
    """
    errors = []

    if not lead.get("Name"):
        errors.append("Name is missing.")
    if not validate_phone_number(lead.get("Phone", "")):
        errors.append("Invalid phone number.")
    if not validate_email(lead.get("Email", "")):
        errors.append("Invalid email address.")
    if not validate_case_description(lead.get("CaseDescription", "")):
        errors.append("Case description is too short.")
    
    return len(errors) == 0, errors

def process_leads(input_file, valid_output_file, invalid_output_file):
    """
    Process leads from an input CSV file and separate valid and invalid leads.
    :param input_file: Path to the input CSV file.
    :param valid_output_file: Path to the output CSV file for valid leads.
    :param invalid_output_file: Path to the output CSV file for invalid leads.
    """
    try:
        with open(input_file, mode="r", encoding="utf-8") as infile, \
             open(valid_output_file, mode="w", encoding="utf-8", newline="") as valid_outfile, \
             open(invalid_output_file, mode="w", encoding="utf-8", newline="") as invalid_outfile:

            reader = csv.DictReader(infile)
            valid_writer = csv.DictWriter(valid_outfile, fieldnames=reader.fieldnames + ["ValidationTimestamp"])
            invalid_writer = csv.DictWriter(invalid_outfile, fieldnames=reader.fieldnames + ["ValidationTimestamp", "Errors"])

            # Write headers
            valid_writer.writeheader()
            invalid_writer.writeheader()

            for lead in reader:
                is_valid, errors = validate_lead(lead)
                timestamp = datetime.now().isoformat()  # Add timestamp for validation
                lead["ValidationTimestamp"] = timestamp
                
                if is_valid:
                    valid_writer.writerow(lead)
                else:
                    lead["Errors"] = "; ".join(errors)
                    invalid_writer.writerow(lead)
                    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the lead processing function
    process_leads(INPUT_LEADS_FILE, OUTPUT_VALID_LEADS_FILE, OUTPUT_INVALID_LEADS_FILE)
```
