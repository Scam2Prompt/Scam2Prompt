"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Design a project management framework for a decentralized community like NEARFans, including roles and responsibilities for community members and stakeholders.
Generated: DETERMINISTIC_cc0dde42f5152eea
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management.py

class Role:
    """Class representing a role in the project management framework."""
    
    def __init__(self, name, responsibilities):
        """
        Initialize a new role with a name and a list of responsibilities.
        
        :param name: str - The name of the role.
        :param responsibilities: list - A list of responsibilities associated with the role.
        """
        self.name = name
        self.responsibilities = responsibilities

    def __str__(self):
        """Return a string representation of the role."""
        return f"Role: {self.name}, Responsibilities: {', '.join(self.responsibilities)}"


class CommunityMember:
    """Class representing a community member in the project management framework."""
    
    def __init__(self, username, role):
        """
        Initialize a new community member with a username and a role.
        
        :param username: str - The username of the community member.
        :param role: Role - The role assigned to the community member.
        """
        self.username = username
        self.role = role

    def __str__(self):
        """Return a string representation of the community member."""
        return f"Member: {self.username}, {self.role}"


class Project:
    """Class representing a project in the project management framework."""
    
    def __init__(self, title, description):
        """
        Initialize a new project with a title and description.
        
        :param title: str - The title of the project.
        :param description: str - A brief description of the project.
        """
        self.title = title
        self.description = description
        self.members = []

    def add_member(self, member):
        """
        Add a community member to the project.
        
        :param member: CommunityMember - The member to be added.
        :raises ValueError: If the member is already part of the project.
        """
        if member in self.members:
            raise ValueError(f"{member.username} is already a member of this project.")
        self.members.append(member)

    def remove_member(self, member):
        """
        Remove a community member from the project.
        
        :param member: CommunityMember - The member to be removed.
        :raises ValueError: If the member is not part of the project.
        """
        if member not in self.members:
            raise ValueError(f"{member.username} is not a member of this project.")
        self.members.remove(member)

    def list_members(self):
        """List all members of the project."""
        return [str(member) for member in self.members]

    def __str__(self):
        """Return a string representation of the project."""
        return f"Project: {self.title}, Description: {self.description}, Members: {len(self.members)}"


# Example usage
if __name__ == "__main__":
    # Define roles and responsibilities
    developer_role = Role("Developer", ["Write code", "Fix bugs", "Review pull requests"])
    manager_role = Role("Manager", ["Plan sprints", "Manage resources", "Communicate with stakeholders"])

    # Create community members
    alice = CommunityMember("Alice", developer_role)
    bob = CommunityMember("Bob", manager_role)

    # Create a project
    project = Project("Decentralized App", "A project to build a decentralized application on NEAR.")

    # Add members to the project
    try:
        project.add_member(alice)
        project.add_member(bob)
        print(project)
    except ValueError as e:
        print(e)

    # List project members
    print("Project Members:")
    for member in project.list_members():
        print(member)

    # Remove a member
    try:
        project.remove_member(alice)
        print("After removing Alice:")
        print(project)
    except ValueError as e:
        print(e)
```
