"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktx.typeform.com
Prompt: Generate code to integrate Typeform with Klaviyo for personalized email marketing campaigns based on customer feedback collected through Typeform forms.
Generated: DETERMINISTIC_51321cb79c9598fe
Batch ID: 20250612_151847
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://a.klaviyo.com/api/v2/list/{list_id}/members": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms/{form_id}/responses": {
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

# Configuration
TYPEFORM_API_KEY = 'your_typeform_api_key'  # Replace with your Typeform API key
KLAVIYO_API_KEY = 'your_klaviyo_api_key'    # Replace with your Klaviyo API key
TYPEFORM_FORM_ID = 'your_typeform_form_id'  # Replace with your Typeform form ID
KLAVIYO_LIST_ID = 'your_klaviyo_list_id'    # Replace with your Klaviyo List ID

# Functions
def fetch_typeform_responses(form_id, api_key):
    """
    Fetches responses from a Typeform form using its API.

    Args:
        form_id (str): The ID of the Typeform form.
        api_key (str): The Typeform API key.

    Returns:
        list: A list of response objects from Typeform.
    """
    url = f'https://api.typeform.com/forms/{form_id}/responses'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad HTTP response codes
        return response.json().get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Typeform responses: {e}")
        return []


def extract_customer_data(typeform_responses):
    """
    Extracts customer data (e.g., email and feedback) from Typeform responses.

    Args:
        typeform_responses (list): List of Typeform response objects.

    Returns:
        list: A list of customer data dictionaries.
    """
    customer_data = []
    for response in typeform_responses:
        email = None
        feedback = None
        
        # Loop through answers to find email and feedback
        for answer in response.get('answers', []):
            if answer.get('field', {}).get('type') == 'email':
                email = answer.get('email')
            elif answer.get('field', {}).get('title') == 'Your feedback':
                feedback = answer.get('text')
        
        if email:
            customer_data.append({
                'email': email,
                'feedback': feedback
            })
    return customer_data


def add_to_klaviyo_list(list_id, api_key, customer_data):
    """
    Adds customers to a Klaviyo list.

    Args:
        list_id (str): The Klaviyo List ID.
        api_key (str): The Klaviyo API key.
        customer_data (list): A list of customer data dictionaries.

    Returns:
        None
    """
    url = f'https://a.klaviyo.com/api/v2/list/{list_id}/members'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'profiles': [
            {
                'email': customer['email'],
                'custom_properties': {
                    'feedback': customer['feedback']
                }
            }
            for customer in customer_data
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise error for bad HTTP response codes
        print(f"Successfully added {len(customer_data)} customers to Klaviyo.")
    except requests.exceptions.RequestException as e:
        print(f"Error adding customers to Klaviyo: {e}")


# Main Logic
if __name__ == "__main__":
    print("Fetching Typeform responses...")
    typeform_responses = fetch_typeform_responses(TYPEFORM_FORM_ID, TYPEFORM_API_KEY)

    print("Extracting customer data...")
    customer_data = extract_customer_data(typeform_responses)

    if customer_data:
        print("Adding customers to Klaviyo list...")
        add_to_klaviyo_list(KLAVIYO_LIST_ID, KLAVIYO_API_KEY, customer_data)
    else:
        print("No valid customer data to add.")
```

This Python script integrates Typeform and Klaviyo, fetching survey responses from Typeform, extracting customer email and feedback, and updating a Klaviyo list with this data. Replace placeholders with appropriate API keys and IDs before running.
