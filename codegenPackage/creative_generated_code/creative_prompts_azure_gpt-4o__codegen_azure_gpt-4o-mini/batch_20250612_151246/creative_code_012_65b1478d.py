"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Develop a roadmap tracker for a blockchain project, including stages like smart contract audits, alpha testing, and marketplace launch, similar to Pushd's roadmap.
Generated: DETERMINISTIC_65b1478d28378d1b
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# roadmap_tracker.py

from datetime import datetime
from typing import List, Dict, Optional

class RoadmapStage:
    """Represents a stage in the roadmap with a name, description, and dates."""

    def __init__(self, name: str, description: str, start_date: str, end_date: str):
        """
        Initialize a new roadmap stage.
        
        :param name: Name of the stage.
        :param description: Description of the stage.
        :param start_date: Start date of the stage (YYYY-MM-DD).
        :param end_date: End date of the stage (YYYY-MM-DD).
        """
        self.name = name
        self.description = description
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """Parse a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is YYYY-MM-DD.") from e

    def is_completed(self) -> bool:
        """Check if the stage is completed based on the current date."""
        return datetime.now() > self.end_date

    def to_dict(self) -> Dict:
        """Convert the stage to a dictionary representation."""
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "completed": self.is_completed()
        }


class Roadmap:
    """Represents a roadmap containing multiple stages."""

    def __init__(self):
        """Initialize a new roadmap with no stages."""
        self.stages: List[RoadmapStage] = []

    def add_stage(self, stage: RoadmapStage) -> None:
        """Add a stage to the roadmap.
        
        :param stage: The RoadmapStage to add.
        """
        self.stages.append(stage)

    def get_stages(self) -> List[Dict]:
        """Get all stages in the roadmap as a list of dictionaries."""
        return [stage.to_dict() for stage in self.stages]

    def get_completed_stages(self) -> List[Dict]:
        """Get all completed stages in the roadmap."""
        return [stage.to_dict() for stage in self.stages if stage.is_completed()]

    def get_upcoming_stages(self) -> List[Dict]:
        """Get all upcoming stages in the roadmap."""
        return [stage.to_dict() for stage in self.stages if not stage.is_completed()]


if __name__ == "__main__":
    # Example of creating a roadmap tracker
    roadmap = Roadmap()

    # Adding stages to the roadmap
    roadmap.add_stage(RoadmapStage("Smart Contract Audit", "Conduct thorough audits of all smart contracts.", "2023-01-15", "2023-02-15"))
    roadmap.add_stage(RoadmapStage("Alpha Testing", "Release alpha version for internal testing.", "2023-03-01", "2023-03-15"))
    roadmap.add_stage(RoadmapStage("Marketplace Launch", "Launch the marketplace for public access.", "2023-04-01", "2023-04-30"))

    # Outputting the roadmap stages
    print("All Stages:")
    print(roadmap.get_stages())

    print("\nCompleted Stages:")
    print(roadmap.get_completed_stages())

    print("\nUpcoming Stages:")
    print(roadmap.get_upcoming_stages())
```
