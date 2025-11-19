"""
Generated Code Metadata:
========================
Original URL: https://lensamaluku.com
Prompt: Create a detailed overview of the community activities during Idul Adha in Buru Selatan, including the distribution of sacrificial meat and the involvement of local authorities.
Generated: DETERMINISTIC_4820e42198082a33
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CommunityActivity:
    """
    A class to represent community activities during Idul Adha in Buru Selatan.
    """

    def __init__(self, activity_name, description, participants):
        """
        Initialize the CommunityActivity object.

        :param activity_name: Name of the activity
        :param description: Description of the activity
        :param participants: List of participants involved in the activity
        """
        self.activity_name = activity_name
        self.description = description
        self.participants = participants

    def to_dict(self):
        """
        Convert the CommunityActivity object to a dictionary.

        :return: Dictionary representation of the activity
        """
        return {
            "activity_name": self.activity_name,
            "description": self.description,
            "participants": self.participants
        }


class IdulAdhaOverview:
    """
    A class to represent the detailed overview of Idul Adha activities in Buru Selatan.
    """

    def __init__(self):
        """
        Initialize the IdulAdhaOverview object with an empty list of activities.
        """
        self.activities = []

    def add_activity(self, activity):
        """
        Add a community activity to the overview.

        :param activity: CommunityActivity object to be added
        """
        if not isinstance(activity, CommunityActivity):
            raise TypeError("activity must be an instance of CommunityActivity")
        self.activities.append(activity)

    def generate_report(self):
        """
        Generate a detailed report of all activities.

        :return: JSON string containing the report
        """
        report = {
            "region": "Buru Selatan",
            "event": "Idul Adha",
            "activities": [activity.to_dict() for activity in self.activities]
        }
        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Create an overview object
        idul_adha_overview = IdulAdhaOverview()

        # Add activities
        idul_adha_overview.add_activity(
            CommunityActivity(
                activity_name="Sacrificial Meat Distribution",
                description="Distribution of sacrificial meat to the local community, including underprivileged families.",
                participants=["Local Authorities", "Community Leaders", "Volunteers"]
            )
        )

        idul_adha_overview.add_activity(
            CommunityActivity(
                activity_name="Prayer Gathering",
                description="Organized prayer gathering at the central mosque.",
                participants=["Religious Leaders", "Community Members"]
            )
        )

        idul_adha_overview.add_activity(
            CommunityActivity(
                activity_name="Community Feast",
                description="A communal feast to celebrate Idul Adha, fostering unity and togetherness.",
                participants=["Families", "Local Authorities", "Visitors"]
            )
        )

        # Generate and print the report
        report = idul_adha_overview.generate_report()
        print(report)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
