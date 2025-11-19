"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applovin.in
Prompt: Explain how to leverage AppLovin Exchange for programmatic advertising and increasing ad inventory.
Generated: DETERMINISTIC_22ae249bed103162
Batch ID: 20250612_164040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.applovin.com": {
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
# Import necessary libraries
import requests
import json

class AppLovinExchange:
    def __init__(self, api_key, base_url="https://api.applovin.com"):
        """
        Initialize AppLovinExchange with API key and base URL.

        :param api_key: The API key for accessing AppLovin Exchange
        :param base_url: The base URL for the AppLovin API
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_ad_inventory(self):
        """
        Retrieve ad inventory from AppLovin Exchange.

        :return: JSON response containing ad inventory data or error message
        """
        endpoint = f"{self.base_url}/v1/inventory"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def create_ad_campaign(self, campaign_data):
        """
        Create a new ad campaign in AppLovin Exchange.

        :param campaign_data: Dictionary containing campaign details
        :return: JSON response containing the created campaign data or error message
        """
        endpoint = f"{self.base_url}/v1/campaigns"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(endpoint, headers=headers, data=json.dumps(campaign_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def optimize_ad_performance(self, campaign_id):
        """
        Optimize the performance of an existing ad campaign.

        :param campaign_id: The ID of the campaign to optimize
        :return: JSON response containing optimization results or error message
        """
        endpoint = f"{self.base_url}/v1/campaigns/{campaign_id}/optimize"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual AppLovin API key
    api_key = "your_api_key"
    app_lovin_exchange = AppLovinExchange(api_key)
    
    # Fetch ad inventory
    inventory = app_lovin_exchange.get_ad_inventory()
    print("Ad Inventory:", inventory)
    
    # Create a new ad campaign (example data)
    campaign_data = {
        "name": "New Campaign",
        "budget": 1000,
        "targetAudience": "18-24",
        "adFormat": "video"
    }
    campaign_response = app_lovin_exchange.create_ad_campaign(campaign_data)
    print("Campaign Response:", campaign_response)
    
    # Optimize an existing ad campaign (replace with actual campaign ID)
    campaign_id = "123456"
    optimization_response = app_lovin_exchange.optimize_ad_performance(campaign_id)
    print("Optimization Response:", optimization_response)
```
