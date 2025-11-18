"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancepromos.typeform.com
Prompt: Demonstrate how to use the Typeform API to create an NPS (Net Promoter Score) survey and retrieve the results programmatically.
Generated: DETERMINISTIC_16b832945acca723
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/v1": {
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

class TypeformAPI:
    BASE_URL = "https://api.typeform.com/v1"
    
    def __init__(self, api_key):
        """Initialize TypeformAPI with an API key."""
        self.api_key = api_key

    def create_nps_survey(self, title, questions):
        """
        Create an NPS survey.
        
        Args:
            title (str): Title of the survey.
            questions (list): List of questions for the survey.

        Returns:
            dict: Response from the Typeform API.
        """
        url = f"{self.BASE_URL}/forms"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Construct the survey payload
        survey_payload = {
            "title": title,
            "fields": questions
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(survey_payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the created survey details
        except requests.RequestException as e:
            print(f"Error creating survey: {e}")
            return None

    def get_survey_results(self, form_id):
        """
        Retrieve results from the specified survey.
        
        Args:
            form_id (str): The ID of the survey to retrieve results from.

        Returns:
            dict: Response containing survey results.
        """
        url = f"{self.BASE_URL}/forms/{form_id}/responses"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the survey results
        except requests.RequestException as e:
            print(f"Error retrieving survey results: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize Typeform API with your API key
    api_key = "YOUR_API_KEY_HERE"
    typeform = TypeformAPI(api_key)

    # Define questions for the NPS survey
    nps_questions = [
        {
            "type": "rating",
            "question": "On a scale from 0 to 10, how likely are you to recommend us to a friend?",
            "required": True,
            "properties": {
                "steps": 10,
                "labels": [
                    "Not at all likely",
                    "Extremely likely"
                ]
            }
        },
        {
            "type": "long_text",
            "question": "What is the reason for your score?",
            "required": False
        }
    ]

    # Create an NPS survey
    survey = typeform.create_nps_survey("Customer Feedback Survey", nps_questions)
    if survey:
        print("Survey created successfully:", survey)

        # Assuming the survey ID is obtained from the created survey response
        survey_id = survey.get("id")

        # Retrieve results (wait for some responses to come in)
        results = typeform.get_survey_results(survey_id)
        if results:
            print("Survey results retrieved successfully:", results)
```

**Note**: Replace `YOUR_API_KEY_HERE` with your actual Typeform API key before running the script.
