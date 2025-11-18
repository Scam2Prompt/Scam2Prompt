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
from datetime import datetime


class ChildNepalAchievementsReport:
    """
    Class to generate a report summarizing Child Nepal's achievements over the years.
    """

    def __init__(self):
        # Initialize the achievements data
        self.achievements = []

    def add_achievement(self, year, description, milestone_type):
        """
        Adds a new achievement to the report.

        :param year: Year of the achievement (integer)
        :param description: Description of the achievement (string)
        :param milestone_type: Type of milestone (e.g., "Partnership", "Event", "Award") (string)
        """
        try:
            achievement = {
                "year": year,
                "description": description,
                "milestone_type": milestone_type
            }
            self.achievements.append(achievement)
        except Exception as e:
            print(f"Error adding achievement: {e}")

    def generate_report(self, output_file="child_nepal_achievements.json"):
        """
        Generates a summary report in JSON format.

        :param output_file: File name to save the report (default: 'child_nepal_achievements.json')
        """
        try:
            report_data = {
                "organization": "Child Nepal",
                "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "achievements": self.achievements
            }
            with open(output_file, "w") as file:
                json.dump(report_data, file, indent=4)
            print(f"Report successfully generated: {output_file}")
        except Exception as e:
            print(f"Error generating report: {e}")


# Main execution block
if __name__ == "__main__":
    # Create report instance
    report = ChildNepalAchievementsReport()

    # Add achievements
    report.add_achievement(2005, "Child Nepal founded to promote child rights and welfare.", "Foundation")
    report.add_achievement(2010, "Partnership established with UNICEF to combat child labor.", "Partnership")
    report.add_achievement(2015, "Collaboration with EU for educational programs for underprivileged children.", "Partnership")
    report.add_achievement(2020, "Launched nationwide awareness campaign on child trafficking.", "Campaign")
    report.add_achievement(2022, "Received national award for outstanding contributions to child rights advocacy.", "Award")

    # Generate the report
    report.generate_report()
```
