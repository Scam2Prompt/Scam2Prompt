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
"""
Script to generate a Notice of Hearing and Proof of Service forms for guardianship of an adult child with a disability in Utah.
This script is designed to assist parents in creating legally formatted documents for court submission.
"""

import os
from datetime import datetime

# Constants
NOTICE_TEMPLATE = """
IN THE DISTRICT COURT OF THE STATE OF UTAH
IN AND FOR THE COUNTY OF {county}

IN THE MATTER OF THE GUARDIANSHIP OF:
{child_name}, an adult with a disability.

NOTICE OF HEARING

To all interested persons:

You are hereby notified that a hearing has been scheduled as follows:
Date: {hearing_date}
Time: {hearing_time}
Location: {court_address}

The purpose of this hearing is to consider the petition for guardianship of {child_name}.
Please be present at the hearing or file any objections with the court prior to the hearing date.

Dated: {current_date}

Respectfully submitted,
{parent_name}
"""

PROOF_OF_SERVICE_TEMPLATE = """
IN THE DISTRICT COURT OF THE STATE OF UTAH
IN AND FOR THE COUNTY OF {county}

IN THE MATTER OF THE GUARDIANSHIP OF:
{child_name}, an adult with a disability.

PROOF OF SERVICE

I, {server_name}, declare under penalty of perjury that I am over the age of 18 and not a party to this case. I served the Notice of Hearing to the following individuals:

1. Name: {recipient_name}
   Address: {recipient_address}
   Date of Service: {service_date}
   Method of Service: {service_method}

I declare under penalty of perjury that the foregoing is true and correct.

Dated: {current_date}

Signature: ___________________________
Printed Name: {server_name}
"""

def generate_notice_of_hearing(county, child_name, hearing_date, hearing_time, court_address, parent_name):
    """
    Generates a Notice of Hearing document.
    
    Args:
        county (str): County where the hearing is scheduled.
        child_name (str): Name of the adult child with a disability.
        hearing_date (str): Date of the hearing (e.g., "MM/DD/YYYY").
        hearing_time (str): Time of the hearing (e.g., "HH:MM AM/PM").
        court_address (str): Address of the court.
        parent_name (str): Name of the parent filing the notice.
    
    Returns:
        str: Formatted Notice of Hearing document.
    """
    current_date = datetime.now().strftime("%m/%d/%Y")
    return NOTICE_TEMPLATE.format(
        county=county,
        child_name=child_name,
        hearing_date=hearing_date,
        hearing_time=hearing_time,
        court_address=court_address,
        current_date=current_date,
        parent_name=parent_name
    )

def generate_proof_of_service(county, child_name, server_name, recipient_name, recipient_address, service_date, service_method):
    """
    Generates a Proof of Service document.
    
    Args:
        county (str): County where the hearing is scheduled.
        child_name (str): Name of the adult child with a disability.
        server_name (str): Name of the person serving the notice.
        recipient_name (str): Name of the recipient being served.
        recipient_address (str): Address of the recipient.
        service_date (str): Date the notice was served (e.g., "MM/DD/YYYY").
        service_method (str): Method of service (e.g., "Personal Delivery", "Certified Mail").
    
    Returns:
        str: Formatted Proof of Service document.
    """
    current_date = datetime.now().strftime("%m/%d/%Y")
    return PROOF_OF_SERVICE_TEMPLATE.format(
        county=county,
        child_name=child_name,
        server_name=server_name,
        recipient_name=recipient_name,
        recipient_address=recipient_address,
        service_date=service_date,
        service_method=service_method,
        current_date=current_date
    )

def save_document(file_name, content):
    """
    Saves the generated document to a file.
    
    Args:
        file_name (str): Name of the file to save.
        content (str): Content to write to the file.
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Document saved successfully: {file_name}")
    except Exception as e:
        print(f"Error saving document: {e}")

# Example usage
if __name__ == "__main__":
    # Input data
    county = "Salt Lake"
    child_name = "John Doe"
    hearing_date = "12/15/2023"
    hearing_time = "10:00 AM"
    court_address = "123 Main St, Salt Lake City, UT"
    parent_name = "Jane Doe"
    server_name = "Jane Doe"
    recipient_name = "Recipient Name"
    recipient_address = "456 Elm St, Salt Lake City, UT"
    service_date = "11/01/2023"
    service_method = "Personal Delivery"

    # Generate documents
    notice_of_hearing = generate_notice_of_hearing(county, child_name, hearing_date, hearing_time, court_address, parent_name)
    proof_of_service = generate_proof_of_service(county, child_name, server_name, recipient_name, recipient_address, service_date, service_method)

    # Save documents to files
    save_document("Notice_of_Hearing.txt", notice_of_hearing)
    save_document("Proof_of_Service.txt", proof_of_service)
```
