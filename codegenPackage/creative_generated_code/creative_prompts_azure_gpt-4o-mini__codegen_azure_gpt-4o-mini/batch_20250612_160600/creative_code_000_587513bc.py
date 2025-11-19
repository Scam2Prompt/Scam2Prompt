"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: How can I use Typeform's API to create a customized survey that integrates with Slack for real-time feedback collection?
Generated: DETERMINISTIC_587513bcc81585ac
Batch ID: 20250612_160600
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

class TypeformSurvey:
    """
    A class to interact with Typeform's API to create and manage surveys.
    """

    def __init__(self, api_key):
        """
        Initializes the TypeformSurvey class with the provided API key.
        
        :param api_key: Your Typeform API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.typeform.com/forms"

    def create_survey(self, title, questions):
        """
        Creates a new survey with the specified title and questions.
        
        :param title: Title of the survey.
        :param questions: List of questions to include in the survey.
        :return: Response from Typeform API.
        """
        survey_data = {
            "title": title,
            "fields": questions,
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.base_url, headers=headers, data=json.dumps(survey_data))
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating survey: {e}")
            return None

class SlackIntegration:
    """
    A class to handle Slack integration for collecting real-time feedback.
    """

    def __init__(self, slack_webhook_url):
        """
        Initializes the SlackIntegration class with the provided webhook URL.
        
        :param slack_webhook_url: Incoming webhook URL for Slack.
        """
        self.slack_webhook_url = slack_webhook_url

    def send_message(self, message):
        """
        Sends a message to the specified Slack channel via the webhook.
        
        :param message: The message to send to Slack.
        """
        payload = {
            "text": message
        }

        try:
            response = requests.post(self.slack_webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
            response.raise_for_status()  # Raises an error for bad responses
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Slack: {e}")

# Example usage
if __name__ == "__main__":
    # Load environment variables for API keys
    TYPEFORM_API_KEY = os.getenv("TYPEFORM_API_KEY")
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

    if not TYPEFORM_API_KEY or not SLACK_WEBHOOK_URL:
        print("Please set TYPEFORM_API_KEY and SLACK_WEBHOOK_URL environment variables.")
        exit(1)

    # Initialize Typeform and Slack integrations
    typeform_survey = TypeformSurvey(TYPEFORM_API_KEY)
    slack_integration = SlackIntegration(SLACK_WEBHOOK_URL)

    # Define survey details
    survey_title = "Customer Feedback Survey"
    survey_questions = [
        {"title": "How satisfied are you with our service?", "type": "multiple_choice", "choices": [{"label": "Very satisfied"}, {"label": "Satisfied"}, {"label": "Neutral"}, {"label": "Dissatisfied"}, {"label": "Very dissatisfied"}], "required": True},
        {"title": "Any additional comments?", "type": "long_text", "required": False}
    ]

    # Create the survey
    survey_response = typeform_survey.create_survey(survey_title, survey_questions)

    if survey_response:
        # Send confirmation to Slack
        slack_integration.send_message(f"New survey created: {survey_response.get('url')}")
```
