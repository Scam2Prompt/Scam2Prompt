"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airgiveaway.typeform.com
Prompt: Create a Typeform-based employee onboarding form using the API, with conditional logic to tailor questions based on the department selected by the user.
Generated: DETERMINISTIC_a69c70f439314b6e
Batch ID: 20250612_151847
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

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_TOKEN = "your_typeform_api_token_here"  # Replace with your Typeform API token.

# Headers for Typeform API requests
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
    "Content-Type": "application/json"
}

def create_onboarding_form():
    """
    Creates an employee onboarding form in Typeform with conditional logic
    based on the department selected by the user.
    """
    # Form payload
    form_payload = {
        "title": "Employee Onboarding Form",
        "fields": [
            {
                "type": "multiple_choice",
                "title": "Which department are you joining?",
                "ref": "department_question",
                "choices": [
                    {"label": "Engineering"},
                    {"label": "Marketing"},
                    {"label": "Sales"},
                    {"label": "HR"}
                ]
            },
            {
                "type": "short_text",
                "title": "What is your preferred programming language?",
                "ref": "engineering_question",
                "properties": {
                    "description": "This is specific to Engineering department."
                },
                "conditions": {
                    "field": "department_question",
                    "value": "Engineering"
                }
            },
            {
                "type": "short_text",
                "title": "Do you have experience with Google Analytics?",
                "ref": "marketing_question",
                "properties": {
                    "description": "This is specific to Marketing department."
                },
                "conditions": {
                    "field": "department_question",
                    "value": "Marketing"
                }
            },
            {
                "type": "short_text",
                "title": "How many years of experience do you have in sales?",
                "ref": "sales_question",
                "properties": {
                    "description": "This is specific to Sales department."
                },
                "conditions": {
                    "field": "department_question",
                    "value": "Sales"
                }
            },
            {
                "type": "short_text",
                "title": "What is your preferred HR management tool?",
                "ref": "hr_question",
                "properties": {
                    "description": "This is specific to HR department."
                },
                "conditions": {
                    "field": "department_question",
                    "value": "HR"
                }
            }
        ]
    }

    try:
        # Create the form via the Typeform API
        response = requests.post(TYPEFORM_API_URL, json=form_payload, headers=HEADERS)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        form_data = response.json()

        print("Form created successfully!")
        print(f"Form ID: {form_data['id']}")
        return form_data
    except requests.exceptions.RequestException as e:
        # Handle API errors
        print(f"Error creating form: {e}")
        return None

# Run the function to create the onboarding form
if __name__ == "__main__":
    create_onboarding_form()
```
