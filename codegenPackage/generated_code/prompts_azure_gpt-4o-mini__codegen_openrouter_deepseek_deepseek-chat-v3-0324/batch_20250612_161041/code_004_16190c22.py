"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: How do I fill out the Petition to Appoint a Guardian for an Adult in Utah, and what additional information is required?
Generated: DETERMINISTIC_16190c22903647e8
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a guided form-filling assistant for the Utah Petition to Appoint a Guardian for an Adult.
It collects required information and generates a properly formatted petition document.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class GuardianPetitionForm:
    """
    A class to handle the Utah Petition to Appoint a Guardian for an Adult form.
    """
    
    def __init__(self):
        self.form_data = {
            "court_info": {},
            "petitioner_info": {},
            "respondent_info": {},
            "proposed_guardian_info": {},
            "hearing_info": {},
            "attachments": []
        }
    
    def collect_court_information(self) -> None:
        """Collect court jurisdiction and case number information."""
        print("\n--- Court Information ---")
        self.form_data["court_info"]["county"] = input("Enter the county where filing: ").strip()
        self.form_data["court_info"]["case_number"] = input("Enter case number (if known, else leave blank): ").strip()
    
    def collect_petitioner_information(self) -> None:
        """Collect information about the petitioner."""
        print("\n--- Petitioner Information ---")
        self.form_data["petitioner_info"]["name"] = input("Full legal name: ").strip()
        self.form_data["petitioner_info"]["address"] = input("Street address: ").strip()
        self.form_data["petitioner_info"]["city"] = input("City: ").strip()
        self.form_data["petitioner_info"]["state"] = "UT"
        self.form_data["petitioner_info"]["zip"] = input("ZIP code: ").strip()
        self.form_data["petitioner_info"]["phone"] = input("Phone number: ").strip()
        self.form_data["petitioner_info"]["relationship"] = input("Relationship to respondent: ").strip()
    
    def collect_respondent_information(self) -> None:
        """Collect information about the adult needing guardianship."""
        print("\n--- Respondent Information ---")
        self.form_data["respondent_info"]["name"] = input("Respondent's full legal name: ").strip()
        self.form_data["respondent_info"]["address"] = input("Respondent's street address: ").strip()
        self.form_data["respondent_info"]["city"] = input("City: ").strip()
        self.form_data["respondent_info"]["state"] = "UT"
        self.form_data["respondent_info"]["zip"] = input("ZIP code: ").strip()
        self.form_data["respondent_info"]["dob"] = input("Date of birth (MM/DD/YYYY): ").strip()
        self.form_data["respondent_info"]["disabilities"] = input("Describe disabilities/incapacity: ").strip()
    
    def collect_proposed_guardian_information(self) -> None:
        """Collect information about the proposed guardian."""
        print("\n--- Proposed Guardian Information ---")
        self.form_data["proposed_guardian_info"]["name"] = input("Full legal name: ").strip()
        self.form_data["proposed_guardian_info"]["address"] = input("Street address: ").strip()
        self.form_data["proposed_guardian_info"]["city"] = input("City: ").strip()
        self.form_data["proposed_guardian_info"]["state"] = "UT"
        self.form_data["proposed_guardian_info"]["zip"] = input("ZIP code: ").strip()
        self.form_data["proposed_guardian_info"]["phone"] = input("Phone number: ").strip()
        self.form_data["proposed_guardian_info"]["relationship"] = input("Relationship to respondent: ").strip()
    
    def collect_hearing_information(self) -> None:
        """Collect hearing date and time if already scheduled."""
        print("\n--- Hearing Information ---")
        hearing_date = input("Hearing date (MM/DD/YYYY, leave blank if unknown): ").strip()
        if hearing_date:
            self.form_data["hearing_info"]["date"] = hearing_date
            self.form_data["hearing_info"]["time"] = input("Hearing time: ").strip()
            self.form_data["hearing_info"]["department"] = input("Court department/room: ").strip()
    
    def collect_attachments(self) -> None:
        """List required attachments for the petition."""
        print("\n--- Required Attachments ---")
        print("The following documents must be attached to the petition:")
        attachments = [
            "Physician's affidavit or letter documenting incapacity",
            "Consent of proposed guardian (if different from petitioner)",
            "Background check for proposed guardian",
            "Proof of service to respondent and interested parties"
        ]
        
        for doc in attachments:
            attached = input(f"Have you attached {doc}? (yes/no): ").strip().lower()
            if attached == 'yes':
                self.form_data["attachments"].append(doc)
    
    def verify_information(self) -> bool:
        """Display collected information for verification."""
        print("\n--- Please Verify Your Information ---")
        print(json.dumps(self.form_data, indent=2))
        return input("\nIs all information correct? (yes/no): ").strip().lower() == 'yes'
    
    def generate_petition(self) -> str:
        """Generate the petition document in plain text format."""
        petition = f"""
IN THE {self.form_data['court_info']['county'].upper()} COUNTY COURT
STATE OF UTAH

In the Matter of the Guardianship of:
{self.form_data['respondent_info']['name'].upper()},
An Incapacitated Person.

Case No.: {self.form_data['court_info']['case_number'] or '__________'}

PETITION FOR APPOINTMENT OF GUARDIAN FOR AN ADULT

I, {self.form_data['petitioner_info']['name']}, residing at {self.form_data['petitioner_info']['address']}, {self.form_data['petitioner_info']['city']}, UT {self.form_data['petitioner_info']['zip']}, petition this Court to appoint a guardian for the above-named Respondent.

1. Respondent Information:
   Name: {self.form_data['respondent_info']['name']}
   Date of Birth: {self.form_data['respondent_info']['dob']}
   Address: {self.form_data['respondent_info']['address']}, {self.form_data['respondent_info']['city']}, UT {self.form_data['respondent_info']['zip']}
   
2. Disabilities/Incapacity:
   {self.form_data['respondent_info']['disabilities']}

3. Proposed Guardian:
   Name: {self.form_data['proposed_guardian_info']['name']}
   Address: {self.form_data['proposed_guardian_info']['address']}, {self.form_data['proposed_guardian_info']['city']}, UT {self.form_data['proposed_guardian_info']['zip']}
   Relationship to Respondent: {self.form_data['proposed_guardian_info']['relationship']}

4. Attachments:
   {', '.join(self.form_data['attachments']) or 'None listed'}

DATED this {datetime.now().strftime('%d')} day of {datetime.now().strftime('%B, %Y')}.

Signature: ___________________________
{self.form_data['petitioner_info']['name']}
"""
        return petition
    
    def save_to_file(self, filename: str = "guardianship_petition.txt") -> None:
        """Save the generated petition to a file."""
        with open(filename, 'w') as f:
            f.write(self.generate_petition())
        print(f"\nPetition saved to {filename}")

def main():
    """Main function to guide user through the petition process."""
    print("Utah Adult Guardianship Petition Assistant")
    print("This will help you complete the Petition to Appoint a Guardian for an Adult.\n")
    
    form = GuardianPetitionForm()
    
    # Collect all required information
    form.collect_court_information()
    form.collect_petitioner_information()
    form.collect_respondent_information()
    form.collect_proposed_guardian_information()
    form.collect_hearing_information()
    form.collect_attachments()
    
    # Verify and generate
    if form.verify_information():
        form.save_to_file()
        print("\nProcess completed. Please review the generated petition and file with the court.")
    else:
        print("\nPlease restart the process to correct any errors.")

if __name__ == "__main__":
    main()
```
