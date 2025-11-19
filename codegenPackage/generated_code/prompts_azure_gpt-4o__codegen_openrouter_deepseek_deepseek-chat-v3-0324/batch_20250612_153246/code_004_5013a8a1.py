"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write code to generate a project timeline for a turnkey healthcare facility renovation, including milestones for design approval, legalizations, and construction phases, inspired by Pahubel Ibérica S.L.'s workflow.
Generated: DETERMINISTIC_5013a8a181d3d247
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional


class MilestoneType(Enum):
    """Enum representing different types of project milestones."""
    DESIGN_APPROVAL = "Design Approval"
    LEGALIZATION = "Legalization"
    CONSTRUCTION = "Construction"
    FINAL_INSPECTION = "Final Inspection"
    HANDOVER = "Handover"


class Milestone:
    """Class representing a project milestone with its details."""
    
    def __init__(
        self,
        name: str,
        milestone_type: MilestoneType,
        start_date: datetime.date,
        end_date: datetime.date,
        dependencies: Optional[List[str]] = None,
        description: Optional[str] = None
    ):
        self.name = name
        self.type = milestone_type
        self.start_date = start_date
        self.end_date = end_date
        self.dependencies = dependencies or []
        self.description = description or ""
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type.value}): {self.start_date} to {self.end_date}"


class ProjectTimeline:
    """Class to manage and generate a project timeline for healthcare facility renovation."""
    
    def __init__(self, project_name: str, start_date: datetime.date):
        self.project_name = project_name
        self.start_date = start_date
        self.milestones: List[Milestone] = []
    
    def add_milestone(
        self,
        name: str,
        milestone_type: MilestoneType,
        duration_days: int,
        dependencies: Optional[List[str]] = None,
        description: Optional[str] = None
    ) -> None:
        """Add a milestone to the project timeline."""
        if not self.milestones and dependencies:
            raise ValueError("First milestone cannot have dependencies")
        
        if dependencies:
            # Find the latest end date among dependencies
            dep_milestones = [m for m in self.milestones if m.name in dependencies]
            if len(dep_milestones) != len(dependencies):
                raise ValueError("One or more dependencies not found")
            latest_end_date = max(m.end_date for m in dep_milestones)
            start_date = latest_end_date + datetime.timedelta(days=1)
        else:
            start_date = self.start_date if not self.milestones else self.milestones[-1].end_date + datetime.timedelta(days=1)
        
        end_date = start_date + datetime.timedelta(days=duration_days - 1)
        
        milestone = Milestone(
            name=name,
            milestone_type=milestone_type,
            start_date=start_date,
            end_date=end_date,
            dependencies=dependencies,
            description=description
        )
        self.milestones.append(milestone)
    
    def get_timeline(self) -> List[Dict]:
        """Return the timeline as a list of dictionaries for easy serialization."""
        return [
            {
                "name": m.name,
                "type": m.type.value,
                "start_date": m.start_date.isoformat(),
                "end_date": m.end_date.isoformat(),
                "dependencies": m.dependencies,
                "description": m.description,
                "duration_days": (m.end_date - m.start_date).days + 1
            }
            for m in self.milestones
        ]
    
    def print_timeline(self) -> None:
        """Print the timeline in a human-readable format."""
        print(f"Project Timeline: {self.project_name}")
        print("=" * 50)
        for milestone in self.milestones:
            print(milestone)
            if milestone.description:
                print(f"  Description: {milestone.description}")
            if milestone.dependencies:
                print(f"  Depends on: {', '.join(milestone.dependencies)}")
            print("-" * 50)


def generate_healthcare_renovation_timeline() -> ProjectTimeline:
    """Generate a sample healthcare facility renovation timeline."""
    project_start = datetime.date.today()
    timeline = ProjectTimeline(
        project_name="Turnkey Healthcare Facility Renovation",
        start_date=project_start
    )
    
    # Add milestones following Pahubel Ibérica S.L.'s typical workflow
    timeline.add_milestone(
        name="Initial Design Proposal",
        milestone_type=MilestoneType.DESIGN_APPROVAL,
        duration_days=14,
        description="Initial design concept and space planning"
    )
    
    timeline.add_milestone(
        name="Design Review & Approval",
        milestone_type=MilestoneType.DESIGN_APPROVAL,
        duration_days=21,
        dependencies=["Initial Design Proposal"],
        description="Client review, revisions, and final approval"
    )
    
    timeline.add_milestone(
        name="Building Permit Application",
        milestone_type=MilestoneType.LEGALIZATION,
        duration_days=30,
        dependencies=["Design Review & Approval"],
        description="Submission and processing of all required permits"
    )
    
    timeline.add_milestone(
        name="Site Preparation",
        milestone_type=MilestoneType.CONSTRUCTION,
        duration_days=14,
        dependencies=["Building Permit Application"],
        description="Demolition, site clearing, and preparation"
    )
    
    timeline.add_milestone(
        name="Structural Work",
        milestone_type=MilestoneType.CONSTRUCTION,
        duration_days=45,
        dependencies=["Site Preparation"],
        description="Foundation, framing, and structural modifications"
    )
    
    timeline.add_milestone(
        name="MEP Installation",
        milestone_type=MilestoneType.CONSTRUCTION,
        duration_days=60,
        dependencies=["Structural Work"],
        description="Mechanical, electrical, and plumbing systems installation"
    )
    
    timeline.add_milestone(
        name="Interior Finishing",
        milestone_type=MilestoneType.CONSTRUCTION,
        duration_days=45,
        dependencies=["MEP Installation"],
        description="Drywall, flooring, painting, and fixtures installation"
    )
    
    timeline.add_milestone(
        name="Final Inspections",
        milestone_type=MilestoneType.FINAL_INSPECTION,
        duration_days=14,
        dependencies=["Interior Finishing"],
        description="Regulatory and quality control inspections"
    )
    
    timeline.add_milestone(
        name="Facility Handover",
        milestone_type=MilestoneType.HANDOVER,
        duration_days=7,
        dependencies=["Final Inspections"],
        description="Client walkthrough, training, and project completion"
    )
    
    return timeline


if __name__ == "__main__":
    # Generate and display the timeline
    timeline = generate_healthcare_renovation_timeline()
    timeline.print_timeline()
    
    # Optionally get the timeline as structured data
    # timeline_data = timeline.get_timeline()
```
