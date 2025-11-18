"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Write code to integrate ActiveCampaign with a website to capture visitor details and automate follow-up messaging, as described by Sales Studios.
Generated: DETERMINISTIC_fa3dec4549bc0e36
Batch ID: 20250612_145255
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://youraccount.api-us1.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://youraccount.api-us1.com/api/3/": {
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

class ActiveCampaignIntegration:
    """
    A class to integrate ActiveCampaign with a website for capturing visitor details
    and automating follow-up messaging.
    """

    def __init__(self, api_url, api_key):
        """
        Initialize the ActiveCampaignIntegration with API credentials.

        :param api_url: The base URL of the ActiveCampaign API (e.g., 'https://youraccount.api-us1.com/api/3/')
        :param api_key: The API key for authenticating with ActiveCampaign
        """
        self.api_url = api_url.rstrip('/') + '/api/3/'
        self.api_key = api_key

    def create_contact(self, email, first_name=None, last_name=None, phone=None):
        """
        Create or update a contact in ActiveCampaign.

        :param email: Email address of the contact (required)
        :param first_name: First name of the contact (optional)
        :param last_name: Last name of the contact (optional)
        :param phone: Phone number of the contact (optional)
        :return: Response from ActiveCampaign API
        """
        url = self.api_url + 'contacts'
        headers = {
            'Content-Type': 'application/json',
            'Api-Token': self.api_key
        }
        payload = {
            'contact': {
                'email': email,
                'firstName': first_name,
                'lastName': last_name,
                'phone': phone
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise error for HTTP codes >= 400
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            # Log error (could replace 'print' with proper logging in production)
            print(f"Error creating contact: {e}")
            return None

    def create_automation_entry(self, contact_id, automation_id):
        """
        Add a contact to an automation in ActiveCampaign.

        :param contact_id: The ID of the contact to add to the automation
        :param automation_id: The ID of the automation
        :return: Response from ActiveCampaign API
        """
        url = self.api_url + 'contactAutomations'
        headers = {
            'Content-Type': 'application/json',
            'Api-Token': self.api_key
        }
        payload = {
            'contactAutomation': {
                'contact': contact_id,
                'automation': automation_id
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise error for HTTP codes >= 400
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            # Log error (could replace 'print' with proper logging in production)
            print(f"Error adding contact to automation: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Replace these with your ActiveCampaign account details
    ACTIVE_CAMPAIGN_API_URL = "https://youraccount.api-us1.com/"
    ACTIVE_CAMPAIGN_API_KEY = "your_api_key"

    # Initialize ActiveCampaignIntegration
    ac_integration = ActiveCampaignIntegration(ACTIVE_CAMPAIGN_API_URL, ACTIVE_CAMPAIGN_API_KEY)

    # Capture visitor details (replace with actual data from your website)
    email = "visitor@example.com"
    first_name = "John"
    last_name = "Doe"
    phone = "1234567890"

    # Create contact in ActiveCampaign
    contact_response = ac_integration.create_contact(email, first_name, last_name, phone)
    if contact_response:
        contact_id = contact_response.get("contact", {}).get("id")
        if contact_id:
            print(f"Contact created with ID: {contact_id}")

            # Add the contact to an automation (replace 'automation_id' with your actual automation ID)
            automation_id = 1  # Example automation ID
            automation_response = ac_integration.create_automation_entry(contact_id, automation_id)
            if automation_response:
                print(f"Contact added to automation ID: {automation_id}")
        else:
            print("Failed to retrieve contact ID from response.")
    else:
        print("Failed to create contact.")
```
