"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Write code to implement a searchable directory of PSHP members, allowing users to filter by organization or role, as mentioned in the "PSHP Members Profile" section.
Generated: DETERMINISTIC_b23326644c0d361b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pshp_members_directory.py

class PSHPMember:
    """Represents a PSHP member with their profile information."""

    def __init__(self, name, organization, role):
        """
        Initializes a PSHPMember object.

        Args:
            name (str): The member's name.
            organization (str): The member's organization.
            role (str): The member's role.
        """
        self.name = name
        self.organization = organization
        self.role = role

    def __repr__(self):
        return f"PSHPMember(name='{self.name}', organization='{self.organization}', role='{self.role}')"


class PSHPMembersDirectory:
    """A searchable directory of PSHP members."""

    def __init__(self):
        """Initializes an empty directory."""
        self.members = []

    def add_member(self, member):
        """
        Adds a PSHP member to the directory.

        Args:
            member (PSHPMember): The member to add.

        Raises:
            TypeError: If the member is not a PSHPMember object.
        """
        if not isinstance(member, PSHPMember):
            raise TypeError("Invalid member type")
        self.members.append(member)

    def search_by_organization(self, organization):
        """
        Searches for members by organization.

        Args:
            organization (str): The organization to search for.

        Returns:
            list[PSHPMember]: A list of members matching the organization.
        """
        return [member for member in self.members if member.organization.lower() == organization.lower()]

    def search_by_role(self, role):
        """
        Searches for members by role.

        Args:
            role (str): The role to search for.

        Returns:
            list[PSHPMember]: A list of members matching the role.
        """
        return [member for member in self.members if member.role.lower() == role.lower()]

    def search(self, organization=None, role=None):
        """
        Searches for members by organization and/or role.

        Args:
            organization (str, optional): The organization to search for. Defaults to None.
            role (str, optional): The role to search for. Defaults to None.

        Returns:
            list[PSHPMember]: A list of members matching the search criteria.
        """
        results = self.members
        if organization:
            results = [member for member in results if member.organization.lower() == organization.lower()]
        if role:
            results = [member for member in results if member.role.lower() == role.lower()]
        return results


def main():
    directory = PSHPMembersDirectory()

    # Add some sample members
    directory.add_member(PSHPMember("John Doe", "Organization A", "Role 1"))
    directory.add_member(PSHPMember("Jane Smith", "Organization B", "Role 2"))
    directory.add_member(PSHPMember("Bob Johnson", "Organization A", "Role 2"))

    # Search by organization
    print("Search by organization:")
    organization = "Organization A"
    results = directory.search_by_organization(organization)
    for member in results:
        print(member)

    # Search by role
    print("\nSearch by role:")
    role = "Role 2"
    results = directory.search_by_role(role)
    for member in results:
        print(member)

    # Search by organization and role
    print("\nSearch by organization and role:")
    organization = "Organization A"
    role = "Role 2"
    results = directory.search(organization, role)
    for member in results:
        print(member)


if __name__ == "__main__":
    main()
```
