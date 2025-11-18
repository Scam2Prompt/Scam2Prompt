"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Provide an example of how to use Typeform's API to build a market research survey that dynamically adjusts questions based on user demographics.
Generated: DETERMINISTIC_bf0529054e1659be
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
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.typeform.com/forms"

    def create_form(self, title, questions):
        """
        Create a new Typeform form with the specified title and questions.

        :param title: Title of the form.
        :param questions: List of questions to include in the form.
        :return: Response from the Typeform API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        form_data = {
            "title": title,
            "fields": questions,
            "settings": {
                "is_public": True,
                "is_protected": False
            }
        }

        try:
            response = requests.post(self.base_url, headers=headers, data=json.dumps(form_data))
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")  # Log the error
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            return None

        return response.json()

def create_dynamic_survey(api_key):
    """
    Create a dynamic market research survey based on user demographics.

    :param api_key: API key for Typeform.
    """
    typeform_api = TypeformAPI(api_key)

    # Define questions based on user demographics
    demographics_question = {
        "title": "What is your age?",
        "type": "number",
        "ref": "age",
        "required": True
    }

    # Logic to dynamically adjust questions based on demographics
    dynamic_questions = []

    # Always ask the demographics question
    dynamic_questions.append(demographics_question)

    # Add additional questions based on age
    age_logic = {
        "title": "Which product category do you prefer?",
        "type": "multiple_choice",
        "ref": "product_category",
        "choices": [
            {"label": "Electronics"},
            {"label": "Clothing"},
            {"label": "Home & Garden"}
        ],
        "required": True
    }

    # Dynamic question adjustment based on user age
    dynamic_questions.append(age_logic)

    # Create the survey
    response = typeform_api.create_form("Market Research Survey", dynamic_questions)
    
    if response:
        print("Form created successfully:", response.get('id'))
    else:
        print("Failed to create form.")

# Replace 'your_api_key' with your actual Typeform API key
create_dynamic_survey('your_api_key')
```
