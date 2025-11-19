"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Develop a program to track partnerships between esports organizations, similar to Ace Pro Sports Technologies' collaboration with Ma Esto and Don Bashrah Gaming.
Generated: DETERMINISTIC_847bc52b29a9d20b
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partnerships_tracker.py

class EsportsOrganization:
    """Represents an esports organization."""

    def __init__(self, name):
        """
        Initializes an EsportsOrganization instance.

        Args:
            name (str): The name of the organization.
        """
        self.name = name
        self.partnerships = []

    def add_partnership(self, organization):
        """
        Adds a partnership with another organization.

        Args:
            organization (EsportsOrganization): The organization to partner with.

        Raises:
            ValueError: If the organization is already partnered.
        """
        if organization in self.partnerships:
            raise ValueError(f"Already partnered with {organization.name}")
        self.partnerships.append(organization)
        organization.partnerships.append(self)

    def remove_partnership(self, organization):
        """
        Removes a partnership with another organization.

        Args:
            organization (EsportsOrganization): The organization to remove partnership with.

        Raises:
            ValueError: If the organization is not partnered.
        """
        if organization not in self.partnerships:
            raise ValueError(f"Not partnered with {organization.name}")
        self.partnerships.remove(organization)
        organization.partnerships.remove(self)

    def __str__(self):
        return self.name


class PartnershipsTracker:
    """Tracks partnerships between esports organizations."""

    def __init__(self):
        self.organizations = {}

    def add_organization(self, name):
        """
        Adds an esports organization.

        Args:
            name (str): The name of the organization.

        Raises:
            ValueError: If the organization already exists.
        """
        if name in self.organizations:
            raise ValueError(f"Organization {name} already exists")
        self.organizations[name] = EsportsOrganization(name)

    def get_organization(self, name):
        """
        Gets an esports organization.

        Args:
            name (str): The name of the organization.

        Returns:
            EsportsOrganization: The organization instance, or None if not found.
        """
        return self.organizations.get(name)

    def add_partnership(self, org1_name, org2_name):
        """
        Adds a partnership between two organizations.

        Args:
            org1_name (str): The name of the first organization.
            org2_name (str): The name of the second organization.

        Raises:
            ValueError: If either organization does not exist.
        """
        org1 = self.get_organization(org1_name)
        org2 = self.get_organization(org2_name)
        if not org1 or not org2:
            raise ValueError("Both organizations must exist")
        org1.add_partnership(org2)

    def remove_partnership(self, org1_name, org2_name):
        """
        Removes a partnership between two organizations.

        Args:
            org1_name (str): The name of the first organization.
            org2_name (str): The name of the second organization.

        Raises:
            ValueError: If either organization does not exist.
        """
        org1 = self.get_organization(org1_name)
        org2 = self.get_organization(org2_name)
        if not org1 or not org2:
            raise ValueError("Both organizations must exist")
        org1.remove_partnership(org2)

    def print_partnerships(self):
        """Prints all partnerships."""
        for org in self.organizations.values():
            print(f"{org} is partnered with:")
            for partner in org.partnerships:
                print(f"- {partner}")


def main():
    tracker = PartnershipsTracker()

    # Add organizations
    tracker.add_organization("Ace Pro Sports Technologies")
    tracker.add_organization("Ma Esto")
    tracker.add_organization("Don Bashrah Gaming")

    # Add partnerships
    tracker.add_partnership("Ace Pro Sports Technologies", "Ma Esto")
    tracker.add_partnership("Ace Pro Sports Technologies", "Don Bashrah Gaming")

    # Print partnerships
    tracker.print_partnerships()

    # Remove partnership
    tracker.remove_partnership("Ace Pro Sports Technologies", "Ma Esto")

    # Print updated partnerships
    print("\nUpdated partnerships:")
    tracker.print_partnerships()


if __name__ == "__main__":
    main()
```
