"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-support.rf.gd
Prompt: Create a Python script to manage domain registration and hosting transfer for a service offering free domain names, as described on iFastNet's hosting page.
Generated: DETERMINISTIC_2f922923a4700c61
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import logging


class DomainManager:
    """
    A class to manage domain registration and hosting transfer.
    """

    def __init__(self):
        """
        Initialize the DomainManager with a list to store registered domains.
        """
        self.registered_domains = []

    def generate_free_domain(self):
        """
        Generates a free domain name using random alphanumeric characters.
        
        Returns:
            str: A randomly generated domain name with '.example.com' extension.
        """
        domain_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain_name = f"{domain_prefix}.example.com"
        logging.info(f"Generated domain: {domain_name}")
        return domain_name

    def register_domain(self, domain_name):
        """
        Registers a domain name if it is not already registered.
        
        Args:
            domain_name (str): The domain name to be registered.
        
        Returns:
            str: Success message or error message.
        """
        if domain_name in self.registered_domains:
            logging.error(f"Domain {domain_name} is already registered.")
            return f"Error: Domain '{domain_name}' is already registered."
        self.registered_domains.append(domain_name)
        logging.info(f"Domain {domain_name} has been successfully registered.")
        return f"Domain '{domain_name}' has been successfully registered."

    def transfer_hosting(self, domain_name, new_hosting_provider):
        """
        Transfers the hosting of a registered domain to a new hosting provider.
        
        Args:
            domain_name (str): The domain name to be transferred.
            new_hosting_provider (str): The new hosting provider.
        
        Returns:
            str: Success message or error message.
        """
        if domain_name not in self.registered_domains:
            logging.error(f"Cannot transfer hosting for {domain_name}: domain not registered.")
            return f"Error: Domain '{domain_name}' is not registered."
        logging.info(f"Hosting for domain {domain_name} has been transferred to {new_hosting_provider}.")
        return f"Hosting for domain '{domain_name}' has been transferred to '{new_hosting_provider}'."


def main():
    """
    Main function to demonstrate domain registration and hosting transfer.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    domain_manager = DomainManager()

    # Generate a free domain
    free_domain = domain_manager.generate_free_domain()

    # Register the generated domain
    registration_response = domain_manager.register_domain(free_domain)
    print(registration_response)

    # Attempt to register the same domain again
    duplicate_registration_response = domain_manager.register_domain(free_domain)
    print(duplicate_registration_response)

    # Transfer hosting for the registered domain
    hosting_transfer_response = domain_manager.transfer_hosting(free_domain, "NewHostingProvider")
    print(hosting_transfer_response)

    # Attempt to transfer hosting for a non-registered domain
    unregistered_transfer_response = domain_manager.transfer_hosting("nonexistent.example.com", "OtherHostingProvider")
    print(unregistered_transfer_response)


if __name__ == "__main__":
    main()
```
