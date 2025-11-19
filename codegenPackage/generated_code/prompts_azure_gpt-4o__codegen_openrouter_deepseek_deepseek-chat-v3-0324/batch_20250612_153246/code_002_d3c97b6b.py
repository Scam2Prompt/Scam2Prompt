"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Generate a template for conducting an environmental impact study (EIA) for an electrical transmission project, incorporating elements from MAROD Consultores SAC's approach.
Generated: DETERMINISTIC_d3c97b6b9dab1d8e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Environmental Impact Assessment (EIA) Template for Electrical Transmission Projects
Inspired by MAROD Consultores SAC's approach
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Union

class EnvironmentalImpactAssessment:
    """
    Class representing an Environmental Impact Assessment (EIA) for electrical transmission projects.
    """
    
    def __init__(self, project_name: str, project_location: str, client: str):
        """
        Initialize the EIA with basic project information.
        
        Args:
            project_name: Name of the electrical transmission project
            project_location: Geographic location of the project
            client: Name of the client/company commissioning the project
        """
        self.project_name = project_name
        self.project_location = project_location
        self.client = client
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.last_updated = self.creation_date
        self.sections = {
            "project_description": None,
            "legal_framework": None,
            "baseline_study": None,
            "impact_assessment": None,
            "mitigation_measures": None,
            "environmental_management_plan": None,
            "monitoring_program": None,
            "public_participation": None,
            "conclusions": None
        }
        self.team_members = []
        self.approvals = []
        self.version = "1.0"
        
    def add_section_content(self, section_name: str, content: Union[str, Dict, List]) -> bool:
        """
        Add or update content for a specific section of the EIA.
        
        Args:
            section_name: Name of the section to update
            content: Content to add (can be text, dict, or list)
            
        Returns:
            bool: True if section was updated, False if section doesn't exist
        """
        if section_name in self.sections:
            self.sections[section_name] = content
            self.last_updated = datetime.now().strftime("%Y-%m-%d")
            return True
        return False
    
    def add_team_member(self, name: str, role: str, organization: str, contact: Optional[str] = None) -> None:
        """
        Add a team member involved in the EIA preparation.
        
        Args:
            name: Full name of the team member
            role: Their role in the project
            organization: Their affiliated organization
            contact: Optional contact information
        """
        member = {
            "name": name,
            "role": role,
            "organization": organization,
            "contact": contact
        }
        self.team_members.append(member)
        self.last_updated = datetime.now().strftime("%Y-%m-%d")
        
    def add_approval(self, approver: str, position: str, date: str, comments: Optional[str] = None) -> None:
        """
        Add an approval record for the EIA.
        
        Args:
            approver: Name of the approving authority
            position: Position/title of the approver
            date: Date of approval (YYYY-MM-DD format)
            comments: Optional comments about the approval
        """
        approval = {
            "approver": approver,
            "position": position,
            "date": date,
            "comments": comments
        }
        self.approvals.append(approval)
        self.last_updated = datetime.now().strftime("%Y-%m-%d")
        
    def generate_report(self, output_format: str = "json") -> Union[Dict, str]:
        """
        Generate the EIA report in the specified format.
        
        Args:
            output_format: Format of the output ('json' or 'string')
            
        Returns:
            The report in the requested format
            
        Raises:
            ValueError: If an unsupported output format is requested
        """
        report = {
            "metadata": {
                "project_name": self.project_name,
                "project_location": self.project_location,
                "client": self.client,
                "creation_date": self.creation_date,
                "last_updated": self.last_updated,
                "version": self.version
            },
            "sections": self.sections,
            "team_members": self.team_members,
            "approvals": self.approvals
        }
        
        if output_format == "json":
            return report
        elif output_format == "string":
            return json.dumps(report, indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the EIA report to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Raises:
            IOError: If there's an issue writing to the file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.generate_report(), f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to save EIA report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a new EIA
    eia = EnvironmentalImpactAssessment(
        project_name="Northern Grid Expansion Project",
        project_location="Andean Region, Peru",
        client="National Grid Corporation"
    )
    
    # Add team members
    eia.add_team_member(
        name="Dr. Maria Rodriguez",
        role="Lead Environmental Consultant",
        organization="MAROD Consultores SAC",
        contact="mrodriguez@marod.com"
    )
    
    # Add section content
    eia.add_section_content(
        section_name="project_description",
        content={
            "project_scope": "Construction of 200km 500kV transmission line",
            "components": ["Towers", "Substations", "Access roads"],
            "timeline": "2023-2025"
        }
    )
    
    # Generate and save report
    report = eia.generate_report(output_format="string")
    print(report)
    eia.save_to_file("northern_grid_eia.json")
```
