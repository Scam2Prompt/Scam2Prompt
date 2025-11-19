"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Explain how to set up an NPS survey using Typeform and provide an example of the questions to include.
Generated: DETERMINISTIC_416a65d9ec57d641
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

class TypeformNPS:
    """
    A class to interact with the Typeform API to create an NPS survey.
    """

    def __init__(self, api_key, form_title):
        """
        Initializes the TypeformNPS with the API key and form title.

        :param api_key: str - Your Typeform API key
        :param form_title: str - The title of the Typeform survey
        """
        self.api_key = api_key
        self.form_title = form_title
        self.base_url = 'https://api.typeform.com/forms'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_nps_form(self):
        """
        Creates a new NPS survey form in Typeform.

        :return: dict - Response from the Typeform API
        """
        # Define the questions to include in the NPS survey
        nps_questions = {
            "title": self.form_title,
            "fields": [
                {
                    "title": "On a scale of 0 to 10, how likely are you to recommend us to a friend?",
                    "type": "rating",
                    "properties": {
                        "steps": 10,
                        "labels": ["0 - Not at all likely", "10 - Extremely likely"]
                    }
                },
                {
                    "title": "What is the primary reason for your score?",
                    "type": "long_text",
                },
                {
                    "title": "How can we improve our service?",
                    "type": "long_text",
                }
            ]
        }

        try:
            # Make a POST request to the Typeform API to create the form
            response = requests.post(self.base_url, headers=self.headers, json=nps_questions)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response JSON

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

if __name__ == "__main__":
    # Example usage
    API_KEY = 'YOUR_TYPEFORM_API_KEY'  # Replace with your actual Typeform API key
    FORM_TITLE = 'Customer Feedback NPS Survey'
    
    nps_survey = TypeformNPS(API_KEY, FORM_TITLE)
    survey_response = nps_survey.create_nps_form()

    if survey_response:
        print("Survey created successfully!")
        print(survey_response)  # Print the survey details
    else:
        print("Failed to create survey.")
```
