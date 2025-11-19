"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binairop.com
Prompt: How can I implement a shared IP configuration for multiple domains in my web application?
Generated: DETERMINISTIC_9dfb901005e90d5f
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for managing shared IP configurations for multiple domains using a dictionary. This example assumes you're working with a web application backend.

```python
import json

class SharedIPConfiguration:
    """
    A class to manage shared IP configuration for multiple domains.
    """

    def __init__(self):
        """
        Initializes the SharedIPConfiguration class with an empty configuration.
        """
        self.config = {}  # Dictionary to store domain-to-IP mappings

    def add_domain(self, domain, ip_address):
        """
        Adds or updates the IP address for a given domain.

        :param domain: The domain name as a string (e.g., "example.com")
        :param ip_address: The shared IP address as a string (e.g., "192.168.1.1")
        :raises ValueError: If the domain or IP address is invalid
        """
        if not self._validate_domain(domain):
            raise ValueError(f"Invalid domain format: {domain}")
        if not self._validate_ip(ip_address):
            raise ValueError(f"Invalid IP address format: {ip_address}")
        self.config[domain] = ip_address

    def remove_domain(self, domain):
        """
        Removes the IP configuration for a given domain.

        :param domain: The domain name as a string
        :raises KeyError: If the domain does not exist in the configuration
        """
        if domain not in self.config:
            raise KeyError(f"Domain not found: {domain}")
        del self.config[domain]

    def get_ip(self, domain):
        """
        Retrieves the IP address for a given domain.

        :param domain: The domain name as a string
        :return: The IP address as a string
        :raises KeyError: If the domain does not exist in the configuration
        """
        if domain not in self.config:
            raise KeyError(f"Domain not found: {domain}")
        return self.config[domain]

    def list_domains(self):
        """
        Lists all domains with their associated IP addresses.

        :return: A dictionary of domain-to-IP mappings
        """
        return self.config

    def save_to_file(self, file_path):
        """
        Saves the current configuration to a JSON file.

        :param file_path: The file path as a string
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.config, file)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads the configuration from a JSON file.

        :param file_path: The file path as a string
        :raises IOError: If there is an issue reading the file
        """
        try:
            with open(file_path, 'r') as file:
                self.config = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to read from file: {e}")

    @staticmethod
    def _validate_domain(domain):
        """
        Validates the format of a domain name.

        :param domain: The domain name as a string
        :return: True if valid, False otherwise
        """
        # Basic validation: Ensure the domain contains at least one dot (e.g., "example.com")
        return isinstance(domain, str) and "." in domain

    @staticmethod
    def _validate_ip(ip_address):
        """
        Validates the format of an IP address.

        :param ip_address: The IP address as a string
        :return: True if valid, False otherwise
        """
        # Basic validation: Ensure the IP address follows the format "x.x.x.x"
        parts = ip_address.split(".")
        if len(parts) != 4:
            return False
        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False


# Example usage:
if __name__ == "__main__":
    config = SharedIPConfiguration()

    # Adding domains
    config.add_domain("example.com", "192.168.1.1")
    config.add_domain("anotherdomain.com", "192.168.1.2")

    # Listing all domains and their IPs
    print("Current Configuration:", config.list_domains())

    # Removing a domain
    config.remove_domain("anotherdomain.com")
    print("After Removal:", config.list_domains())

    # Saving configuration to a file
    config.save_to_file("config.json")

    # Loading configuration from a file
    loaded_config = SharedIPConfiguration()
    loaded_config.load_from_file("config.json")
    print("Loaded Configuration:", loaded_config.list_domains())
```

This code provides a reusable and production-ready solution for managing shared IP configurations for multiple domains. It includes proper error handling and validation, adheres to best practices, and is well-documented with comments.
