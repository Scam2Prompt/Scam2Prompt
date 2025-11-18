"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Write a script to use Typeform's API for sending follow-up questions to survey respondents based on their previous answers.
Generated: DETERMINISTIC_deea0393b2731a93
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
import json

class TypeformAPI:
    def __init__(self, api_key):
        """
        Initialize the TypeformAPI with the provided API key.

        :param api_key: The API key for authenticating requests to Typeform.
        """
        self.api_key = api_key
        self.base_url = "https://api.typeform.com"

    def send_follow_up(self, form_id, responses):
        """
        Send follow-up questions based on the respondent's previous answers.

        :param form_id: The ID of the Typeform form to which the follow-up will be sent.
        :param responses: A dictionary containing the respondent's previous answers.
        :return: The response from the Typeform API.
        """
        try:
            for question_id, answer in responses.items():
                follow_up_question = self.get_follow_up_question(question_id, answer)
                if follow_up_question:
                    self.post_follow_up(form_id, follow_up_question)

        except Exception as e:
            print(f"An error occurred while sending follow-up questions: {e}")

    def get_follow_up_question(self, question_id, answer):
        """
        Determine the follow-up question based on the previous answer.

        :param question_id: The ID of the question answered by the respondent.
        :param answer: The answer given by the respondent.
        :return: A follow-up question if applicable; otherwise, None.
        """
        # This is a placeholder for the actual logic to determine follow-up questions
        follow_up_questions = {
            "Q1": {
                "Yes": "What motivated your decision?",
                "No": "What were your concerns?"
            }
        }

        return follow_up_questions.get(question_id, {}).get(answer, None)

    def post_follow_up(self, form_id, follow_up_question):
        """
        Post the follow-up question to the Typeform API.

        :param form_id: The ID of the Typeform form.
        :param follow_up_question: The follow-up question to be sent.
        :return: The response from the API call.
        """
        url = f"{self.base_url}/forms/{form_id}/responses"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "answers": [
                {
                    "question_id": form_id,  # In a real-world scenario, this would be the actual question ID
                    "text": follow_up_question
                }
            ]
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code != 201:
            print(f"Error posting follow-up question: {response.status_code} - {response.text}")
        else:
            print("Follow-up question sent successfully.")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_typeform_api_key"
    FORM_ID = "your_form_id"
    
    # Example responses from a respondent
    responses = {
        "Q1": "Yes",  # Respondent's answer
    }

    typeform_api = TypeformAPI(API_KEY)
    typeform_api.send_follow_up(FORM_ID, responses)
```
