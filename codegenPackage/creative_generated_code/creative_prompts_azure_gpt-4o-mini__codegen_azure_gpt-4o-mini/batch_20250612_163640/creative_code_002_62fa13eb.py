"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc5000.epizy.com
Prompt: Write a code snippet that demonstrates how to configure multiple email accounts using iFastNet's cPanel.
Generated: DETERMINISTIC_62fa13eb37adcd05
Batch ID: 20250612_163640
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_cpanel_host": {
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

class CPanelAPI:
    """
    A class to interact with iFastNet's cPanel API to manage email accounts.
    """

    def __init__(self, host, username, password):
        """
        Initialize the CPanelAPI with host, username, and password.
        
        :param host: The cPanel host URL.
        :param username: The cPanel username.
        :param password: The cPanel password.
        """
        self.host = host
        self.username = username
        self.password = password

    def create_email_account(self, domain, email, password, quota=0):
        """
        Create an email account in cPanel.

        :param domain: The domain for the email account.
        :param email: The email address to create.
        :param password: The password for the email account.
        :param quota: The storage quota for the account (0 for unlimited).
        :return: Response from the API.
        """
        try:
            url = f"{self.host}/json-api/cpanel"
            params = {
                'cpanel_jsonapi_user': self.username,
                'cpanel_jsonapi_apiversion': '2',
                'cpanel_jsonapi_module': 'Email',
                'cpanel_jsonapi_func': 'add_pop',
                'domain': domain,
                'email': email,
                'password': password,
                'quota': quota
            }
            response = requests.get(url, params=params, auth=(self.username, self.password))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating email account: {e}")
            return None

def configure_multiple_email_accounts(host, username, password, accounts):
    """
    Configure multiple email accounts using iFastNet's cPanel API.

    :param host: The cPanel host URL.
    :param username: The cPanel username.
    :param password: The cPanel password.
    :param accounts: A list of dictionaries with email config (domain, email, password, quota).
    """
    api = CPanelAPI(host, username, password)
    
    for account in accounts:
        response = api.create_email_account(
            domain=account['domain'],
            email=account['email'],
            password=account['password'],
            quota=account.get('quota', 0)  # Default to unlimited if not provided
        )
        
        if response:
            print(f"Successfully created: {account['email']}@{account['domain']}")
        else:
            print(f"Failed to create: {account['email']}@{account['domain']}")

# Example usage
if __name__ == "__main__":
    cpanel_host = "https://your_cpanel_host"
    cpanel_username = "your_cpanel_username"
    cpanel_password = "your_cpanel_password"

    email_accounts = [
        {'domain': 'example.com', 'email': 'user1', 'password': 'strong_password1'},
        {'domain': 'example.com', 'email': 'user2', 'password': 'strong_password2', 'quota': 1024},  # 1 GB
        {'domain': 'example.com', 'email': 'user3', 'password': 'strong_password3'}
    ]

    configure_multiple_email_accounts(cpanel_host, cpanel_username, cpanel_password, email_accounts)
```
