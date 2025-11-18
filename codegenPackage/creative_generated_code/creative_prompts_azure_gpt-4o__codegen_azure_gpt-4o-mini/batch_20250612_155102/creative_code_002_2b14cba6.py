"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: Provide an example of using the Porkbun API to retrieve DNS records for a domain.
Generated: DETERMINISTIC_2b14cba6fdfbe621
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3": {
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

class PorkbunAPI:
    """A class to interact with the Porkbun API."""

    BASE_URL = "https://porkbun.com/api/json/v3"

    def __init__(self, api_key, secret_key):
        """
        Initializes the PorkbunAPI instance.

        :param api_key: Your Porkbun API key.
        :param secret_key: Your Porkbun API secret key.
        """
        self.api_key = api_key
        self.secret_key = secret_key

    def get_dns_records(self, domain):
        """
        Retrieve DNS records for a specified domain.

        :param domain: The domain for which to retrieve DNS records.
        :return: A list of DNS records or an error message.
        """
        try:
            response = requests.post(
                f"{self.BASE_URL}/dns/retrieve",
                json={"apikey": self.api_key, "secret": self.secret_key, "domain": domain}
            )
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            data = response.json()
            if data['success']:
                return data['data']  # Return DNS records if successful
            else:
                return f"Error retrieving DNS records: {data['message']}"

        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key and secret
    API_KEY = "your_api_key"
    SECRET_KEY = "your_secret_key"
    DOMAIN = "example.com"

    porkbun = PorkbunAPI(API_KEY, SECRET_KEY)
    dns_records = porkbun.get_dns_records(DOMAIN)

    if isinstance(dns_records, list):
        print("DNS Records:")
        for record in dns_records:
            print(record)
    else:
        print(dns_records)  # Print error message
```
