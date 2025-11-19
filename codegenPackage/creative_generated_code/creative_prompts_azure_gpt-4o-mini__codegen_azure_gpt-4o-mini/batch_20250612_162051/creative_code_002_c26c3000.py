"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bvitravel.co.uk
Prompt: Create a function that recommends luxury resorts in the British Virgin Islands based on user preferences for activities like diving and watersports.
Generated: DETERMINISTIC_c26c30002e2ef8f0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

# Define a class to represent a luxury resort
class Resort:
    def __init__(self, name: str, activities: List[str], location: str):
        self.name = name
        self.activities = activities
        self.location = location

    def __repr__(self):
        return f"{self.name} located in {self.location}, Activities: {', '.join(self.activities)}"


# Sample data of luxury resorts in the British Virgin Islands
RESORTS = [
    Resort("Rosewood Little Dix Bay", ["diving", "snorkeling", "spa"], "Virgin Gorda"),
    Resort("Bitter End Yacht Club", ["watersports", "sailing", "hiking"], "Virgin Gorda"),
    Resort("Peter Island Resort & Spa", ["diving", "beach", "spa"], "Peter Island"),
    Resort("The Bitter End Yacht Club", ["windsurfing", "kayaking", "fishing"], "North Sound"),
    Resort("Guana Island", ["hiking", "snorkeling", "yoga"], "Guana Island"),
]

def recommend_resorts(preferred_activities: List[str]) -> List[Resort]:
    """
    Recommend luxury resorts based on user preferences for activities.

    :param preferred_activities: A list of activities the user is interested in.
    :return: A list of recommended resorts that match the user's preferences.
    :raises ValueError: If preferred_activities is empty or not a list.
    """
    # Validate input
    if not isinstance(preferred_activities, list) or not preferred_activities:
        raise ValueError("Please provide a non-empty list of preferred activities.")

    # Filter resorts based on user preferences
    recommended = [
        resort for resort in RESORTS 
        if any(activity in resort.activities for activity in preferred_activities)
    ]

    # Handle case where no resorts match the preferences
    if not recommended:
        print("No resorts found matching your preferences.")
    return recommended

# Example usage
if __name__ == "__main__":
    try:
        user_preferences = ["diving", "spa"]  # Example user preferences
        recommendations = recommend_resorts(user_preferences)
        print("Recommended Resorts:")
        for resort in recommendations:
            print(resort)
    except ValueError as e:
        print(f"Error: {e}")
```
