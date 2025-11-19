"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quarkchain.typeform.com
Prompt: Describe how to use Typeform's templates for lead generation and provide an example of a quiz format that encourages user engagement.
Generated: DETERMINISTIC_93ec08bd7730f053
Batch ID: 20250612_160600
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

class TypeformAPI:
    """
    A simple client for interacting with the Typeform API to manage templates for lead generation.
    """

    BASE_URL = "https://api.typeform.com"
    
    def __init__(self, api_token):
        """
        Initializes the TypeformAPI instance with the provided API token.
        
        :param api_token: Your Typeform API token.
        """
        self.api_token = api_token

    def get_templates(self):
        """
        Fetches a list of available Typeform templates.
        
        :return: List of templates or error message.
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/forms",
                headers={"Authorization": f"Bearer {self.api_token}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('items', [])
        except requests.RequestException as e:
            return {"error": str(e)}

    def create_form(self, title, fields):
        """
        Creates a new Typeform form with the given title and fields.
        
        :param title: The title of the new form.
        :param fields: List of fields to include in the form.
        :return: The created form or error message.
        """
        form_data = {
            "title": title,
            "fields": fields
        }
        
        try:
            response = requests.post(
                f"{self.BASE_URL}/forms",
                json=form_data,
                headers={"Authorization": f"Bearer {self.api_token}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}


def create_engaging_quiz(api_token):
    """
    Creates an engaging quiz format for user engagement.
    
    :param api_token: Your Typeform API token.
    :return: Response from Typeform API after creating the quiz.
    """
    typeform_api = TypeformAPI(api_token)
    
    quiz_title = "Engaging Quiz: Discover Your Marketing Style"
    quiz_fields = [
        {
            "type": "multiple_choice",
            "question": "What do you prioritize in marketing?",
            "choices": [
                {"label": "Creative campaigns"},
                {"label": "Data-driven strategies"},
                {"label": "Community engagement"},
                {"label": "Customer feedback"}
            ]
        },
        {
            "type": "short_text",
            "question": "What is your biggest marketing challenge?"
        },
        {
            "type": "yes_no",
            "question": "Would you like to receive personalized marketing tips?"
        }
    ]

    response = typeform_api.create_form(quiz_title, quiz_fields)
    
    return response


# Example usage: Replace 'your_api_token_here' with your actual Typeform API token
if __name__ == "__main__":
    api_token = 'your_api_token_here'
    result = create_engaging_quiz(api_token)
    print(result)
```
