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
# Utah Notice of Hearing and Proof of Service Generator

import os
from datetime import date

def generate_notice_of_hearing(child_name, hearing_date, court_name, case_number):
    """
    Generate a sample Notice of Hearing for guardianship of an adult child with a disability in Utah.

    Args:
        child_name (str): The name of the adult child with a disability.
        hearing_date (str): The date of the hearing in 'YYYY-MM-DD' format.
        court_name (str): The name of the court.
        case_number (str): The case number.

    Returns:
        str: The sample Notice of Hearing.
    """
    notice_of_hearing = f"""
IN THE {court_name} COURT OF UTAH

IN THE MATTER OF: {child_name}, an adult with a disability

Case No. {case_number}

NOTICE OF HEARING

To: {child_name}'s Guardian ad Litem and all interested parties:

You are hereby notified that a hearing has been scheduled to consider the petition for guardianship of {child_name}, an adult with a disability.

The hearing will be held on:

Date: {hearing_date}
Time: 9:00 a.m.
Location: {court_name}

At the hearing, the court will consider the petition for guardianship and any objections thereto.

Dated: {date.today().strftime('%Y-%m-%d')}

[Your Name]
[Your Title]

    """
    return notice_of_hearing

def generate_proof_of_service(served_on, method_of_service, server_name, server_address):
    """
    Generate a sample Proof of Service form.

    Args:
        served_on (str): The date the document was served in 'YYYY-MM-DD' format.
        method_of_service (str): The method of service (e.g., 'personal', 'mail').
        server_name (str): The name of the person serving the document.
        server_address (str): The address of the person serving the document.

    Returns:
        str: The sample Proof of Service form.
    """
    proof_of_service = f"""
PROOF OF SERVICE

I, {server_name}, hereby declare under penalty of perjury:

1. I served a copy of the Notice of Hearing and petition for guardianship on {served_on} by {method_of_service} service.

2. I am over 18 years of age and not a party to the action.

3. My address is: {server_address}

4. I declare that I served the document(s) as described above.

Dated: {date.today().strftime('%Y-%m-%d')}

{server_name}

    """
    return proof_of_service

def main():
    try:
        child_name = input("Enter the adult child's name: ")
        hearing_date = input("Enter the hearing date (YYYY-MM-DD): ")
        court_name = input("Enter the court name: ")
        case_number = input("Enter the case number: ")

        notice_of_hearing = generate_notice_of_hearing(child_name, hearing_date, court_name, case_number)
        print("Notice of Hearing:")
        print(notice_of_hearing)

        served_on = input("Enter the date the document was served (YYYY-MM-DD): ")
        method_of_service = input("Enter the method of service (e.g., 'personal', 'mail'): ")
        server_name = input("Enter the name of the person serving the document: ")
        server_address = input("Enter the address of the person serving the document: ")

        proof_of_service = generate_proof_of_service(served_on, method_of_service, server_name, server_address)
        print("\nProof of Service:")
        print(proof_of_service)

        # Save to file
        save_to_file = input("\nSave to file? (y/n): ")
        if save_to_file.lower() == 'y':
            with open(f"{child_name}_notice_of_hearing_and_proof_of_service.txt", 'w') as f:
                f.write(notice_of_hearing)
                f.write("\n\n")
                f.write(proof_of_service)
            print(f"Saved to {child_name}_notice_of_hearing_and_proof_of_service.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
