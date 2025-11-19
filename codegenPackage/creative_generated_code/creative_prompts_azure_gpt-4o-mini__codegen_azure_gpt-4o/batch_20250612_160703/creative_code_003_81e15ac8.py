"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avaxweb.typeform.com
Prompt: Create a Typeform application form using the API that collects candidate feedback and integrates with a CRM system.
Generated: DETERMINISTIC_81e15ac8b8c2b0f6
Batch ID: 20250612_160703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.your-crm.com/v1/contacts": {
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

# Typeform API and CRM API Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_KEY = "your_typeform_api_key"
CRM_API_URL = "https://api.your-crm.com/v1/contacts"
CRM_API_KEY = "your_crm_api_key"

def create_typeform_form():
    """
    Creates a Typeform application form using Typeform API.

    Returns:
        form_id (str): The ID of the created Typeform form.
    """
    # Typeform form payload
    form_payload = {
        "title": "Candidate Feedback Form",
        "fields": [
            {
                "title": "What is your full name?",
                "type": "short_text",
                "id": "full_name"
            },
            {
                "title": "What is your email address?",
                "type": "email",
                "id": "email"
            },
            {
                "title": "Provide feedback about the application process",
                "type": "long_text",
                "id": "feedback"
            },
            {
                "title": "Rate your overall experience (1-5)",
                "type": "number",
                "id": "rating"
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Send request to Typeform API
        response = requests.post(TYPEFORM_API_URL, json=form_payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        form_data = response.json()
        return form_data.get("id")  # Return the form ID
    except requests.exceptions.RequestException as e:
        print(f"Error creating Typeform form: {e}")
        return None


def process_candidate_feedback(typeform_responses):
    """
    Processes responses from Typeform and integrates with a CRM system.

    Args:
        typeform_responses (list): List of candidate responses from Typeform.
    """
    headers = {
        "Authorization": f"Bearer {CRM_API_KEY}",
        "Content-Type": "application/json"
    }

    for response in typeform_responses:
        # Extract relevant fields from Typeform response
        full_name = response.get("answers", {}).get("full_name")
        email = response.get("answers", {}).get("email")
        feedback = response.get("answers", {}).get("feedback")
        rating = response.get("answers", {}).get("rating")

        if full_name and email:
            # CRM payload to create a contact
            crm_payload = {
                "name": full_name,
                "email": email,
                "custom_fields": {
                    "feedback": feedback,
                    "rating": rating
                }
            }

            try:
                # Send request to CRM API
                crm_response = requests.post(CRM_API_URL, json=crm_payload, headers=headers)
                crm_response.raise_for_status()  # Raise an HTTPError for bad responses
                print(f"Candidate {full_name} successfully added to CRM.")
            except requests.exceptions.RequestException as e:
                print(f"Error adding candidate {full_name} to CRM: {e}")
        else:
            print("Incomplete response received. Skipping candidate.")


def main():
    """
    Main function to create a Typeform form and process responses.
    """
    print("Creating Typeform application form...")
    form_id = create_typeform_form()

    if form_id:
        print(f"Form created successfully. Form ID: {form_id}")
        print("Processing candidate feedback...")

        # Simulated list of candidate responses fetched from Typeform
        # Replace with actual API call to fetch responses using Typeform API
        typeform_responses = [
            {
                "answers": {
                    "full_name": "John Doe",
                    "email": "john.doe@example.com",
                    "feedback": "The process was smooth!",
                    "rating": 5
                }
            },
            {
                "answers": {
                    "full_name": "Jane Smith",
                    "email": "jane.smith@example.com",
                    "feedback": "It could have been better.",
                    "rating": 3
                }
            }
        ]

        process_candidate_feedback(typeform_responses)


if __name__ == "__main__":
    main()
```
