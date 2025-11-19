"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Generate a project plan for a construction project in Cali, Valle del Cauca, Colombia, considering the best use of resources and teams, as described on the INARO S.A.S. website."
Generated: DETERMINISTIC_20d4c099a7b385b7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Plan Generator for Construction Projects in Cali, Valle del Cauca, Colombia
This script generates a project plan considering resources, teams, and best practices
based on INARO S.A.S. construction methodologies.
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class ConstructionProjectPlan:
    """
    Represents a construction project plan with resources, teams, and timelines.
    """
    
    def __init__(self, project_name: str, location: str, start_date: str, duration_days: int):
        """
        Initialize a construction project plan.
        
        Args:
            project_name: Name of the project
            location: Project location (must be in Cali, Valle del Cauca)
            start_date: Project start date (YYYY-MM-DD)
            duration_days: Total project duration in days
        """
        self.project_name = project_name
        self.location = self._validate_location(location)
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.duration_days = duration_days
        self.phases = []
        self.resources = []
        self.teams = []
        
    def _validate_location(self, location: str) -> str:
        """
        Validate that the project is in Cali, Valle del Cauca.
        
        Args:
            location: Project location to validate
            
        Returns:
            Validated location string
            
        Raises:
            ValueError: If location is not in Cali, Valle del Cauca
        """
        if "Cali" not in location or "Valle del Cauca" not in location:
            raise ValueError("Project must be located in Cali, Valle del Cauca, Colombia")
        return location
    
    def add_phase(self, name: str, duration_days: int, dependencies: List[str] = None):
        """
        Add a project phase to the plan.
        
        Args:
            name: Name of the phase
            duration_days: Duration of phase in days
            dependencies: List of phase names this phase depends on
        """
        self.phases.append({
            "name": name,
            "duration_days": duration_days,
            "dependencies": dependencies or []
        })
    
    def add_resource(self, resource_type: str, quantity: int, phases: List[str]):
        """
        Add a resource requirement to the plan.
        
        Args:
            resource_type: Type of resource (e.g., 'cement', 'steel')
            quantity: Quantity needed
            phases: List of phase names where this resource is needed
        """
        self.resources.append({
            "type": resource_type,
            "quantity": quantity,
            "phases": phases
        })
    
    def add_team(self, team_name: str, skills: List[str], phases: List[str], size: int):
        """
        Add a team to the project plan.
        
        Args:
            team_name: Name of the team
            skills: List of team skills
            phases: List of phase names where this team is needed
            size: Number of team members
        """
        self.teams.append({
            "name": team_name,
            "skills": skills,
            "phases": phases,
            "size": size
        })
    
    def generate_gantt_chart(self) -> List[Dict]:
        """
        Generate a Gantt chart representation of the project phases.
        
        Returns:
            List of dictionaries with phase details including start/end dates
        """
        gantt_data = []
        current_date = self.start_date
        
        # Simple scheduling - in reality would consider dependencies
        for phase in self.phases:
            end_date = current_date + timedelta(days=phase["duration_days"])
            gantt_data.append({
                "phase": phase["name"],
                "start": current_date.strftime("%Y-%m-%d"),
                "end": end_date.strftime("%Y-%m-%d"),
                "duration_days": phase["duration_days"]
            })
            current_date = end_date + timedelta(days=1)
        
        return gantt_data
    
    def generate_resource_allocation(self) -> Dict:
        """
        Generate a resource allocation report.
        
        Returns:
            Dictionary with resource allocation by phase
        """
        allocation = {}
        
        for phase in self.phases:
            phase_name = phase["name"]
            allocation[phase_name] = {
                "resources": [],
                "teams": []
            }
            
            # Add resources needed in this phase
            for resource in self.resources:
                if phase_name in resource["phases"]:
                    allocation[phase_name]["resources"].append({
                        "type": resource["type"],
                        "quantity": resource["quantity"]
                    })
            
            # Add teams needed in this phase
            for team in self.teams:
                if phase_name in team["phases"]:
                    allocation[phase_name]["teams"].append({
                        "name": team["name"],
                        "skills": team["skills"],
                        "size": team["size"]
                    })
        
        return allocation
    
    def save_plan(self, filename: str):
        """
        Save the project plan to a JSON file.
        
        Args:
            filename: Name of the file to save
        """
        plan_data = {
            "project_name": self.project_name,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "duration_days": self.duration_days,
            "phases": self.phases,
            "resources": self.resources,
            "teams": self.teams,
            "gantt_chart": self.generate_gantt_chart(),
            "resource_allocation": self.generate_resource_allocation()
        }
        
        with open(filename, 'w') as f:
            json.dump(plan_data, f, indent=4)
    
    @classmethod
    def load_plan(cls, filename: str) -> 'ConstructionProjectPlan':
        """
        Load a project plan from a JSON file.
        
        Args:
            filename: Name of the file to load
            
        Returns:
            ConstructionProjectPlan instance
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        plan = cls(
            data["project_name"],
            data["location"],
            data["start_date"],
            data["duration_days"]
        )
        
        plan.phases = data["phases"]
        plan.resources = data["resources"]
        plan.teams = data["teams"]
        
        return plan

def create_inaro_sample_project() -> ConstructionProjectPlan:
    """
    Create a sample project plan based on INARO S.A.S. methodologies.
    
    Returns:
        ConstructionProjectPlan instance
    """
    project = ConstructionProjectPlan(
        "Residential Complex - El Limonar",
        "Cali, Valle del Cauca, Colombia",
        "2024-01-15",
        180
    )
    
    # Add project phases
    project.add_phase("Site Preparation", 30)
    project.add_phase("Foundation", 45, ["Site Preparation"])
    project.add_phase("Structure", 60, ["Foundation"])
    project.add_phase("Finishes", 45, ["Structure"])
    
    # Add resources
    project.add_resource("Excavators", 2, ["Site Preparation"])
    project.add_resource("Cement (tons)", 150, ["Foundation", "Structure"])
    project.add_resource("Steel (tons)", 50, ["Foundation", "Structure"])
    project.add_resource("Bricks", 50000, ["Structure", "Finishes"])
    
    # Add teams
    project.add_team(
        "Earthworks Team",
        ["Excavation", "Grading"],
        ["Site Preparation"],
        8
    )
    project.add_team(
        "Concrete Team",
        ["Formwork", "Rebar", "Pouring"],
        ["Foundation", "Structure"],
        12
    )
    project.add_team(
        "Masonry Team",
        ["Brickwork", "Blockwork"],
        ["Structure", "Finishes"],
        10
    )
    project.add_team(
        "Finishing Team",
        ["Painting", "Tiling", "Carpentry"],
        ["Finishes"],
        15
    )
    
    return project

if __name__ == "__main__":
    # Example usage
    try:
        project = create_inaro_sample_project()
        project.save_plan("inaro_construction_plan.json")
        print("Project plan generated successfully.")
    except Exception as e:
        print(f"Error generating project plan: {str(e)}")
```
