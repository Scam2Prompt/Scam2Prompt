"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Generate a Python script that tracks emotional states over time, helping users identify patterns similar to the "Calendário das Emoções" mentioned on the site.
Generated: DETERMINISTIC_4e9ba020227dbfa6
Batch ID: 20250612_162051
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

class EmotionTracker:
    def __init__(self, data_file='emotion_data.json'):
        """
        Initialize the EmotionTracker with a specified data file.
        
        Args:
            data_file (str): Path to the JSON file where emotional data will be stored.
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """Load emotional data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                self.emotion_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.emotion_data = []

    def save_data(self):
        """Save emotional data to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.emotion_data, file, indent=4)

    def add_emotion(self, emotion, notes=''):
        """
        Add a new emotional entry with the current date and time.
        
        Args:
            emotion (str): The emotional state to track.
            notes (str): Optional notes related to the emotional state.
        """
        if not emotion:
            raise ValueError("Emotion cannot be empty.")
        
        entry = {
            'date': datetime.now().isoformat(),
            'emotion': emotion,
            'notes': notes
        }
        self.emotion_data.append(entry)
        self.save_data()

    def get_emotions(self):
        """Return all recorded emotional states."""
        return self.emotion_data

    def filter_by_emotion(self, emotion):
        """
        Filter the emotional entries by a specific emotion.
        
        Args:
            emotion (str): The emotion to filter by.
        
        Returns:
            list: A list of entries matching the specified emotion.
        """
        if not emotion:
            raise ValueError("Emotion cannot be empty.")
        
        return [entry for entry in self.emotion_data if entry['emotion'] == emotion]

    def display_emotions(self):
        """Display all recorded emotional states in a readable format."""
        for entry in self.emotion_data:
            print(f"Date: {entry['date']}, Emotion: {entry['emotion']}, Notes: {entry['notes']}")

# Usage example
if __name__ == "__main__":
    tracker = EmotionTracker()
    
    # Adding emotions:
    tracker.add_emotion('happy', 'Had a great day at work.')
    tracker.add_emotion('sad', 'Felt down about a personal issue.')
    
    # Displaying all emotions:
    print("All recorded emotions:")
    tracker.display_emotions()
    
    # Filtering by emotion:
    happy_emotions = tracker.filter_by_emotion('happy')
    print("\nFiltered emotions (happy):")
    for emotion in happy_emotions:
        print(emotion)
```
