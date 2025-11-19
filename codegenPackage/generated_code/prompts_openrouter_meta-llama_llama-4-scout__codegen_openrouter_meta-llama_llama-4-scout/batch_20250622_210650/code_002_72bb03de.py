"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: "Design a community program based on Premchand's vision of building with purpose and leading with heart."
Generated: DETERMINISTIC_72bb03de8c7fb282
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_program.py

class CommunityMember:
    """Represents a member of the community."""

    def __init__(self, name, skills):
        """
        Initializes a CommunityMember.

        Args:
            name (str): The member's name.
            skills (list): A list of the member's skills.
        """
        self.name = name
        self.skills = skills

    def __str__(self):
        return f"{self.name} - {', '.join(self.skills)}"


class CommunityProject:
    """Represents a project undertaken by the community."""

    def __init__(self, name, purpose, members):
        """
        Initializes a CommunityProject.

        Args:
            name (str): The project's name.
            purpose (str): The project's purpose.
            members (list): A list of CommunityMember objects.
        """
        self.name = name
        self.purpose = purpose
        self.members = members

    def __str__(self):
        members_str = '\n'.join(['  ' + str(member) for member in self.members])
        return f"{self.name} - {self.purpose}\nMembers:\n{members_str}"


class Community:
    """Represents the community."""

    def __init__(self):
        """Initializes an empty community."""
        self.members = []
        self.projects = []

    def add_member(self, member):
        """
        Adds a member to the community.

        Args:
            member (CommunityMember): The member to add.

        Raises:
            ValueError: If the member is already in the community.
        """
        if member in self.members:
            raise ValueError("Member already exists in the community.")
        self.members.append(member)

    def add_project(self, project):
        """
        Adds a project to the community.

        Args:
            project (CommunityProject): The project to add.

        Raises:
            ValueError: If the project is already in the community.
        """
        if project in self.projects:
            raise ValueError("Project already exists in the community.")
        self.projects.append(project)

    def __str__(self):
        members_str = '\n'.join([str(member) for member in self.members])
        projects_str = '\n\n'.join([str(project) for project in self.projects])
        return f"Community Members:\n{members_str}\n\nProjects:\n{projects_str}"


def main():
    try:
        community = Community()

        # Create community members
        member1 = CommunityMember("Rahul", ["Python", "JavaScript"])
        member2 = CommunityMember("Priya", ["Design", "Marketing"])
        member3 = CommunityMember("Karan", ["Python", "Data Analysis"])

        # Add members to the community
        community.add_member(member1)
        community.add_member(member2)
        community.add_member(member3)

        # Create community projects
        project1 = CommunityProject("Education Initiative", "Provide educational resources to underprivileged children.", [member1, member2])
        project2 = CommunityProject("Environmental Conservation", "Organize events to promote environmental conservation.", [member3, member1])

        # Add projects to the community
        community.add_project(project1)
        community.add_project(project2)

        # Print community information
        print(community)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
