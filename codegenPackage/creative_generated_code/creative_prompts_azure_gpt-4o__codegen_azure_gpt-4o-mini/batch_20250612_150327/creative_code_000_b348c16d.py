"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Write a Python script using the Typeform API to create a branded survey form with follow-up questions based on user responses. Include integration with Slack to notify the team when a response is submitted.
Generated: DETERMINISTIC_b348c16d05ec1257
Batch ID: 20250612_150327
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
import os

# Constants for API endpoints and tokens
TYPEFORM_API_URL = "https://api.typeform.com/forms"
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
TYPEFORM_API_TOKEN = os.getenv("TYPEFORM_API_TOKEN")

# Function to create a new Typeform survey
def create_typeform_survey(title, questions):
    """
    Create a new Typeform survey with the given title and questions.
    
    Args:
        title (str): The title of the survey.
        questions (list): A list of dictionaries representing the questions.

    Returns:
        str: The ID of the created Typeform survey.
    """
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Define the survey structure
    survey_data = {
        "title": title,
        "fields": questions
    }

    try:
        response = requests.post(TYPEFORM_API_URL, headers=headers, data=json.dumps(survey_data))
        response.raise_for_status()
        survey_id = response.json().get("id")
        return survey_id
    except requests.exceptions.HTTPError as e:
        print(f"An error occurred while creating Typeform survey: {e}")
        return None

# Function to send a notification to Slack
def notify_slack(response_data):
    """
    Send a notification to Slack when a response is submitted.

    Args:
        response_data (dict): The response data from Typeform.
    """
    message = {
        "text": f"New response received: {response_data}"
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to send Slack notification: {e}")

# Function to process the Typeform webhook responses
def process_typeform_response(response):
    """
    Process the Typeform webhook response and notify Slack.

    Args:
        response (dict): The response received from Typeform webhook.
    """
    try:
        # Here you can customize the processing, e.g., extracting specific fields
        response_data = response.get("form_response", {})
        notify_slack(response_data)
    except Exception as e:
        print(f"Error processing Typeform response: {e}")

# Main execution block
if __name__ == "__main__":
    survey_title = "Customer Feedback Survey"
    questions = [
        {
            "title": "How satisfied are you with our service?",
            "type": "opinion_scale",
            "properties": {
                "steps": 5
            }
        },
        {
            "title": "What can we improve?",
            "type": "long_text"
        }
    ]

    # Create the Typeform survey
    survey_id = create_typeform_survey(survey_title, questions)
    if survey_id:
        print(f"Survey created successfully with ID: {survey_id}")
    else:
        print("Failed to create survey.")
```

**Note:** Make sure to set the environment variables `SLACK_WEBHOOK_URL` and `TYPEFORM_API_TOKEN` with the appropriate values before running the script. This code does not include a webhook listener for Typeform; you will need to set up an endpoint to receive webhook notifications and call `process_typeform_response`.
