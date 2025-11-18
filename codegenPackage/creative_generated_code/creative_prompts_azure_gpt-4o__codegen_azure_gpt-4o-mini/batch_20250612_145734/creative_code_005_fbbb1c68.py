"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-steth.com
Prompt: Suggest APIs for enabling enterprise data protection when using Microsoft 365 Copilot in a hybrid work environment.
Generated: DETERMINISTIC_fbbb1c68b9e15ec9
Batch ID: 20250612_145734
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://graph.microsoft.com/v1.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.microsoft.com/.default": {
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

class Microsoft365CopilotAPI:
    """
    A class to interact with Microsoft 365 Copilot APIs to enable enterprise data protection.
    """

    def __init__(self, tenant_id, client_id, client_secret):
        """
        Initializes the Microsoft365CopilotAPI with tenant and authentication details.
        
        Args:
            tenant_id (str): The Azure tenant ID.
            client_id (str): The Azure client ID.
            client_secret (str): The Azure client secret.
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://graph.microsoft.com/v1.0"
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """
        Obtains an access token using client credentials.
        
        Returns:
            str: Access token for Microsoft Graph API.
        """
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'scope': 'https://graph.microsoft.com/.default'
        }
        
        try:
            response = requests.post(url, headers=headers, data=body)
            response.raise_for_status()  # Raise an error for bad responses
            token_info = response.json()
            return token_info['access_token']
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining access token: {e}")
            return None

    def get_data_protection_settings(self):
        """
        Retrieves enterprise data protection settings for the tenant.
        
        Returns:
            dict: Data protection settings or error message.
        """
        url = f"{self.base_url}/identityProtection/conditionalAccessPolicies"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving data protection settings: {e}")
            return {"error": str(e)}

    def update_data_protection_policy(self, policy_id, updated_policy):
        """
        Updates a specified data protection policy.
        
        Args:
            policy_id (str): The ID of the policy to update.
            updated_policy (dict): The updated policy details.
        
        Returns:
            dict: Updated policy details or error message.
        """
        url = f"{self.base_url}/identityProtection/conditionalAccessPolicies/{policy_id}"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.put(url, headers=headers, data=json.dumps(updated_policy))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating data protection policy: {e}")
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Replace with your Azure tenant ID, client ID, and client secret
    TENANT_ID = "your_tenant_id"
    CLIENT_ID = "your_client_id"
    CLIENT_SECRET = "your_client_secret"
    
    # Initialize API class
    copilot_api = Microsoft365CopilotAPI(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
    
    # Get data protection settings
    settings = copilot_api.get_data_protection_settings()
    print("Data Protection Settings:", settings)
    
    # Example of updating a policy (replace with actual policy ID and details)
    policy_id = "example_policy_id"
    updated_policy = {
        "displayName": "Updated Policy",
        "conditions": {
            "users": {
                "include": ["user@example.com"]
            },
            "applications": {
                "include": ["app_id"]
            }
        },
        "grantControls": {
            "operator": "OR",
            "controls": ["mfa"]
        }
    }
    update_response = copilot_api.update_data_protection_policy(policy_id, updated_policy)
    print("Update Response:", update_response)
```
