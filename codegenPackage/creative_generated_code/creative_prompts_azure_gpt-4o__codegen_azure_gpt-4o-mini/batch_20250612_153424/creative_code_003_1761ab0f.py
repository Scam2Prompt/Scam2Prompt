"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vilavi.online
Prompt: Provide an example of using Plesk's GUI to configure email services for a hosting business.
Generated: DETERMINISTIC_1761ab0f53f89096
Batch ID: 20250612_153424
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://{self.host}:8443/api/v2/email/accounts/{email}@{domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{self.host}:8443/api/v2/email/accounts": {
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

class PleskEmailConfigurator:
    def __init__(self, host, username, password):
        """
        Initializes the PleskEmailConfigurator class.

        :param host: The Plesk server host.
        :param username: The Plesk admin username.
        :param password: The Plesk admin password.
        """
        self.host = host
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def create_email_account(self, domain, email, password):
        """
        Creates an email account for a specified domain.

        :param domain: The domain to create the email account for.
        :param email: The email address to create (e.g., user@domain).
        :param password: The password for the email account.
        :raises Exception: If the email account creation fails.
        """
        url = f'https://{self.host}:8443/api/v2/email/accounts'
        data = {
            "email-account": {
                "name": email,
                "password": password,
                "domain": domain,
                "mailbox": {
                    "status": "active"
                }
            }
        }

        try:
            response = self.session.post(url, json=data, verify=False)
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Email account {email} created successfully.")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log general errors
            raise

    def delete_email_account(self, domain, email):
        """
        Deletes an email account for a specified domain.

        :param domain: The domain to delete the email account from.
        :param email: The email address to delete (e.g., user@domain).
        :raises Exception: If the email account deletion fails.
        """
        url = f'https://{self.host}:8443/api/v2/email/accounts/{email}@{domain}'

        try:
            response = self.session.delete(url, verify=False)
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Email account {email} deleted successfully.")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log general errors
            raise

# Example usage
if __name__ == "__main__":
    # Replace these with your Plesk server details
    PLESK_HOST = 'your-plesk-host.com'
    PLESK_USERNAME = 'admin'
    PLESK_PASSWORD = 'your-password'

    email_configurator = PleskEmailConfigurator(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)

    # Creating an email account
    email_configurator.create_email_account('example.com', 'user@example.com', 'securepassword123')

    # Deleting an email account
    email_configurator.delete_email_account('example.com', 'user@example.com')
```
