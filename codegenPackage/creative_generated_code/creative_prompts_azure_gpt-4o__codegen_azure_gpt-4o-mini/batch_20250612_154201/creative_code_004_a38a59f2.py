"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendainforma.zya.me
Prompt: Write a script to automate the setup of multiple email accounts on iFastNet hosting, using their cPanel interface.
Generated: DETERMINISTIC_a38a59f2def7c5d8
Batch ID: 20250612_154201
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-ifastnet-api-endpoint.com": {
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

# Define constants for the iFastNet API
IFASTNET_API_URL = 'https://your-ifastnet-api-endpoint.com'
IFASTNET_API_KEY = 'your_api_key_here'

def create_email_account(domain, email, password, quota):
    """
    Create an email account on iFastNet hosting.

    Args:
        domain (str): The domain name to create the email on.
        email (str): The email account name (local part).
        password (str): The password for the email account.
        quota (int): The quota in MB for the email account.

    Returns:
        str: The response from the iFastNet API indicating success or failure.
    """
    endpoint = f"{IFASTNET_API_URL}/cpanel/email/addpop"
    data = {
        'api_key': IFASTNET_API_KEY,
        'domain': domain,
        'email': email,
        'password': password,
        'quota': quota
    }
    
    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        result = response.json()
        if result.get('result') == 'success':
            return f"Email account {email}@{domain} created successfully."
        else:
            return f"Error creating email account: {result.get('message')}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def main():
    # List of email accounts to create
    email_accounts = [
        {'domain': 'example.com', 'email': 'user1', 'password': 'secure_password1', 'quota': 100},
        {'domain': 'example.com', 'email': 'user2', 'password': 'secure_password2', 'quota': 100},
        # Add more email accounts as needed
    ]
    
    for account in email_accounts:
        result = create_email_account(
            domain=account['domain'],
            email=account['email'],
            password=account['password'],
            quota=account['quota']
        )
        print(result)

if __name__ == "__main__":
    main()
```

**Note:** Ensure to replace `'your-ifastnet-api-endpoint.com'` and `'your_api_key_here'` with the actual iFastNet API endpoint and your API key.
