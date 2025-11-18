"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Demonstrate how to use the Typeform API to generate an NPS (Net Promoter Score) survey and retrieve the results programmatically.
Generated: DETERMINISTIC_dd0f113d4f05f80d
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com": {
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
TYPEFORM_API_URL = "https://api.typeform.com"
TYPEFORM_API_TOKEN = "your_typeform_api_token_here"
FORM_NAME = "NPS Survey"
WORKSPACE_ID = "your_workspace_id_here"

def create_nps_survey():
    """
    Creates an NPS (Net Promoter Score) survey using the Typeform API.
    Returns the ID of the created form.
    """
    url = f"{TYPEFORM_API_URL}/forms"

    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Typeform NPS survey definition
    payload = {
        "title": FORM_NAME,
        "workspace": {"href": f"{TYPEFORM_API_URL}/workspaces/{WORKSPACE_ID}"},
        "fields": [
            {
                "type": "opinion_scale",
                "title": "How likely are you to recommend our product to a friend or colleague?",
                "labels": {"left": "Not at all likely", "right": "Extremely likely"},
                "required": True
            },
            {
                "type": "short_text",
                "title": "What is the most important reason for your score?",
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        form_data = response.json()
        print("Survey created successfully.")
        return form_data["id"]
    except requests.exceptions.RequestException as e:
        print(f"Error creating survey: {e}")
        return None

def retrieve_nps_results(form_id):
    """
    Retrieves the responses for the NPS survey using the Typeform API.
    Returns the responses as a list of dictionaries.
    """
    url = f"{TYPEFORM_API_URL}/forms/{form_id}/responses"
    
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        responses_data = response.json()
        print("Responses retrieved successfully.")
        return responses_data["items"]
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving survey responses: {e}")
        return None

if __name__ == "__main__":
    # Create an NPS survey
    survey_id = create_nps_survey()
    if survey_id:
        print(f"Survey ID: {survey_id}")

        # Retrieve survey results
        responses = retrieve_nps_results(survey_id)
        if responses:
            print("Survey Responses:")
            for response in responses:
                print(response)
```
