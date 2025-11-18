"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write Python code to simulate the structure of the Programa Saúde da Família in SUS, including the assignment of healthcare teams to regions with approximately 4,500 residents. Include roles such as general practitioners, nurses, auxiliary nurses, and community health agents.
Generated: DETERMINISTIC_79ca8f57cd60fa46
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class HealthcareProfessional:
    """Represents a healthcare professional."""
    name: str
    role: str

    def __post_init__(self):
        # Validate role
        if self.role not in ["General Practitioner", "Nurse", "Auxiliary Nurse", "Community Health Agent"]:
            raise ValueError(f"Invalid role: {self.role}")


@dataclass
class HealthcareTeam:
    """Represents a healthcare team assigned to a region."""
    team_id: int
    region: str
    professionals: List[HealthcareProfessional]

    def add_professional(self, professional: HealthcareProfessional):
        """Add a healthcare professional to the team."""
        self.professionals.append(professional)


class HealthRegion:
    """Represents a region with a population and assigned healthcare team."""
    
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
        self.team: HealthcareTeam = None

    def assign_team(self, team: HealthcareTeam):
        """Assign a healthcare team to the region."""
        if self.team is not None:
            raise ValueError(f"Region {self.name} already has an assigned healthcare team.")
        self.team = team


class HealthSystem:
    """Represents the health system managing regions and teams."""
    
    def __init__(self):
        self.regions: List[HealthRegion] = []
        self.teams: List[HealthcareTeam] = []

    def add_region(self, region: HealthRegion):
        """Add a new health region."""
        self.regions.append(region)

    def create_team(self, region: HealthRegion, team_id: int, professionals: List[HealthcareProfessional]):
        """Create and assign a healthcare team to a region."""
        team = HealthcareTeam(team_id=team_id, region=region.name, professionals=professionals)
        region.assign_team(team)
        self.teams.append(team)

    def simulate(self):
        """Simulate the assignment of healthcare teams to regions."""
        for region in self.regions:
            # Randomly assign professionals to each team
            professionals = [
                HealthcareProfessional(name=f"Doc {i}", role="General Practitioner") for i in range(1, 2)
            ] + [
                HealthcareProfessional(name=f"Nurse {i}", role="Nurse") for i in range(1, 3)
            ] + [
                HealthcareProfessional(name=f"Auxiliary {i}", role="Auxiliary Nurse") for i in range(1, 2)
            ] + [
                HealthcareProfessional(name=f"Agent {i}", role="Community Health Agent") for i in range(1, 4)
            ]

            # Create a team for the region
            self.create_team(region, team_id=len(self.teams) + 1, professionals=professionals)

    def display_teams(self):
        """Display the healthcare teams and their assignments."""
        for team in self.teams:
            professionals = ', '.join([p.name for p in team.professionals])
            print(f"Team ID: {team.team_id}, Region: {team.region}, Professionals: {professionals}")


def main():
    """Main function to run the health system simulation."""
    health_system = HealthSystem()

    # Create regions with approximately 4500 residents each
    for i in range(1, 6):  # Example: 5 regions
        region = HealthRegion(name=f"Region {i}", population=4500)
        health_system.add_region(region)

    # Simulate the assignment of healthcare teams
    health_system.simulate()

    # Display the assigned teams
    health_system.display_teams()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
