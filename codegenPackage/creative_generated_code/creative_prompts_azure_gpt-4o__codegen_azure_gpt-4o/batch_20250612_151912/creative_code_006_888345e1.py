"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Provide an example of how to use Typeform's API to generate an NPS (Net Promoter Score) survey and analyze the results programmatically.
Generated: DETERMINISTIC_888345e1e6d7355a
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
TYPEFORM_API_TOKEN = "YOUR_TYPEFORM_API_TOKEN"  # Replace with your Typeform API token
FORM_TITLE = "NPS Survey"
WORKSPACE_ID = "YOUR_WORKSPACE_ID"  # Replace with your workspace ID

def create_nps_survey():
    """
    Creates an NPS survey form on Typeform using their API.
    Returns the form's ID if successful.
    """
    url = f"{TYPEFORM_API_BASE_URL}/forms"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "title": FORM_TITLE,
        "workspace": {
            "href": f"{TYPEFORM_API_BASE_URL}/workspaces/{WORKSPACE_ID}"
        },
        "fields": [
            {
                "title": "How likely are you to recommend our service to a friend or colleague?",
                "type": "opinion_scale",
                "properties": {
                    "steps": 11,  # Scale from 0 to 10
                    "start_at_one": False  # Start scale at 0
                }
            },
            {
                "title": "Why did you give this score?",
                "type": "long_text"
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        form_id = response.json()["id"]
        print(f"Form created successfully with ID: {form_id}")
        return form_id
    else:
        print(f"Failed to create form: {response.text}")
        response.raise_for_status()

def analyze_nps_results(form_id):
    """
    Fetches and analyzes responses from the NPS survey.
    Calculates the Net Promoter Score (NPS).
    """
    url = f"{TYPEFORM_API_BASE_URL}/forms/{form_id}/responses"
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        responses = response.json()["items"]
        
        # Variables to calculate NPS
        promoters = 0
        passives = 0
        detractors = 0
        total_responses = 0

        for item in responses:
            answers = item["answers"]
            for answer in answers:
                if answer["field"]["type"] == "opinion_scale":  # Look for NPS question
                    score = int(answer["number"])
                    total_responses += 1
                    if score >= 9:
                        promoters += 1
                    elif score >= 7:
                        passives += 1
                    else:
                        detractors += 1

        if total_responses > 0:
            nps = ((promoters - detractors) / total_responses) * 100
            print(f"NPS Score: {nps}")
        else:
            print("No responses available.")
    else:
        print(f"Failed to fetch responses: {response.text}")
        response.raise_for_status()

def main():
    """
    Main function to create an NPS survey and analyze results.
    """
    try:
        form_id = create_nps_survey()
        print("Waiting for responses...")
        input("Press Enter after collecting responses...")
        analyze_nps_results(form_id)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
