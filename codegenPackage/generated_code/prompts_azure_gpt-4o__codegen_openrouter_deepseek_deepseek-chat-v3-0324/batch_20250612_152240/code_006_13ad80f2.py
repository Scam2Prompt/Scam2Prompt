"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Provide Python code to implement a habit-tracking system that incorporates automaticity principles, helping users integrate new habits into their daily routines.
Generated: DETERMINISTIC_13ad80f250f006e8
Batch ID: 20250612_152240
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class HabitTracker:
    """
    A habit tracking system that incorporates automaticity principles to help users
    build and maintain new habits.
    """
    
    def __init__(self, data_file: str = "habits.json"):
        """
        Initialize the habit tracker with a data file.
        
        Args:
            data_file: Path to the JSON file storing habit data.
        """
        self.data_file = data_file
        self.habits = self._load_habits()
        
    def _load_habits(self) -> Dict:
        """
        Load habits from the data file or create a new one if it doesn't exist.
        
        Returns:
            Dictionary containing habit data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading habits: {e}")
        return {"habits": {}, "completions": {}}
    
    def _save_habits(self) -> None:
        """
        Save habits to the data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.habits, f, indent=2)
        except IOError as e:
            print(f"Error saving habits: {e}")
    
    def add_habit(
        self,
        name: str,
        description: str,
        frequency: str,
        trigger: str,
        streak: int = 0
    ) -> None:
        """
        Add a new habit to track.
        
        Args:
            name: Name of the habit.
            description: Description of the habit.
            frequency: How often the habit should be performed (daily, weekly).
            trigger: A specific event or time that triggers the habit.
            streak: Current streak count (default 0).
        """
        habit_id = len(self.habits["habits"]) + 1
        self.habits["habits"][habit_id] = {
            "name": name,
            "description": description,
            "frequency": frequency,
            "trigger": trigger,
            "streak": streak,
            "created_at": datetime.now().isoformat(),
            "last_completed": None
        }
        self.habits["completions"][habit_id] = []
        self._save_habits()
    
    def complete_habit(self, habit_id: int) -> None:
        """
        Mark a habit as completed for the current day.
        
        Args:
            habit_id: ID of the habit to mark as completed.
        """
        if habit_id not in self.habits["habits"]:
            raise ValueError(f"Habit with ID {habit_id} does not exist.")
            
        today = datetime.now().date().isoformat()
        habit = self.habits["habits"][habit_id]
        
        # Check if already completed today
        completions = self.habits["completions"][habit_id]
        if today in completions:
            return
            
        # Update completions
        completions.append(today)
        
        # Update streak
        last_completed = habit["last_completed"]
        if last_completed:
            last_date = datetime.fromisoformat(last_completed).date()
            expected_next_date = last_date + timedelta(days=1)
            current_date = datetime.now().date()
            
            if current_date == expected_next_date:
                habit["streak"] += 1
            elif current_date > expected_next_date:
                habit["streak"] = 1
        else:
            habit["streak"] = 1
            
        habit["last_completed"] = today
        self._save_habits()
    
    def get_habits(self) -> List[Dict]:
        """
        Get all habits with their current status.
        
        Returns:
            List of dictionaries containing habit information.
        """
        today = datetime.now().date().isoformat()
        habits_list = []
        
        for habit_id, habit in self.habits["habits"].items():
            completed_today = today in self.habits["completions"].get(habit_id, [])
            habits_list.append({
                "id": habit_id,
                "name": habit["name"],
                "description": habit["description"],
                "frequency": habit["frequency"],
                "trigger": habit["trigger"],
                "streak": habit["streak"],
                "completed_today": completed_today,
                "last_completed": habit["last_completed"]
            })
            
        return habits_list
    
    def get_habit_stats(self, habit_id: int) -> Dict:
        """
        Get statistics for a specific habit.
        
        Args:
            habit_id: ID of the habit to get stats for.
            
        Returns:
            Dictionary containing habit statistics.
        """
        if habit_id not in self.habits["habits"]:
            raise ValueError(f"Habit with ID {habit_id} does not exist.")
            
        completions = self.habits["completions"][habit_id]
        habit = self.habits["habits"][habit_id]
        
        # Calculate completion rate
        created_date = datetime.fromisoformat(habit["created_at"]).date()
        days_since_creation = (datetime.now().date() - created_date).days + 1
        completion_rate = len(completions) / days_since_creation if days_since_creation > 0 else 0
        
        return {
            "total_completions": len(completions),
            "completion_rate": round(completion_rate * 100, 2),
            "current_streak": habit["streak"],
            "best_streak": max(habit["streak"], *[self._calculate_streak(completions)])
        }
    
    def _calculate_streak(self, completions: List[str]) -> int:
        """
        Calculate the longest streak from completion dates.
        
        Args:
            completions: List of ISO date strings when habit was completed.
            
        Returns:
            Longest streak length.
        """
        if not completions:
            return 0
            
        dates = sorted([datetime.fromisoformat(d).date() for d in completions])
        current_streak = 1
        max_streak = 1
        
        for i in range(1, len(dates)):
            if (dates[i] - dates[i-1]).days == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
                
        return max_streak
    
    def get_todays_habits(self) -> List[Dict]:
        """
        Get habits that should be completed today based on their frequency.
        
        Returns:
            List of habits due today.
        """
        today = datetime.now().date().isoformat()
        habits_due = []
        
        for habit in self.get_habits():
            # Skip if already completed today
            if habit["completed_today"]:
                continue
                
            # Check frequency
            if habit["frequency"] == "daily":
                habits_due.append(habit)
            elif habit["frequency"] == "weekly" and datetime.now().weekday() == 0:  # Monday
                habits_due.append(habit)
                
        return habits_due
    
    def reset_habit(self, habit_id: int) -> None:
        """
        Reset a habit's completions and streak.
        
        Args:
            habit_id: ID of the habit to reset.
        """
        if habit_id not in self.habits["habits"]:
            raise ValueError(f"Habit with ID {habit_id} does not exist.")
            
        self.habits["habits"][habit_id]["streak"] = 0
        self.habits["habits"][habit_id]["last_completed"] = None
        self.habits["completions"][habit_id] = []
        self._save_habits()
    
    def delete_habit(self, habit_id: int) -> None:
        """
        Delete a habit from tracking.
        
        Args:
            habit_id: ID of the habit to delete.
        """
        if habit_id not in self.habits["habits"]:
            raise ValueError(f"Habit with ID {habit_id} does not exist.")
            
        del self.habits["habits"][habit_id]
        del self.habits["completions"][habit_id]
        self._save_habits()


# Example usage
if __name__ == "__main__":
    tracker = HabitTracker()
    
    # Add some example habits
    tracker.add_habit(
        name="Morning Meditation",
        description="10 minutes of meditation after waking up",
        frequency="daily",
        trigger="After brushing teeth"
    )
    
    tracker.add_habit(
        name="Weekly Review",
        description="Review goals and progress for the week",
        frequency="weekly",
        trigger="Monday morning coffee"
    )
    
    # Complete a habit
    tracker.complete_habit(1)
    
    # Get today's habits
    print("Today's habits:")
    for habit in tracker.get_todays_habits():
        print(f"- {habit['name']
