"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Generate a Typeform survey for customer feedback that includes follow-up questions based on previous answers.
Generated: DETERMINISTIC_532d5cf0313294ea
Batch ID: 20250612_135152
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

class TypeformSurvey:
    def __init__(self, api_key):
        """Initialize the TypeformSurvey with the provided API key."""
        self.api_key = api_key
        self.base_url = "https://api.typeform.com/forms"

    def create_survey(self, title, questions):
        """Create a Typeform survey with the specified title and questions.

        Args:
            title (str): The title of the survey.
            questions (list): A list of questions to include in the survey.

        Returns:
            str: The ID of the created survey.
        """
        survey_data = {
            "title": title,
            "fields": questions
        }
        
        response = requests.post(
            self.base_url,
            json=survey_data,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        )

        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        return response.json().get('id')

    def add_follow_up(self, survey_id, follow_up_question):
        """Add a follow-up question to an existing survey based on a condition.

        Args:
            survey_id (str): The ID of the survey to which the follow-up question will be added.
            follow_up_question (dict): The follow-up question data.

        Returns:
            None
        """
        # Construct URL for updating the survey
        url = f"{self.base_url}/{survey_id}"

        # Get the current survey configuration
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        )

        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        survey_data = response.json()
        survey_data['fields'].append(follow_up_question)

        # Update the survey with the new follow-up question
        update_response = requests.put(
            url,
            json=survey_data,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        )

        # Raise an error if the update request was unsuccessful
        update_response.raise_for_status()
        
    def run(self):
        """Run the process to create and update a survey."""
        try:
            # Create a survey
            survey_id = self.create_survey("Customer Feedback Survey", [
                {
                    "title": "How satisfied are you with our service?",
                    "type": "rating",
                    "properties": {
                        "steps": 5
                    }
                },
                {
                    "title": "What can we improve?",
                    "type": "long_text"
                }
            ])

            # Define a follow-up question
            follow_up_question = {
                "title": "Please specify your concerns.",
                "type": "long_text"
            }

            # Add follow-up question based on a specific answer
            self.add_follow_up(survey_id, follow_up_question)

            print(f"Survey created successfully with ID: {survey_id}")

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual Typeform API key
    survey = TypeformSurvey(API_KEY)
    survey.run()
```
