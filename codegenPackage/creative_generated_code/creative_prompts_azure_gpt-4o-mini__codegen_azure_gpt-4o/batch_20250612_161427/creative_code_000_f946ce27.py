"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: How can I implement HubSpot CRM for lead generation using the strategies discussed by Trekk, the tech-driven creative services agency?
Generated: DETERMINISTIC_f946ce27408f94ad
Batch ID: 20250612_161427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubapi.com": {
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
"""
Script to integrate with HubSpot CRM for lead generation.
This script uses HubSpot's API to create and manage leads based on the strategies discussed.
Ensure you have access to HubSpot API and an API key for authentication.
"""

import requests
import json

# HubSpot API Key (replace with your actual key)
HUBSPOT_API_KEY = 'your_hubspot_api_key'

# HubSpot API Base URL
HUBSPOT_API_BASE_URL = 'https://api.hubapi.com'

# Headers for API requests
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {HUBSPOT_API_KEY}'
}

def create_lead(first_name, last_name, email, company):
    """
    Create a new lead in HubSpot CRM.
    
    Args:
        first_name (str): First name of the lead.
        last_name (str): Last name of the lead.
        email (str): Email address of the lead.
        company (str): Company name of the lead.
    
    Returns:
        dict: The response data from the HubSpot API.
    """
    url = f"{HUBSPOT_API_BASE_URL}/crm/v3/objects/contacts"
    
    # Payload with lead data
    payload = {
        "properties": {
            "firstname": first_name,
            "lastname": last_name,
            "email": email,
            "company": company
        }
    }
    
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad HTTP response codes
        return response.json()  # Return the response data as JSON
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while creating lead: {e}")
        return None

def fetch_leads():
    """
    Fetch all leads from HubSpot CRM.

    Returns:
        list: A list of leads retrieved from the HubSpot API.
    """
    url = f"{HUBSPOT_API_BASE_URL}/crm/v3/objects/contacts"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get('results', [])  # Extract and return the 'results' data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching leads: {e}")
        return []

def delete_lead(contact_id):
    """
    Delete a lead by their contact ID in HubSpot CRM.

    Args:
        contact_id (str): The unique ID of the contact to delete.

    Returns:
        bool: True if the lead was deleted successfully, False otherwise.
    """
    url = f"{HUBSPOT_API_BASE_URL}/crm/v3/objects/contacts/{contact_id}"
    
    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return True  # If successful, return True
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while deleting lead: {e}")
        return False

if __name__ == "__main__":
    # Example usage of the script
    
    # Create a new lead
    new_lead = create_lead(
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        company="Example Company"
    )
    if new_lead:
        print("Lead created successfully:", new_lead)
    
    # Fetch all leads
    leads = fetch_leads()
    print("Retrieved leads:", leads)
    
    # Delete a lead (if you have a valid contact_id)
    if leads:
        contact_id_to_delete = leads[0]['id']  # Example: Delete the first lead
        if delete_lead(contact_id_to_delete):
            print(f"Lead with ID {contact_id_to_delete} deleted successfully.")
```
