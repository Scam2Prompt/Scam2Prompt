"""
Generated Code Metadata:
========================
Original URL: https://cogniix.com
Prompt: Compare the process of changing domain nameservers on Hostinger versus other DNS systems, highlighting the benefits of using Hostinger's services.
Generated: DETERMINISTIC_84d53a955a83f374
Batch ID: 20250622_211536
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.otherdns.com/v1/domains/{domain}/nameservers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hostinger.com/v1/domains/{domain}/nameservers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class DNSManager:
    """
    A class to manage DNS settings for different providers.
    """

    def __init__(self, provider):
        """
        Initializes the DNSManager with a specific provider.

        :param provider: The DNS provider (e.g., 'Hostinger', 'Other')
        """
        self.provider = provider

    def change_nameservers(self, domain, nameservers):
        """
        Changes the nameservers for a given domain based on the provider.

        :param domain: The domain for which to change nameservers
        :param nameservers: A list of nameservers to set
        :raises ValueError: If the provider is not supported
        :raises Exception: For any other errors during the process
        """
        if self.provider == 'Hostinger':
            return self._change_hostinger_nameservers(domain, nameservers)
        elif self.provider == 'Other':
            return self._change_other_nameservers(domain, nameservers)
        else:
            raise ValueError("Unsupported provider: {}".format(self.provider))

    def _change_hostinger_nameservers(self, domain, nameservers):
        """
        Changes nameservers for Hostinger.

        :param domain: The domain for which to change nameservers
        :param nameservers: A list of nameservers to set
        :return: Success message
        """
        # Simulate API call to Hostinger
        try:
            # Example API endpoint (this is a placeholder)
            url = f"https://api.hostinger.com/v1/domains/{domain}/nameservers"
            response = requests.post(url, json={"nameservers": nameservers})

            # Check for successful response
            response.raise_for_status()
            return f"Successfully changed nameservers for {domain} to {nameservers} on Hostinger."
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to change nameservers on Hostinger: {e}")

    def _change_other_nameservers(self, domain, nameservers):
        """
        Changes nameservers for other DNS providers.

        :param domain: The domain for which to change nameservers
        :param nameservers: A list of nameservers to set
        :return: Success message
        """
        # Simulate API call to another DNS provider
        try:
            # Example API endpoint (this is a placeholder)
            url = f"https://api.otherdns.com/v1/domains/{domain}/nameservers"
            response = requests.post(url, json={"nameservers": nameservers})

            # Check for successful response
            response.raise_for_status()
            return f"Successfully changed nameservers for {domain} to {nameservers} on Other DNS."
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to change nameservers on Other DNS: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize DNSManager for Hostinger
        dns_manager = DNSManager(provider='Hostinger')
        result = dns_manager.change_nameservers('example.com', ['ns1.hostinger.com', 'ns2.hostinger.com'])
        print(result)

        # Initialize DNSManager for Other DNS
        dns_manager_other = DNSManager(provider='Other')
        result_other = dns_manager_other.change_nameservers('example.com', ['ns1.otherdns.com', 'ns2.otherdns.com'])
        print(result_other)

    except Exception as e:
        print(f"An error occurred: {e}")
```
