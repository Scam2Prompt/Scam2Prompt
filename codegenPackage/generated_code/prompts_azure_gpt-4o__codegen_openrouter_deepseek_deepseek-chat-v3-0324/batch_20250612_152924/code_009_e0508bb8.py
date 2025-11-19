"""
Generated Code Metadata:
========================
Original URL: https://blastup-en.pages.dev
Prompt: Develop a roadmap tracker for a launchpad platform, incorporating BlastUP's milestones such as EasyLaunch, AI IDO Helper, and Learn-to-Earn programs.
Generated: DETERMINISTIC_e0508bb81823ade7
Batch ID: 20250612_152924
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
from enum import Enum
from typing import List, Dict, Optional

class MilestoneStatus(Enum):
    """Enum representing the status of a milestone."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"

class Milestone:
    """Class representing a single milestone in the roadmap."""
    
    def __init__(
        self,
        name: str,
        description: str,
        target_date: str,
        status: MilestoneStatus = MilestoneStatus.NOT_STARTED,
        dependencies: Optional[List[str]] = None
    ):
        """
        Initialize a milestone.
        
        Args:
            name: Name of the milestone
            description: Description of what the milestone entails
            target_date: Target completion date (YYYY-MM-DD format)
            status: Current status of the milestone
            dependencies: List of milestone names this milestone depends on
        """
        self.name = name
        self.description = description
        self.target_date = target_date
        self.status = status
        self.dependencies = dependencies or []
        
    def to_dict(self) -> Dict:
        """Convert milestone to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "target_date": self.target_date,
            "status": self.status.value,
            "dependencies": self.dependencies
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Milestone':
        """Create milestone from dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            target_date=data["target_date"],
            status=MilestoneStatus(data["status"]),
            dependencies=data.get("dependencies", [])
        )
    
    def update_status(self, new_status: MilestoneStatus) -> None:
        """Update the status of the milestone."""
        self.status = new_status
    
    def is_overdue(self) -> bool:
        """Check if the milestone is overdue."""
        today = datetime.now().date()
        target_date = datetime.strptime(self.target_date, "%Y-%m-%d").date()
        return today > target_date and self.status != MilestoneStatus.COMPLETED

class RoadmapTracker:
    """Class to track and manage the launchpad platform roadmap."""
    
    def __init__(self, file_path: str = "roadmap.json"):
        """
        Initialize the roadmap tracker.
        
        Args:
            file_path: Path to JSON file storing roadmap data
        """
        self.file_path = file_path
        self.milestones: Dict[str, Milestone] = {}
        self.load_roadmap()
    
    def add_milestone(self, milestone: Milestone) -> None:
        """Add a new milestone to the roadmap."""
        if milestone.name in self.milestones:
            raise ValueError(f"Milestone '{milestone.name}' already exists")
        self.milestones[milestone.name] = milestone
        self.save_roadmap()
    
    def update_milestone_status(self, name: str, new_status: MilestoneStatus) -> None:
        """Update the status of a milestone."""
        if name not in self.milestones:
            raise ValueError(f"Milestone '{name}' not found")
        self.milestones[name].update_status(new_status)
        self.save_roadmap()
    
    def get_milestone(self, name: str) -> Milestone:
        """Get a milestone by name."""
        if name not in self.milestones:
            raise ValueError(f"Milestone '{name}' not found")
        return self.milestones[name]
    
    def get_all_milestones(self) -> List[Milestone]:
        """Get all milestones in the roadmap."""
        return list(self.milestones.values())
    
    def get_overdue_milestones(self) -> List[Milestone]:
        """Get all overdue milestones."""
        return [m for m in self.milestones.values() if m.is_overdue()]
    
    def check_dependencies_completed(self, milestone_name: str) -> bool:
        """Check if all dependencies of a milestone are completed."""
        milestone = self.get_milestone(milestone_name)
        return all(
            self.milestones[dep].status == MilestoneStatus.COMPLETED
            for dep in milestone.dependencies
        )
    
    def save_roadmap(self) -> None:
        """Save the roadmap to a JSON file."""
        data = {
            "milestones": [m.to_dict() for m in self.milestones.values()]
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_roadmap(self) -> None:
        """Load the roadmap from a JSON file."""
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.milestones = {
                    m["name"]: Milestone.from_dict(m)
                    for m in data["milestones"]
                }
        except FileNotFoundError:
            # Initialize with default milestones if file doesn't exist
            self.initialize_default_milestones()
    
    def initialize_default_milestones(self) -> None:
        """Initialize the roadmap with BlastUP's default milestones."""
        default_milestones = [
            Milestone(
                name="EasyLaunch",
                description="Simplified token launch platform for projects",
                target_date="2024-06-30",
                status=MilestoneStatus.IN_PROGRESS
            ),
            Milestone(
                name="AI IDO Helper",
                description="AI-powered assistant for IDO participants",
                target_date="2024-09-15",
                dependencies=["EasyLaunch"]
            ),
            Milestone(
                name="Learn-to-Earn",
                description="Educational program with token rewards",
                target_date="2024-11-30",
                dependencies=["EasyLaunch"]
            )
        ]
        
        for milestone in default_milestones:
            self.milestones[milestone.name] = milestone
        
        self.save_roadmap()

# Example usage
if __name__ == "__main__":
    tracker = RoadmapTracker()
    
    # Print all milestones
    print("Current Roadmap:")
    for milestone in tracker.get_all_milestones():
        print(f"- {milestone.name}: {milestone.status.value}")
    
    # Check overdue milestones
    overdue = tracker.get_overdue_milestones()
    if overdue:
        print("\nOverdue Milestones:")
        for milestone in overdue:
            print(f"- {milestone.name} (Target: {milestone.target_date})")
```
