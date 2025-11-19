"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Write code to generate a report summarizing client requirements and proposed solutions for building design, referencing the consultation process described on Tari.ee.
Generated: DETERMINISTIC_659b8e3607313f84
Batch ID: 20250612_154250
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
from typing import List, Dict, Optional

class ClientRequirement:
    """Class representing a single client requirement."""
    
    def __init__(self, id: int, description: str, priority: str, category: str):
        """
        Initialize a client requirement.
        
        Args:
            id: Unique identifier for the requirement
            description: Text description of the requirement
            priority: Priority level (High/Medium/Low)
            category: Category of requirement (e.g., Structural, Aesthetic)
        """
        self.id = id
        self.description = description
        self.priority = priority
        self.category = category
        
    def to_dict(self) -> Dict:
        """Convert requirement to dictionary for serialization."""
        return {
            'id': self.id,
            'description': self.description,
            'priority': self.priority,
            'category': self.category
        }

class ProposedSolution:
    """Class representing a proposed solution for a requirement."""
    
    def __init__(self, requirement_id: int, solution: str, materials: List[str], 
                 estimated_cost: float, timeline: str):
        """
        Initialize a proposed solution.
        
        Args:
            requirement_id: ID of the requirement this solution addresses
            solution: Description of the proposed solution
            materials: List of materials needed
            estimated_cost: Estimated cost of implementation
            timeline: Estimated timeline for implementation
        """
        self.requirement_id = requirement_id
        self.solution = solution
        self.materials = materials
        self.estimated_cost = estimated_cost
        self.timeline = timeline
        
    def to_dict(self) -> Dict:
        """Convert solution to dictionary for serialization."""
        return {
            'requirement_id': self.requirement_id,
            'solution': self.solution,
            'materials': self.materials,
            'estimated_cost': self.estimated_cost,
            'timeline': self.timeline
        }

class ConsultationReport:
    """Class to generate a building design consultation report."""
    
    def __init__(self, client_name: str, project_name: str, consultation_date: str):
        """
        Initialize a consultation report.
        
        Args:
            client_name: Name of the client
            project_name: Name of the project
            consultation_date: Date of consultation (YYYY-MM-DD)
        """
        self.client_name = client_name
        self.project_name = project_name
        self.consultation_date = consultation_date
        self.requirements: List[ClientRequirement] = []
        self.solutions: List[ProposedSolution] = []
        
    def add_requirement(self, requirement: ClientRequirement) -> None:
        """Add a client requirement to the report."""
        self.requirements.append(requirement)
        
    def add_solution(self, solution: ProposedSolution) -> None:
        """Add a proposed solution to the report."""
        if not any(req.id == solution.requirement_id for req in self.requirements):
            raise ValueError("No matching requirement found for this solution")
        self.solutions.append(solution)
        
    def generate_report(self) -> Dict:
        """Generate the full report as a dictionary."""
        if not self.requirements:
            raise ValueError("No requirements added to the report")
            
        report = {
            'metadata': {
                'client_name': self.client_name,
                'project_name': self.project_name,
                'consultation_date': self.consultation_date,
                'generated_date': datetime.now().strftime("%Y-%m-%d"),
                'report_version': '1.0'
            },
            'requirements': [req.to_dict() for req in self.requirements],
            'solutions': [sol.to_dict() for sol in self.solutions],
            'summary': self._generate_summary()
        }
        
        return report
    
    def _generate_summary(self) -> Dict:
        """Generate summary statistics for the report."""
        total_requirements = len(self.requirements)
        total_solutions = len(self.solutions)
        high_priority = sum(1 for req in self.requirements if req.priority == 'High')
        estimated_total_cost = sum(sol.estimated_cost for sol in self.solutions)
        
        return {
            'total_requirements': total_requirements,
            'requirements_with_solutions': total_solutions,
            'high_priority_requirements': high_priority,
            'estimated_total_cost': estimated_total_cost
        }
    
    def save_report(self, filename: str, format: str = 'json') -> None:
        """
        Save the report to a file.
        
        Args:
            filename: Output filename
            format: Output format ('json' or 'txt')
        """
        report = self.generate_report()
        
        try:
            if format == 'json':
                with open(filename, 'w') as f:
                    json.dump(report, f, indent=4)
            elif format == 'txt':
                with open(filename, 'w') as f:
                    f.write(self._format_text_report(report))
            else:
                raise ValueError("Unsupported format. Use 'json' or 'txt'")
        except IOError as e:
            raise IOError(f"Failed to save report: {str(e)}")
    
    def _format_text_report(self, report: Dict) -> str:
        """Format the report as human-readable text."""
        text = f"Building Design Consultation Report\n"
        text += f"==================================\n\n"
        text += f"Client: {report['metadata']['client_name']}\n"
        text += f"Project: {report['metadata']['project_name']}\n"
        text += f"Consultation Date: {report['metadata']['consultation_date']}\n"
        text += f"Report Generated: {report['metadata']['generated_date']}\n\n"
        
        text += "Requirements:\n"
        text += "-------------\n"
        for req in report['requirements']:
            text += f"ID: {req['id']}\n"
            text += f"Category: {req['category']}\n"
            text += f"Priority: {req['priority']}\n"
            text += f"Description: {req['description']}\n\n"
        
        text += "\nProposed Solutions:\n"
        text += "------------------\n"
        for sol in report['solutions']:
            req = next(r for r in report['requirements'] if r['id'] == sol['requirement_id'])
            text += f"Requirement ID: {sol['requirement_id']} ({req['description'][:50]}...)\n"
            text += f"Solution: {sol['solution']}\n"
            text += f"Materials: {', '.join(sol['materials'])}\n"
            text += f"Estimated Cost: {sol['estimated_cost']}\n"
            text += f"Timeline: {sol['timeline']}\n\n"
        
        text += "\nSummary:\n"
        text += "-------\n"
        summary = report['summary']
        text += f"Total Requirements: {summary['total_requirements']}\n"
        text += f"Requirements with Solutions: {summary['requirements_with_solutions']}\n"
        text += f"High Priority Requirements: {summary['high_priority_requirements']}\n"
        text += f"Estimated Total Cost: {summary['estimated_total_cost']}\n"
        
        return text

# Example usage
if __name__ == "__main__":
    # Create a new report
    report = ConsultationReport(
        client_name="ABC Construction",
        project_name="Residential Complex",
        consultation_date="2023-11-15"
    )
    
    # Add requirements
    req1 = ClientRequirement(
        id=1,
        description="Energy-efficient building design with solar panel integration",
        priority="High",
        category="Sustainability"
    )
    
    req2 = ClientRequirement(
        id=2,
        description="Modern aesthetic with large glass facades",
        priority="Medium",
        category="Aesthetic"
    )
    
    report.add_requirement(req1)
    report.add_requirement(req2)
    
    # Add solutions
    sol1 = ProposedSolution(
        requirement_id=1,
        solution="Install rooftop solar panels with battery storage system",
        materials=["Solar panels", "Battery storage", "Inverters"],
        estimated_cost=25000,
        timeline="4 weeks"
    )
    
    sol2 = ProposedSolution(
        requirement_id=2,
        solution="Use floor-to-ceiling tempered glass with steel supports",
        materials=["Tempered glass", "Steel supports", "Thermal insulation"],
        estimated_cost=18000,
        timeline="3 weeks"
    )
    
    report.add_solution(sol1)
    report.add_solution(sol2)
    
    # Save reports
    report.save_report("building_design_report.json")
    report.save_report("building_design_report.txt", format="txt")
```
