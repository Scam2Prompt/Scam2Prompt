"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write Python code to simulate the structure of the Programa Saúde da Família in SUS, including the assignment of healthcare teams to regions with approximately 4,500 residents. Include roles such as general practitioners, nurses, auxiliary nurses, and community health agents.
Generated: DETERMINISTIC_79ca8f57cd60fa46
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class HealthcareTeam:
    """Represents a healthcare team assigned to a specific region."""
    
    def __init__(self, team_id: int, region: str):
        self.team_id = team_id
        self.region = region
        self.members = {
            "general_practitioner": None,
            "nurse": None,
            "auxiliary_nurse": None,
            "community_health_agent": None
        }

    def assign_member(self, role: str, name: str):
        """Assign a member to the healthcare team."""
        if role in self.members:
            self.members[role] = name
        else:
            raise ValueError(f"Role '{role}' is not valid for this healthcare team.")

    def __str__(self):
        return f"Team ID: {self.team_id}, Region: {self.region}, Members: {self.members}"


class HealthSystem:
    """Simulates the Programa Saúde da Família in SUS."""
    
    def __init__(self):
        self.teams: List[HealthcareTeam] = []
        self.residents_per_team = 4500

    def create_teams(self, num_teams: int, regions: List[str]):
        """Create healthcare teams for the specified regions."""
        if num_teams > len(regions):
            raise ValueError("Number of teams exceeds available regions.")
        
        for i in range(num_teams):
            region = regions[i]
            team = HealthcareTeam(team_id=i + 1, region=region)
            self.teams.append(team)

    def assign_members(self, team_id: int, members: Dict[str, str]):
        """Assign members to a specific healthcare team."""
        if team_id < 1 or team_id > len(self.teams):
            raise IndexError("Team ID is out of range.")
        
        team = self.teams[team_id - 1]
        for role, name in members.items():
            try:
                team.assign_member(role, name)
            except ValueError as e:
                print(f"Error assigning member: {e}")

    def display_teams(self):
        """Display all healthcare teams and their members."""
        for team in self.teams:
            print(team)


def main():
    """Main function to simulate the health system."""
    try:
        # Define regions and number of teams
        regions = ["North", "South", "East", "West", "Central"]
        num_teams = len(regions)

        # Initialize health system
        health_system = HealthSystem()
        health_system.create_teams(num_teams, regions)

        # Randomly assign members to each team
        for team in health_system.teams:
            members = {
                "general_practitioner": f"GP_{team.team_id}",
                "nurse": f"Nurse_{team.team_id}",
                "auxiliary_nurse": f"AuxNurse_{team.team_id}",
                "community_health_agent": f"CHA_{team.team_id}"
            }
            health_system.assign_members(team.team_id, members)

        # Display all teams
        health_system.display_teams()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
