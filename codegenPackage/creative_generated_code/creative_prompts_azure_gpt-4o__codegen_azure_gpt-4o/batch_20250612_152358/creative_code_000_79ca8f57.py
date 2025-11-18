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
"""
Programa Saúde da Família (Family Health Program) Simulation

This Python script models the structure of the Programa Saúde da Família
in the Brazilian Unified Health System (SUS). It assigns healthcare teams
to regions with approximately 4,500 residents. Each team consists of 
general practitioners, nurses, auxiliary nurses, and community health agents.

Author: Expert Programmer
"""

import math

class Region:
    """
    Represents a region with a population.
    """
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.healthcare_team = None
    
    def assign_team(self, healthcare_team):
        """
        Assigns a healthcare team to this region.
        """
        self.healthcare_team = healthcare_team

class HealthcareTeam:
    """
    Represents a healthcare team which consists of:
    - General Practitioners
    - Nurses
    - Auxiliary Nurses
    - Community Health Agents
    """
    def __init__(self, team_id):
        self.team_id = team_id
        self.general_practitioners = []
        self.nurses = []
        self.auxiliary_nurses = []
        self.community_health_agents = []
    
    def add_general_practitioner(self, name):
        self.general_practitioners.append(name)
    
    def add_nurse(self, name):
        self.nurses.append(name)
    
    def add_auxiliary_nurse(self, name):
        self.auxiliary_nurses.append(name)
    
    def add_community_health_agent(self, name):
        self.community_health_agents.append(name)

def create_healthcare_team(team_id):
    """
    Factory function to create and populate a healthcare team.
    """
    team = HealthcareTeam(team_id)
    
    # Adding team members (these could be dynamic in a real-world scenario)
    team.add_general_practitioner("Dr. Alice")
    team.add_nurse("Nurse Bob")
    team.add_auxiliary_nurse("Aux Nurse Charlie")
    
    # Adding multiple community health agents (typically more numerous)
    for i in range(6):  # Example: 6 community health agents per team
        team.add_community_health_agent(f"Agent{i + 1}")
    
    return team

def assign_teams_to_regions(regions):
    """
    Assigns appropriate healthcare teams to a list of regions.
    Each team covers approximately 4,500 residents.
    """
    team_id_counter = 1
    for region in regions:
        num_teams_required = math.ceil(region.population / 4500)  # Calculate number of teams needed
        teams = []
        for _ in range(num_teams_required):
            team = create_healthcare_team(team_id_counter)
            team_id_counter += 1
            teams.append(team)
        region.assign_team(teams)

def main():
    """
    Main function to simulate the Programa Saúde da Família structure.
    """
    try:
        # Define regions in the system
        regions = [
            Region("Region A", 4500),
            Region("Region B", 8900),
            Region("Region C", 12000),
        ]
        
        # Assign healthcare teams to regions
        assign_teams_to_regions(regions)
        
        # Display the assignments
        print("Healthcare Team Assignments:")
        for region in regions:
            print(f"\n{region.name} (Population: {region.population})")
            if region.healthcare_team:
                for team in region.healthcare_team:
                    print(f"  Team {team.team_id}:")
                    print(f"    General Practitioners: {', '.join(team.general_practitioners)}")
                    print(f"    Nurses: {', '.join(team.nurses)}")
                    print(f"    Auxiliary Nurses: {', '.join(team.auxiliary_nurses)}")
                    print(f"    Community Health Agents: {', '.join(team.community_health_agents)}")
            else:
                print("  No healthcare team assigned.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
