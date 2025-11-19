"""
Generated Code Metadata:
========================
Original URL: https://metamash.co
Prompt: Create a Python script to map client requirements and build a strategic growth plan, inspired by Metamash's theoretical structure and timeframes.
Generated: DETERMINISTIC_00ad2cde951f3f57
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Client Growth Strategy Mapper
Inspired by Metamash's theoretical structure and timeframes.

This script helps map client requirements and build a strategic growth plan
with defined timeframes and milestones.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class GrowthPlanBuilder:
    """
    A class to build and manage strategic growth plans for clients.
    """

    def __init__(self, client_name: str, start_date: str = None):
        """
        Initialize the GrowthPlanBuilder with client details.

        Args:
            client_name: Name of the client
            start_date: Start date in YYYY-MM-DD format (default: today)
        """
        self.client_name = client_name
        self.start_date = datetime.now().date() if not start_date else datetime.strptime(start_date, "%Y-%m-%d").date()
        self.requirements: List[Dict] = []
        self.milestones: List[Dict] = []
        self.timeframes: Dict[str, Tuple[datetime, datetime]] = {}

    def add_requirement(self, description: str, priority: str, category: str) -> None:
        """
        Add a client requirement to the growth plan.

        Args:
            description: Description of the requirement
            priority: Priority level (high/medium/low)
            category: Category of requirement (e.g., technical, marketing)
        """
        if priority.lower() not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")

        self.requirements.append({
            "description": description,
            "priority": priority.lower(),
            "category": category,
            "added_date": datetime.now().date().isoformat()
        })

    def add_milestone(self, name: str, description: str, timeframe_days: int) -> None:
        """
        Add a milestone to the growth plan.

        Args:
            name: Name of the milestone
            description: Description of the milestone
            timeframe_days: Days from start date to complete this milestone
        """
        if timeframe_days < 0:
            raise ValueError("Timeframe cannot be negative")

        start_date = self.start_date
        end_date = start_date + timedelta(days=timeframe_days)

        self.milestones.append({
            "name": name,
            "description": description,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "status": "planned"
        })

        self.timeframes[name] = (start_date, end_date)

    def update_milestone_status(self, milestone_name: str, status: str) -> None:
        """
        Update the status of a milestone.

        Args:
            milestone_name: Name of the milestone to update
            status: New status (planned/in-progress/completed/delayed)
        """
        valid_statuses = ["planned", "in-progress", "completed", "delayed"]
        if status.lower() not in valid_statuses:
            raise ValueError(f"Status must be one of: {valid_statuses}")

        for milestone in self.milestones:
            if milestone["name"] == milestone_name:
                milestone["status"] = status.lower()
                return

        raise ValueError(f"Milestone '{milestone_name}' not found")

    def get_plan_summary(self) -> Dict:
        """
        Get a summary of the growth plan.

        Returns:
            Dictionary containing plan summary
        """
        return {
            "client": self.client_name,
            "start_date": self.start_date.isoformat(),
            "requirements_count": len(self.requirements),
            "milestones_count": len(self.milestones),
            "high_priority_requirements": len(
                [r for r in self.requirements if r["priority"] == "high"]
            ),
            "completed_milestones": len(
                [m for m in self.milestones if m["status"] == "completed"]
            )
        }

    def save_plan_to_file(self, filename: str) -> None:
        """
        Save the growth plan to a JSON file.

        Args:
            filename: Name of the file to save to
        """
        plan_data = {
            "client": self.client_name,
            "start_date": self.start_date.isoformat(),
            "requirements": self.requirements,
            "milestones": self.milestones
        }

        with open(filename, 'w') as f:
            json.dump(plan_data, f, indent=4)

    @classmethod
    def load_plan_from_file(cls, filename: str) -> 'GrowthPlanBuilder':
        """
        Load a growth plan from a JSON file.

        Args:
            filename: Name of the file to load from

        Returns:
            GrowthPlanBuilder instance with loaded data
        """
        with open(filename, 'r') as f:
            plan_data = json.load(f)

        builder = cls(plan_data["client"], plan_data["start_date"])
        builder.requirements = plan_data["requirements"]
        builder.milestones = plan_data["milestones"]

        # Rebuild timeframes dictionary
        for milestone in builder.milestones:
            builder.timeframes[milestone["name"]] = (
                datetime.strptime(milestone["start_date"], "%Y-%m-%d").date(),
                datetime.strptime(milestone["end_date"], "%Y-%m-%d").date()
            )

        return builder


def main():
    """Example usage of the GrowthPlanBuilder."""
    try:
        # Create a new growth plan
        plan = GrowthPlanBuilder("Acme Corp", "2023-01-01")

        # Add requirements
        plan.add_requirement(
            "Implement new CRM system",
            "high",
            "technical"
        )
        plan.add_requirement(
            "Increase social media presence",
            "medium",
            "marketing"
        )

        # Add milestones
        plan.add_milestone(
            "CRM Implementation",
            "Complete CRM system setup and training",
            30
        )
        plan.add_milestone(
            "Marketing Campaign",
            "Launch new marketing campaign",
            60
        )

        # Update milestone status
        plan.update_milestone_status("CRM Implementation", "completed")

        # Save and load plan
        plan.save_plan_to_file("acme_growth_plan.json")
        loaded_plan = GrowthPlanBuilder.load_plan_from_file("acme_growth_plan.json")

        # Print summary
        print(json.dumps(loaded_plan.get_plan_summary(), indent=2))

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
