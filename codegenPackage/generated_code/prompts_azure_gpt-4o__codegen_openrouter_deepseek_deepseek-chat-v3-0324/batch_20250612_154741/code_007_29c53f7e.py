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
import datetime
import os
from typing import Dict, Optional

# Constants
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"
DATE_FORMAT = "%B %d, %Y"

# Form templates
NOTICE_OF_HEARING_TEMPLATE = """
NOTICE OF HEARING

Case No.: {case_number}
In the Matter of the Guardianship of: {ward_name}

TO: {interested_party_name}

NOTICE IS HEREBY GIVEN that a hearing will be held on {hearing_date} at {hearing_time}, 
at {court_location}, regarding the petition for guardianship of {ward_name}.

You are required to appear at this hearing. If you fail to appear, the court may proceed 
without you.

Dated this {notice_date}.

{prepared_by_name}
{prepared_by_title}
"""

PROOF_OF_SERVICE_TEMPLATE = """
PROOF OF SERVICE

Case No.: {case_number}
In the Matter of the Guardianship of: {ward_name}

I, {server_name}, declare:

1. I am over the age of 18 and not a party to this action.
2. On {service_date}, I served the Notice of Hearing on {interested_party_name} by:
   [ ] Personal delivery
   [ ] Mail
   [ ] Other (specify): ____________________
3. The address where service was made: {service_address}

I declare under penalty of perjury under the laws of the State of Utah that the foregoing 
is true and correct.

Executed on {proof_date} at {proof_location}.

{server_name}
"""


def create_output_directory() -> None:
    """Create output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def validate_input(data: Dict[str, str]) -> bool:
    """Validate required form fields."""
    required_fields = [
        "case_number",
        "ward_name",
        "interested_party_name",
        "hearing_date",
        "hearing_time",
        "court_location",
        "prepared_by_name",
        "prepared_by_title",
        "server_name",
        "service_date",
        "service_address",
        "proof_location",
    ]
    
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"Missing required field: {field}")
    
    try:
        datetime.datetime.strptime(data["hearing_date"], DATE_FORMAT)
        datetime.datetime.strptime(data["service_date"], DATE_FORMAT)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use '{DATE_FORMAT}'") from e
    
    return True


def generate_notice_of_hearing(data: Dict[str, str]) -> str:
    """Generate Notice of Hearing document."""
    current_date = datetime.datetime.now().strftime(DATE_FORMAT)
    
    notice_data = {
        "case_number": data["case_number"],
        "ward_name": data["ward_name"],
        "interested_party_name": data["interested_party_name"],
        "hearing_date": data["hearing_date"],
        "hearing_time": data["hearing_time"],
        "court_location": data["court_location"],
        "notice_date": current_date,
        "prepared_by_name": data["prepared_by_name"],
        "prepared_by_title": data["prepared_by_title"],
    }
    
    return NOTICE_OF_HEARING_TEMPLATE.format(**notice_data)


def generate_proof_of_service(data: Dict[str, str]) -> str:
    """Generate Proof of Service document."""
    current_date = datetime.datetime.now().strftime(DATE_FORMAT)
    
    proof_data = {
        "case_number": data["case_number"],
        "ward_name": data["ward_name"],
        "server_name": data["server_name"],
        "interested_party_name": data["interested_party_name"],
        "service_date": data["service_date"],
        "service_address": data["service_address"],
        "proof_date": current_date,
        "proof_location": data["proof_location"],
    }
    
    return PROOF_OF_SERVICE_TEMPLATE.format(**proof_data)


def save_document(filename: str, content: str) -> str:
    """Save document to file and return path."""
    create_output_directory()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w") as f:
        f.write(content)
    
    return filepath


def generate_forms(data: Dict[str, str]) -> Dict[str, str]:
    """Generate both Notice of Hearing and Proof of Service forms."""
    validate_input(data)
    
    notice_content = generate_notice_of_hearing(data)
    proof_content = generate_proof_of_service(data)
    
    notice_filename = f"Notice_of_Hearing_{data['case_number']}.txt"
    proof_filename = f"Proof_of_Service_{data['case_number']}.txt"
    
    notice_path = save_document(notice_filename, notice_content)
    proof_path = save_document(proof_filename, proof_content)
    
    return {
        "notice_of_hearing": notice_path,
        "proof_of_service": proof_path,
    }


def main():
    """Main function to demonstrate form generation."""
    sample_data = {
        "case_number": "GU-2023-001",
        "ward_name": "John Doe",
        "interested_party_name": "Jane Smith",
        "hearing_date": "November 15, 2023",
        "hearing_time": "10:00 AM",
        "court_location": "Salt Lake County Courthouse, 450 S State St, Salt Lake City, UT",
        "prepared_by_name": "Michael Johnson",
        "prepared_by_title": "Attorney for Petitioner",
        "server_name": "Robert Williams",
        "service_date": "November 1, 2023",
        "service_address": "123 Main St, Salt Lake City, UT 84101",
        "proof_location": "Salt Lake City, UT",
    }
    
    try:
        result = generate_forms(sample_data)
        print(f"Forms generated successfully:\nNotice of Hearing: {result['notice_of_hearing']}\nProof of Service: {result['proof_of_service']}")
    except ValueError as e:
        print(f"Error generating forms: {e}")


if __name__ == "__main__":
    main()
```
