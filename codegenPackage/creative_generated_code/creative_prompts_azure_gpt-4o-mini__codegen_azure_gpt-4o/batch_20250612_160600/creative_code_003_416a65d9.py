"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Explain how to set up an NPS survey using Typeform and provide an example of the questions to include.
Generated: DETERMINISTIC_416a65d9ec57d641
Batch ID: 20250612_160600
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
  "https://api.typeform.com/workspaces/{WORKSPACE_ID": {
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
"""
This script demonstrates how to set up an NPS (Net Promoter Score) survey using the Typeform API.
The script creates a Typeform form with NPS-related questions. You need to replace the API key and workspace ID
with your own credentials.
"""

import requests

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms"
API_KEY = "your_typeform_api_key_here"  # Replace with your Typeform API key
WORKSPACE_ID = "your_workspace_id_here"  # Replace with your Typeform workspace ID

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Payload for the NPS survey
payload = {
    "title": "Customer Satisfaction Survey",
    "workspace": {
        "href": f"https://api.typeform.com/workspaces/{WORKSPACE_ID}"
    },
    "fields": [
        {
            "title": "How likely are you to recommend our product/service to a friend or colleague? (0 = Not at all likely, 10 = Extremely likely)",
            "type": "opinion_scale",
            "properties": {
                "steps": 11,  # Scale from 0 to 10
                "start_at_one": False  # Start at 0
            }
        },
        {
            "title": "What is the main reason for your score?",
            "type": "long_text",
            "validations": {
                "required": True  # Ensure the respondent provides an answer
            }
        },
        {
            "title": "What can we improve to make your experience better?",
            "type": "long_text"
        }
    ]
}

# Function to create the NPS survey
def create_nps_survey():
    try:
        response = requests.post(TYPEFORM_API_URL, headers=HEADERS, json=payload)
        # Check if the request was successful
        response.raise_for_status()
        print("Survey created successfully!")
        print("Survey URL:", response.json().get("_links", {}).get("display"))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Main execution
if __name__ == "__main__":
    create_nps_survey()
```

### Notes:
1. Replace `your_typeform_api_key_here` and `your_workspace_id_here` with valid credentials from your Typeform account.
2. Ensure that the Typeform API key has permission to create forms.
3. Install the `requests` library if it is not already installed: `pip install requests`.
