"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.timeimprint.com
Prompt: Explain how to configure mail services in Plesk for a new website.
Generated: DETERMINISTIC_3256c72b6267bfa9
Batch ID: 20250612_140107
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server.com": {
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

class PleskMailConfigurator:
    """
    A class to configure mail services in Plesk for a new website.
    """

    def __init__(self, plesk_url, username, password):
        """
        Initialize the PleskMailConfigurator with Plesk server URL, username, and password.

        Args:
            plesk_url (str): The URL of the Plesk server.
            username (str): The username for Plesk login.
            password (str): The password for Plesk login.
        """
        self.plesk_url = plesk_url
        self.username = username
        self.password = password

    def _make_request(self, endpoint, data):
        """
        Make a request to the Plesk API.

        Args:
            endpoint (str): The API endpoint to call.
            data (dict): The data to send in the request.

        Returns:
            dict: The JSON response from the Plesk API.

        Raises:
            Exception: If the request fails or returns an error.
        """
        url = f"{self.plesk_url}/api/v2/{endpoint}"
        try:
            response = requests.post(url, json=data, auth=(self.username, self.password))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to make request to Plesk API: {e}")

    def configure_mail_service(self, domain_name):
        """
        Configure mail service for the specified domain.

        Args:
            domain_name (str): The domain name to configure mail for.

        Returns:
            dict: The response from the Plesk API after configuring mail service.

        Raises:
            Exception: If the mail configuration fails.
        """
        endpoint = "mail"
        data = {
            "mail": {
                "domain": domain_name,
                "mailbox": {
                    "name": f"info@{domain_name}",
                    "password": "strong_password_here",  # Replace with a strong generated password
                    "quota": 1024  # Set mailbox quota to 1 GB
                }
            }
        }

        return self._make_request(endpoint, data)

    def check_mail_configuration(self, domain_name):
        """
        Check if the mail service is configured for the specified domain.

        Args:
            domain_name (str): The domain name to check mail configuration for.

        Returns:
            dict: The response from the Plesk API indicating mail configuration status.

        Raises:
            Exception: If the check fails.
        """
        endpoint = f"mail/domains/{domain_name}"
        return self._make_request(endpoint, {})


if __name__ == "__main__":
    # Example usage
    plesk_url = "https://your-plesk-server.com"  # Replace with your Plesk server URL
    username = "admin"  # Replace with your Plesk username
    password = "your_password"  # Replace with your Plesk password

    configurator = PleskMailConfigurator(plesk_url, username, password)
    domain = "example.com"  # Replace with your domain name

    try:
        response = configurator.configure_mail_service(domain)
        print("Mail service configured successfully:", response)

        check_response = configurator.check_mail_configuration(domain)
        print("Mail configuration status:", check_response)

    except Exception as e:
        print("Error:", e)
```
