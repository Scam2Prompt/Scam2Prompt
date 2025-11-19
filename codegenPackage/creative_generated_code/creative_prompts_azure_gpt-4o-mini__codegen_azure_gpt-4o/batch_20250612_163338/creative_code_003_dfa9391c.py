"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Provide an example of configuring email accounts on iFastNet Web Hosting using modern cPanel.
Generated: DETERMINISTIC_dfa9391c28041d72
Batch ID: 20250612_163338
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://<your-cpanel-domain>:2083/json-api/cpanel": {
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
"""
This Python script automates the process of configuring email accounts in cPanel
for iFastNet Web Hosting. It uses the cPanel API for accessing and creating email accounts.
Ensure you have API credentials and access to the cPanel API.

Requirements:
- Python 3.x
- requests library (install with `pip install requests`)

Note: Replace placeholders with your actual API credentials and details.
"""

import requests

# cPanel API credentials and endpoint
CPANEL_API_URL = "https://<your-cpanel-domain>:2083/json-api/cpanel"
CPANEL_USERNAME = "<your-cpanel-username>"
CPANEL_PASSWORD = "<your-cpanel-password>"

# Email account details
DOMAIN = "<your-domain.com>"  # Replace with your hosted domain
EMAIL_USER = "newemailuser"   # Email username to create
EMAIL_PASSWORD = "securepassword123!"  # Secure password for the email account
EMAIL_QUOTA = 1024  # Quota in MB, set to 0 for unlimited

def create_email_account(api_url, username, password, domain, email_user, email_password, email_quota):
    """
    Creates an email account in cPanel using the cPanel API.

    :param api_url: The cPanel API endpoint URL.
    :param username: cPanel username for authentication.
    :param password: cPanel password for authentication.
    :param domain: Domain name where the email account will be created.
    :param email_user: Username for the new email account.
    :param email_password: Password for the new email account.
    :param email_quota: Quota for the email account in MB.
    """
    # API payload for creating the email account
    payload = {
        "cpanel_jsonapi_user": username,
        "cpanel_jsonapi_apiversion": "2",
        "cpanel_jsonapi_module": "Email",
        "cpanel_jsonapi_func": "addpop",
        "domain": domain,
        "email": email_user,
        "password": email_password,
        "quota": email_quota,
    }

    try:
        # Send the request using HTTP Basic Authentication
        response = requests.post(api_url, auth=(username, password), data=payload)
        response.raise_for_status()  # Raise HTTPError for bad HTTP response codes

        # Parse the JSON response
        result = response.json()
        
        # Check the response from the API
        if result.get("cpanelresult", {}).get("error"):
            print("Error creating email account:", result["cpanelresult"]["error"])
        else:
            print("Email account created successfully!")
    except requests.exceptions.RequestException as e:
        # Handle connection or request errors
        print("Failed to connect to cPanel API:", str(e))
    except Exception as e:
        # General error handling
        print("An unexpected error occurred:", str(e))

# Run the function to create the email account
create_email_account(
    CPANEL_API_URL,
    CPANEL_USERNAME,
    CPANEL_PASSWORD,
    DOMAIN,
    EMAIL_USER,
    EMAIL_PASSWORD,
    EMAIL_QUOTA
)
```
