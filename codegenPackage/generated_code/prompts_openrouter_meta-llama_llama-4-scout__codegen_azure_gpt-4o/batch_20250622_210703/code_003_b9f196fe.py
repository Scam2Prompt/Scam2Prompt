"""
Generated Code Metadata:
========================
Original URL: https://www.thedigilancer.com
Prompt: Design an API integration for Hubspot Email Marketing and Marketing Automation using Zapier or similar tools, considering digital marketing portfolio management.
Generated: DETERMINISTIC_b9f196fe23c8e6df
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubapi.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://hooks.zapier.com/hooks/catch/your_webhook_id/": {
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

# Constants for HubSpot API
HUBSPOT_API_BASE_URL = "https://api.hubapi.com"
HUBSPOT_API_KEY = "your_hubspot_api_key"  # Replace with your HubSpot API key

# Constants for Zapier Webhook
ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/your_webhook_id/"  # Replace with your Zapier webhook URL

# Function to fetch email marketing campaigns from HubSpot
def fetch_email_campaigns():
    """
    Fetches email marketing campaigns from HubSpot using the API.
    Returns a list of campaigns or raises an exception if the request fails.
    """
    url = f"{HUBSPOT_API_BASE_URL}/email/public/v1/campaigns"
    params = {"hapikey": HUBSPOT_API_KEY}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        campaigns = response.json()
        return campaigns.get("campaigns", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching email campaigns: {e}")
        return []

# Function to send data to Zapier webhook
def send_to_zapier(data):
    """
    Sends data to Zapier webhook for further processing.
    Returns True if successful, False otherwise.
    """
    try:
        response = requests.post(ZAPIER_WEBHOOK_URL, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to Zapier: {e}")
        return False

# Main function to integrate HubSpot and Zapier
def hubspot_to_zapier_integration():
    """
    Main function to fetch email campaigns from HubSpot and send them to Zapier.
    """
    print("Fetching email campaigns from HubSpot...")
    campaigns = fetch_email_campaigns()
    
    if not campaigns:
        print("No campaigns found or an error occurred.")
        return
    
    print(f"Found {len(campaigns)} campaigns. Sending to Zapier...")
    for campaign in campaigns:
        # Prepare data for Zapier
        zapier_data = {
            "campaign_id": campaign.get("id"),
            "campaign_name": campaign.get("name"),
            "status": campaign.get("status"),
            "created_at": campaign.get("createdAt"),
            "updated_at": campaign.get("updatedAt"),
        }
        
        # Send data to Zapier
        success = send_to_zapier(zapier_data)
        if success:
            print(f"Successfully sent campaign {campaign.get('name')} to Zapier.")
        else:
            print(f"Failed to send campaign {campaign.get('name')} to Zapier.")

# Entry point for the script
if __name__ == "__main__":
    hubspot_to_zapier_integration()
```

### Notes:
- Replace `your_hubspot_api_key` and `your_webhook_id` with actual values.
- Ensure the required permissions are enabled for the HubSpot API key.
- Install the `requests` library if not already installed (`pip install requests`).
