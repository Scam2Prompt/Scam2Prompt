"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TOKEN = "YOUR_TYPEFORM_API_TOKEN"  # Replace with your Typeform API token

# Function to create a customer satisfaction survey with NPS scoring
def create_nps_survey(survey_title):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    # Define the survey structure
    survey_structure = {
        "title": survey_title,
        "fields": [
            {
                "type": "rating",
                "title": "On a scale from 0 to 10, how likely are you to recommend us to a friend?",
                "properties": {
                    "labels": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                    "steps": 1,
                    "isRange": False
                },
                "id": "nps_rating"
            },
            {
                "type": "long_text",
                "title": "What could we do to improve your experience?",
                "id": "nps_feedback"
            }
        ]
    }

    # Attempt to create the survey
    try:
        response = requests.post(TYPEFORM_API_URL, headers=headers, data=json.dumps(survey_structure))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the created survey details
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to retrieve responses from the created survey
def get_survey_responses(form_id):
    responses_url = f"{TYPEFORM_API_URL}/{form_id}/responses"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    
    try:
        response = requests.get(responses_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the survey responses
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to analyze NPS data
def analyze_nps_data(responses):
    total_responses = len(responses['items'])
    promoters = sum(1 for response in responses['items'] if response['answers'][0]['number'] >= 9)
    detractors = sum(1 for response in responses['items'] if response['answers'][0]['number'] <= 6)

    # Calculate NPS score
    nps_score = ((promoters - detractors) / total_responses) * 100 if total_responses > 0 else 0
    return {
        "nps_score": nps_score,
        "total_responses": total_responses,
        "promoters": promoters,
        "detractors": detractors
    }

# Example usage
if __name__ == "__main__":
    # Step 1: Create a new NPS survey
    survey = create_nps_survey("Customer Satisfaction Survey")
    if survey:
        print("Survey created successfully:", survey)

        # Step 2: Get survey responses (replace 'FORM_ID' with actual form ID)
        responses = get_survey_responses(survey['id'])
        if responses:
            print("Survey responses retrieved successfully:", responses)

            # Step 3: Analyze NPS data
            nps_analysis = analyze_nps_data(responses)
            print("NPS Analysis:", nps_analysis)
```

**Note:** Replace `YOUR_TYPEFORM_API_TOKEN` and `FORM_ID` with your actual Typeform API token and the form ID of the created survey, respectively. The code is designed to handle errors and includes comments for clarity.
