"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Show how to use the Typeform API to create a job application form that includes a file upload option for resumes.
Generated: DETERMINISTIC_f643c7f8f114f586
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

# Constants
BASE_URL = "https://api.typeform.com/forms"
API_TOKEN = "YOUR_TYPEFORM_API_TOKEN"  # Replace with your Typeform API token

def create_job_application_form():
    """
    Create a job application form with a file upload option for resumes.
    
    Returns:
        str: The ID of the created form.
    """
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Define the form structure
    form_data = {
        "title": "Job Application Form",
        "fields": [
            {
                "type": "short_text",
                "title": "Full Name",
                "required": True
            },
            {
                "type": "email",
                "title": "Email Address",
                "required": True
            },
            {
                "type": "long_text",
                "title": "Cover Letter",
                "required": False
            },
            {
                "type": "file_upload",
                "title": "Upload Your Resume",
                "required": True,
                "properties": {
                    "allowed_file_types": ["pdf", "doc", "docx"],
                    "max_file_size": 10485760  # 10 MB
                }
            },
            {
                "type": "yes_no",
                "title": "Do you have any relevant work experience?",
                "required": True
            }
        ]
    }

    try:
        # Send the request to create the form
        response = requests.post(BASE_URL, headers=headers, json=form_data)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Return the form ID if successful
        return response.json().get("id")

    except requests.exceptions.RequestException as e:
        print(f"Error creating form: {e}")
        return None

if __name__ == "__main__":
    form_id = create_job_application_form()
    if form_id:
        print(f"Successfully created the job application form with ID: {form_id}")
    else:
        print("Failed to create the job application form.")
```
