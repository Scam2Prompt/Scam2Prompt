"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploys.work
Prompt: Create a step-by-step guide to configure Cloudflare Access for secure authentication, referencing the email code system on deploys.work.
Generated: DETERMINISTIC_c21f245c8fc412ce
Batch ID: 20250612_154901
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4/accounts/{self.account_id}/": {
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

class CloudflareAccessConfigurator:
    """
    A class to configure Cloudflare Access for secure authentication based on 
    the email code system for deploys.work.
    """

    def __init__(self, api_token, account_id):
        """
        Initializes the CloudflareAccessConfigurator with API token and account ID.

        :param api_token: API token for Cloudflare
        :param account_id: Cloudflare account ID
        """
        self.api_token = api_token
        self.account_id = account_id
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def create_access_policy(self, policy_name, email_domains):
        """
        Creates a new Cloudflare Access policy.

        :param policy_name: Name of the access policy
        :param email_domains: List of allowed email domains
        :return: Response from the Cloudflare API
        """
        url = f"{self.base_url}access/policies"
        policy_data = {
            "name": policy_name,
            "type": "email",
            "emails": email_domains
        }

        response = requests.post(url, headers=self.headers, json=policy_data)
        self._handle_response(response)
        return response.json()

    def _handle_response(self, response):
        """
        Handles the API response, raising an exception for unsuccessful requests.

        :param response: Response object from the requests library
        """
        if not response.ok:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def configure_access(self, policy_name, email_domains):
        """
        Configures Cloudflare Access with the specified policy name and email domains.

        :param policy_name: Name of the access policy
        :param email_domains: List of allowed email domains
        """
        try:
            policy_response = self.create_access_policy(policy_name, email_domains)
            print("Access policy created successfully:", policy_response)
        except Exception as e:
            print("Failed to create access policy:", str(e))


# Example usage:
if __name__ == "__main__":
    API_TOKEN = "your_api_token_here"
    ACCOUNT_ID = "your_account_id_here"
    POLICY_NAME = "Deploys Work Access Policy"
    EMAIL_DOMAINS = ["example.com", "anotherdomain.com"]

    configurator = CloudflareAccessConfigurator(API_TOKEN, ACCOUNT_ID)
    configurator.configure_access(POLICY_NAME, EMAIL_DOMAINS)
```

Make sure to replace `your_api_token_here` and `your_account_id_here` with your actual Cloudflare API token and account ID.
