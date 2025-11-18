"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scburnet.okta.acmecorp.name
Prompt: How can I troubleshoot issues with disabled cookies when implementing custom Okta sign-in workflows?
Generated: DETERMINISTIC_c538c734ef2b5900
Batch ID: 20250612_150615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-redirect.uri": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-org.okta.com": {
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
from requests.exceptions import RequestException

class OktaSignIn:
    """
    A class to handle custom Okta sign-in workflows and troubleshoot issues with disabled cookies.
    """

    def __init__(self, okta_domain, client_id, redirect_uri):
        """
        Initializes the OktaSignIn instance with the necessary Okta configuration.

        Args:
            okta_domain (str): The Okta domain (e.g., 'https://your-org.okta.com').
            client_id (str): The client ID for your Okta application.
            redirect_uri (str): The URI to redirect to after sign-in.
        """
        self.okta_domain = okta_domain
        self.client_id = client_id
        self.redirect_uri = redirect_uri

    def construct_login_url(self):
        """
        Constructs the login URL for Okta sign-in.

        Returns:
            str: The full login URL for Okta.
        """
        return f"{self.okta_domain}/oauth2/default/v1/authorize?client_id={self.client_id}&response_type=code&redirect_uri={self.redirect_uri}&scope=openid"

    def check_cookies_enabled(self):
        """
        Checks if cookies are enabled in the browser environment.

        Raises:
            EnvironmentError: If cookies are not enabled.
        """
        try:
            response = requests.get(self.redirect_uri, allow_redirects=False)
            if 'Set-Cookie' not in response.headers:
                raise EnvironmentError("Cookies are disabled in the browser environment.")

        except RequestException as e:
            raise RuntimeError(f"Error checking cookie status: {e}")

    def sign_in(self):
        """
        Initiates the sign-in process and performs cookie checks.

        Raises:
            RuntimeError: If there's an issue with the sign-in process.
        """
        try:
            # Check if cookies are enabled before proceeding
            self.check_cookies_enabled()
            login_url = self.construct_login_url()
            print(f"Navigate to the following URL to sign in: {login_url}")

        except EnvironmentError as e:
            print(f"Troubleshooting Error: {e}")
            print("Please enable cookies in your browser and try again.")
        except RuntimeError as e:
            print(f"Sign-in Error: {e}")

# Example usage
if __name__ == "__main__":
    okta_sign_in = OktaSignIn(
        okta_domain="https://your-org.okta.com",
        client_id="your-client-id",
        redirect_uri="https://your-redirect.uri"
    )
    okta_sign_in.sign_in()
```
