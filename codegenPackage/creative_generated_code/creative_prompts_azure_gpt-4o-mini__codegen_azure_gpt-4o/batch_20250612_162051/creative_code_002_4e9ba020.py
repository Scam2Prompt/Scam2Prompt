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
import os
from datetime import datetime

class EmotionTracker:
    def __init__(self, data_file="emotion_data.json"):
        """
        Initialize the EmotionTracker with a file to store emotional data history.
        
        :param data_file: Name of the JSON file where emotional data will be stored.
        """
        self.data_file = data_file
        self.emotion_data = {}
        self._load_data()

    def _load_data(self):
        """
        Load existing emotion data from the JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.emotion_data = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data file: {e}")

    def _save_data(self):
        """
        Save current emotion data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.emotion_data, file, indent=4)
        except IOError as e:
            print(f"Error saving data file: {e}")

    def record_emotion(self, emotion, intensity):
        """
        Record a new emotional state with the current timestamp.
        
        :param emotion: The name of the emotion (e.g., "happy", "sad").
        :param intensity: The intensity of the emotion (e.g., 1-10 scale).
        """
        if not (1 <= intensity <= 10):
            print("Intensity must be between 1 and 10.")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.emotion_data[timestamp] = {"emotion": emotion, "intensity": intensity}
        
        self._save_data()
        print("Emotion successfully recorded.")

    def view_emotions(self):
        """
        Display all recorded emotional states in chronological order.
        """
        if not self.emotion_data:
            print("No emotions recorded yet.")
            return
        
        print("Emotion History:")
        for timestamp, data in sorted(self.emotion_data.items()):
            print(f"{timestamp}: Emotion - {data['emotion']}, Intensity - {data['intensity']}")

    def identify_patterns(self):
        """
        Identify and display patterns in emotional states over time.
        """
        if not self.emotion_data:
            print("No emotions recorded yet.")
            return
        
        emotion_counts = {}
        for data in self.emotion_data.values():
            emotion = data['emotion']
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

        print("Emotion Patterns:")
        for emotion, count in emotion_counts.items():
            print(f"{emotion}: Recorded {count} times")
            

if __name__ == "__main__":
    tracker = EmotionTracker()

    while True:
        print("\nEmotion Tracker Menu:")
        print("1. Record a new emotion")
        print("2. View emotional history")
        print("3. Identify emotion patterns")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            emotion = input("Enter the emotion: ").strip().lower()
            try:
                intensity = int(input("Enter the intensity (1-10): "))
                tracker.record_emotion(emotion, intensity)
            except ValueError:
                print("Invalid intensity. Please enter a number between 1 and 10.")
        elif choice == 2:
            tracker.view_emotions()
        elif choice == 3:
            tracker.identify_patterns()
        elif choice == 4:
            print("Exiting Emotion Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
```
