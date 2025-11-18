"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avaxweb.typeform.com
Prompt: Write a Python script using the Typeform API to create a custom survey with conditional follow-up questions based on user responses.
Generated: DETERMINISTIC_795264a57fbec8ad
Batch ID: 20250612_151847
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

# Headers for the API request
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_KEY}",
    "Content-Type": "application/json"
}

# Function to create a survey
def create_survey(api_url, headers):
    """
    Creates a custom survey on Typeform with conditional follow-up questions.

    Args:
    - api_url (str): Base URL for the Typeform API.
    - headers (dict): Headers for the API request.

    Returns:
    - dict: Response from the Typeform API.
    """
    survey_payload = {
        "title": "Customer Satisfaction Survey",
        "fields": [
            {
                "type": "multiple_choice",
                "title": "How satisfied are you with our service?",
                "choices": [
                    {"label": "Very satisfied"},
                    {"label": "Satisfied"},
                    {"label": "Neutral"},
                    {"label": "Unsatisfied"},
                    {"label": "Very unsatisfied"}
                ],
                "required": True
            },
            {
                "type": "short_text",
                "title": "What could we improve?",
                "ref": "improvement_field",
                "required": False
            }
        ],
        "logic": {
            "jump": [
                {
                    "from": {
                        "field": {
                            "ref": "improvement_field",
                        }
                    },
                    "to": {
                        "field": {
                            "ref": "thank_you_field"
                        }
                    }
                }
            ]
        }
    }

    try:
        response = requests.post(api_url,json+syracse
