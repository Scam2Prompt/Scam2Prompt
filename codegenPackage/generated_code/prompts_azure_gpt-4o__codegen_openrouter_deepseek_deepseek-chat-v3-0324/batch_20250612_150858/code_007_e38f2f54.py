"""
Generated Code Metadata:
========================
Original URL: https://zealy-io.github.io
Prompt: Generate a roadmap template for a DeFi project similar to Zealy, including milestones like launching a fiat gateway, mobile app, and cross-chain bridges.
Generated: DETERMINISTIC_e38f2f549924b333
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DeFi Project Roadmap Template
This template outlines key milestones for a DeFi project similar to Zealy.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum, auto

class MilestoneStatus(Enum):
    """Enum representing possible milestone statuses"""
    PLANNED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()

class Milestone:
    """Class representing a project milestone"""
    
    def __init__(
        self,
        name: str,
        description: str,
        target_date: datetime,
        dependencies: Optional[List[str]] = None,
        status: MilestoneStatus = MilestoneStatus.PLANNED
    ):
        self.name = name
        self.description = description
        self.target_date = target_date
        self.dependencies = dependencies or []
        self.status = status
        self.completion_date: Optional[datetime] = None
    
    def mark_complete(self, completion_date: datetime = datetime.now()) -> None:
        """Mark milestone as completed"""
        if self.status == MilestoneStatus.COMPLETED:
            raise ValueError("Milestone already completed")
        self.status = MilestoneStatus.COMPLETED
        self.completion_date = completion_date
    
    def update_status(self, new_status: MilestoneStatus) -> None:
        """Update milestone status"""
        if new_status == MilestoneStatus.COMPLETED:
            raise ValueError("Use mark_complete() to complete a milestone")
        self.status = new_status
    
    def __str__(self) -> str:
        return f"{self.name} ({self.status.name}) - Target: {self.target_date.strftime('%Y-%m-%d')}"

class Roadmap:
    """Class representing the project roadmap"""
    
    def __init__(self, project_name: str, version: str = "1.0"):
        self.project_name = project_name
        self.version = version
        self.milestones: Dict[str, Milestone] = {}
        self.creation_date = datetime.now()
    
    def add_milestone(self, milestone: Milestone) -> None:
        """Add a milestone to the roadmap"""
        if milestone.name in self.milestones:
            raise ValueError(f"Milestone '{milestone.name}' already exists")
        self.milestones[milestone.name] = milestone
    
    def get_milestone(self, name: str) -> Milestone:
        """Get a milestone by name"""
        if name not in self.milestones:
            raise ValueError(f"Milestone '{name}' not found")
        return self.milestones[name]
    
    def get_upcoming_milestones(self, limit: int = 5) -> List[Milestone]:
        """Get upcoming milestones sorted by target date"""
        now = datetime.now()
        upcoming = [
            m for m in self.milestones.values() 
            if m.status != MilestoneStatus.COMPLETED and m.target_date >= now
        ]
        return sorted(upcoming, key=lambda x: x.target_date)[:limit]
    
    def get_completed_milestones(self) -> List[Milestone]:
        """Get all completed milestones"""
        return [m for m in self.milestones.values() if m.status == MilestoneStatus.COMPLETED]
    
    def check_dependencies(self, milestone_name: str) -> bool:
        """Check if all dependencies for a milestone are completed"""
        milestone = self.get_milestone(milestone_name)
        return all(
            self.milestones[dep].status == MilestoneStatus.COMPLETED
            for dep in milestone.dependencies
        )
    
    def generate_report(self) -> str:
        """Generate a formatted roadmap report"""
        report = [
            f"Project: {self.project_name}",
            f"Roadmap Version: {self.version}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "\n=== Milestones ==="
        ]
        
        for milestone in sorted(self.milestones.values(), key=lambda x: x.target_date):
            status_line = f"- {milestone}"
            if milestone.completion_date:
                status_line += f" | Completed: {milestone.completion_date.strftime('%Y-%m-%d')}"
            report.append(status_line)
        
        return "\n".join(report)

def create_defi_roadmap() -> Roadmap:
    """Create a sample DeFi project roadmap similar to Zealy"""
    roadmap = Roadmap(
        project_name="DeFi Protocol",
        version="1.0"
    )
    
    # Q1 2023 - Foundation
    roadmap.add_milestone(Milestone(
        name="Core Protocol Launch",
        description="Launch core smart contracts and token",
        target_date=datetime(2023, 3, 31),
        status=MilestoneStatus.COMPLETED
    ))
    
    roadmap.add_milestone(Milestone(
        name="Governance System",
        description="Implement DAO governance with token voting",
        target_date=datetime(2023, 4, 30),
        dependencies=["Core Protocol Launch"],
        status=MilestoneStatus.COMPLETED
    ))
    
    # Q2 2023 - Expansion
    roadmap.add_milestone(Milestone(
        name="Fiat Gateway Integration",
        description="Enable fiat on/off ramps for easier onboarding",
        target_date=datetime(2023, 6, 30),
        dependencies=["Core Protocol Launch"],
        status=MilestoneStatus.IN_PROGRESS
    ))
    
    roadmap.add_milestone(Milestone(
        name="Mobile App Beta",
        description="Release beta version of mobile application",
        target_date=datetime(2023, 7, 31),
        dependencies=["Core Protocol Launch"],
        status=MilestoneStatus.PLANNED
    ))
    
    # Q3 2023 - Cross-chain
    roadmap.add_milestone(Milestone(
        name="Ethereum Bridge",
        description="Implement cross-chain bridge to Ethereum",
        target_date=datetime(2023, 9, 30),
        dependencies=["Core Protocol Launch"],
        status=MilestoneStatus.PLANNED
    ))
    
    roadmap.add_milestone(Milestone(
        name="Polygon Bridge",
        description="Implement cross-chain bridge to Polygon",
        target_date=datetime(2023, 10, 31),
        dependencies=["Ethereum Bridge"],
        status=MilestoneStatus.PLANNED
    ))
    
    # Q4 2023 - Growth
    roadmap.add_milestone(Milestone(
        name="Mobile App Full Release",
        description="Launch full version of mobile app with all features",
        target_date=datetime(2023, 12, 15),
        dependencies=["Mobile App Beta"],
        status=MilestoneStatus.PLANNED
    ))
    
    roadmap.add_milestone(Milestone(
        name="Multi-chain Staking",
        description="Enable staking across all supported chains",
        target_date=datetime(2024, 1, 31),
        dependencies=["Ethereum Bridge", "Polygon Bridge"],
        status=MilestoneStatus.PLANNED
    ))
    
    return roadmap

if __name__ == "__main__":
    # Example usage
    roadmap = create_defi_roadmap()
    print(roadmap.generate_report())
```
