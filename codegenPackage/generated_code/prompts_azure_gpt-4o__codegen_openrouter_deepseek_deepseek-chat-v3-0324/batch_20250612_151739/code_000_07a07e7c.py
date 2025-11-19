"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write Python code to generate a risk prevention plan template for "Coordination SPS" as described by AFCO Fédération, including sections for construction, exploitation, and maintenance phases.
Generated: DETERMINISTIC_07a07e7c09159d98
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class RiskPreventionPlan:
    """
    A class to generate a risk prevention plan template for Coordination SPS.
    Follows AFCO Fédération guidelines with sections for construction, exploitation, and maintenance.
    """
    
    def __init__(self, project_name: str, project_manager: str, location: str):
        """
        Initialize the risk prevention plan with basic project information.
        
        Args:
            project_name: Name of the project
            project_manager: Name of the project manager
            location: Project location
        """
        self.project_name = project_name
        self.project_manager = project_manager
        self.location = location
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.sections = {
            "construction": [],
            "exploitation": [],
            "maintenance": []
        }
        self.participants = []
    
    def add_participant(self, name: str, role: str, company: str) -> None:
        """
        Add a participant to the prevention plan.
        
        Args:
            name: Participant's name
            role: Participant's role
            company: Participant's company
        """
        self.participants.append({
            "name": name,
            "role": role,
            "company": company
        })
    
    def add_risk(self, phase: str, description: str, prevention_measures: List[str], 
                 responsible: str, severity: str = "medium") -> None:
        """
        Add a risk to a specific phase of the project.
        
        Args:
            phase: Project phase (construction/exploitation/maintenance)
            description: Risk description
            prevention_measures: List of prevention measures
            responsible: Responsible party
            severity: Risk severity (low/medium/high)
        
        Raises:
            ValueError: If phase is invalid
        """
        if phase not in self.sections:
            raise ValueError(f"Invalid phase: {phase}. Must be one of {list(self.sections.keys())}")
        
        self.sections[phase].append({
            "description": description,
            "prevention_measures": prevention_measures,
            "responsible": responsible,
            "severity": severity,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        })
    
    def generate_report(self, output_format: str = "json") -> Optional[Dict]:
        """
        Generate the risk prevention plan report.
        
        Args:
            output_format: Output format ('json' or 'dict')
        
        Returns:
            The report in requested format or None if format is invalid
        
        Raises:
            ValueError: If output format is invalid
        """
        report = {
            "project_name": self.project_name,
            "project_manager": self.project_manager,
            "location": self.location,
            "creation_date": self.creation_date,
            "last_update": datetime.now().strftime("%Y-%m-%d"),
            "participants": self.participants,
            "risk_prevention_plan": self.sections
        }
        
        if output_format == "dict":
            return report
        elif output_format == "json":
            return json.dumps(report, indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Invalid output format: {output_format}. Must be 'json' or 'dict'")
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the risk prevention plan to a JSON file.
        
        Args:
            filename: Name of the output file
        
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.generate_report("dict"), f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to write to file {filename}: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new risk prevention plan
        plan = RiskPreventionPlan(
            project_name="New Office Building",
            project_manager="Jean Dupont",
            location="Paris, France"
        )
        
        # Add participants
        plan.add_participant("Marie Curie", "Safety Officer", "ConstructCo")
        plan.add_participant("Pierre Durand", "Site Manager", "BuildCorp")
        
        # Add risks for construction phase
        plan.add_risk(
            phase="construction",
            description="Fall from height during roof installation",
            prevention_measures=[
                "Use of safety harnesses",
                "Installation of guardrails",
                "Regular safety inspections"
            ],
            responsible="Site Manager",
            severity="high"
        )
        
        # Add risks for exploitation phase
        plan.add_risk(
            phase="exploitation",
            description="Electrical hazards in server rooms",
            prevention_measures=[
                "Regular equipment maintenance",
                "Use of PPE when working with electrical systems",
                "Clear labeling of electrical panels"
            ],
            responsible="Facility Manager"
        )
        
        # Add risks for maintenance phase
        plan.add_risk(
            phase="maintenance",
            description="Exposure to hazardous materials during HVAC maintenance",
            prevention_measures=[
                "Proper ventilation during work",
                "Use of appropriate PPE",
                "Training on hazardous materials handling"
            ],
            responsible="Maintenance Team",
            severity="medium"
        )
        
        # Generate and save the report
        print(plan.generate_report("json"))
        plan.save_to_file("risk_prevention_plan.json")
        
    except Exception as e:
        print(f"Error generating risk prevention plan: {str(e)}")
```
