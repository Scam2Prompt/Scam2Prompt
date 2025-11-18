"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Write code to generate a report summarizing Child Nepal's achievements over the years, including key milestones like partnerships with UNICEF and EU, using Python.
Generated: DETERMINISTIC_d6b353dcd8eb9446
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict

class Achievement:
    """A class to represent an achievement with a description and date."""
    
    def __init__(self, description: str, date: str):
        """
        Initialize an Achievement instance.
        
        Parameters:
            description (str): A description of the achievement.
            date (str): The date of the achievement in YYYY-MM-DD format.
        """
        self.description = description
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        
    def to_dict(self) -> Dict:
        """Convert the Achievement instance to a dictionary."""
        return {
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d"),
        }

class Report:
    """A class to generate a report summarizing achievements."""
    
    def __init__(self, title: str):
        """
        Initialize a Report instance.
        
        Parameters:
            title (str): The title of the report.
        """
        self.title = title
        self.achievements: List[Achievement] = []

    def add_achievement(self, achievement: Achievement):
        """Add an achievement to the report."""
        self.achievements.append(achievement)

    def generate_summary(self) -> Dict:
        """Generate a summary of the report."""
        return {
            "title": self.title,
            "achievements": [achievement.to_dict() for achievement in self.achievements]
        }

    def save_to_file(self, filename: str):
        """Save the report summary to a JSON file."""
        report_summary = self.generate_summary()
        try:
            with open(filename, 'w') as file:
                json.dump(report_summary, file, indent=4)
            print(f"Report saved successfully to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving the report: {e}")

def main():
    """Main function to create and save the report."""
    # Initialize the report
    report = Report(title="Child Nepal Achievements Report")

    # Add key milestones
    milestones = [
        Achievement(description="Partnership with UNICEF established.", date="2015-03-10"),
        Achievement(description="Collaboration with the EU for education programs.", date="2018-06-05"),
        Achievement(description="Launched a health awareness campaign.", date="2020-09-15"),
        Achievement(description="Expanded community outreach programs.", date="2021-11-20"),
    ]

    for milestone in milestones:
        report.add_achievement(milestone)

    # Save the report to a JSON file
    report.save_to_file("child_nepal_achievements_report.json")

if __name__ == "__main__":
    main()
```
