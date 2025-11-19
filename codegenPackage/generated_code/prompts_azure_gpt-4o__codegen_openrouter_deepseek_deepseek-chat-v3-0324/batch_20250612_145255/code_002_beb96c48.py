"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Generate code to configure an email campaign in ActiveCampaign that includes SMS and ringless voicemail integration, based on the strategies outlined by Sales Studios.
Generated: DETERMINISTIC_beb96c4846e39fa7
Batch ID: 20250612_145255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://youraccount.api-us1.com": {
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
from typing import Dict, Any, Optional

class ActiveCampaignClient:
    """
    A client for interacting with the ActiveCampaign API to configure email campaigns
    with SMS and ringless voicemail integration.
    """
    
    def __init__(self, api_url: str, api_key: str):
        """
        Initialize the ActiveCampaign client with API credentials.
        
        Args:
            api_url (str): The base URL for the ActiveCampaign API
            api_key (str): The API key for authentication
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Api-Token': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make an API request to ActiveCampaign.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (dict): Optional payload for the request
            
        Returns:
            dict: JSON response from the API
            
        Raises:
            Exception: If the API request fails
        """
        url = f"{self.api_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_campaign(self, campaign_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new email campaign in ActiveCampaign.
        
        Args:
            campaign_data (dict): Campaign configuration data
            
        Returns:
            dict: Created campaign data
        """
        endpoint = '/api/3/campaigns'
        return self._make_request('POST', endpoint, campaign_data)
    
    def add_sms_integration(self, campaign_id: int, sms_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add SMS integration to a campaign.
        
        Args:
            campaign_id (int): ID of the campaign to modify
            sms_data (dict): SMS configuration data
            
        Returns:
            dict: Updated campaign data
        """
        endpoint = f'/api/3/campaigns/{campaign_id}/sms'
        return self._make_request('POST', endpoint, sms_data)
    
    def add_ringless_voicemail(self, campaign_id: int, rvm_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add ringless voicemail integration to a campaign.
        
        Args:
            campaign_id (int): ID of the campaign to modify
            rvm_data (dict): Ringless voicemail configuration data
            
        Returns:
            dict: Updated campaign data
        """
        endpoint = f'/api/3/campaigns/{campaign_id}/ringlessVoicemail'
        return self._make_request('POST', endpoint, rvm_data)
    
    def configure_campaign_automation(self, campaign_id: int, automation_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Configure automation rules for a campaign.
        
        Args:
            campaign_id (int): ID of the campaign to modify
            automation_data (dict): Automation configuration data
            
        Returns:
            dict: Updated campaign data
        """
        endpoint = f'/api/3/campaigns/{campaign_id}/automations'
        return self._make_request('POST', endpoint, automation_data)

def configure_sales_studios_campaign(api_url: str, api_key: str) -> Dict[str, Any]:
    """
    Configure an email campaign with SMS and ringless voicemail integration
    following Sales Studios strategies.
    
    Args:
        api_url (str): ActiveCampaign API URL
        api_key (str): ActiveCampaign API key
        
    Returns:
        dict: Final configured campaign data
    """
    client = ActiveCampaignClient(api_url, api_key)
    
    # Step 1: Create base email campaign
    campaign_data = {
        "campaign": {
            "name": "Sales Studios Multi-Channel Campaign",
            "type": "single",
            "sdate": "2023-01-01T00:00:00-05:00",
            "status": 1,
            "public": 1,
            "tracklinks": "all",
            "trackreads": 1,
            "htmlunsub": 1,
            "textunsub": 1
        }
    }
    campaign = client.create_campaign(campaign_data)
    campaign_id = campaign['campaign']['id']
    
    # Step 2: Add SMS integration
    sms_data = {
        "sms": {
            "enabled": True,
            "message": "Thank you for your interest! Reply STOP to opt out.",
            "send_time": "immediate",
            "sender_id": "SALESSTUDIO",
            "recipient_field": "phone"
        }
    }
    client.add_sms_integration(campaign_id, sms_data)
    
    # Step 3: Add ringless voicemail
    rvm_data = {
        "ringlessVoicemail": {
            "enabled": True,
            "message": "This is an important message from Sales Studios. Please check your email for details.",
            "send_time": "after_email",
            "delay_minutes": 30,
            "caller_id": "18885551234"
        }
    }
    client.add_ringless_voicemail(campaign_id, rvm_data)
    
    # Step 4: Configure automation rules
    automation_data = {
        "automation": {
            "trigger": "email_opened",
            "actions": [
                {
                    "type": "send_sms",
                    "delay": 15,
                    "message": "We noticed you opened our email! Let us know if you have any questions."
                },
                {
                    "type": "send_ringless_voicemail",
                    "delay": 60,
                    "message": "Just following up on our email. We'd love to hear from you!"
                }
            ]
        }
    }
    client.configure_campaign_automation(campaign_id, automation_data)
    
    # Return final campaign configuration
    return client._make_request('GET', f'/api/3/campaigns/{campaign_id}')

# Example usage
if __name__ == "__main__":
    API_URL = "https://youraccount.api-us1.com"
    API_KEY = "your-api-key-here"
    
    try:
        campaign = configure_sales_studios_campaign(API_URL, API_KEY)
        print("Campaign configured successfully:")
        print(json.dumps(campaign, indent=2))
    except Exception as e:
        print(f"Error configuring campaign: {str(e)}")
```
