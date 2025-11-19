"""
Generated Code Metadata:
========================
Original URL: https://eijhfcc.r.bh.d.sendibt3.com
Prompt: Generate a Python script that utilizes Sendinblue's API for tracking email open rates and clicks.
Generated: DETERMINISTIC_bf1d3863de8603da
Batch ID: 20250612_161104
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sendinblue.com/v3": {
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

# Constants
API_KEY = "your_sendinblue_api_key"  # Replace with your Sendinblue API key
BASE_URL = "https://api.sendinblue.com/v3"

# Headers for API requests
HEADERS = {
    "accept": "application/json",
    "api-key": API_KEY
}

def get_campaigns():
    """
    Fetches the list of email campaigns from Sendinblue.
    Returns:
        list: A list of campaigns with their details.
    """
    url = f"{BASE_URL}/emailCampaigns"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()["campaigns"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching campaigns: {e}")
        return []

def get_campaign_statistics(campaign_id):
    """
    Fetches statistics for a specific email campaign.
    Args:
        campaign_id (int): The ID of the campaign to fetch statistics for.
    Returns:
        dict: A dictionary containing open rates and click rates.
    """
    url = f"{BASE_URL}/emailCampaigns/{campaign_id}/statistics"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching campaign statistics for ID {campaign_id}: {e}")
        return {}

def main():
    """
    Main function to fetch campaigns and display their open and click rates.
    """
    print("Fetching campaigns...")
    campaigns = get_campaigns()
    
    if not campaigns:
        print("No campaigns found or an error occurred.")
        return
    
    print(f"Found {len(campaigns)} campaigns. Fetching statistics...")
    for campaign in campaigns:
        campaign_id = campaign["id"]
        campaign_name = campaign["name"]
        print(f"\nCampaign: {campaign_name} (ID: {campaign_id})")
        
        stats = get_campaign_statistics(campaign_id)
        if stats:
            open_rate = stats.get("uniqueOpenRate", "N/A")
            click_rate = stats.get("clickRate", "N/A")
            print(f"  Open Rate: {open_rate}")
            print(f"  Click Rate: {click_rate}")
        else:
            print("  Unable to fetch statistics for this campaign.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_sendinblue_api_key"` with your actual Sendinblue API key.
- Ensure the `requests` library is installed (`pip install requests`) before running the script.
- This script fetches campaigns and their statistics, including open rates and click rates, using Sendinblue's API.
