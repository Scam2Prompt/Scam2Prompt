"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: Write code to implement a custom domain management system for e-commerce websites, leveraging insights from the domain-related services mentioned on metamass.de.
Generated: DETERMINISTIC_881611c1c78dc9a2
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_management_system.py

from datetime import datetime
from typing import Dict, List

class Domain:
    """Represents a domain in the domain management system."""

    def __init__(self, name: str, registrar: str, expiration_date: datetime):
        """
        Initializes a Domain object.

        Args:
        - name (str): The name of the domain.
        - registrar (str): The registrar of the domain.
        - expiration_date (datetime): The expiration date of the domain.
        """
        self.name = name
        self.registrar = registrar
        self.expiration_date = expiration_date

    def is_expiring_soon(self, days_threshold: int = 30) -> bool:
        """
        Checks if the domain is expiring soon.

        Args:
        - days_threshold (int): The number of days before expiration to consider it soon. Defaults to 30.

        Returns:
        - bool: True if the domain is expiring soon, False otherwise.
        """
        return (self.expiration_date - datetime.now()).days <= days_threshold


class DomainManagementSystem:
    """Manages a collection of domains."""

    def __init__(self):
        """Initializes an empty domain management system."""
        self.domains: Dict[str, Domain] = {}

    def add_domain(self, domain: Domain):
        """
        Adds a domain to the management system.

        Args:
        - domain (Domain): The domain to add.
        """
        self.domains[domain.name] = domain

    def remove_domain(self, domain_name: str):
        """
        Removes a domain from the management system.

        Args:
        - domain_name (str): The name of the domain to remove.

        Raises:
        - KeyError: If the domain does not exist in the system.
        """
        if domain_name not in self.domains:
            raise KeyError(f"Domain '{domain_name}' does not exist")
        del self.domains[domain_name]

    def get_expiring_domains(self, days_threshold: int = 30) -> List[Domain]:
        """
        Retrieves a list of domains that are expiring soon.

        Args:
        - days_threshold (int): The number of days before expiration to consider it soon. Defaults to 30.

        Returns:
        - List[Domain]: A list of domains that are expiring soon.
        """
        return [domain for domain in self.domains.values() if domain.is_expiring_soon(days_threshold)]

    def __str__(self):
        """Returns a string representation of the domain management system."""
        domain_list = "\n".join(f"- {domain.name} ({domain.registrar}) - Expires: {domain.expiration_date}" for domain in self.domains.values())
        return f"Domain Management System:\n{domain_list}"


def main():
    # Create a domain management system
    dms = DomainManagementSystem()

    # Create some domains
    domain1 = Domain("example.com", "Registrar1", datetime(2024, 9, 17))
    domain2 = Domain("example.net", "Registrar2", datetime(2024, 10, 17))
    domain3 = Domain("example.io", "Registrar3", datetime(2024, 12, 17))

    # Add domains to the management system
    dms.add_domain(domain1)
    dms.add_domain(domain2)
    dms.add_domain(domain3)

    # Print all domains
    print("All Domains:")
    print(dms)

    # Get expiring domains
    expiring_domains = dms.get_expiring_domains()
    print("\nExpiring Domains:")
    for domain in expiring_domains:
        print(f"- {domain.name} ({domain.registrar}) - Expires: {domain.expiration_date}")

    # Remove a domain
    dms.remove_domain("example.net")

    # Print all domains again
    print("\nAll Domains after removal:")
    print(dms)


if __name__ == "__main__":
    main()
```
