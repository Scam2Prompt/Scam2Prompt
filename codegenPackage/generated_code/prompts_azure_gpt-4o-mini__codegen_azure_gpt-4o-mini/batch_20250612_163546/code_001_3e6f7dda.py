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
import csv
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Lead:
    """Class representing a legal lead."""
    
    def __init__(self, name: str, email: str, phone: str, case_type: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.case_type = case_type

    def is_valid(self) -> bool:
        """Validate the lead's information."""
        return self.validate_email() and self.validate_phone()

    def validate_email(self) -> bool:
        """Check if the email is valid."""
        return "@" in self.email and "." in self.email

    def validate_phone(self) -> bool:
        """Check if the phone number is valid (simple check)."""
        return len(self.phone) >= 10 and self.phone.isdigit()

def read_leads_from_csv(file_path: str) -> List[Lead]:
    """Read leads from a CSV file and return a list of Lead objects."""
    leads = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lead = Lead(name=row['Name'], email=row['Email'], phone=row['Phone'], case_type=row['CaseType'])
                leads.append(lead)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while reading the CSV file: {e}")
    return leads

def vet_leads(leads: List[Lead]) -> List[Lead]:
    """Vet leads and return only valid leads."""
    valid_leads = []
    for lead in leads:
        if lead.is_valid():
            valid_leads.append(lead)
            logging.info(f"Valid lead: {lead.name} - {lead.email}")
        else:
            logging.warning(f"Invalid lead: {lead.name} - {lead.email}")
    return valid_leads

def write_valid_leads_to_csv(valid_leads: List[Lead], output_file_path: str) -> None:
    """Write valid leads to a new CSV file."""
    try:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Email', 'Phone', 'CaseType']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for lead in valid_leads:
                writer.writerow({'Name': lead.name, 'Email': lead.email, 'Phone': lead.phone, 'CaseType': lead.case_type})
        logging.info(f"Valid leads written to {output_file_path}")
    except Exception as e:
        logging.error(f"An error occurred while writing to the CSV file: {e}")

def main(input_file: str, output_file: str) -> None:
    """Main function to vet legal leads."""
    leads = read_leads_from_csv(input_file)
    valid_leads = vet_leads(leads)
    write_valid_leads_to_csv(valid_leads, output_file)

if __name__ == "__main__":
    # Example usage
    input_csv_file = 'leads.csv'  # Input CSV file containing leads
    output_csv_file = 'valid_leads.csv'  # Output CSV file for valid leads
    main(input_csv_file, output_csv_file)
```
