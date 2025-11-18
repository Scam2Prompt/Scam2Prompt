"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Provide an example of using Typeform's API to create an interactive story template with branching logic based on user input.
Generated: DETERMINISTIC_e19cf3ce4f5722f2
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

# Constants
TYPEFORM_API_URL = "https://api.typeform.com/forms"
TYPEFORM_API_TOKEN = "your_typeform_api_token_here"  # Replace with your actual API token

def create_typeform_story_template():
    """
    Creates an interactive story template in Typeform with branching logic.
    The story template includes questions and branches based on user input.
    """
    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "title": "Interactive Story Template",
        "fields": [
            {
                "type": "multiple_choice",
                "title": "You wake up in a forest. What do you do?",
                "ref": "question1",
                "choices": [
                    {"ref": "choice1", "label": "Look for food"},
                    {"ref": "choice2", "label": "Keep walking"}
                ]
            },
            {
                "type": "multiple_choice",
                "title": "You find a river. What do you do?",
                "ref": "question2",
                "choices": [
                    {"ref": "choice3", "label": "Drink water"},
                    {"ref": "choice4", "label": "Follow the river"}
                ]
            },
            {
                "type": "statement",
                "title": "You encounter a bear. The story ends here!",
                "ref": "ending1"
            },
            {
                "type": "statement",
                "title": "You find a village and get help. The story ends happily!",
                "ref": "ending2"
            }
        ],
        "logic": [
            {
                "type": "jump",
                "ref": "logic1",
                "from": {
                    "type": "answer",
                    "field": {
                        "ref": "question1"
                    },
                    "choice": {
                        "ref": "choice1"
                    }
                },
                "to": {
                    "type": "field",
                    "ref": "question2"
                }
            },
            {
                "type": "jump",
                "ref": "logic2",
                "from": {
                    "type": "answer",
                    "field": {
                        "ref": "question2"
                    },
                    "choice": {
                        "ref": "choice3"
                    }
                },
                "to": {
                    "type": "field",
                    "ref": "ending1"
                }
            },
            {
                "type": "jump",
                "ref": "logic3",
                "from": {
                    "type": "answer",
                    "field": {
                        "ref": "question2"
                    },
                    "choice": {
                        "ref": "choice4"
                    }
                },
                "to": {
                    "type": "field",
                    "ref": "ending2"
                }
            }
        ]
    }

    try:
        response = requests.post(TYPEFORM_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad status codes
        form_data = response.json()
        print("Typeform successfully created!")
        print(f"Form ID: {form_data['id']}")
        print(f"Share URL: {form_data['_links']['display']}")
    except requests.exceptions.RequestException as e:
        print(f"Error creating Typeform: {e}")

# Run the function
if __name__ == "__main__":
    create_typeform_story_template()
```
