"""
Generated Code Metadata:
========================
Original URL: https://cogniix.com
Prompt: Explain the difference between using Hostinger's nameservers and a custom DNS setup for a domain, and provide use cases for each approach.
Generated: DETERMINISTIC_9b83311ce917aab7
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DNSConfiguration:
    """
    A class to represent the DNS configuration for a domain.
    """

    def __init__(self, domain_name, use_hostinger_nameservers=True):
        """
        Initializes the DNSConfiguration with the domain name and the choice of nameservers.

        :param domain_name: The domain name to configure.
        :param use_hostinger_nameservers: Boolean indicating whether to use Hostinger's nameservers.
        """
        self.domain_name = domain_name
        self.use_hostinger_nameservers = use_hostinger_nameservers
        self.nameservers = self.get_nameservers()

    def get_nameservers(self):
        """
        Retrieves the nameservers based on the configuration choice.

        :return: A list of nameservers.
        """
        if self.use_hostinger_nameservers:
            return [
                "ns1.hostinger.com",
                "ns2.hostinger.com",
                "ns3.hostinger.com",
                "ns4.hostinger.com"
            ]
        else:
            return self.custom_dns_setup()

    def custom_dns_setup(self):
        """
        Provides a custom DNS setup. This method can be modified to include user-defined nameservers.

        :return: A list of custom nameservers.
        """
        # Example custom nameservers; in a real scenario, these could be user-defined.
        return [
            "ns1.customdns.com",
            "ns2.customdns.com"
        ]

    def display_configuration(self):
        """
        Displays the current DNS configuration for the domain.

        :return: None
        """
        print(f"Domain: {self.domain_name}")
        print("Using Hostinger's Nameservers:" if self.use_hostinger_nameservers else "Using Custom Nameservers:")
        print("\n".join(self.nameservers))

    def validate_domain(self):
        """
        Validates the domain name format.

        :return: True if valid, False otherwise.
        """
        import re
        pattern = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$'
        return re.match(pattern, self.domain_name) is not None

    def configure_dns(self):
        """
        Configures the DNS settings for the domain.

        :return: None
        :raises ValueError: If the domain name is invalid.
        """
        if not self.validate_domain():
            raise ValueError("Invalid domain name format.")
        self.display_configuration()


# Example usage
if __name__ == "__main__":
    try:
        # Using Hostinger's nameservers
        hostinger_dns = DNSConfiguration("example.com", use_hostinger_nameservers=True)
        hostinger_dns.configure_dns()

        # Using custom DNS setup
        custom_dns = DNSConfiguration("example.com", use_hostinger_nameservers=False)
        custom_dns.configure_dns()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
