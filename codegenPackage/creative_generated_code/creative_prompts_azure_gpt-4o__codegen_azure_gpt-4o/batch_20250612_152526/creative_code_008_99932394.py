"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Generate code to integrate Plesk with a third-party email service for automated email account creation and management.
Generated: DETERMINISTIC_99932394803a79bd
Batch ID: 20250612_152526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.emailservice.com/v1/accounts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://plesk.example.com:8443/api/v2": {
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

# Configuration for Plesk API and Email Service
PLESK_API_URL = "https://plesk.example.com:8443/api/v2"
PLESK_API_KEY = "your_plesk_api_key_here"
EMAIL_SERVICE_API_URL = "https://api.emailservice.com/v1/accounts"
EMAIL_SERVICE_API_KEY = "your_email_service_api_key_here"

def create_plesk_email_account(domain, username, password):
    """
    Creates an email account in Plesk.
    
    Parameters:
        domain (str): The domain for the email account.
        username (str): The username for the email account.
        password (str): The password for the email account.

    Returns:
        dict: Response from the Plesk API.
    """
    url = f"{PLESK_API_URL}/domains/{domain}/mailAccounts"
    headers = {
        "Authorization": f"Bearer {PLESK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": username,
        "password": password
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating Plesk email account: {e}")
        return None

def create_third_party_email_account(email, password):
    """
    Creates an email account in the third-party email service.
    
    Parameters:
        email (str): The email address to be created.
        password (str): The password for the email account.

    Returns:
        dict: Response from the third-party email service API.
    """
    headers = {
        "Authorization": f"Bearer {EMAIL_SERVICE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "email": email,
        "password": password
    }
    
    try:
        response = requests.post(EMAIL_SERVICE_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating third-party email account: {e}")
        return None

def main():
    """
    Main function to integrate Plesk with the third-party email service
    for automated email account creation and management.
    """
    # Example input
    domain = "example.com"
    username = "newuser"
    password = "securepassword123"
    email = f"{username}@{domain}"
    
    # Create email account in Plesk
    plesk_response = create_plesk_email_account(domain, username, password)
    if plesk_response:
        print("Plesk email account created successfully:", plesk_response)
    else:
        print("Failed to create Plesk email account.")
        return
    
    # Create email account in third-party service
    third_party_response = create_third_party_email_account(email, password)
    if third_party_response:
        print("Third-party email account created successfully:", third_party_response)
    else:
        print("Failed to create third-party email account.")
        return

if __name__ == "__main__":
    main()
```
