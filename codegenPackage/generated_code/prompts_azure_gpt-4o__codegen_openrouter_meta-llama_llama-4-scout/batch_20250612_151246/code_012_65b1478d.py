"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Develop a roadmap tracker for a blockchain project, including stages like smart contract audits, alpha testing, and marketplace launch, similar to Pushd's roadmap.
Generated: DETERMINISTIC_65b1478d28378d1b
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List

class RoadmapStage(str, Enum):
    """Enum representing the different stages of the roadmap."""
    SMART_CONTRACT_AUDIT = "Smart Contract Audit"
    ALPHA_TESTING = "Alpha Testing"
    BETA_TESTING = "Beta Testing"
    MARKETPLACE_LAUNCH = "Marketplace Launch"
    FULL_LAUNCH = "Full Launch"

class RoadmapTracker:
    """Class responsible for tracking the roadmap stages."""

    def __init__(self):
        """Initialize the roadmap tracker."""
        self.stages = {}

    def add_stage(self, stage: RoadmapStage, start_date: datetime, end_date: datetime):
        """
        Add a new stage to the roadmap.

        Args:
        - stage (RoadmapStage): The stage to add.
        - start_date (datetime): The start date of the stage.
        - end_date (datetime): The end date of the stage.
        """
        if stage in self.stages:
            raise ValueError(f"Stage {stage} already exists.")

        self.stages[stage] = {
            "start_date": start_date,
            "end_date": end_date,
            "status": "Not Started"
        }

    def update_stage_status(self, stage: RoadmapStage, status: str):
        """
        Update the status of a stage.

        Args:
        - stage (RoadmapStage): The stage to update.
        - status (str): The new status of the stage.
        """
        if stage not in self.stages:
            raise ValueError(f"Stage {stage} does not exist.")

        self.stages[stage]["status"] = status

    def get_stage(self, stage: RoadmapStage):
        """
        Get the details of a stage.

        Args:
        - stage (RoadmapStage): The stage to get.

        Returns:
        - dict: The details of the stage.
        """
        if stage not in self.stages:
            raise ValueError(f"Stage {stage} does not exist.")

        return self.stages[stage]

    def get_all_stages(self):
        """
        Get all stages.

        Returns:
        - dict: All stages.
        """
        return self.stages


def main():
    tracker = RoadmapTracker()

    # Add stages
    tracker.add_stage(
        RoadmapStage.SMART_CONTRACT_AUDIT,
        datetime(2024, 9, 1),
        datetime(2024, 9, 30)
    )
    tracker.add_stage(
        RoadmapStage.ALPHA_TESTING,
        datetime(2024, 10, 1),
        datetime(2024, 10, 31)
    )
    tracker.add_stage(
        RoadmapStage.MARKETPLACE_LAUNCH,
        datetime(2024, 11, 1),
        datetime(2024, 11, 30)
    )

    # Update stage status
    tracker.update_stage_status(RoadmapStage.SMART_CONTRACT_AUDIT, "In Progress")

    # Get stage details
    print(tracker.get_stage(RoadmapStage.SMART_CONTRACT_AUDIT))

    # Get all stages
    print(tracker.get_all_stages())


if __name__ == "__main__":
    main()
```
