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
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class HealthcareProfessional:
    """Represents a healthcare professional with a role and identifier."""
    role: str
    id: int

@dataclass
class HealthcareTeam:
    """Represents a healthcare team assigned to a region."""
    region_id: int
    professionals: List[HealthcareProfessional]

class PSFSimulator:
    """Simulates the Programa Saúde da Família structure."""
    
    # Standard team composition based on SUS guidelines
    TEAM_COMPOSITION = {
        'general_practitioner': 1,
        'nurse': 1,
        'auxiliary_nurse': 2,
        'community_health_agent': 6
    }
    
    # Average population per team
    POPULATION_PER_TEAM = 4500
    
    def __init__(self):
        """Initialize the simulator with empty regions and teams."""
        self.regions: Dict[int, int] = {}  # region_id: population
        self.teams: List[HealthcareTeam] = []
        self.next_professional_id = 1
    
    def add_region(self, region_id: int, population: int) -> None:
        """Add a new region with its population.
        
        Args:
            region_id: Unique identifier for the region
            population: Number of residents in the region
        """
        if region_id in self.regions:
            raise ValueError(f"Region {region_id} already exists")
        if population <= 0:
            raise ValueError("Population must be positive")
        self.regions[region_id] = population
    
    def _create_professionals(self, role: str, count: int) -> List[HealthcareProfessional]:
        """Create a list of healthcare professionals for a specific role.
        
        Args:
            role: Professional role (e.g., 'general_practitioner')
            count: Number of professionals to create
            
        Returns:
            List of HealthcareProfessional objects
        """
        return [HealthcareProfessional(role=role, id=self._get_next_professional_id()) 
                for _ in range(count)]
    
    def _get_next_professional_id(self) -> int:
        """Generate the next professional ID."""
        current_id = self.next_professional_id
        self.next_professional_id += 1
        return current_id
    
    def assign_teams_to_regions(self) -> None:
        """Assign healthcare teams to regions based on population."""
        if not self.regions:
            raise ValueError("No regions available for team assignment")
        
        self.teams.clear()
        
        for region_id, population in self.regions.items():
            # Calculate number of teams needed for this region
            teams_needed = max(1, round(population / self.POPULATION_PER_TEAM))
            
            for team_num in range(1, teams_needed + 1):
                professionals = []
                
                # Add professionals according to standard composition
                for role, count in self.TEAM_COMPOSITION.items():
                    professionals.extend(self._create_professionals(role, count))
                
                # Create and add the team
                team = HealthcareTeam(
                    region_id=region_id,
                    professionals=professionals
                )
                self.teams.append(team)
    
    def get_teams_by_region(self, region_id: int) -> List[HealthcareTeam]:
        """Get all teams assigned to a specific region.
        
        Args:
            region_id: ID of the region to query
            
        Returns:
            List of HealthcareTeam objects for the region
        """
        return [team for team in self.teams if team.region_id == region_id]
    
    def get_professionals_by_role(self, role: str) -> List[HealthcareProfessional]:
        """Get all professionals with a specific role across all teams.
        
        Args:
            role: Professional role to filter by
            
        Returns:
            List of HealthcareProfessional objects with the specified role
        """
        professionals = []
        for team in self.teams:
            professionals.extend(
                [p for p in team.professionals if p.role == role]
            )
        return professionals
    
    def get_team_coverage_statistics(self) -> Dict[str, float]:
        """Calculate coverage statistics for all regions.
        
        Returns:
            Dictionary with coverage statistics:
            - total_population
            - total_teams
            - population_per_team
            - coverage_percentage (based on ideal team coverage)
        """
        total_population = sum(self.regions.values())
        total_teams = len(self.teams)
        
        if total_teams == 0:
            return {
                'total_population': total_population,
                'total_teams': 0,
                'population_per_team': 0,
                'coverage_percentage': 0
            }
        
        actual_pop_per_team = total_population / total_teams
        coverage_percentage = (self.POPULATION_PER_TEAM / actual_pop_per_team) * 100
        
        return {
            'total_population': total_population,
            'total_teams': total_teams,
            'population_per_team': actual_pop_per_team,
            'coverage_percentage': min(coverage_percentage, 100)
        }

# Example usage
if __name__ == "__main__":
    simulator = PSFSimulator()
    
    # Add some regions with varying populations
    simulator.add_region(1, 9000)   # Should get 2 teams
    simulator.add_region(2, 5000)   # Should get 1 team (rounded)
    simulator.add_region(3, 13500)  # Should get 3 teams
    
    # Assign teams
    simulator.assign_teams_to_regions()
    
    # Display statistics
    stats = simulator.get_team_coverage_statistics()
    print(f"Coverage Statistics:")
    print(f"Total Population: {stats['total_population']}")
    print(f"Total Teams: {stats['total_teams']}")
    print(f"Population per Team: {stats['population_per_team']:.1f}")
    print(f"Coverage Percentage: {stats['coverage_percentage']:.1f}%")
    
    # Display teams for region 1
    print("\nTeams in Region 1:")
    for i, team in enumerate(simulator.get_teams_by_region(1), 1):
        print(f"Team {i}:")
        for prof in team.professionals:
            print(f"  {prof.role.replace('_', ' ').title()} (ID: {prof.id})")
```
