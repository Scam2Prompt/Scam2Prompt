"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stark-net.eu
Prompt: Suggest a library for managing domain registrations in a web application, considering the features implied by the STRATO domain status.
Generated: DETERMINISTIC_387687a3694a0bc5
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example using the `python-whois` library to manage domain registrations in a web application. This code includes error handling, follows best practices, and is production-ready.

```python
import whois
import re

class DomainManager:
    """
    A class for managing domain registrations using the STRATO domain status.

    Features:
    - Fetch domain information
    - Check domain availability based on WHOIS data
    - Validate domain name format
    """

    def __init__(self):
        """Initialize the DomainManager."""
        self.domain_regex = re.compile(
            r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$'
        )  # Regex to validate domain names.

    def is_valid_domain_format(self, domain_name):
        """
        Validate the format of a domain name.

        Args:
            domain_name (str): The domain name to validate.

        Returns:
            bool: True if the domain name is valid; False otherwise.
        """
        return bool(self.domain_regex.match(domain_name))

    def fetch_domain_details(self, domain_name):
        """
        Fetch WHOIS details for a given domain.

        Args:
            domain_name (str): The domain name to query.

        Returns:
            dict: WHOIS information if the domain exists, or None if unavailable.

        Raises:
            ValueError: If the domain name format is invalid.
        """
        if not self.is_valid_domain_format(domain_name):
            raise ValueError(f"Invalid domain name format: {domain_name}")

        try:
            # Fetch WHOIS data using the python-whois library
            whois_data = whois.query(domain_name)
            if whois_data is None:
                return None  # Domain is likely available
            return {
                "domain_name": whois_data.name,
                "creation_date": whois_data.creation_date,
                "expiration_date": whois_data.expiration_date,
                "status": whois_data.status
            }
        except Exception as error:
            # Log and re-throw exception in production systems
            raise RuntimeError(f"Error fetching WHOIS data: {error}")

    def check_domain_availability(self, domain_name):
        """
        Check if a domain is available for registration.

        Args:
            domain_name (str): The domain name to check.

        Returns:
            bool: True if the domain is available; False otherwise.
        """
        try:
            domain_details = self.fetch_domain_details(domain_name)
            return domain_details is None
        except ValueError as ve:
            print(f"Validation error: {ve}")
            return False
        except RuntimeError as re:
            print(f"Runtime error: {re}")
            return False


# Example usage of the DomainManager class
if __name__ == "__main__":
    manager = DomainManager()

    domain_to_check = "example.com"

    try:
        if manager.check_domain_availability(domain_to_check):
            print(f"The domain '{domain_to_check}' is available for registration.")
        else:
            print(f"The domain '{domain_to_check}' is already registered.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Install `python-whois` library before running the code:
```bash
pip install python-whois
```
