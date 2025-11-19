"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Create a Typeform quiz that gathers deeper insights by asking follow-up questions based on previous answers. Include design customization tips.
Generated: DETERMINISTIC_a3e5ba04407182cb
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

# Constants
TYPEFORM_API_BASE_URL = "https://api.typeform.com"
TYPEFORM_API_TOKEN = "your_typeform_api_token"  # Replace with your Typeform API token

# Create headers for API requests
HEADERS = {
    "Authorization": f"Bearer {TYPEFORM_API_TOKEN}",
    "Content-Type": "application/json"
}

def create_typeform_quiz():
    """
    Creates a Typeform quiz with follow-up conditional logic based on answers.
    """
    # Define the form structure
    form_data = {
        "title": "Dynamic Insights Quiz",
        "type": "form",
        "fields": [
            {
                "type": "multiple_choice",
                "title": "What's your preferred method of learning?",
                "choices": [
                    {"label": "Videos"},
                    {"label": "Books"},
                    {"label": "Interactive workshops"}
                ],
                "ref": "learning_preference"
            },
            {
                "type": "short_text",
                "title": "What topics are you interested in learning?",
                "ref": "topics"
            },
            {
                "type": "statement",
                "title": "Follow-up: You selected Videos. What's your favorite platform?",
                "ref": "followup_videos",
                "layout": "classic",
                "hidden": True  # This field is conditionally shown
            },
            {
                "type": "statement",
                "title": "Follow-up: You selected Books. Favorite author or genre?",
                "ref": "followup_books",
                "layout": "classic",
                "hidden": True  # This field is conditionally shown
            },
            {
                "type": "statement",
                "title": "Follow-up: You selected Interactive workshops. What topics do you enjoy?",
                "ref": "followup_workshops",
                "layout": "classic",
                "hidden": True  # This field is conditionally shown
            }
        ],
        "logic": [
            {
                "type": "field",
                "ref": "learning_preference",
                "actions": [
                    {
                        "action": "jump",
                        "condition": {
                            "op": "is",
                            "vars": [{"type": "field", "value": "learning_preference"}, {"type": "constant", "value": "Videos"}]
                        },
                        "to": {"type": "field", "value": "followup_videos"}
                    },
                    {
                        "action": "jump",
                        "condition": {
                            "op": "is",
                            "vars": [{"type": "field", "value": "learning_preference"}, {"type": "constant", "value": "Books"}]
                        },
                        "to": {"type": "field", "value": "followup_books"}
                    },
                    {
                        "action": "jump",
                        "condition": {
                            "op": "is",
                            "vars": [{"type": "field", "value": "learning_preference"}, {"type": "constant", "value": "Interactive workshops"}]
                        },
                        "to": {"type": "field", "value": "followup_workshops"}
                    }
                ]
            }
        ]
    }

    # Make the API request to create the form
    try:
        response = requests.post(
            f"{TYPEFORM_API_BASE_URL}/forms",
            headers=HEADERS,
            json=form_data
        )
        response.raise_for_status()  # Raise an error for bad HTTP responses
        form_id = response.json().get("id")
        print(f"Form successfully created! Form ID: {form_id}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating the form: {e}")

if __name__ == "__main__":
    create_typeform_quiz()
```

### Design Customization Tips:
1. Set the `layout` property for fields to `classic` or `modern` depending on the desired aesthetics.
2. Add branding (logo and theme) via the Typeform admin panel or API.
3. Use custom fonts, colors, and background images to align the quiz with your organization's branding.
