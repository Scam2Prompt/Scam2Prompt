"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradise-app.com
Prompt: Generate code to create a secure domain registration system for a travel or relaxation app, inspired by the domain promotion on paradise-app.com.
Generated: DETERMINISTIC_1027f30a0eebb314
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import uuid
from hashlib import sha256


class DomainRegistrationSystem:
    """
    A secure domain registration system for a travel or relaxation app.
    """

    def __init__(self):
        # Initialize an in-memory store to keep registered domains
        self.registered_domains = {}

    def validate_domain_name(self, domain_name):
        """
        Validate the format of a domain name.

        :param domain_name: str - The domain name to validate
        :return: bool - True if valid, False otherwise
        """
        # Regex to match valid domain names (e.g., paradise-app.com)
        domain_pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        if not re.match(domain_pattern, domain_name):
            return False
        return True

    def check_domain_availability(self, domain_name):
        """
        Check if the domain name is available for registration.

        :param domain_name: str - The domain name to check
        :return: bool - True if available, False otherwise
        """
        return domain_name not in self.registered_domains

    def register_domain(self, domain_name, user_id):
        """
        Register a domain name for a given user.

        :param domain_name: str - The domain name to register
        :param user_id: str - The unique identifier for the user
        :return: str - Success message or failure reason
        """
        # Validate the domain name format
        if not self.validate_domain_name(domain_name):
            return "Error: Invalid domain name format."

        # Check domain availability
        if not self.check_domain_availability(domain_name):
            return "Error: Domain name is already registered."

        # Generate a unique domain ID using UUID and hash for security
        domain_id = sha256(uuid.uuid4().hex.encode()).hexdigest()

        # Store the domain in the registered_domains dictionary
        self.registered_domains[domain_name] = {
            "domain_id": domain_id,
            "user_id": user_id,
        }

        return f"Success: Domain '{domain_name}' has been registered with ID '{domain_id}'."

    def list_registered_domains(self):
        """
        List all registered domains.

        :return: dict - Dictionary of registered domains
        """
        return self.registered_domains


# Example Usage
if __name__ == "__main__":
    # Create an instance of the domain registration system
    system = DomainRegistrationSystem()

    # Mock user ID (e.g., fetched from a secure authentication system)
    user_id = "user_12345"

    # Register domains
    print(system.register_domain("paradise-app.com", user_id))
    print(system.register_domain("relax-zone.org", user_id))

    # Attempt to register an invalid domain
    print(system.register_domain("invalid_domain_name", user_id))

    # Attempt to register a duplicate domain
    print(system.register_domain("paradise-app.com", user_id))

    # List all registered domains
    print("Registered Domains:")
    print(system.list_registered_domains())
```
