"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.pages.dev
Prompt: How can I implement a sub-domain acquisition process to prevent misuse in a web application?
Generated: DETERMINISTIC_08a79e589e15d0a4
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class SubdomainManager:
    """
    A class to manage subdomain acquisition and validation.
    """

    def __init__(self):
        # A set of reserved subdomains that cannot be used by users (e.g., admin, www, etc.)
        self.reserved_subdomains = {'admin', 'www', 'support', 'help'}
        # A set to store already acquired subdomains
        self.acquired_subdomains = set()

    def is_valid_subdomain(self, subdomain):
        """
        Validate the subdomain against rules to prevent misuse.

        :param subdomain: str, the subdomain to validate
        :return: bool, True if the subdomain is valid, False otherwise
        """
        # Rule 1: Subdomain must be alphanumeric and may include hyphens but no special characters
        if not re.match(r'^[a-zA-Z0-9-]+$', subdomain):
            return False
        # Rule 2: Subdomain cannot start or end with a hyphen
        if subdomain.startswith('-') or subdomain.endswith('-'):
            return False
        # Rule 3: Subdomain must be between 3 and 63 characters long
        if len(subdomain) < 3 or len(subdomain) > 63:
            return False
        return True

    def is_subdomain_available(self, subdomain):
        """
        Check if the subdomain is available for acquisition.

        :param subdomain: str, the subdomain to check
        :return: bool, True if available, False otherwise
        """
        # Check if the subdomain is reserved
        if subdomain.lower() in self.reserved_subdomains:
            return False
        # Check if the subdomain is already acquired
        if subdomain.lower() in self.acquired_subdomains:
            return False
        return True

    def acquire_subdomain(self, subdomain):
        """
        Attempt to acquire a subdomain.

        :param subdomain: str, the subdomain to acquire
        :return: str, message indicating success or failure
        """
        # Validate the subdomain
        if not self.is_valid_subdomain(subdomain):
            return "Invalid subdomain. Please follow the naming rules."
        # Check availability
        if not self.is_subdomain_available(subdomain):
            return "Subdomain is not available."
        # Acquire the subdomain
        self.acquired_subdomains.add(subdomain.lower())
        return f"Subdomain '{subdomain}' successfully acquired."

# Example usage
if __name__ == "__main__":
    manager = SubdomainManager()

    # Test with various subdomains
    print(manager.acquire_subdomain("valid-subdomain"))  # Should succeed
    print(manager.acquire_subdomain("admin"))            # Reserved subdomain
    print(manager.acquire_subdomain("invalid@name"))     # Invalid due to special character
    print(manager.acquire_subdomain("short"))            # Should succeed if available
    print(manager.acquire_subdomain("short"))            # Already acquired
```
