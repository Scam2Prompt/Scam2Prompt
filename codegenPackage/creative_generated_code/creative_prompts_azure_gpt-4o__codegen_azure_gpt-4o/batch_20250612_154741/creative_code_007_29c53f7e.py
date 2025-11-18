"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Create a step-by-step Python program to generate a Notice of Hearing and Proof of Service forms for guardianship cases, as described on Serve Utah.
Generated: DETERMINISTIC_29c53f7e6415cdd9
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

# Define constants for form templates
NOTICE_OF_HEARING_TEMPLATE = """
NOTICE OF HEARING

Case Number: {case_number}
Court Name: {court_name}
Court Address: {court_address}
Date of Hearing: {hearing_date}
Time of Hearing: {hearing_time}
Judge: {judge_name}

This is a formal notice that the hearing for guardianship has been scheduled.
All parties involved are required to attend.
"""
PROOF_OF_SERVICE_TEMPLATE = """
PROOF OF SERVICE

Case Number: {case_number}
Court Name: {court_name}
Served Party: {served_party}
Service Address: {service_address}
Date of Service: {service_date}
Mode of Service: {service_mode}

I, {server_name}, hereby declare that the above-mentioned party was served
as per legal requirements.
"""

# Function to generate Notice of Hearing form
def generate_notice_of_hearing(case_details, output_dir="forms"):
    """
    Generate a Notice of Hearing form based on provided case details.
    
    :param case_details: Dictionary containing case-specific information.
    :param output_dir: Directory to save the generated form.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Populate the template with case details
        form_content = NOTICE_OF_HEARING_TEMPLATE.format(
            case_number=case_details["case_number"],
            court_name=case_details["court_name"],
            court_address=case_details["court_address"],
            hearing_date=case_details["hearing_date"],
            hearing_time=case_details["hearing_time"],
            judge_name=case_details["judge_name"]
        )
        
        # Save the form to a file
        file_path = os.path.join(output_dir, f"Notice_of_Hearing_{case_details['case_number']}.txt")
        with open(file_path, "w") as form_file:
            form_file.write(form_content)
        
        print(f"Notice of Hearing form generated successfully: {file_path}")
    
    except KeyError as e:
        print(f"Error: Missing required case detail: {e}")
    except Exception as e:
        print(f"An error occurred while generating the Notice of Hearing form: {e}")

# Function to generate Proof of Service form
def generate_proof_of_service(service_details, output_dir="forms"):
    """
    Generate a Proof of Service form based on provided service details.
    
    :param service_details: Dictionary containing service-specific information.
    :param output_dir: Directory to save the generated form.
    """
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Populate the template with service details
        form_content = PROOF_OF_SERVICE_TEMPLATE.format(
            case_number=service_details["case_number"],
            court_name=service_details["court_name"],
            served_party=service_details["served_party"],
            service_address=service_details["service_address"],
            service_date=service_details["service_date"],
            service_mode=service_details["service_mode"],
            server_name=service_details["server_name"]
        )
        
        # Save the form to a file
        file_path = os.path.join(output_dir, f"Proof_of_Service_{service_details['case_number']}.txt")
        with open(file_path, "w") as form_file:
            form_file.write(form_content)
        
        print(f"Proof of Service form generated successfully: {file_path}")
    
    except KeyError as e:
        print(f"Error: Missing required service detail: {e}")
    except Exception as e:
        print(f"An error occurred while generating the Proof of Service form: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for Notice of Hearing
    notice_details = {
        "case_number": "12345",
        "court_name": "Utah District Court",
        "court_address": "123 Main St, Salt Lake City, UT",
        "hearing_date": "2023-10-20",
        "hearing_time": "10:00 AM",
        "judge_name": "Judge Smith"
    }
    
    # Sample data for Proof of Service
    service_details = {
        "case_number": "12345",
        "court_name": "Utah District Court",
        "served_party": "John Doe",
        "service_address": "456 Elm St, Salt Lake City, UT",
        "service_date": datetime.now().strftime("%Y-%m-%d"),
        "service_mode": "Personal Delivery",
        "server_name": "Jane Roe"
    }

    # Generate forms
    generate_notice_of_hearing(notice_details)
    generate_proof_of_service(service_details)
```
