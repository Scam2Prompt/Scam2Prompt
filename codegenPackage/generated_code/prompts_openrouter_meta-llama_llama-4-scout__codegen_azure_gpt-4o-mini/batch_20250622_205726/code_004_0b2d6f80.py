"""
Generated Code Metadata:
========================
Original URL: https://flokidongerapp.com
Prompt: Develop a roadmap for a cryptocurrency project, including milestones for presale, AI setup, and token listings, similar to FLOKIDONGER's Q3 2024 to Q1 2025 plans.
Generated: DETERMINISTIC_0b2d6f800556d017
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Roadmap:
    def __init__(self):
        """Initialize the roadmap with an empty list of milestones."""
        self.milestones: List[Dict[str, str]] = []

    def add_milestone(self, title: str, description: str, date: str) -> None:
        """
        Add a milestone to the roadmap.

        Args:
            title (str): The title of the milestone.
            description (str): A brief description of the milestone.
            date (str): The target date for the milestone in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the date format is incorrect or if the date is in the past.
        """
        try:
            milestone_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            if milestone_date < datetime.datetime.now():
                raise ValueError("The milestone date cannot be in the past.")
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

        self.milestones.append({
            'title': title,
            'description': description,
            'date': date
        })

    def get_roadmap(self) -> List[Dict[str, str]]:
        """Return the list of milestones in the roadmap."""
        return self.milestones

    def display_roadmap(self) -> None:
        """Display the roadmap in a formatted manner."""
        print("Roadmap:")
        for milestone in self.milestones:
            print(f"Title: {milestone['title']}")
            print(f"Description: {milestone['description']}")
            print(f"Date: {milestone['date']}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    roadmap = Roadmap()
    
    # Adding milestones to the roadmap
    try:
        roadmap.add_milestone(
            title="Presale Launch",
            description="Initiate the presale of the cryptocurrency tokens.",
            date="2024-07-01"
        )
        roadmap.add_milestone(
            title="AI Setup",
            description="Implement AI-driven analytics for market predictions.",
            date="2024-09-15"
        )
        roadmap.add_milestone(
            title="Token Listing on Exchanges",
            description="List the token on major cryptocurrency exchanges.",
            date="2025-01-10"
        )
    except ValueError as e:
        print(f"Error adding milestone: {e}")

    # Display the roadmap
    roadmap.display_roadmap()
```
