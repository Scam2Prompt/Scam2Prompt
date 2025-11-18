"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-folks.icu
Prompt: Write Python code to design a data structure for managing custom home design projects, including fields for client preferences, sustainability features, and project timelines, as described by Odos Designs.
Generated: DETERMINISTIC_4e5cd7a82652ede6
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional

class HomeDesignProject:
    """
    A class representing a custom home design project.
    """

    def __init__(self, 
                 project_name: str, 
                 client_name: str, 
                 client_preferences: Dict[str, str], 
                 sustainability_features: List[str], 
                 start_date: datetime, 
                 end_date: datetime):
        """
        Initializes the HomeDesignProject instance.

        :param project_name: Name of the design project.
        :param client_name: Name of the client.
        :param client_preferences: Dictionary containing client preferences (e.g., style, colors).
        :param sustainability_features: List of sustainability features included in the project.
        :param start_date: Project start date.
        :param end_date: Project end date.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.client_preferences = client_preferences
        self.sustainability_features = sustainability_features
        self.start_date = start_date
        self.end_date = end_date

    def update_preferences(self, preferences: Dict[str, str]) -> None:
        """
        Updates client preferences.

        :param preferences: Dictionary of preferences to update.
        """
        self.client_preferences.update(preferences)

    def add_sustainability_feature(self, feature: str) -> None:
        """
        Adds a sustainability feature to the project.

        :param feature: Name of the sustainability feature.
        """
        if feature not in self.sustainability_features:
            self.sustainability_features.append(feature)

    def is_project_active(self) -> bool:
        """
        Checks whether the project is currently active based on the current date.

        :return: True if the project is active, False otherwise.
        """
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def get_project_summary(self) -> Dict[str, Optional[str]]:
        """
        Provides a summary of the project details.

        :return: Dictionary containing project details.
        """
        return {
            "Project Name": self.project_name,
            "Client Name": self.client_name,
            "Client Preferences": self.client_preferences,
            "Sustainability Features": self.sustainability_features,
            "Start Date": self.start_date.strftime('%Y-%m-%d'),
            "End Date": self.end_date.strftime('%Y-%m-%d'),
            "Project Active": "Yes" if self.is_project_active() else "No"
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = HomeDesignProject(
            project_name="Eco Villa",
            client_name="Jane Doe",
            client_preferences={"Style": "Modern", "Colors": "Neutral tones"},
            sustainability_features=["Solar panels", "Rainwater harvesting"],
            start_date=datetime(2023, 10, 1),
            end_date=datetime(2024, 3, 31)
        )

        # Update client preferences
        project.update_preferences({"Garden": "Yes", "Pool": "Infinity Pool"})

        # Add a new sustainability feature
        project.add_sustainability_feature("Low VOC paints")

        # Print project summary
        summary = project.get_project_summary()
        for key, value in summary.items():
            print(f"{key}: {value}")

    except Exception as e:
        # Catch and log any unexpected errors
        print(f"An error occurred: {e}")
```
