"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Generate a script to create a branded customer satisfaction survey using Typeform's API, including custom design elements and follow-up questions based on user responses.
Generated: DETERMINISTIC_4f792d730d059df2
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
API_KEY = 'YOUR_TYPEFORM_API_KEY'
TYPEFORM_API_URL = 'https://api.typeform.com/forms'

# Function to create a branded customer satisfaction survey
def create_survey():
    # Survey definition
    survey_data = {
        "title": "Customer Satisfaction Survey",
        "fields": [
            {
                "title": "How satisfied are you with our service?",
                "type": "opinion_scale",
                "properties": {
                    "scale": 5
                }
            },
            {
                "title": "What did you like about our service?",
                "type": "long_text"
            },
            {
                "title": "What can we improve?",
                "type": "long_text"
            },
            {
                "title": "Would you recommend us to a friend?",
                "type": "yes_no"
            },
            {
                "title": "Please provide your email if you'd like to receive follow-up",
                "type": "email"
            }
        ],
        "settings": {
            "is_public": True,
            "language": "en",
            "theme": "YOUR_THEME_ID"  # Replace with your theme ID
        }
    }

    # Make a request to Typeform API to create the survey
    try:
        response = requests.post(
            TYPEFORM_API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=survey_data
        )
        
        # Check for successful response
        response.raise_for_status()
        survey_id = response.json().get('id')
        print(f"Survey created successfully! Survey ID: {survey_id}")
        return survey_id

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Main function to execute the script
if __name__ == "__main__":
    create_survey()
```

**Note**: Replace `YOUR_TYPEFORM_API_KEY` and `YOUR_THEME_ID` with your actual Typeform API key and the theme ID you want to use for branding. Make sure to install the `requests` library if you haven't done so by running `pip install requests`.
