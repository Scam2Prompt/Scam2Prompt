"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Describe the process of creating a subscription in Plesk for Media Temple hosting, including any API calls that might be needed.
Generated: DETERMINISTIC_9482159c15bf0b03
Batch ID: 20250612_155200
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/api/v2": {
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

# Define constants for Plesk API
PLESK_API_URL = "https://your-plesk-server:8443/api/v2"
PLESK_API_KEY = "your-plesk-api-key"

# Helper function to create a subscription
def create_subscription(domain_name, username, password, plan_id):
    """
    Creates a subscription in Plesk using the API.
    
    Args:
        domain_name (str): Domain name for the subscription.
        username (str): Username for the subscription.
        password (str): Password for the subscription.
        plan_id (int): ID of the service plan to associate with the subscription.
    
    Returns:
        dict: Response from the Plesk API.
    """
    # Endpoint for creating a subscription
    endpoint = f"{PLESK_API_URL}/subscriptions"
    
    # Data payload for the subscription
    payload = {
        "name": domain_name,
        "username": username,
        "password": password,
        "plan": {"id": plan_id},
        "hosting": {
            "webspace": {
                "type": "virtual",
                "properties": {
                    "ftp_login": username,
                    "ftp_password": password
                }
            }
        }
    }
    
    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {PLESK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send POST request to Plesk API
        response = requests.post(endpoint, json=payload, headers=headers)
        
        # Raise an exception if the request failed
        response.raise_for_status()
        
        # Return JSON response on success
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and return error details
        print(f"Error creating subscription: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Input values (replace with actual data)
    DOMAIN_NAME = "example.com"
    USERNAME = "exampleuser"
    PASSWORD = "examplepassword"
    PLAN_ID = 12345  # Replace with actual plan ID from Plesk
    
    # Create a subscription
    result = create_subscription(DOMAIN_NAME, USERNAME, PASSWORD, PLAN_ID)
    
    # Print response
    print("Response from Plesk:")
    print(result)
```

Make sure to replace the placeholders (`your-plesk-server`, `your-plesk-api-key`, etc.) with actual values from your Plesk setup, and test the code in your environment before using it in production.
