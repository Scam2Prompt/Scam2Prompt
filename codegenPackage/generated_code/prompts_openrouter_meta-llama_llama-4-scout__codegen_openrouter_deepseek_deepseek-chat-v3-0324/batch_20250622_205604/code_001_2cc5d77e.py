"""
Generated Code Metadata:
========================
Original URL: https://cloudsolution.co.id
Prompt: "How can I customize Zoho's marketing automation platform to improve lead conversion rates, and what are the benefits of using Cloud Solution's consulting services?"
Generated: DETERMINISTIC_2cc5d77ebb880248
Batch ID: 20250622_205604
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudsolutions.com/v1": {
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
  },
  "https://marketingautomation.zoho.com/api/v1": {
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
# This script demonstrates how to interact with Zoho's Marketing Automation API
# to customize lead conversion workflows and track performance metrics.

import requests
import json
from datetime import datetime
from typing import Dict, List, Optional

class ZohoMarketingAutomation:
    """
    A class to interact with Zoho's Marketing Automation API for lead conversion optimization.
    """
    
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        """
        Initialize the Zoho Marketing Automation client.
        
        Args:
            client_id: Zoho client ID
            client_secret: Zoho client secret
            refresh_token: Zoho refresh token
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = self._get_access_token()
        self.base_url = "https://marketingautomation.zoho.com/api/v1"
        
    def _get_access_token(self) -> str:
        """
        Get access token using refresh token.
        
        Returns:
            Access token string
            
        Raises:
            Exception: If token retrieval fails
        """
        url = "https://accounts.zoho.com/oauth/v2/token"
        params = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }
        
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            return response.json()["access_token"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get access token: {str(e)}")
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Make authenticated API request to Zoho Marketing Automation.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request payload
            
        Returns:
            API response as dictionary
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.access_token}",
            "Content-Type": "application/json"
        }
        
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_custom_workflow(self, name: str, triggers: List[str], actions: List[Dict]) -> Dict:
        """
        Create a custom workflow for lead conversion.
        
        Args:
            name: Workflow name
            triggers: List of trigger conditions
            actions: List of actions to perform
            
        Returns:
            Workflow creation response
        """
        endpoint = "workflows"
        data = {
            "name": name,
            "triggers": triggers,
            "actions": actions,
            "is_active": True
        }
        return self._make_request("POST", endpoint, data)
    
    def update_lead_scoring(self, criteria: Dict, score_values: Dict) -> Dict:
        """
        Update lead scoring rules.
        
        Args:
            criteria: Scoring criteria
            score_values: Score values for each criterion
            
        Returns:
            Lead scoring update response
        """
        endpoint = "leadscoring/rules"
        data = {
            "criteria": criteria,
            "score_values": score_values,
            "updated_time": datetime.now().isoformat()
        }
        return self._make_request("PUT", endpoint, data)
    
    def get_conversion_metrics(self, start_date: str, end_date: str) -> Dict:
        """
        Get lead conversion metrics for a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Conversion metrics data
        """
        endpoint = f"reports/conversions?start_date={start_date}&end_date={end_date}"
        return self._make_request("GET", endpoint)
    
    def integrate_with_crm(self, crm_name: str, mapping_config: Dict) -> Dict:
        """
        Integrate with external CRM system.
        
        Args:
            crm_name: Name of CRM system
            mapping_config: Field mapping configuration
            
        Returns:
            Integration response
        """
        endpoint = f"integrations/{crm_name.lower()}"
        return self._make_request("POST", endpoint, mapping_config)

class CloudSolutionsConsulting:
    """
    A class to demonstrate integration with Cloud Solution's consulting services.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize Cloud Solutions Consulting client.
        
        Args:
            api_key: API key for Cloud Solutions Consulting
        """
        self.api_key = api_key
        self.base_url = "https://api.cloudsolutions.com/v1"
    
    def get_consulting_benefits(self) -> Dict:
        """
        Get benefits of using Cloud Solution's consulting services.
        
        Returns:
            Dictionary of consulting benefits
            
        Raises:
            Exception: If API request fails
        """
        endpoint = "consulting/benefits"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get consulting benefits: {str(e)}")
    
    def request_consultation(self, contact_info: Dict, requirements: str) -> Dict:
        """
        Request a consultation with Cloud Solutions.
        
        Args:
            contact_info: Dictionary with contact details
            requirements: Description of consulting requirements
            
        Returns:
            Consultation request response
        """
        endpoint = "consulting/request"
        data = {
            "contact_info": contact_info,
            "requirements": requirements,
            "request_date": datetime.now().isoformat()
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to request consultation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize Zoho Marketing Automation client
    zoho_client = ZohoMarketingAutomation(
        client_id="your_client_id",
        client_secret="your_client_secret",
        refresh_token="your_refresh_token"
    )
    
    # Create a custom workflow
    workflow = zoho_client.create_custom_workflow(
        name="High Intent Lead Follow-up",
        triggers=["form_submission", "page_visit"],
        actions=[
            {"action": "send_email", "template_id": "welcome_series_1"},
            {"action": "assign_to_sales", "team": "inside_sales"}
        ]
    )
    
    # Update lead scoring
    scoring = zoho_client.update_lead_scoring(
        criteria={"pages_visited": 3, "time_on_site": 300},
        score_values={"pages_visited": 10, "time_on_site": 15}
    )
    
    # Get conversion metrics
    metrics = zoho_client.get_conversion_metrics(
        start_date="2023-01-01",
        end_date="2023-01-31"
    )
    
    # Initialize Cloud Solutions Consulting client
    consulting_client = CloudSolutionsConsulting(api_key="your_api_key")
    
    # Get consulting benefits
    benefits = consulting_client.get_consulting_benefits()
    
    # Request consultation
    consultation = consulting_client.request_consultation(
        contact_info={
            "name": "John Doe",
            "email": "john@example.com",
            "company": "Acme Inc"
        },
        requirements="Zoho Marketing Automation optimization for lead conversion"
    )
```
