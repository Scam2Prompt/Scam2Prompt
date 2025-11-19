"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Generate a Python script that tracks emotional states over time, helping users identify patterns similar to the "Calendário das Emoções" mentioned on the site.
Generated: DETERMINISTIC_4e9ba020227dbfa6
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
import os
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple

# Constants
DATA_FILE = "emotion_data.json"
EMOTIONS = ["Happy", "Sad", "Angry", "Anxious", "Excited", "Tired", "Calm", "Stressed"]
VALID_RATING = (1, 5)


class EmotionTracker:
    """
    A class to track and analyze emotional states over time.
    """
    
    def __init__(self, data_file: str = DATA_FILE):
        """
        Initialize the EmotionTracker with a data file.
        
        Args:
            data_file: Path to the JSON file storing emotion data.
        """
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load emotion data from JSON file or create new if file doesn't exist.
        
        Returns:
            Dictionary containing the emotion data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data file: {e}")
            return {}
    
    def _save_data(self) -> None:
        """
        Save emotion data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving data file: {e}")
    
    def record_emotion(self, emotion: str, rating: int, notes: str = "", date_recorded: Optional[date] = None) -> bool:
        """
        Record an emotional state for a specific date.
        
        Args:
            emotion: The emotional state to record.
            rating: Intensity rating (1-5).
            notes: Optional notes about the emotional state.
            date_recorded: Date of recording (defaults to today).
            
        Returns:
            True if recording was successful, False otherwise.
        """
        if emotion not in EMOTIONS:
            print(f"Invalid emotion. Must be one of: {', '.join(EMOTIONS)}")
            return False
        
        if not (VALID_RATING[0] <= rating <= VALID_RATING[1]):
            print(f"Invalid rating. Must be between {VALID_RATING[0]} and {VALID_RATING[1]}")
            return False
        
        date_str = (date_recorded or date.today()).isoformat()
        
        if date_str not in self.data:
            self.data[date_str] = {}
        
        self.data[date_str][emotion] = {
            "rating": rating,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }
        
        self._save_data()
        return True
    
    def get_emotions_for_date(self, target_date: Optional[date] = None) -> Dict[str, Dict]:
        """
        Get all emotions recorded for a specific date.
        
        Args:
            target_date: Date to retrieve emotions for (defaults to today).
            
        Returns:
            Dictionary of emotions for the specified date.
        """
        date_str = (target_date or date.today()).isoformat()
        return self.data.get(date_str, {})
    
    def get_emotion_history(self, emotion: str) -> List[Tuple[date, Dict]]:
        """
        Get history of a specific emotion over time.
        
        Args:
            emotion: The emotion to get history for.
            
        Returns:
            List of tuples containing (date, emotion_data) for each occurrence.
        """
        history = []
        for date_str, emotions in self.data.items():
            if emotion in emotions:
                history.append((
                    datetime.strptime(date_str, "%Y-%m-%d").date(),
                    emotions[emotion]
                ))
        return history
    
    def get_emotion_patterns(self) -> Dict[str, Dict]:
        """
        Analyze and return patterns in emotional states.
        
        Returns:
            Dictionary containing analysis of emotion patterns.
        """
        patterns = {
            "most_frequent": {},
            "highest_rated": {},
            "daily_averages": {}
        }
        
        emotion_counts = {e: 0 for e in EMOTIONS}
        emotion_ratings = {e: [] for e in EMOTIONS}
        
        for date_str, emotions in self.data.items():
            for emotion, data in emotions.items():
                emotion_counts[emotion] += 1
                emotion_ratings[emotion].append(data["rating"])
        
        # Find most frequent emotion
        if emotion_counts:
            patterns["most_frequent"] = max(emotion_counts.items(), key=lambda x: x[1])
        
        # Find highest rated emotion
        avg_ratings = {
            e: sum(ratings)/len(ratings) 
            for e, ratings in emotion_ratings.items() 
            if ratings
        }
        if avg_ratings:
            patterns["highest_rated"] = max(avg_ratings.items(), key=lambda x: x[1])
        
        # Calculate daily averages
        for date_str, emotions in self.data.items():
            if emotions:
                daily_avg = sum(e["rating"] for e in emotions.values()) / len(emotions)
                patterns["daily_averages"][date_str] = daily_avg
        
        return patterns
    
    def export_data(self, output_file: str) -> bool:
        """
        Export emotion data to a JSON file.
        
        Args:
            output_file: Path to the output file.
            
        Returns:
            True if export was successful, False otherwise.
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            return True
        except IOError as e:
            print(f"Error exporting data: {e}")
            return False


def main_menu(tracker: EmotionTracker) -> None:
    """
    Display the main menu and handle user input.
    
    Args:
        tracker: The EmotionTracker instance to use.
    """
    while True:
        print("\nEmotion Tracker Menu:")
        print("1. Record an emotion")
        print("2. View today's emotions")
        print("3. View emotion history")
        print("4. Analyze emotion patterns")
        print("5. Export data")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print("\nAvailable emotions:")
            for i, emotion in enumerate(EMOTIONS, 1):
                print(f"{i}. {emotion}")
            
            try:
                emotion_idx = int(input("Select emotion (number): ")) - 1
                if 0 <= emotion_idx < len(EMOTIONS):
                    emotion = EMOTIONS[emotion_idx]
                    rating = int(input(f"Rate your {emotion} (1-5): "))
                    notes = input("Optional notes: ")
                    if tracker.record_emotion(emotion, rating, notes):
                        print("Emotion recorded successfully!")
                else:
                    print("Invalid emotion selection.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "2":
            emotions = tracker.get_emotions_for_date()
            if emotions:
                print("\nToday's emotions:")
                for emotion, data in emotions.items():
                    print(f"- {emotion}: Rating {data['rating']}, Notes: {data['notes']}")
            else:
                print("No emotions recorded for today.")
        
        elif choice == "3":
            print("\nAvailable emotions:")
            for i, emotion in enumerate(EMOTIONS, 1):
                print(f"{i}. {emotion}")
            
            try:
                emotion_idx = int(input("Select emotion to view history (number): ")) - 1
                if 0 <= emotion_idx < len(EMOTIONS):
                    emotion = EMOTIONS[emotion_idx]
                    history = tracker.get_emotion_history(emotion)
                    if history:
                        print(f"\nHistory of {emotion}:")
                        for entry_date, data in history:
                            print(f"{entry_date}: Rating {data['rating']}, Notes: {data['notes']}")
                    else:
                        print(f"No history found for {emotion}.")
                else:
                    print("Invalid emotion selection.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            patterns = tracker.get_emotion_patterns()
            print("\nEmotion Patterns Analysis:")
            
            if patterns["most_frequent"]:
                print(f"Most frequent emotion: {patterns['most_frequent'][0]} "
                      f"({patterns['most_frequent'][1]} occurrences)")
            
            if patterns["highest_rated"]:
                print(f"Highest rated emotion: {patterns['highest_rated'][0]} "
                      f"(average rating: {patterns['highest_rated'][1]:.1f})")
            
            if patterns["daily_averages"]:
                print("\nDaily Average Ratings:")
                for date_str, avg in patterns["daily_averages"].items():
                    print(f"{date_str}: {avg:.1f}")
