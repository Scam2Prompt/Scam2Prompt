"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsolution.co.id
Prompt: What are the best practices for implementing Zoho's Sales and Marketing Automation tools in a small business?
Generated: DETERMINISTIC_4e3bb72e5db571d8
Batch ID: 20250612_155301
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.zohoapis.com/crm/v2/Leads": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.zohoapis.com/crm/v2/Leads/{lead_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.zoho.com/oauth/v2/token": {
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

class ZohoCRM:
    """
    A class to interact with Zoho's Sales and Marketing Automation APIs.
    This example includes methods for authentication, obtaining leads,
    and updating lead status.
    """

    def __init__(self, client_id, client_secret, redirect_uri, refresh_token):
        """
        Initializes the ZohoCRM instance with the required credentials.

        :param client_id: The client ID from Zoho
        :param client_secret: The client secret from Zoho
        :param redirect_uri: The redirect URI configured in Zoho
        :param refresh_token: The refresh token obtained during OAuth flow
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token
        self.access_token = None

    def get_access_token(self):
        """
        Obtains an access token using the refresh token.
        This token is used to authenticate API requests.

        :return: Access token string
        """
        token_url = "https://accounts.zoho.com/oauth/v2/token"
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }

        try:
            response = requests.post(token_url, data=params)
            response.raise_for_status()  # Raise an error for bad responses
            self.access_token = response.json().get('access_token')
            return self.access_token
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining access token: {e}")
            return None

    def get_leads(self):
        """
        Fetches leads from Zoho CRM.

        :return: List of leads or None on failure
        """
        if not self.access_token:
            print("Access token is not available.")
            return None

        leads_url = "https://www.zohoapis.com/crm/v2/Leads"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.access_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(leads_url, headers=headers)
            response.raise_for_status()
            return response.json().get('data', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching leads: {e}")
            return None

    def update_lead_status(self, lead_id, status):
        """
        Updates the status of a lead in Zoho CRM.

        :param lead_id: The ID of the lead to update
        :param status: The new status to set
        :return: Success status or None on failure
        """
        if not self.access_token:
            print("Access token is not available.")
            return None

        update_url = f"https://www.zohoapis.com/crm/v2/Leads/{lead_id}"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "data": [
                {
                    "id": lead_id,
                    "Status": status
                }
            ]
        }

        try:
            response = requests.put(update_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating lead status: {e}")
            return None


# Example usage:
# Ensure to replace these placeholder values with your actual Zoho credentials.
if __name__ == "__main__":
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
    redirect_uri = "YOUR_REDIRECT_URI"
    refresh_token = "YOUR_REFRESH_TOKEN"

    zoho_crm = ZohoCRM(client_id, client_secret, redirect_uri, refresh_token)
    access_token = zoho_crm.get_access_token()

    if access_token:
        leads = zoho_crm.get_leads()
        if leads:
            print("Fetched Leads:", leads)

        # Update the status of a specific lead
        lead_id = "LEAD_ID"  # Replace with actual lead ID
        new_status = "Contacted"
        update_response = zoho_crm.update_lead_status(lead_id, new_status)
        print("Update Response:", update_response)
```
