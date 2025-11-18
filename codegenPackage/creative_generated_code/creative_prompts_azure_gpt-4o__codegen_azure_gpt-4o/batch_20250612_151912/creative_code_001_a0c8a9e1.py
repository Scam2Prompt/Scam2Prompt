"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenform.typeform.com
Prompt: Generate a script that uses Typeform's API to create a branded survey with follow-up questions based on user responses.
Generated: DETERMINISTIC_a0c8a9e1861c5583
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

# Constants for Typeform API
TYPEFORM_API_BASE_URL = "https://api.typeform.com"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"  # Replace with your Typeform API key
TYPEFORM_WORKSPACE_ID = "YOUR_WORKSPACE_ID"  # Replace with your Typeform workspace ID

# Headers required for API requests
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_KEY}",
    "Content-Type": "application/json"
}

def create_survey():
    """
    Creates a branded survey with follow-up questions using Typeform's API.
    Returns the survey ID if successful.
    """
    survey_payload = {
        "title": "Branded Survey",
        "workspace": {
            "href": f"{TYPEFORM_API_BASE_URL}/workspaces/{TYPEFORM_WORKSPACE_ID}"
        },
        "theme": {
            "href": f"{TYPEFORM_API_BASE_URL}/themes/default"  # Use a default theme; customize as needed
        },
        "fields": [
            # Initial question: Ask user's name
            {
                "title": "What is your name?",
                "type": "short_text",
                "ref": "user_name"
            },
            # Follow-up question 1: Ask user's favorite color
            {
                "title": "What is your favorite color?",
                "type": "multiple_choice",
                "ref": "favorite_color",
                "properties": {
                    "choices": [
                        {"label": "Red"},
                        {"label": "Blue"},
                        {"label": "Green"},
                        {"label": "Yellow"}
                    ]
                }
            },
            # Follow-up question 2: Ask user's feedback
            {
                "title": "Do you have any feedback for us?",
                "type": "long_text",
                "ref": "feedback"
            }
        ]
    }

    try:
        response = requests.post(
            f"{TYPEFORM_API_BASE_URL}/forms",
            headers=HEADERS,
            json=survey_payload
        )

        # Check if the request succeeded
        if response.status_code == 201:
            survey_id = response.json()["id"]
            print(f"Survey created successfully! Survey ID: {survey_id}")
            return survey_id
        else:
            # Log and raise an exception on failure
            print(f"Failed to create survey. Status Code: {response.status_code}, Response: {response.text}")
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating the survey: {e}")
        raise

if __name__ == "__main__":
    # Run the survey creation script
    create_survey()
```
