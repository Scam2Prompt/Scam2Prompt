"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Demonstrate how to create an event registration form using Typeform's API, including fields for name, email, and event preferences.
Generated: DETERMINISTIC_1f0f9052a8b1a4da
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

class TypeformAPI:
    """
    A class to interact with Typeform's API for creating an event registration form.
    """

    def __init__(self, api_key):
        """
        Initializes the TypeformAPI with the provided API key.

        Args:
            api_key (str): Your Typeform API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.typeform.com/forms"

    def create_form(self, title, fields):
        """
        Creates a new Typeform form with the provided title and fields.

        Args:
            title (str): The title of the form.
            fields (list): A list of field dictionaries to include in the form.

        Returns:
            dict: The response from the Typeform API containing form details.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        form_data = {
            "title": title,
            "fields": fields
        }

        try:
            response = requests.post(self.base_url, json=form_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

def main():
    # Replace 'your_api_key' with your actual Typeform API Key
    api_key = 'your_api_key'
    typeform_api = TypeformAPI(api_key)

    # Define the fields for the event registration form
    fields = [
        {
            "id": "name",
            "title": "What is your name?",
            "type": "short_text",
            "required": True
        },
        {
            "id": "email",
            "title": "What is your email?",
            "type": "email",
            "required": True
        },
        {
            "id": "event_preferences",
            "title": "What events are you interested in?",
            "type": "multiple_choice",
            "choices": [
                {"id": "event_1", "label": "Event 1"},
                {"id": "event_2", "label": "Event 2"},
                {"id": "event_3", "label": "Event 3"}
            ],
            "required": True
        }
    ]

    # Create the form
    form_title = "Event Registration"
    form_response = typeform_api.create_form(form_title, fields)

    if form_response:
        print("Form created successfully!")
        print("Form Details:", form_response)
    else:
        print("Failed to create the form.")

if __name__ == "__main__":
    main()
```
