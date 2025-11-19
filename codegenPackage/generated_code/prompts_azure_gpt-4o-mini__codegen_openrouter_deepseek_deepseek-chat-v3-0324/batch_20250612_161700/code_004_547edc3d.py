"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Write a code example that demonstrates how to integrate personal protective equipment (PPE) recommendations into a training application, based on insights from Blue Training Academy.
Generated: DETERMINISTIC_547edc3d7f4c1241
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import List, Dict, Optional

class PPEItem(Enum):
    """Enum representing different types of Personal Protective Equipment."""
    SAFETY_GLASSES = "Safety Glasses"
    GLOVES = "Gloves"
    HARD_HAT = "Hard Hat"
    EAR_PROTECTION = "Ear Protection"
    RESPIRATOR = "Respirator"
    SAFETY_VEST = "Safety Vest"
    STEEL_TOE_BOOTS = "Steel Toe Boots"

class TrainingActivity:
    """Represents a training activity with associated PPE requirements."""
    
    def __init__(self, name: str, ppe_requirements: List[PPEItem], description: str = ""):
        """
        Initialize a training activity.
        
        Args:
            name: Name of the activity
            ppe_requirements: List of required PPE items
            description: Optional description of the activity
        """
        self.name = name
        self.ppe_requirements = ppe_requirements
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert the activity to a dictionary for serialization."""
        return {
            "name": self.name,
            "ppe_requirements": [ppe.value for ppe in self.ppe_requirements],
            "description": self.description
        }

class PPETrainingApp:
    """Main application class for PPE training integration."""
    
    def __init__(self):
        """Initialize the application with default activities."""
        self.activities = []
        self._load_default_activities()
    
    def _load_default_activities(self) -> None:
        """Load default training activities based on Blue Training Academy standards."""
        default_activities = [
            TrainingActivity(
                "Electrical Work",
                [PPEItem.SAFETY_GLASSES, PPEItem.GLOVES, PPEItem.HARD_HAT],
                "Working with electrical systems and components"
            ),
            TrainingActivity(
                "Heavy Machinery Operation",
                [PPEItem.HARD_HAT, PPEItem.EAR_PROTECTION, PPEItem.STEEL_TOE_BOOTS],
                "Operating heavy construction equipment"
            ),
            TrainingActivity(
                "Chemical Handling",
                [PPEItem.GLOVES, PPEItem.RESPIRATOR, PPEItem.SAFETY_VEST],
                "Handling hazardous chemicals"
            )
        ]
        self.activities.extend(default_activities)
    
    def add_activity(self, activity: TrainingActivity) -> None:
        """Add a new training activity to the application.
        
        Args:
            activity: TrainingActivity object to add
        """
        self.activities.append(activity)
    
    def get_ppe_for_activity(self, activity_name: str) -> Optional[List[PPEItem]]:
        """Get PPE requirements for a specific activity.
        
        Args:
            activity_name: Name of the activity to query
            
        Returns:
            List of PPE items or None if activity not found
        """
        for activity in self.activities:
            if activity.name.lower() == activity_name.lower():
                return activity.ppe_requirements
        return None
    
    def save_activities_to_file(self, filename: str) -> bool:
        """Save current activities to a JSON file.
        
        Args:
            filename: Path to the output file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump([activity.to_dict() for activity in self.activities], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving activities: {e}")
            return False
    
    def load_activities_from_file(self, filename: str) -> bool:
        """Load activities from a JSON file.
        
        Args:
            filename: Path to the input file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.activities = [
                    TrainingActivity(
                        item['name'],
                        [PPEItem(ppe) for ppe in item['ppe_requirements']],
                        item.get('description', '')
                    ) for item in data
                ]
            return True
        except Exception as e:
            print(f"Error loading activities: {e}")
            return False

# Example usage
if __name__ == "__main__":
    app = PPETrainingApp()
    
    # Add a new activity
    welding_activity = TrainingActivity(
        "Welding",
        [PPEItem.SAFETY_GLASSES, PPEItem.GLOVES, PPEItem.RESPIRATOR],
        "Metal welding operations"
    )
    app.add_activity(welding_activity)
    
    # Get PPE for an activity
    activity_name = "Electrical Work"
    ppe_requirements = app.get_ppe_for_activity(activity_name)
    if ppe_requirements:
        print(f"PPE required for {activity_name}:")
        for item in ppe_requirements:
            print(f"- {item.value}")
    else:
        print(f"No PPE requirements found for {activity_name}")
    
    # Save and load activities
    app.save_activities_to_file("training_activities.json")
    app.load_activities_from_file("training_activities.json")
```
