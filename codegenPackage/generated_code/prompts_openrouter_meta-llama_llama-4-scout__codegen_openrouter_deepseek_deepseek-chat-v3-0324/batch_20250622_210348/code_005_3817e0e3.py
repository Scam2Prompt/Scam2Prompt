"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Create a roadmap for a cryptocurrency project that includes key milestones such as NFT debut, game beta launch, and multi-chain bridge integration, similar to the Bitcoin Dogs Club roadmap.
Generated: DETERMINISTIC_3817e0e3f8f7f7aa
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cryptocurrency Project Roadmap Implementation
Defines key milestones and timeline for a cryptocurrency project.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
from typing import List, Dict, Optional


class MilestoneStatus(Enum):
    """Enum representing possible statuses of project milestones."""
    PLANNED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()


class Milestone:
    """Class representing a single project milestone."""
    
    def __init__(
        self,
        name: str,
        description: str,
        target_date: datetime,
        status: MilestoneStatus = MilestoneStatus.PLANNED
    ):
        """
        Initialize a milestone.
        
        Args:
            name: Short name of the milestone
            description: Detailed description of what this milestone entails
            target_date: Planned completion date
            status: Current status of the milestone
        """
        self.name = name
        self.description = description
        self.target_date = target_date
        self.status = status
        self.completed_date: Optional[datetime] = None
    
    def update_status(self, new_status: MilestoneStatus, completion_date: Optional[datetime] = None) -> None:
        """
        Update the status of this milestone.
        
        Args:
            new_status: The new status to set
            completion_date: Date when milestone was completed (required if status is COMPLETED)
        
        Raises:
            ValueError: If completion_date is None when status is COMPLETED
        """
        if new_status == MilestoneStatus.COMPLETED and completion_date is None:
            raise ValueError("Completion date must be provided when marking milestone as completed")
        
        self.status = new_status
        if new_status == MilestoneStatus.COMPLETED:
            self.completed_date = completion_date
    
    def __str__(self) -> str:
        """Return string representation of the milestone."""
        status_str = self.status.name.replace("_", " ").title()
        date_str = self.target_date.strftime("%Y-%m-%d")
        return f"{self.name} ({date_str}) - {status_str}"


class ProjectRoadmap:
    """Class representing the complete project roadmap."""
    
    def __init__(self, project_name: str):
        """
        Initialize a project roadmap.
        
        Args:
            project_name: Name of the cryptocurrency project
        """
        self.project_name = project_name
        self.milestones: List[Milestone] = []
    
    def add_milestone(self, milestone: Milestone) -> None:
        """Add a milestone to the roadmap."""
        self.milestones.append(milestone)
    
    def get_upcoming_milestones(self, limit: int = 3) -> List[Milestone]:
        """
        Get upcoming milestones sorted by target date.
        
        Args:
            limit: Maximum number of milestones to return
            
        Returns:
            List of upcoming milestones
        """
        now = datetime.now()
        upcoming = [m for m in self.milestones if m.target_date > now and m.status != MilestoneStatus.COMPLETED]
        upcoming.sort(key=lambda m: m.target_date)
        return upcoming[:limit]
    
    def get_completed_milestones(self) -> List[Milestone]:
        """Get all completed milestones."""
        return [m for m in self.milestones if m.status == MilestoneStatus.COMPLETED]
    
    def get_status_report(self) -> Dict[str, float]:
        """
        Generate a status report with completion statistics.
        
        Returns:
            Dictionary containing:
            - total_milestones: Total number of milestones
            - completed: Number of completed milestones
            - completion_percentage: Percentage of milestones completed
        """
        total = len(self.milestones)
        completed = len(self.get_completed_milestones())
        return {
            "total_milestones": total,
            "completed": completed,
            "completion_percentage": (completed / total * 100) if total > 0 else 0
        }
    
    def __str__(self) -> str:
        """Return string representation of the roadmap."""
        report = self.get_status_report()
        lines = [
            f"Project: {self.project_name}",
            f"Milestones: {report['completed']}/{report['total_milestones']} completed ({report['completion_percentage']:.1f}%)",
            "\nUpcoming Milestones:"
        ]
        
        for milestone in self.get_upcoming_milestones():
            lines.append(f"- {milestone}")
        
        return "\n".join(lines)


def create_sample_roadmap() -> ProjectRoadmap:
    """Create a sample cryptocurrency project roadmap similar to Bitcoin Dogs Club."""
    roadmap = ProjectRoadmap("CryptoPaws Project")
    
    # Define milestones with realistic dates
    now = datetime.now()
    
    roadmap.add_milestone(Milestone(
        name="Project Announcement",
        description="Official project launch and whitepaper release",
        target_date=now - timedelta(days=60),
        status=MilestoneStatus.COMPLETED
    ))
    
    roadmap.add_milestone(Milestone(
        name="Community Building",
        description="Establish social media presence and grow community",
        target_date=now - timedelta(days=30),
        status=MilestoneStatus.COMPLETED
    ))
    
    roadmap.add_milestone(Milestone(
        name="NFT Collection Debut",
        description="Launch initial NFT collection with utility features",
        target_date=now + timedelta(days=30)
    ))
    
    roadmap.add_milestone(Milestone(
        name="Token Presale",
        description="Initial token offering for early supporters",
        target_date=now + timedelta(days=45)
    ))
    
    roadmap.add_milestone(Milestone(
        name="Game Beta Launch",
        description="Release playable beta version of the game",
        target_date=now + timedelta(days=90)
    ))
    
    roadmap.add_milestone(Milestone(
        name="Multi-chain Bridge Integration",
        description="Enable cross-chain transfers between Ethereum and Binance Smart Chain",
        target_date=now + timedelta(days=120)
    ))
    
    roadmap.add_milestone(Milestone(
        name="Full Game Release",
        description="Official launch of the complete game with all features",
        target_date=now + timedelta(days=180)
    ))
    
    roadmap.add_milestone(Milestone(
        name="DAO Implementation",
        description="Transition to decentralized governance model",
        target_date=now + timedelta(days=240)
    ))
    
    return roadmap


if __name__ == "__main__":
    # Example usage
    roadmap = create_sample_roadmap()
    print(roadmap)
    
    # Mark some milestones as completed
    try:
        nft_milestone = roadmap.milestones[2]
        nft_milestone.update_status(
            MilestoneStatus.COMPLETED,
            datetime.now() - timedelta(days=5)
        )
    except IndexError:
        print("Error: Milestone not found")
    
    print("\nAfter updating NFT milestone:")
    print(roadmap)
```
