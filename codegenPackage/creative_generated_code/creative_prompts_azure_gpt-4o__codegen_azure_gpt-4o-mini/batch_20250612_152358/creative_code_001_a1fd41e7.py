"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Create a roadmap for a crypto project inspired by Marvin's roadmap, including milestones like utility bot creation, influencer collaborations, tier-one exchange listings, and mobile app development.
Generated: DETERMINISTIC_a1fd41e7fa706a40
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoProjectRoadmap:
    def __init__(self):
        """Initialize the roadmap with an empty list of milestones."""
        self.milestones = []

    def add_milestone(self, title, description, target_date):
        """
        Add a milestone to the roadmap.

        Args:
            title (str): The title of the milestone.
            description (str): A brief description of the milestone.
            target_date (str): The target completion date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the target date is not in correct format.
        """
        if not self.validate_date(target_date):
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
        
        milestone = {
            'title': title,
            'description': description,
            'target_date': target_date,
            'completed': False
        }
        self.milestones.append(milestone)

    def validate_date(self, date_str):
        """Validate the date format."""
        from datetime import datetime
        
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def mark_completed(self, title):
        """
        Mark a milestone as completed.

        Args:
            title (str): The title of the milestone to mark as completed.

        Raises:
            ValueError: If the milestone does not exist.
        """
        for milestone in self.milestones:
            if milestone['title'] == title:
                milestone['completed'] = True
                return
        raise ValueError(f'Milestone "{title}" not found.')

    def show_roadmap(self):
        """Print the current roadmap milestones."""
        for milestone in self.milestones:
            status = "✅ Completed" if milestone['completed'] else "❌ Pending"
            print(f"{milestone['title']} - {status}\n  Description: {milestone['description']}\n  Target Date: {milestone['target_date']}\n")


# Example usage:
if __name__ == "__main__":
    roadmap = CryptoProjectRoadmap()
    
    # Adding milestones to the roadmap
    roadmap.add_milestone(
        "Utility Bot Creation",
        "Develop a bot that provides utility functions for users.",
        "2024-06-01"
    )
    
    roadmap.add_milestone(
        "Influencer Collaborations",
        "Partner with influencers to promote the project.",
        "2024-07-15"
    )

    roadmap.add_milestone(
        "Tier-One Exchange Listings",
        "Secure listings on top-tier cryptocurrency exchanges.",
        "2024-09-30"
    )

    roadmap.add_milestone(
        "Mobile App Development",
        "Develop a mobile application for easier access to project services.",
        "2024-12-15"
    )
    
    # Marking a milestone as completed
    try:
        roadmap.mark_completed("Utility Bot Creation")
    except ValueError as e:
        print(e)

    # Displaying the roadmap
    roadmap.show_roadmap()
```
