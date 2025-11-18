"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Provide an example of how to use Typeform's API to generate an NPS (Net Promoter Score) survey and analyze the results programmatically.
Generated: DETERMINISTIC_888345e1e6d7355a
Batch ID: 20250612_151912
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/{form_id}/responses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

# Define constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_TOKEN = "YOUR_TYPEFORM_API_TOKEN"

# Function to create an NPS survey
def create_nps_survey():
    # Define the survey structure
    survey_data = {
        "title": "Customer Satisfaction Survey",
        "fields": [
            {
                "id": "nps_question",
                "type": "rating",
                "title": "On a scale of 0 to 10, how likely are you to recommend us to a friend?",
                "description": "0 = Not at all likely, 10 = Extremely likely",
                "required": True,
                "properties": {
                    "steps": 11,
                    "labels": ["Not at all likely", "Extremely likely"]
                }
            }
        ]
    }

    # Send a POST request to create the survey
    try:
        response = requests.post(
            TYPEFORM_API_URL,
            headers={
                "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
                "Content-Type": "application/json"
            },
            data=json.dumps(survey_data)
        )
        
        # Check for successful response
        response.raise_for_status()
        survey = response.json()
        print("NPS Survey Created Successfully!")
        return survey['id']  # Return the survey ID for future use
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Function to retrieve NPS responses
def get_nps_responses(form_id):
    responses_url = f"https://api.typeform.com/forms/{form_id}/responses"

    try:
        response = requests.get(
            responses_url,
            headers={
                "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
                "Content-Type": "application/json"
            }
        )
        
        response.raise_for_status()
        responses_data = response.json()
        return responses_data['items']  # Return responses
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Function to calculate NPS
def calculate_nps(responses):
    promoters = 0
    detractors = 0
    total_responses = len(responses)

    for response in responses:
        nps_score = response['answers'][0]['number']
        if nps_score >= 9:
            promoters += 1
        elif nps_score <= 6:
            detractors += 1

    # Calculate NPS
    nps = (promoters - detractors) / total_responses * 100 if total_responses > 0 else 0
    return nps

if __name__ == "__main__":
    # Create the NPS survey and get the form ID
    form_id = create_nps_survey()
    
    if form_id:
        # Retrieve responses for the created NPS survey
        responses = get_nps_responses(form_id)
        
        if responses:
            # Calculate and display the NPS
            nps_score = calculate_nps(responses)
            print(f"The Net Promoter Score (NPS) is: {nps_score:.2f}")
        else:
            print("No responses found.")
    else:
        print("Survey creation failed.")
```

**Note**: Before running this code, replace `YOUR_TYPEFORM_API_TOKEN` with your actual Typeform API token. Make sure to install the `requests` library if you haven't already, using `pip install requests`.
