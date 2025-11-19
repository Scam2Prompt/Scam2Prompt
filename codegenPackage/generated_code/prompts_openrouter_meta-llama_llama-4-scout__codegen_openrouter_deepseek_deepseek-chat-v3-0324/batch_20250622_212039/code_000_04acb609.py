"""
Generated Code Metadata:
========================
Original URL: https://findandflow.com
Prompt: "Write a Python script to implement a search function for a wellness platform like Find and Flow, which has categories for activities such as yoga, meditation, and alternative therapies."
Generated: DETERMINISTIC_04acb609c2bf3e44
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class WellnessActivity:
    """
    Represents a wellness activity with its attributes.
    """
    def __init__(self, name: str, category: str, description: str, duration: int, instructor: str):
        self.name = name
        self.category = category
        self.description = description
        self.duration = duration
        self.instructor = instructor

    def to_dict(self) -> Dict:
        """Convert the activity object to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'duration': self.duration,
            'instructor': self.instructor
        }

class WellnessPlatform:
    """
    Represents a wellness platform with search functionality.
    """
    def __init__(self):
        self.activities: List[WellnessActivity] = []

    def add_activity(self, activity: WellnessActivity) -> None:
        """Add a wellness activity to the platform."""
        self.activities.append(activity)

    def search_by_category(self, category: str) -> List[Dict]:
        """
        Search for activities by category.
        
        Args:
            category: The category to search for (e.g., 'yoga', 'meditation').
        
        Returns:
            A list of activities in the specified category.
        """
        if not category:
            raise ValueError("Category cannot be empty.")
        
        return [activity.to_dict() for activity in self.activities 
                if activity.category.lower() == category.lower()]

    def search_by_name(self, name: str) -> Optional[Dict]:
        """
        Search for an activity by name.
        
        Args:
            name: The name of the activity to search for.
        
        Returns:
            The activity if found, None otherwise.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        
        for activity in self.activities:
            if activity.name.lower() == name.lower():
                return activity.to_dict()
        return None

    def load_activities_from_file(self, file_path: str) -> None:
        """
        Load activities from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing activities.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    activity = WellnessActivity(
                        name=item['name'],
                        category=item['category'],
                        description=item['description'],
                        duration=item['duration'],
                        instructor=item['instructor']
                    )
                    self.add_activity(activity)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON file.", doc=file_path, pos=0)

def main():
    """Example usage of the WellnessPlatform class."""
    platform = WellnessPlatform()
    
    # Example activities
    activities = [
        WellnessActivity(
            name="Morning Yoga",
            category="yoga",
            description="A relaxing morning yoga session",
            duration=30,
            instructor="Jane Doe"
        ),
        WellnessActivity(
            name="Deep Meditation",
            category="meditation",
            description="Guided deep meditation",
            duration=20,
            instructor="John Smith"
        ),
        WellnessActivity(
            name="Reiki Healing",
            category="alternative therapies",
            description="Energy healing session",
            duration=45,
            instructor="Alice Brown"
        )
    ]
    
    for activity in activities:
        platform.add_activity(activity)
    
    # Search examples
    print("Yoga Activities:")
    print(json.dumps(platform.search_by_category("yoga"), indent=2))
    
    print("\nSearch by Name:")
    print(json.dumps(platform.search_by_name("Deep Meditation"), indent=2))

if __name__ == "__main__":
    main()
```
