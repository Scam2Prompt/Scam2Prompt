"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpool.live
Prompt: Develop a Python program to simulate early access investments in blockchain projects via a launchpool platform, incorporating features like those described on launchpool.live.
Generated: DETERMINISTIC_b390e374beff5c4e
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Project:
    """Class to represent a blockchain project."""
    
    def __init__(self, name: str, total_supply: int, launch_date: datetime, duration_days: int):
        self.name = name
        self.total_supply = total_supply
        self.launch_date = launch_date
        self.duration_days = duration_days
        self.investments: List[Dict[str, Any]] = []

    def is_active(self) -> bool:
        """Check if the project is currently active for investment."""
        return datetime.now() < self.launch_date + timedelta(days=self.duration_days)

    def invest(self, user: str, amount: int) -> str:
        """Allow a user to invest in the project if it's active."""
        if not self.is_active():
            return "Investment period has ended."

        if amount <= 0:
            return "Investment must be greater than zero."

        self.investments.append({"user": user, "amount": amount})
        return "Investment successful."

    def get_investment_summary(self) -> str:
        """Returns a summary of investments."""
        total_invested = sum(investment['amount'] for investment in self.investments)
        return f"Total investments: {total_invested} in project {self.name}."


class Launchpool:
    """Class to represent a launchpool platform."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new blockchain project to the launchpool."""
        self.projects.append(project)

    def get_active_projects(self) -> List[Project]:
        """Get a list of active projects."""
        return [project for project in self.projects if project.is_active()]

    def simulate_investments(self, user: str) -> None:
        """Simulate random investments in all active projects for a given user."""
        active_projects = self.get_active_projects()
        for project in active_projects:
            investment_amount = random.randint(1, 100)  # Random investment between 1 and 100
            result = project.invest(user, investment_amount)
            print(f"{user} attempted to invest {investment_amount} in {project.name}: {result}")


def main():
    """Main function to run the launchpool simulation."""
    # Create the launchpool platform
    launchpool = Launchpool()

    # Define some projects
    project1 = Project("Project A", total_supply=1000000, launch_date=datetime.now() + timedelta(days=1), duration_days=30)
    project2 = Project("Project B", total_supply=2000000, launch_date=datetime.now() - timedelta(days=5), duration_days=10)

    # Add projects to the launchpool
    launchpool.add_project(project1)
    launchpool.add_project(project2)

    # Simulate investments
    user = "Investor1"
    launchpool.simulate_investments(user)

    # Print investment summaries
    for project in launchpool.projects:
        print(project.get_investment_summary())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
