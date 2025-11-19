"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Create a sample project plan for a CGI animation series, including milestones for concept art and animation production as practiced at Sprout Studios.
Generated: DETERMINISTIC_a55cd3cd0ef15c5c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CGI Animation Series Project Plan for Sprout Studios

This script outlines a sample project plan for a CGI animation series,
including key milestones for concept art and animation production.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

class ProjectMilestone:
    """Represents a key milestone in the animation production process."""
    
    def __init__(self, name: str, description: str, duration_days: int, 
                 dependencies: Optional[List[str]] = None):
        """
        Initialize a project milestone.
        
        Args:
            name: Name of the milestone
            description: Detailed description of the milestone
            duration_days: Estimated duration in working days
            dependencies: List of milestone names that must be completed first
        """
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.dependencies = dependencies or []
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
    
    def to_dict(self) -> Dict:
        """Convert milestone to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "duration_days": self.duration_days,
            "dependencies": self.dependencies,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

class AnimationProjectPlan:
    """Manages the complete project plan for a CGI animation series."""
    
    def __init__(self, project_name: str, start_date: datetime):
        """
        Initialize the animation project plan.
        
        Args:
            project_name: Name of the animation project
            start_date: Project start date
        """
        self.project_name = project_name
        self.start_date = start_date
        self.milestones: Dict[str, ProjectMilestone] = {}
        
        # Initialize with standard Sprout Studios production milestones
        self._initialize_standard_milestones()
    
    def _initialize_standard_milestones(self) -> None:
        """Create standard production milestones as practiced at Sprout Studios."""
        self.add_milestone(
            ProjectMilestone(
                "Concept Development",
                "Develop initial concept art, character designs, and world building",
                30
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Script Finalization",
                "Complete all episode scripts and story outlines",
                45,
                ["Concept Development"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Storyboarding",
                "Create detailed storyboards for all episodes",
                60,
                ["Script Finalization"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Pre-visualization",
                "Create animatics and pre-visualization sequences",
                30,
                ["Storyboarding"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Asset Production",
                "Modeling, texturing, and rigging of all characters and environments",
                90,
                ["Concept Development"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Animation Blocking",
                "Initial blocking of all character animation",
                60,
                ["Pre-visualization", "Asset Production"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Animation Polish",
                "Refine and polish all animation sequences",
                90,
                ["Animation Blocking"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Lighting & Rendering",
                "Final lighting setup and render all sequences",
                60,
                ["Animation Polish"]
            )
        )
        
        self.add_milestone(
            ProjectMilestone(
                "Post-Production",
                "Compositing, VFX, color grading, and final output",
                45,
                ["Lighting & Rendering"]
            )
        )
    
    def add_milestone(self, milestone: ProjectMilestone) -> None:
        """Add a milestone to the project plan."""
        if milestone.name in self.milestones:
            raise ValueError(f"Milestone '{milestone.name}' already exists")
        self.milestones[milestone.name] = milestone
    
    def calculate_schedule(self) -> None:
        """Calculate start and end dates for all milestones based on dependencies."""
        scheduled = set()
        
        # Initialize with milestones that have no dependencies
        queue = [name for name, m in self.milestones.items() if not m.dependencies]
        
        while queue:
            current_name = queue.pop(0)
            current = self.milestones[current_name]
            
            # Calculate start date based on dependencies
            if not current.dependencies:
                current.start_date = self.start_date
            else:
                latest_end = max(
                    self.milestones[dep].end_date 
                    for dep in current.dependencies 
                    if dep in scheduled
                )
                current.start_date = latest_end + timedelta(days=1)
            
            current.end_date = current.start_date + timedelta(days=current.duration_days - 1)
            scheduled.add(current_name)
            
            # Add dependent milestones to queue if all their dependencies are scheduled
            for name, milestone in self.milestones.items():
                if name not in scheduled and name not in queue:
                    if all(dep in scheduled for dep in milestone.dependencies):
                        queue.append(name)
    
    def to_json(self) -> str:
        """Serialize the project plan to JSON format."""
        plan_dict = {
            "project_name": self.project_name,
            "start_date": self.start_date.isoformat(),
            "milestones": [m.to_dict() for m in self.milestones.values()]
        }
        return json.dumps(plan_dict, indent=2)
    
    def print_timeline(self) -> None:
        """Print a human-readable timeline of the project."""
        print(f"Project: {self.project_name}")
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n")
        
        sorted_milestones = sorted(
            self.milestones.values(), 
            key=lambda m: m.start_date if m.start_date else datetime.max
        )
        
        for milestone in sorted_milestones:
            if milestone.start_date and milestone.end_date:
                print(f"{milestone.name}:")
                print(f"  Description: {milestone.description}")
                print(f"  Duration: {milestone.duration_days} days")
                print(f"  Start: {milestone.start_date.strftime('%Y-%m-%d')}")
                print(f"  End: {milestone.end_date.strftime('%Y-%m-%d')}")
                if milestone.dependencies:
                    print(f"  Depends on: {', '.join(milestone.dependencies)}")
                print()

# Example usage
if __name__ == "__main__":
    # Create a new project starting today
    project = AnimationProjectPlan(
        "Fantasy Adventure Series",
        datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    )
    
    # Calculate the schedule
    project.calculate_schedule()
    
    # Print the timeline
    project.print_timeline()
    
    # Optionally save to JSON
    # with open("animation_project_plan.json", "w") as f:
    #     f.write(project.to_json())
```
