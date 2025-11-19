"""
Generated Code Metadata:
========================
Original URL: https://electrocoin.typeform.com
Prompt: Using Typeform's API, generate a customer satisfaction survey with NPS scoring and explain how to retrieve and analyze the collected data.
Generated: DETERMINISTIC_803c48917157b3b4
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

# Generated Code:
# ===============

```python
import requests
import json

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_KEY = "YOUR_TYPEFORM_API_KEY"  # Replace with your Typeform API key

# Function to create a customer satisfaction survey with NPS scoring
def create_nps_survey():
    # Define the survey structure
    survey_data = {
        "title": "Customer Satisfaction Survey",
        "fields": [
            {
                "type": "statement",
                "title": "We value your feedback!"
            },
            {
                "type": "rating",
                "title": "On a scale of 0 to 10, how likely are you to recommend us to a friend?",
                "description": "0 = Not at all likely, 10 = Extremely likely",
                "key": "nps_score",
                "steps": 10,
                "labels": {
                    "0": "Not at all likely",
                    "10": "Extremely likely"
                }
            },
            {
                "type": "long_text",
                "title": "What can we do to improve?",
                "key": "improvement_feedback"
            }
        ]
    }

    # Set headers for the API request
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Make a POST request to create the survey
        response = requests.post(TYPEFORM_API_URL, headers=headers, data=json.dumps(survey_data))
        response.raise_for_status()  # Raise an error for bad responses

        # Return the created survey's ID
        survey_id = response.json().get("id")
        print(f"Survey created successfully with ID: {survey_id}")
        return survey_id

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Function to retrieve responses from the survey
def retrieve_survey_responses(survey_id):
    responses_url = f"{TYPEFORM_API_URL}/{survey_id}/responses"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}"
    }

    try:
        # Make a GET request to retrieve responses
        response = requests.get(responses_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse and return the responses
        responses = response.json()
        return responses

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Function to analyze NPS data
def analyze_nps_data(responses):
    nps_scores = []
    for response in responses.get("items", []):
        nps_score = response.get("answers", {}).get("nps_score")
        if nps_score is not None:
            nps_scores.append(nps_score)

    if nps_scores:
        nps_score = (sum(nps_scores) / len(nps_scores)) - 7  # NPS calculation
        print(f"Average NPS Score: {nps_score}")
    else:
        print("No NPS scores available for analysis.")

# Main execution
if __name__ == "__main__":
    survey_id = create_nps_survey()
    if survey_id:
        responses = retrieve_survey_responses(survey_id)
        analyze_nps_data(responses)
```

**Note:** Replace `YOUR_TYPEFORM_API_KEY` with your actual Typeform API key before running the code.
