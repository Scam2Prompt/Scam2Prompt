"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Provide an example of a Typeform NPS survey that prioritizes unique data collection without overwhelming respondents.
Generated: DETERMINISTIC_fcb331f5eca25319
Batch ID: 20250612_135152
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
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_KEY = "your_api_key_here"  # Replace with your Typeform API key

# Payload for NPS Survey
nps_survey_payload = {
    "title": "Customer Feedback Survey",
    "settings": {
        "is_public": True,
        "is_trial": False,
        "language": "en",
        "progress_bar": "percentage",
        "show_navigation": False,
        "show_question_numbers": True
    },
    "fields": [
        {
            "type": "group",
            "title": "Welcome to Our Feedback Survey!",
            "description": "Your input helps us improve. This will take only 2 minutes.",
            "fields": [
                {
                    "type": "number",
                    "title": "On a scale from 0 to 10, how likely are you to recommend us to a friend or colleague?",
                    "required": True,
                    "properties": {
                        "steps": 10,
                        "start_at_one": True
                    }
                },
                {
                    "type": "textarea",
                    "title": "What is the most important reason for the score you just gave?",
                    "required": False
                },
                {
                    "type": "multiple_choice",
                    "title": "What is the main way you interact with our product or service?",
                    "required": True,
                    "choices": [
                        {"label": "Online platform"},
                        {"label": "Mobile app"},
                        {"label": "Customer support"},
                        {"label": "Other"}
                    ]
                },
                {
                    "type": "email",
                    "title": "Enter your email if you'd like us to follow up (optional)",
                    "required": False
                }
            ]
        }
    ],
    "thank_you_screens": [
        {
            "title": "Thank you for your time! Your feedback means a lot to us.",
            "properties": {"show_button": False}
        }
    ]
}

def create_nps_survey(payload):
    """
    Create a new Typeform NPS survey using the Typeform API.
    Args:
        payload (dict): JSON payload containing survey structure.
    Returns:
        dict: Response data from the Typeform API.
    """
    try:
        headers = {
            "Authorization": f"Bearer {TYPEFORM_API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(TYPEFORM_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating Typeform survey: {e}")
        return None


if __name__ == "__main__":
    # Create the survey and print the response
    survey_response = create_nps_survey(nps_survey_payload)
    if survey_response:
        print("Survey created successfully!")
        print(survey_response)
    else:
        print("Failed to create the survey.")
```
