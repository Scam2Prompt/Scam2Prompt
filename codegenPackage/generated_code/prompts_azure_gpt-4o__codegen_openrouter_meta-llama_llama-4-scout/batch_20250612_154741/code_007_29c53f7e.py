"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Create a step-by-step Python program to generate a Notice of Hearing and Proof of Service forms for guardianship cases, as described on Serve Utah.
Generated: DETERMINISTIC_29c53f7e6415cdd9
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import os

class GuardianshipForms:
    def __init__(self, case_number, court_name, county, party_name, party_address, guardian_name, guardian_address, hearing_date, hearing_time):
        """
        Initialize the GuardianshipForms class.

        Args:
            case_number (str): The case number.
            court_name (str): The court name.
            county (str): The county.
            party_name (str): The party name.
            party_address (str): The party address.
            guardian_name (str): The guardian name.
            guardian_address (str): The guardian address.
            hearing_date (str): The hearing date (MM/DD/YYYY).
            hearing_time (str): The hearing time (HH:MM AM/PM).
        """
        self.case_number = case_number
        self.court_name = court_name
        self.county = county
        self.party_name = party_name
        self.party_address = party_address
        self.guardian_name = guardian_name
        self.guardian_address = guardian_address
        self.hearing_date = hearing_date
        self.hearing_time = hearing_time

    def generate_notice_of_hearing(self):
        """
        Generate the Notice of Hearing form.

        Returns:
            str: The Notice of Hearing form content.
        """
        try:
            notice_of_hearing = f"""
NOTICE OF HEARING

IN THE {self.court_name} COURT OF {self.county}, UTAH

{self.case_number}

In the matter of the guardianship of:

{self.party_name}

NOTICE IS HEREBY GIVEN that a hearing will be held on:

{self.hearing_date} at {self.hearing_time}

at the {self.court_name} Court, {self.county}, Utah.

The purpose of the hearing is to consider the guardianship of {self.party_name}.

You are commanded to appear at the hearing.

DATED: {datetime.date.today().strftime("%B %d, %Y")}

{self.guardian_name}
{self.guardian_address}
"""
            return notice_of_hearing
        except Exception as e:
            print(f"Error generating Notice of Hearing: {e}")
            return None

    def generate_proof_of_service(self):
        """
        Generate the Proof of Service form.

        Returns:
            str: The Proof of Service form content.
        """
        try:
            proof_of_service = f"""
PROOF OF SERVICE

I, {self.guardian_name}, hereby declare under penalty of perjury that on {datetime.date.today().strftime("%B %d, %Y")}, 
I served a copy of the Notice of Hearing in the above-entitled matter upon:

{self.party_name}
{self.party_address}

by (check one):
    [ ] Hand delivery
    [ ] U.S. Mail

I declare under penalty of perjury under the laws of the State of Utah that the foregoing is true and correct.

Executed on: {datetime.date.today().strftime("%B %d, %Y")}

{self.guardian_name}
{self.guardian_address}
"""
            return proof_of_service
        except Exception as e:
            print(f"Error generating Proof of Service: {e}")
            return None

def main():
    # Example usage
    case_number = "2023-001"
    court_name = "Utah County Court"
    county = "Utah"
    party_name = "John Doe"
    party_address = "123 Main St, Utah County, UT 84101"
    guardian_name = "Jane Smith"
    guardian_address = "456 Elm St, Utah County, UT 84101"
    hearing_date = "09/16/2024"
    hearing_time = "10:00 AM"

    forms = GuardianshipForms(case_number, court_name, county, party_name, party_address, guardian_name, guardian_address, hearing_date, hearing_time)

    notice_of_hearing = forms.generate_notice_of_hearing()
    proof_of_service = forms.generate_proof_of_service()

    if notice_of_hearing and proof_of_service:
        # Save to files
        with open("notice_of_hearing.txt", "w") as f:
            f.write(notice_of_hearing)

        with open("proof_of_service.txt", "w") as f:
            f.write(proof_of_service)

        print("Forms generated and saved to files.")
    else:
        print("Error generating forms.")

if __name__ == "__main__":
    main()
```
