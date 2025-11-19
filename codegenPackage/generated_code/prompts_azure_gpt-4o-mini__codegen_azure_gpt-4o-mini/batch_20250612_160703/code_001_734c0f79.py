"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: How can I implement a multi-disciplinary team model in a child neurology clinic, similar to the ICON Foundation's services for ADHD and motor delays?
Generated: DETERMINISTIC_734c0f79cc5c98b0
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TeamMember:
    """
    Represents a member of the multi-disciplinary team.
    Each team member has a name, role, and specialty.
    """
    def __init__(self, name: str, role: str, specialty: str):
        self.name = name
        self.role = role
        self.specialty = specialty

    def __str__(self):
        return f"{self.name} - {self.role} ({self.specialty})"


class MultiDisciplinaryTeam:
    """
    Represents a multi-disciplinary team in a child neurology clinic.
    The team can include various specialists to address different aspects of child neurology.
    """
    def __init__(self):
        self.members = []

    def add_member(self, member: TeamMember):
        """
        Adds a new member to the team.
        
        :param member: An instance of TeamMember to be added to the team.
        """
        if not isinstance(member, TeamMember):
            raise ValueError("member must be an instance of TeamMember")
        self.members.append(member)

    def remove_member(self, name: str):
        """
        Removes a member from the team by name.
        
        :param name: The name of the member to be removed.
        :raises ValueError: If the member is not found in the team.
        """
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                return
        raise ValueError(f"Member with name {name} not found in the team.")

    def list_members(self):
        """
        Lists all members of the team.
        
        :return: A list of strings representing each team member.
        """
        return [str(member) for member in self.members]


# Example usage
if __name__ == "__main__":
    try:
        # Create a multi-disciplinary team
        team = MultiDisciplinaryTeam()

        # Add team members
        team.add_member(TeamMember("Dr. Smith", "Neurologist", "Child Neurology"))
        team.add_member(TeamMember("Ms. Johnson", "Psychologist", "ADHD Specialist"))
        team.add_member(TeamMember("Mr. Brown", "Occupational Therapist", "Motor Skills"))

        # List team members
        print("Team Members:")
        for member in team.list_members():
            print(member)

        # Remove a team member
        team.remove_member("Ms. Johnson")
        print("\nAfter removing Ms. Johnson:")
        for member in team.list_members():
            print(member)

    except ValueError as e:
        print(f"Error: {e}")
```
