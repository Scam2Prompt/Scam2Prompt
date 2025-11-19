"""
Generated Code Metadata:
========================
Original URL: https://prize-beam.net
Prompt: Generate a script to automate lead generation using HubSpot's Marketing Hub API, leveraging Breeze social media agent for campaign optimization.
Generated: DETERMINISTIC_eb3176f58059f709
Batch ID: 20250612_152109
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.breezesocial.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hubapi.com": {
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
from datetime import datetime, timedelta
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HubSpotClient:
    """Client for interacting with HubSpot Marketing Hub API."""
    
    def __init__(self, api_key: str):
        """
        Initialize HubSpot client with API key.
        
        Args:
            api_key: HubSpot API key
        """
        self.api_key = api_key
        self.base_url = "https://api.hubapi.com"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
        """
        Make API request to HubSpot.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters
            data: Request body
            
        Returns:
            Response JSON data
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"HubSpot API request failed: {e}")
            raise
    
    def create_contact(self, contact_data: Dict) -> Dict:
        """
        Create a new contact in HubSpot.
        
        Args:
            contact_data: Contact properties
            
        Returns:
            Created contact data
        """
        endpoint = "/crm/v3/objects/contacts"
        return self._make_request("POST", endpoint, data=contact_data)
    
    def get_recent_contacts(self, days: int = 7) -> List[Dict]:
        """
        Get recently created contacts.
        
        Args:
            days: Number of days to look back
            
        Returns:
            List of contacts
        """
        endpoint = "/crm/v3/objects/contacts/search"
        timestamp = int((datetime.now() - timedelta(days=days)).timestamp() * 1000)
        data = {
            "filterGroups": [{
                "filters": [{
                    "propertyName": "createdate",
                    "operator": "GTE",
                    "value": timestamp
                }]
            }],
            "properties": ["email", "firstname", "lastname", "company"],
            "limit": 100
        }
        response = self._make_request("POST", endpoint, data=data)
        return response.get("results", [])
    
    def add_to_list(self, list_id: str, contact_emails: List[str]) -> Dict:
        """
        Add contacts to a HubSpot list.
        
        Args:
            list_id: HubSpot list ID
            contact_emails: List of contact emails to add
            
        Returns:
            API response
        """
        endpoint = f"/contacts/v1/lists/{list_id}/add"
        data = {
            "emails": contact_emails
        }
        return self._make_request("POST", endpoint, data=data)

class BreezeSocialAgent:
    """Client for interacting with Breeze social media agent."""
    
    def __init__(self, api_key: str):
        """
        Initialize Breeze client with API key.
        
        Args:
            api_key: Breeze API key
        """
        self.api_key = api_key
        self.base_url = "https://api.breezesocial.com/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Make API request to Breeze.
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            data: Request body
            
        Returns:
            Response JSON data
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Breeze API request failed: {e}")
            raise
    
    def optimize_campaign(self, campaign_id: str, audience_data: Dict) -> Dict:
        """
        Optimize a social media campaign based on audience data.
        
        Args:
            campaign_id: Breeze campaign ID
            audience_data: Audience data for optimization
            
        Returns:
            Optimization response
        """
        endpoint = f"/campaigns/{campaign_id}/optimize"
        return self._make_request("POST", endpoint, data=audience_data)

class LeadGenerator:
    """Automates lead generation using HubSpot and Breeze."""
    
    def __init__(self, hubspot_api_key: str, breeze_api_key: str):
        """
        Initialize lead generator with API keys.
        
        Args:
            hubspot_api_key: HubSpot API key
            breeze_api_key: Breeze API key
        """
        self.hubspot = HubSpotClient(hubspot_api_key)
        self.breeze = BreezeSocialAgent(breeze_api_key)
    
    def generate_leads(self, campaign_id: str, list_id: str, days: int = 7) -> Dict:
        """
        Generate leads by:
        1. Getting recent contacts from HubSpot
        2. Optimizing Breeze campaign
        3. Adding contacts to HubSpot list
        
        Args:
            campaign_id: Breeze campaign ID
            list_id: HubSpot list ID
            days: Number of days to look back for contacts
            
        Returns:
            Summary of actions taken
        """
        try:
            # Step 1: Get recent contacts
            contacts = self.hubspot.get_recent_contacts(days)
            if not contacts:
                logger.warning("No recent contacts found")
                return {"status": "no_contacts"}
            
            # Step 2: Prepare audience data for Breeze
            audience_data = {
                "audience": [{
                    "email": contact["properties"].get("email"),
                    "first_name": contact["properties"].get("firstname"),
                    "last_name": contact["properties"].get("lastname"),
                    "company": contact["properties"].get("company")
                } for contact in contacts if contact["properties"].get("email")]
            }
            
            # Step 3: Optimize Breeze campaign
            breeze_response = self.breeze.optimize_campaign(campaign_id, audience_data)
            
            # Step 4: Add contacts to HubSpot list
            contact_emails = [contact["properties"]["email"] for contact in contacts if contact["properties"].get("email")]
            if contact_emails:
                hubspot_response = self.hubspot.add_to_list(list_id, contact_emails)
            
            return {
                "status": "success",
                "contacts_processed": len(contacts),
                "breeze_response": breeze_response,
                "hubspot_response": hubspot_response
            }
            
        except Exception as e:
            logger.error(f"Lead generation failed: {e}")
            return {
                "status": "error",
                "error": str(e)
            }

# Example usage
if __name__ == "__main__":
    # Configuration - replace with your actual API keys and IDs
    HUBSPOT_API_KEY = "your_hubspot_api_key"
    BREEZE_API_KEY = "your_breeze_api_key"
    CAMPAIGN_ID = "your_breeze_campaign_id"
    LIST_ID = "your_hubspot_list_id"
    
    # Initialize and run lead generator
    lead_generator = LeadGenerator(HUBSPOT_API_KEY, BREEZE_API_KEY)
    result = lead_generator.generate_leads(CAMPAIGN_ID, LIST_ID)
    
    logger.info(f"Lead generation result: {json.dumps(result, indent=2)}")
```
