"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: "Write a code snippet for data entry and virtual assistant tasks using Zoho CRM and HubSpot APIs."
Generated: DETERMINISTIC_909ce32d92a741a4
Batch ID: 20250622_210443
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.zohoapis.com/crm/v2/Leads": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hubapi.com/crm/v3/objects/contacts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Constants for API endpoints and authentication
ZOHO_API_URL = "https://www.zohoapis.com/crm/v2/Leads"
ZOHO_ACCESS_TOKEN = "your_zoho_access_token_here"
HUBSPOT_API_URL = "https://api.hubapi.com/crm/v3/objects/contacts"
HUBSPOT_ACCESS_TOKEN = "your_hubspot_access_token_here"

def create_lead_in_zoho(data):
    """
    Create a lead in Zoho CRM.
    :param data: Dictionary containing lead information.
    :return: Response from Zoho API.
    """
    headers = {
        "Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(ZOHO_API_URL, headers=headers, json={"data": [data]})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating lead in Zoho: {e}")
        return None

def create_contact_in_hubspot(data):
    """
    Create a contact in HubSpot CRM.
    :param data: Dictionary containing contact information.
    :return: Response from HubSpot API.
    """
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(HUBSPOT_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating contact in HubSpot: {e}")
        return None

def main():
    """
    Main function to handle data entry and virtual assistant tasks.
    """
    # Example data for Zoho lead
    zoho_lead_data = {
        "Company": "Example Corp",
        "Last_Name": "Doe",
        "First_Name": "John",
        "Email": "john.doe@example.com",
        "Phone": "1234567890"
    }

    # Example data for HubSpot contact
    hubspot_contact_data = {
        "properties": {
            "email": "john.doe@example.com",
            "firstname": "John",
            "lastname": "Doe",
            "phone": "1234567890",
            "company": "Example Corp"
        }
    }

    # Create lead in Zoho CRM
    zoho_response = create_lead_in_zoho(zoho_lead_data)
    if zoho_response:
        print("Successfully created lead in Zoho CRM:", json.dumps(zoho_response, indent=4))

    # Create contact in HubSpot CRM
    hubspot_response = create_contact_in_hubspot(hubspot_contact_data)
    if hubspot_response:
        print("Successfully created contact in HubSpot CRM:", json.dumps(hubspot_response, indent=4))

if __name__ == "__main__":
    main()
```
