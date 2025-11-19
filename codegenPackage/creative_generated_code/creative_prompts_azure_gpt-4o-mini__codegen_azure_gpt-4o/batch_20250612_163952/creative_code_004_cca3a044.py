"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsplug.epizy.com
Prompt: Create a guide for enabling SSL on a website hosted with iFastNet, focusing on the free and simple SSL feature.
Generated: DETERMINISTIC_cca3a044a66593be
Batch ID: 20250612_163952
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/v1": {
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
Guide to Enable Free SSL on Website Hosted with iFastNet

This script demonstrates the steps to enable SSL for a website hosted with iFastNet using the
free and simple SSL feature. This code assumes the user has access to their iFastNet hosting 
control panel and their domain is already pointed to iFastNet's servers.

IMPORTANT: This code is meant to serve as a guide to automate simple API interactions (if available) 
or provide scripted instructions. Not all steps may be automatable due to hosting provider restrictions.
"""

import requests

class IFastNetSSLActivator:
    """
    A class to represent the SSL activation process for iFastNet-hosted websites.
    """

    def __init__(self, api_url, api_key):
        """
        Initialize the SSLActivator with API URL and API key.

        :param api_url: The URL for the hosting provider's API
        :param api_key: The API key for authenticating requests
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_domains(self):
        """
        Fetch the list of domains associated with the hosting account.

        :return: List of domains
        """
        try:
            response = requests.get(
                f"{self.api_url}/domains",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response.json()["domains"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching domains: {e}")
            return []

    def enable_ssl(self, domain):
        """
        Enable free SSL for the specified domain.

        :param domain: The domain to enable SSL for
        :return: Boolean indicating success or failure
        """
        try:
            response = requests.post(
                f"{self.api_url}/enable-ssl",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"domain": domain}
            )
            response.raise_for_status()
            if response.json().get("status") == "success":
                print(f"SSL successfully enabled for {domain}")
                return True
            else:
                print(f"Failed to enable SSL for {domain}: {response.json().get('message')}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error enabling SSL for {domain}: {e}")
            return False

def main():
    """
    Main function to guide the user through the SSL enabling process.
    """
    # Replace these variables with your iFastNet API details
    API_URL = "https://api.ifastnet.com/v1"  # Example API URL (adjust to real URL)
    API_KEY = "your_api_key_here"

    ssl_activator = IFastNetSSLActivator(API_URL, API_KEY)

    # Step 1: Get the list of domains
    domains = ssl_activator.get_domains()
    if not domains:
        print("No domains found or failed to fetch domains.")
        return

    print("Domains found:")
    for idx, domain in enumerate(domains, start=1):
        print(f"{idx}. {domain}")

    # Step 2: Ask the user to select a domain
    try:
        choice = int(input("Enter the number of the domain you want to enable SSL for: "))
        if choice < 1 or choice > len(domains):
            print("Invalid choice. Exiting.")
            return
        selected_domain = domains[choice - 1]
    except ValueError:
        print("Invalid input. Exiting.")
        return

    # Step 3: Enable SSL for the selected domain
    ssl_activator.enable_ssl(selected_domain)

if __name__ == "__main__":
    main()
```
