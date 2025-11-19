"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Generate a Python function that implements a cognitive behavioral therapy technique for managing anxiety disorders, as discussed on the Psikoloji Bakırköy website.
Generated: DETERMINISTIC_ac96456ed4d3a6d0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class CBTTool:
    """
    A cognitive behavioral therapy (CBT) tool for managing anxiety disorders.
    Implements techniques such as thought recording, cognitive restructuring,
    and exposure planning.
    """

    def __init__(self, user_data_file="user_data.json"):
        """
        Initialize the CBT tool with a data file for persistence.
        
        Args:
            user_data_file (str): Path to JSON file for storing user data.
        """
        self.user_data_file = user_data_file
        self.user_data = self._load_user_data()

    def _load_user_data(self):
        """
        Load user data from JSON file or initialize if file doesn't exist.
        
        Returns:
            dict: User data dictionary
        """
        try:
            with open(self.user_data_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "thought_records": [],
                "exposure_hierarchy": [],
                "relaxation_exercises": []
            }

    def _save_user_data(self):
        """
        Save user data to JSON file.
        """
        with open(self.user_data_file, 'w') as f:
            json.dump(self.user_data, f, indent=2)

    def record_thought(self, situation, automatic_thought, emotion, intensity):
        """
        Record a cognitive thought record.
        
        Args:
            situation (str): The triggering situation
            automatic_thought (str): The automatic negative thought
            emotion (str): The primary emotion experienced
            intensity (int): Emotion intensity (1-10 scale)
            
        Returns:
            dict: The recorded thought entry
        """
        if not 1 <= intensity <= 10:
            raise ValueError("Intensity must be between 1 and 10")

        entry = {
            "timestamp": datetime.now().isoformat(),
            "situation": situation,
            "automatic_thought": automatic_thought,
            "emotion": emotion,
            "intensity": intensity,
            "alternative_thought": None,
            "rational_response": None,
            "outcome": None
        }

        self.user_data["thought_records"].append(entry)
        self._save_user_data()
        return entry

    def restructure_thought(self, record_id, alternative_thought, rational_response, outcome):
        """
        Complete cognitive restructuring for a recorded thought.
        
        Args:
            record_id (int): Index of the thought record to update
            alternative_thought (str): Balanced alternative thought
            rational_response (str): Rational counter to automatic thought
            outcome (str): Description of emotional outcome
            
        Returns:
            dict: The updated thought record
        """
        try:
            record = self.user_data["thought_records"][record_id]
        except IndexError:
            raise ValueError("Invalid thought record ID")

        record.update({
            "alternative_thought": alternative_thought,
            "rational_response": rational_response,
            "outcome": outcome
        })

        self._save_user_data()
        return record

    def add_exposure_item(self, description, fear_level):
        """
        Add an item to the exposure hierarchy.
        
        Args:
            description (str): Description of feared situation
            fear_level (int): Fear level (1-10 scale)
            
        Returns:
            dict: The added exposure item
        """
        if not 1 <= fear_level <= 10:
            raise ValueError("Fear level must be between 1 and 10")

        item = {
            "description": description,
            "fear_level": fear_level,
            "completed": False,
            "notes": ""
        }

        self.user_data["exposure_hierarchy"].append(item)
        self._save_user_data()
        return item

    def complete_exposure_item(self, item_id, notes=""):
        """
        Mark an exposure hierarchy item as completed.
        
        Args:
            item_id (int): Index of the exposure item
            notes (str): Optional notes about the experience
            
        Returns:
            dict: The updated exposure item
        """
        try:
            item = self.user_data["exposure_hierarchy"][item_id]
        except IndexError:
            raise ValueError("Invalid exposure item ID")

        item.update({
            "completed": True,
            "notes": notes
        })

        self._save_user_data()
        return item

    def add_relaxation_exercise(self, technique, duration_minutes, notes=""):
        """
        Record a relaxation exercise session.
        
        Args:
            technique (str): Relaxation technique used
            duration_minutes (int): Duration in minutes
            notes (str): Optional notes about the session
            
        Returns:
            dict: The recorded exercise
        """
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")

        exercise = {
            "timestamp": datetime.now().isoformat(),
            "technique": technique,
            "duration_minutes": duration_minutes,
            "notes": notes
        }

        self.user_data["relaxation_exercises"].append(exercise)
        self._save_user_data()
        return exercise

    def get_thought_records(self):
        """Return all thought records."""
        return self.user_data["thought_records"]

    def get_exposure_hierarchy(self):
        """Return exposure hierarchy items, sorted by fear level."""
        return sorted(
            self.user_data["exposure_hierarchy"],
            key=lambda x: x["fear_level"],
            reverse=True
        )

    def get_relaxation_exercises(self):
        """Return all relaxation exercises."""
        return self.user_data["relaxation_exercises"]
```
