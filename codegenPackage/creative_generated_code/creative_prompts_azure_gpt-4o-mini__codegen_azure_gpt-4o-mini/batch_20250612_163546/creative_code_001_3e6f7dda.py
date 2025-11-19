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
import csv
import logging
from typing import List, Dict

# Configure logging for tracking the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Lead:
    """Class to represent a legal lead with relevant attributes."""

    def __init__(self, name: str, contact_info: str, case_type: str, status: str):
        self.name = name
        self.contact_info = contact_info
        self.case_type = case_type
        self.status = status

    def is_valid(self) -> bool:
        """Check if the lead has valid information."""
        return bool(self.name and self.contact_info and self.case_type and self.status)

class LeadVetter:
    """Class to vet legal leads based on predefined criteria."""

    def __init__(self, leads: List[Lead]):
        self.leads = leads

    def vet_leads(self) -> List[Lead]:
        """Filter and return only the valid leads."""
        valid_leads = [lead for lead in self.leads if lead.is_valid()]
        logging.info(f"Vetted leads: {len(valid_leads)} valid out of {len(self.leads)} total leads.")
        return valid_leads

def load_leads_from_csv(file_path: str) -> List[Lead]:
    """Load leads from a CSV file and return a list of Lead objects."""
    leads = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lead = Lead(
                    name=row.get('Name', ''),
                    contact_info=row.get('ContactInfo', ''),
                    case_type=row.get('CaseType', ''),
                    status=row.get('Status', '')
                )
                leads.append(lead)
    except FileNotFoundError:
        logging.error("The specified CSV file was not found.")
    except Exception as e:
        logging.error(f"An error occurred while reading the CSV file: {e}")
    
    return leads

def save_valid_leads_to_csv(leads: List[Lead], file_path: str) -> None:
    """Save vetted leads to a new CSV file."""
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'ContactInfo', 'CaseType', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for lead in leads:
                writer.writerow({
                    'Name': lead.name,
                    'ContactInfo': lead.contact_info,
                    'CaseType': lead.case_type,
                    'Status': lead.status
                })
        logging.info(f"Successfully saved {len(leads)} valid leads to {file_path}.")
    except Exception as e:
        logging.error(f"An error occurred while saving leads to CSV: {e}")

def main(input_file: str, output_file: str) -> None:
    """Main function to execute lead vetting."""
    leads = load_leads_from_csv(input_file)
    vetter = LeadVetter(leads)
    valid_leads = vetter.vet_leads()
    save_valid_leads_to_csv(valid_leads, output_file)

if __name__ == "__main__":
    input_csv_file = 'leads.csv'  # Input CSV file path
    output_csv_file = 'valid_leads.csv'  # Output CSV file path
    main(input_csv_file, output_csv_file)
```
