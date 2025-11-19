"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Provide a sample script for a parent to follow when serving a Notice of Hearing for guardianship of an adult child with a disability in Utah, including the required Proof of Service forms.
Generated: DETERMINISTIC_d9febfa2d1b79c69
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Utah Guardianship Notice of Hearing Script

This script generates a Notice of Hearing and Proof of Service form
for guardianship of an adult child with a disability in Utah.

Required forms:
1. Notice of Hearing
2. Proof of Service

Follows Utah Code Ann. § 75-5-303 and Utah Court Rules.
"""

import datetime
from typing import Dict

def generate_notice_of_hearing(case_details: Dict) -> str:
    """
    Generates Notice of Hearing document based on provided case details.
    
    Args:
        case_details: Dictionary containing case information
        
    Returns:
        Formatted Notice of Hearing document as string
    """
    notice = f"""
IN THE DISTRICT COURT OF {case_details['county'].upper()} COUNTY
STATE OF UTAH

IN THE MATTER OF THE GUARDIANSHIP OF:
{case_details['ward_name'].upper()},
AN ADULT WITH A DISABILITY.

Case No.: {case_details['case_number']}

NOTICE OF HEARING

TO: {case_details['ward_name']} and all interested persons

PLEASE TAKE NOTICE that a hearing will be held before the {case_details['county']} 
County District Court on {case_details['hearing_date']} at {case_details['hearing_time']} 
in {case_details['courtroom']}, located at {case_details['court_address']}, 
to consider the Petition for Appointment of Guardian of an Adult filed in this matter.

You have the right to appear at the hearing and oppose the petition. 
You may hire an attorney to represent you at the hearing. 
If you cannot afford an attorney, you may contact the Utah State Bar 
at (801) 531-9077 to inquire about legal assistance.

If you do not appear at the hearing, the court may grant the petition 
without further notice to you.

DATED this {datetime.datetime.now().strftime('%d')} day of {datetime.datetime.now().strftime('%B, %Y')}.

{case_details['petitioner_name']}
Petitioner
"""

    return notice.strip()


def generate_proof_of_service(case_details: Dict) -> str:
    """
    Generates Proof of Service document based on provided case details.
    
    Args:
        case_details: Dictionary containing case information
        
    Returns:
        Formatted Proof of Service document as string
    """
    proof = f"""
IN THE DISTRICT COURT OF {case_details['county'].upper()} COUNTY
STATE OF UTAH

IN THE MATTER OF THE GUARDIANSHIP OF:
{case_details['ward_name'].upper()},
AN ADULT WITH A DISABILITY.

Case No.: {case_details['case_number']}

PROOF OF SERVICE

I, {case_details['server_name']}, declare:

1. I am over 18 years of age and not a party to this proceeding.
2. On {case_details['service_date']}, I served the Notice of Hearing in this matter:
   a. By personally delivering a copy to {case_details['ward_name']} at {case_details['service_address']}
   b. By mailing a copy via certified mail, return receipt requested, to:
      {case_details['ward_name']}
      {case_details['service_address']}
3. The documents served were: Notice of Hearing and Petition for Guardianship.

I declare under penalty of perjury under the laws of the State of Utah that the foregoing is true and correct.

DATED this {datetime.datetime.now().strftime('%d')} day of {datetime.datetime.now().strftime('%B, %Y')}.

___________________________
{case_details['server_name']}
Server
"""

    return proof.strip()


def validate_case_details(case_details: Dict) -> bool:
    """
    Validates required case details are present.
    
    Args:
        case_details: Dictionary to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_fields = [
        'ward_name', 'case_number', 'county', 
        'hearing_date', 'hearing_time', 'courtroom',
        'court_address', 'petitioner_name', 'server_name',
        'service_date', 'service_address'
    ]
    
    missing_fields = [field for field in required_fields if field not in case_details]
    
    if missing_fields:
        print(f"Missing required fields: {', '.join(missing_fields)}")
        return False
    
    try:
        datetime.datetime.strptime(case_details['hearing_date'], '%Y-%m-%d')
        datetime.datetime.strptime(case_details['service_date'], '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return False
    
    return True


def main():
    """Main execution function for the script."""
    # Example case details - replace with actual case information
    case_details = {
        'ward_name': 'John Doe',
        'case_number': 'PR20230045',
        'county': 'Salt Lake',
        'hearing_date': '2023-12-15',
        'hearing_time': '9:00 AM',
        'courtroom': 'Courtroom 3A',
        'court_address': '450 S State St, Salt Lake City, UT 84111',
        'petitioner_name': 'Jane Doe',
        'server_name': 'Michael Smith',
        'service_date': '2023-11-20',
        'service_address': '123 Main St, Salt Lake City, UT 84111'
    }
    
    if not validate_case_details(case_details):
        print("Invalid case details. Please correct and try again.")
        return
    
    notice = generate_notice_of_hearing(case_details)
    proof = generate_proof_of_service(case_details)
    
    print("\n=== NOTICE OF HEARING ===\n")
    print(notice)
    
    print("\n=== PROOF OF SERVICE ===\n")
    print(proof)
    
    print("\nDocuments generated successfully. Please review, sign, and file with the court.")


if __name__ == "__main__":
    main()
```
