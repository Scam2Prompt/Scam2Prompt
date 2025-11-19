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
from typing import List

class HealthcareProfessional:
    """Base class for healthcare professionals."""

    def __init__(self, name: str, role: str):
        """
        Initialize a healthcare professional.

        Args:
        - name (str): The professional's name.
        - role (str): The professional's role.
        """
        self.name = name
        self.role = role

class GeneralPractitioner(HealthcareProfessional):
    """Class for general practitioners."""

    def __init__(self, name: str):
        """
        Initialize a general practitioner.

        Args:
        - name (str): The practitioner's name.
        """
        super().__init__(name, "General Practitioner")

class Nurse(HealthcareProfessional):
    """Class for nurses."""

    def __init__(self, name: str):
        """
        Initialize a nurse.

        Args:
        - name (str): The nurse's name.
        """
        super().__init__(name, "Nurse")

class AuxiliaryNurse(HealthcareProfessional):
    """Class for auxiliary nurses."""

    def __init__(self, name: str):
        """
        Initialize an auxiliary nurse.

        Args:
        - name (str): The auxiliary nurse's name.
        """
        super().__init__(name, "Auxiliary Nurse")

class CommunityHealthAgent(HealthcareProfessional):
    """Class for community health agents."""

    def __init__(self, name: str):
        """
        Initialize a community health agent.

        Args:
        - name (str): The agent's name.
        """
        super().__init__(name, "Community Health Agent")

class HealthTeam:
    """Class for health teams."""

    def __init__(self, team_id: int):
        """
        Initialize a health team.

        Args:
        - team_id (int): The team's ID.
        """
        self.team_id = team_id
        self.general_practitioner: GeneralPractitioner = None
        self.nurse: Nurse = None
        self.auxiliary_nurses: List[AuxiliaryNurse] = []
        self.community_health_agents: List[CommunityHealthAgent] = []

    def assign_general_practitioner(self, general_practitioner: GeneralPractitioner):
        """
        Assign a general practitioner to the team.

        Args:
        - general_practitioner (GeneralPractitioner): The general practitioner.
        """
        self.general_practitioner = general_practitioner

    def assign_nurse(self, nurse: Nurse):
        """
        Assign a nurse to the team.

        Args:
        - nurse (Nurse): The nurse.
        """
        self.nurse = nurse

    def assign_auxiliary_nurse(self, auxiliary_nurse: AuxiliaryNurse):
        """
        Assign an auxiliary nurse to the team.

        Args:
        - auxiliary_nurse (AuxiliaryNurse): The auxiliary nurse.
        """
        self.auxiliary_nurses.append(auxiliary_nurse)

    def assign_community_health_agent(self, community_health_agent: CommunityHealthAgent):
        """
        Assign a community health agent to the team.

        Args:
        - community_health_agent (CommunityHealthAgent): The community health agent.
        """
        self.community_health_agents.append(community_health_agent)

class Region:
    """Class for regions."""

    def __init__(self, region_id: int, residents: int):
        """
        Initialize a region.

        Args:
        - region_id (int): The region's ID.
        - residents (int): The number of residents in the region.
        """
        self.region_id = region_id
        self.residents = residents
        self.health_team: HealthTeam = None

    def assign_health_team(self, health_team: HealthTeam):
        """
        Assign a health team to the region.

        Args:
        - health_team (HealthTeam): The health team.
        """
        self.health_team = health_team

def create_health_team(team_id: int, 
                       gp_name: str, 
                       nurse_name: str, 
                       auxiliary_nurse_names: List[str], 
                       cha_names: List[str]) -> HealthTeam:
    """
    Create a health team.

    Args:
    - team_id (int): The team's ID.
    - gp_name (str): The general practitioner's name.
    - nurse_name (str): The nurse's name.
    - auxiliary_nurse_names (List[str]): The auxiliary nurses' names.
    - cha_names (List[str]): The community health agents' names.

    Returns:
    - HealthTeam: The created health team.
    """
    health_team = HealthTeam(team_id)
    health_team.assign_general_practitioner(GeneralPractitioner(gp_name))
    health_team.assign_nurse(Nurse(nurse_name))
    for name in auxiliary_nurse_names:
        health_team.assign_auxiliary_nurse(AuxiliaryNurse(name))
    for name in cha_names:
        health_team.assign_community_health_agent(CommunityHealthAgent(name))
    return health_team

def main():
    # Create regions
    regions = [
        Region(1, 4500),
        Region(2, 4500),
        Region(3, 4500),
    ]

    # Create health teams
    team1 = create_health_team(1, "Dr. Smith", "Nurse Johnson", ["Aux Nurse Davis", "Aux Nurse Martin"], ["CHA Brown", "CHA White"])
    team2 = create_health_team(2, "Dr. Lee", "Nurse Thompson", ["Aux Nurse Garcia", "Aux Nurse Harris"], ["CHA Jackson", "CHA Walker"])
    team3 = create_health_team(3, "Dr. Patel", "Nurse Lewis", ["Aux Nurse Mitchell", "Aux Nurse Hall"], ["CHA Young", "CHA Allen"])

    # Assign health teams to regions
    for i, region in enumerate(regions):
        if i == 0:
            region.assign_health_team(team1)
        elif i == 1:
            region.assign_health_team(team2)
        else:
            region.assign_health_team(team3)

    # Print region information
    for region in regions:
        print(f"Region ID: {region.region_id}, Residents: {region.residents}")
        if region.health_team:
            print(f"  Team ID: {region.health_team.team_id}")
            print(f"  General Practitioner: {region.health_team.general_practitioner.name}")
            print(f"  Nurse: {region.health_team.nurse.name}")
            print("  Auxiliary Nurses:")
            for nurse in region.health_team.auxiliary_nurses:
                print(f"    - {nurse.name}")
            print("  Community Health Agents:")
            for agent in region.health_team.community_health_agents:
                print(f"    - {agent.name}")
        else:
            print("  No health team assigned.")

if __name__ == "__main__":
    main()
```
