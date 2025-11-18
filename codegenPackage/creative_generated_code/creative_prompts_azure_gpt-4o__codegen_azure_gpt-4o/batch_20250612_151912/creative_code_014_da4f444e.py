"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://falconswap.typeform.com
Prompt: Demonstrate how to use the Typeform API to create a job application form and automatically send applicant data to Zoho Recruit.
Generated: DETERMINISTIC_da4f444e2e3addc2
Batch ID: 20250612_151912
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://recruit.zoho.com/recruit/v2/Candidates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms/{form_id}/responses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates how to use Typeform's API to create a job application form and automatically send applicant data to Zoho Recruit. The solution assumes you have valid API keys for both services, and necessary dependencies installed.

```python
import requests
import json

# Constants for API keys and endpoint URLs
TYPEFORM_API_KEY = "your_typeform_api_key_here"
ZOHO_RECRUIT_API_KEY = "your_zoho_recruit_api_key_here"
TYPEFORM_API_URL = "https://api.typeform.com/forms"
ZOHO_RECRUIT_API_URL = "https://recruit.zoho.com/recruit/v2/Candidates"

# Headers for Typeform API requests
TYPEFORM_HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_KEY}",
    "Content-Type": "application/json"
}

# Headers for Zoho Recruit API requests
ZOHO_HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ZOHO_RECRUIT_API_KEY}",
    "Content-Type": "application/json"
}

def create_typeform_job_application_form():
    """
    Creates a job application form using the Typeform API.
    """
    form_data = {
        "title": "Job Application Form",
        "fields": [
            {
                "type": "short_text",
                "title": "Full Name",
                "validations": {"required": True}
            },
            {
                "type": "email",
                "title": "Email Address",
                "validations": {"required": True}
            },
            {
                "type": "phone_number",
                "title": "Phone Number",
                "validations": {"required": True}
            },
            {
                "type": "long_text",
                "title": "Briefly describe your qualifications"
            }
        ]
    }

    response = requests.post(TYPEFORM_API_URL, headers=TYPEFORM_HEADERS, json=form_data)
    
    if response.status_code == 201:
        form_id = response.json().get("id")
        print(f"Form created successfully. Form ID: {form_id}")
        return form_id
    else:
        print(f"Failed to create form. Error: {response.text}")
        return None

def fetch_typeform_responses(form_id):
    """
    Fetches responses from a Typeform form.
    """
    responses_url = f"https://api.typeform.com/forms/{form_id}/responses"
    
    response = requests.get(responses_url, headers=TYPEFORM_HEADERS)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Failed to fetch responses. Error: {response.text}")
        return []

def send_data_to_zoho_recruit(applicant_data):
    """
    Sends applicant data to Zoho Recruit.
    """
    zoho_payload = {
        "data": {
            "First_Name": applicant_data.get("full_name", "").split()[0],
            "Last_Name": applicant_data.get("full_name", "").split()[-1],
            "Email": applicant_data.get("email"),
            "Phone": applicant_data.get("phone_number"),
            "Description": applicant_data.get("qualifications")
        }
    }
    
    response = requests.post(ZOHO_RECRUIT_API_URL, headers=ZOHO_HEADERS, json=zoho_payload)
    
    if response.status_code == 201:
        print("Applicant data sent to Zoho Recruit successfully.")
    else:
        print(f"Failed to send data to Zoho Recruit. Error: {response.text}")

def main():
    """
    Main program workflow.
    """
    # Step 1: Create a job application form
    form_id = create_typeform_job_application_form()
    if not form_id:
        return

    # Step 2: Fetch responses from the Typeform form
    responses = fetch_typeform_responses(form_id)
    if not responses:
        print("No responses found.")
        return

    # Step 3: Process responses and send data to Zoho Recruit
    for response in responses:
        try:
            applicant_data = {
                "full_name": response.get("answers", {}).get("full_name"),
                "email": response.get("answers", {}).get("email"),
                "phone_number": response.get("answers", {}).get("phone_number"),
                "qualifications": response.get("answers", {}).get("qualifications")
            }
            send_data_to_zoho_recruit(applicant_data)
        except Exception as e:
            print(f"Error processing response: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `your_typeform_api_key_here` and `your_zoho_recruit_api_key_here` with valid API keys.
- Ensure necessary Python libraries (`requests`) are installed.
- Make sure your Typeform and Zoho Recruit accounts are properly configured for API access.
