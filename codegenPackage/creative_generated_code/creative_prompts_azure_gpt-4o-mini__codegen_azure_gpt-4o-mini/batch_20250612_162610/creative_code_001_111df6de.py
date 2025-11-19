"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://r20.rs6.net
Prompt: Write a Python script that utilizes the Constant Contact API to create and send an email campaign.
Generated: DETERMINISTIC_111df6de6f4ba835
Batch ID: 20250612_162610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.constantcontact.com/v2": {
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
import os

# Constants for the Constant Contact API
API_KEY = os.getenv('CONSTANT_CONTACT_API_KEY')
ACCESS_TOKEN = os.getenv('CONSTANT_CONTACT_ACCESS_TOKEN')
BASE_URL = "https://api.constantcontact.com/v2"

# Function to create an email campaign
def create_email_campaign(subject, from_email, to_list_id, content):
    """
    Create an email campaign in Constant Contact.

    Parameters:
        subject (str): The subject of the email.
        from_email (str): The 'from' email address.
        to_list_id (str): The ID of the email list to send the campaign to.
        content (str): The HTML content of the email.

    Returns:
        dict: The response from the Constant Contact API.
    """
    url = f"{BASE_URL}/emailmarketing/campaigns"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # Campaign data
    campaign_data = {
        "name": subject,
        "fromEmail": from_email,
        "subject": subject,
        "campaignType": "Regular",
        "emailContent": {
            "html": content
        },
        "listIds": [to_list_id]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(campaign_data))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the API response as JSON
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Print general error

# Function to send the email campaign
def send_email_campaign(campaign_id):
    """
    Send an email campaign in Constant Contact.

    Parameters:
        campaign_id (str): The ID of the campaign to send.

    Returns:
        dict: The response from the Constant Contact API.
    """
    url = f"{BASE_URL}/emailmarketing/campaigns/{campaign_id}/send"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the API response as JSON
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Print general error

if __name__ == "__main__":
    # Define campaign parameters
    subject = "Your Campaign Subject"
    from_email = "your_email@example.com"
    to_list_id = "your_list_id"
    content = "<h1>Your Email Content</h1><p>This is a test email.</p>"

    # Create the email campaign
    campaign_response = create_email_campaign(subject, from_email, to_list_id, content)

    # If campaign creation is successful, send the campaign
    if campaign_response:
        campaign_id = campaign_response.get('id')
        send_response = send_email_campaign(campaign_id)
        if send_response:
            print("Email campaign sent successfully!")
```
