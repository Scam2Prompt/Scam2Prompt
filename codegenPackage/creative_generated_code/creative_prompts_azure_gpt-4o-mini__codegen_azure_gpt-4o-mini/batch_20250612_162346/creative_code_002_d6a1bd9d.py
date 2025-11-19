"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azumi.vercel.app
Prompt: Can you provide details on the Azumi team and their roles in the project?
Generated: DETERMINISTIC_d6a1bd9d3f9e4de6
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TeamMember:
    """
    Class representing a team member in the Azumi project.
    """

    def __init__(self, name: str, role: str):
        """
        Initializes a new team member with a name and role.

        Args:
            name (str): The name of the team member.
            role (str): The role of the team member in the project.
        """
        if not name or not role:
            raise ValueError("Name and role cannot be empty.")
        self.name = name
        self.role = role

    def __repr__(self):
        return f"{self.name} - {self.role}"


class AzumiTeam:
    """
    Class representing the Azumi team.
    """

    def __init__(self):
        """
        Initializes a new Azumi team with an empty list of members.
        """
        self.members = []

    def add_member(self, name: str, role: str):
        """
        Adds a new member to the Azumi team.

        Args:
            name (str): The name of the team member.
            role (str): The role of the team member.

        Raises:
            ValueError: If the name or role is empty.
        """
        member = TeamMember(name, role)
        self.members.append(member)

    def get_team_details(self):
        """
        Returns the details of the team members.

        Returns:
            list: A list of strings representing team members and their roles.
        """
        return [str(member) for member in self.members]


if __name__ == "__main__":
    # Create an instance of the Azumi team
    azumi_team = AzumiTeam()

    # Add team members
    try:
        azumi_team.add_member("Alice", "Project Manager")
        azumi_team.add_member("Bob", "Lead Developer")
        azumi_team.add_member("Charlie", "QA Engineer")
    except ValueError as e:
        print(f"Error adding team member: {e}")

    # Retrieve and print team details
    team_details = azumi_team.get_team_details()
    for detail in team_details:
        print(detail)
```
