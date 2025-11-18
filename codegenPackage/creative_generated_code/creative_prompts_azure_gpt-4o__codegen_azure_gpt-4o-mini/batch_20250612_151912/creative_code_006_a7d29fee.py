"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://essentialairdrop.typeform.com
Prompt: Provide a step-by-step guide to integrate Typeform with Mailchimp for automated email campaigns based on form submissions.
Generated: DETERMINISTIC_a7d29fee2df0e480
Batch ID: 20250612_151912
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms/{form_id}/responses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://<dc>.api.mailchimp.com/3.0/lists/{list_id}/members": {
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

# Constants for Typeform API
TYPEFORM_API_URL = "https://api.typeform.com/forms/{form_id}/responses"
TYPEFORM_ACCESS_TOKEN = "YOUR_TYPEFORM_ACCESS_TOKEN"

# Constants for Mailchimp API
MAILCHIMP_API_URL = "https://<dc>.api.mailchimp.com/3.0/lists/{list_id}/members"
MAILCHIMP_API_KEY = "YOUR_MAILCHIMP_API_KEY"
MAILCHIMP_LIST_ID = "YOUR_MAILCHIMP_LIST_ID"

def fetch_typeform_responses(form_id):
    """
    Fetch responses from Typeform.

    Args:
        form_id (str): The ID of the Typeform form.

    Returns:
        list: A list of responses from the Typeform API.
    """
    url = TYPEFORM_API_URL.format(form_id=form_id)
    headers = {
        "Authorization": f"Bearer {TYPEFORM_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Typeform responses: {e}")
        return []

def add_to_mailchimp(email):
    """
    Add a new subscriber to Mailchimp.

    Args:
        email (str): The email address to subscribe.

    Returns:
        None
    """
    url = MAILCHIMP_API_URL.format(list_id=MAILCHIMP_LIST_ID)
    headers = {
        "Authorization": f"anystring:{MAILCHIMP_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        print(f"Successfully added {email} to Mailchimp.")
    except requests.exceptions.RequestException as e:
        print(f"Error adding to Mailchimp: {e}")

def process_responses(form_id):
    """
    Process Typeform responses and add emails to Mailchimp.

    Args:
        form_id (str): The ID of the Typeform form.

    Returns:
        None
    """
    responses = fetch_typeform_responses(form_id)
    for response in responses:
        email = None
        # Assuming the email is captured in a field named 'email'
        for answer in response['answers']:
            if answer['field']['id'] == 'YOUR_EMAIL_FIELD_ID':
                email = answer['text']
                break
        
        if email:
            add_to_mailchimp(email)

if __name__ == "__main__":
    # Replace 'YOUR_TYPEFORM_FORM_ID' with the actual Typeform form ID
    FORM_ID = "YOUR_TYPEFORM_FORM_ID"
    process_responses(FORM_ID)
```
