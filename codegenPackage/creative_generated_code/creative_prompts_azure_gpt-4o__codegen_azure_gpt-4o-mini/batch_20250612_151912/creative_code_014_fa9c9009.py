"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Show how to use the Typeform API to create a trivia quiz with real-time scoring and display results to participants.
Generated: DETERMINISTIC_fa9c9009b70cf3a4
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

class TypeformAPI:
    """
    A class to interact with the Typeform API for creating trivia quizzes.
    """

    BASE_URL = "https://api.typeform.com/forms"
    
    def __init__(self, api_key):
        """
        Initializes the TypeformAPI with the provided API key.

        :param api_key: The API key for Typeform.
        """
        self.api_key = api_key

    def create_quiz(self, title, questions):
        """
        Creates a trivia quiz by sending a POST request to the Typeform API.

        :param title: The title of the quiz.
        :param questions: A list of question objects for the quiz.
        :return: The response from the API containing the created form ID or an error message.
        """
        # Construct the form data
        form_data = {
            "title": title,
            "fields": questions
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.BASE_URL, headers=headers, data=json.dumps(form_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the created form data
        except requests.exceptions.RequestException as e:
            print(f"Error creating quiz: {e}")
            return None

    def get_quiz_results(self, form_id):
        """
        Retrieves the results from the specified quiz.

        :param form_id: The ID of the quiz to fetch results for.
        :return: The results of the quiz or an error message.
        """
        results_url = f"{self.BASE_URL}/{form_id}/responses"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(results_url, headers=headers)
            response.raise_for_status()
            return response.json()  # Return the quiz results
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quiz results: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_typeform_api_key_here"  # Replace with your Typeform API key

    # Define questions for the trivia quiz
    questions = [
        {
            "title": "What is the capital of France?",
            "type": "multiple_choice",
            "choices": [
                {"label": "London"},
                {"label": "Berlin"},
                {"label": "Paris"},
                {"label": "Madrid"}
            ],
            "required": True
        },
        {
            "title": "What is 2 + 2?",
            "type": "number",
            "required": True
        }
    ]

    typeform_api = TypeformAPI(API_KEY)
    quiz_response = typeform_api.create_quiz("Trivia Quiz", questions)

    if quiz_response:
        print("Quiz created successfully! Form ID:", quiz_response.get("id"))
        # You can now present the quiz to participants and collect responses

        # To fetch results later
        form_id = quiz_response.get("id")
        results = typeform_api.get_quiz_results(form_id)

        if results:
            print("Quiz results:", results)
        else:
            print("No results found or error fetching results.")
```
