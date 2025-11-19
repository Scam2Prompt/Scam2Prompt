"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: How can I use Cloudflare's features to enhance the security of my web application against DDoS attacks?
Generated: DETERMINISTIC_5577b98644e9626b
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script demonstrating how to use Cloudflare's API to configure rate-limiting rules to protect your web application against DDoS attacks. This assumes you have access to Cloudflare's API credentials.

```python
import requests
import json

# Cloudflare API base URL
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"

# Cloudflare API token (replace with your actual token)
API_TOKEN = "your_cloudflare_api_token"

# Your Zone ID (replace with your actual Zone ID)
ZONE_ID = "your_zone_id"

# Headers for authorization
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_rate_limit_rule(zone_id, headers):
    """
    Creates a rate-limiting rule in Cloudflare to mitigate potential DDoS attacks.
    
    :param zone_id: Cloudflare Zone ID.
    :param headers: Authorization headers for Cloudflare API.
    """
    # Define rate-limiting rule payload
    rule_payload = {
        "threshold": 10,  # Maximum number of requests allowed per period
        "period": 60,     # Time period in seconds
        "description": "Mitigate DDoS attack by limiting excessive requests",
        "action": {
            "mode": "challenge",  # Forces CAPTCHA challenge for excessive requests
            "timeout": 60         # CAPTCHA timeout duration
        },
        "match": {
            "request": {
                "methods": ["GET", "POST"],  # Apply to GET and POST requests
                "url": "example.com/*"       # Match all paths of your domain
            }
        }
    }

    # API endpoint to create rate-limiting rules
    url = f"{CLOUDFLARE_API_URL}/zones/{zone_id}/rate_limits"

    try:
        # Send request to create rate-limiting rule
        response = requests.post(url, headers=headers, data=json.dumps(rule_payload))
        
        # Parse and handle response
        if response.status_code == 200:
            print("Rate-limiting rule successfully created.")
            print(response.json())
        else:
            print(f"Failed to create rate-limiting rule: {response.status_code}")
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating the rate-limiting rule: {str(e)}")

if __name__ == "__main__":
    # Execute rate-limiting rule creation
    create_rate_limit_rule(ZONE_ID, HEADERS)
```

### Notes:
1. Replace `your_cloudflare_api_token` and `your_zone_id` placeholders with actual values from your Cloudflare account.
2. Install the `requests` library if not already installed: `pip install requests`.
3. Ensure that your API token has sufficient permissions to manage rate-limiting rules.
