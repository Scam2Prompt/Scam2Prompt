"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write a program to measure the success of a grants program using key results and indicators, as outlined in Gitcoin's Playbook.
Generated: DETERMINISTIC_8d5ca06cc5c600ba
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grant Success Measurement Tool

This program measures the success of a grants program using key results and indicators
as outlined in Gitcoin's Playbook. It tracks metrics like funds disbursed, projects funded,
community engagement, and impact metrics.

Key Features:
- Tracks financial metrics (funds raised, disbursed)
- Measures project success (number funded, completion rate)
- Evaluates community engagement (contributors, voters)
- Calculates impact metrics (lives impacted, carbon reduced)
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
import csv
import statistics

@dataclass
class Grant:
    """Represents a single grant in the program."""
    id: str
    name: str
    funding_received: float
    funding_goal: float
    completion_status: str  # "planned", "in_progress", "completed", "failed"
    impact_metrics: Dict[str, float]  # e.g., {"lives_impacted": 1000, "carbon_reduced": 500}
    date_awarded: datetime
    date_completed: Optional[datetime] = None

@dataclass
class GrantRound:
    """Represents a funding round with multiple grants."""
    id: str
    name: str
    start_date: datetime
    end_date: datetime
    total_funding: float
    grants: List[Grant]

class GrantsProgram:
    """Main class to manage and analyze grants program metrics."""
    
    def __init__(self, program_name: str):
        self.program_name = program_name
        self.rounds: List[GrantRound] = []
        self.community_metrics = {
            "total_contributors": 0,
            "unique_voters": 0,
            "total_votes": 0
        }
    
    def add_round(self, grant_round: GrantRound) -> None:
        """Add a funding round to the program."""
        self.rounds.append(grant_round)
    
    def update_community_metrics(self, contributors: int, voters: int, votes: int) -> None:
        """Update community engagement metrics."""
        self.community_metrics["total_contributors"] += contributors
        self.community_metrics["unique_voters"] += voters
        self.community_metrics["total_votes"] += votes
    
    def calculate_financial_metrics(self) -> Dict[str, float]:
        """Calculate financial metrics across all rounds."""
        total_funds_raised = sum(r.total_funding for r in self.rounds)
        total_funds_disbursed = sum(
            sum(g.funding_received for g in r.grants)
            for r in self.rounds
        )
        average_grant_size = statistics.mean(
            [g.funding_received for r in self.rounds for g in r.grants]
        ) if any(r.grants for r in self.rounds) else 0
        
        return {
            "total_funds_raised": total_funds_raised,
            "total_funds_disbursed": total_funds_disbursed,
            "funds_utilization_percentage": (total_funds_disbursed / total_funds_raised * 100) if total_funds_raised > 0 else 0,
            "average_grant_size": average_grant_size
        }
    
    def calculate_project_metrics(self) -> Dict[str, float]:
        """Calculate project success metrics."""
        all_grants = [g for r in self.rounds for g in r.grants]
        completed_grants = [g for g in all_grants if g.completion_status == "completed"]
        success_rate = (len(completed_grants) / len(all_grants)) * 100 if all_grants else 0
        
        return {
            "total_projects_funded": len(all_grants),
            "projects_completed": len(completed_grants),
            "completion_rate": success_rate,
            "average_funding_goal_met": statistics.mean(
                [g.funding_received / g.funding_goal for g in all_grants if g.funding_goal > 0]
            ) if any(g.funding_goal > 0 for g in all_grants) else 0
        }
    
    def calculate_impact_metrics(self) -> Dict[str, float]:
        """Calculate aggregate impact metrics across all grants."""
        all_grants = [g for r in self.rounds for g in r.grants]
        impact_metrics = {}
        
        if not all_grants:
            return impact_metrics
        
        # Sum all impact metrics across grants
        for grant in all_grants:
            for metric, value in grant.impact_metrics.items():
                if metric in impact_metrics:
                    impact_metrics[metric] += value
                else:
                    impact_metrics[metric] = value
        
        # Calculate averages where applicable
        impact_metrics["average_lives_impacted_per_grant"] = (
            impact_metrics.get("lives_impacted", 0) / len(all_grants)
        ) if "lives_impacted" in impact_metrics else 0
        
        return impact_metrics
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report of all metrics."""
        return {
            "program_name": self.program_name,
            "financial_metrics": self.calculate_financial_metrics(),
            "project_metrics": self.calculate_project_metrics(),
            "community_metrics": self.community_metrics,
            "impact_metrics": self.calculate_impact_metrics(),
            "total_rounds": len(self.rounds),
            "last_updated": datetime.now().isoformat()
        }
    
    def save_report_to_json(self, filename: str) -> None:
        """Save the report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
    
    def save_report_to_csv(self, filename: str) -> None:
        """Save the report to a CSV file."""
        report = self.generate_report()
        flattened_data = []
        
        # Flatten the nested structure
        for category, metrics in report.items():
            if isinstance(metrics, dict):
                for metric, value in metrics.items():
                    flattened_data.append({
                        "category": category,
                        "metric": metric,
                        "value": value
                    })
            else:
                flattened_data.append({
                    "category": "program",
                    "metric": category,
                    "value": metrics
                })
        
        # Write to CSV
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["category", "metric", "value"])
            writer.writeheader()
            writer.writerows(flattened_data)

# Example usage
if __name__ == "__main__":
    # Create a grants program
    program = GrantsProgram("Climate Change Solutions Fund")
    
    # Add some rounds
    round1 = GrantRound(
        id="R1",
        name="Spring 2023 Round",
        start_date=datetime(2023, 3, 1),
        end_date=datetime(2023, 5, 31),
        total_funding=1000000,
        grants=[
            Grant(
                id="G1",
                name="Solar Panel Initiative",
                funding_received=250000,
                funding_goal=300000,
                completion_status="completed",
                impact_metrics={"lives_impacted": 5000, "carbon_reduced": 10000},
                date_awarded=datetime(2023, 4, 1),
                date_completed=datetime(2023, 10, 15)
            ),
            Grant(
                id="G2",
                name="Urban Farming Project",
                funding_received=150000,
                funding_goal=150000,
                completion_status="in_progress",
                impact_metrics={"lives_impacted": 2000, "carbon_reduced": 3000},
                date_awarded=datetime(2023, 4, 1)
            )
        ]
    )
    
    program.add_round(round1)
    
    # Update community metrics
    program.update_community_metrics(contributors=1500, voters=5000, votes=25000)
    
    # Generate and save reports
    program.save_report_to_json("grants_report.json")
    program.save_report_to_csv("grants_report.csv")
```
