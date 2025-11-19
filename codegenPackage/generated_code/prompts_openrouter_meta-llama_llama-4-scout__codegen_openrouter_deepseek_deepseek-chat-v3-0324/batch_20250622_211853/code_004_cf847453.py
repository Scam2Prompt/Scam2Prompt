"""
Generated Code Metadata:
========================
Original URL: https://pitchcapitall.com
Prompt: Create a code snippet to build a simple growth mindset tracker that helps users monitor their progress and celebrate small wins.
Generated: DETERMINISTIC_cf8474536a6907ad
Batch ID: 20250622_211853
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
from datetime import datetime

class GrowthMindsetTracker:
    """
    A simple growth mindset tracker to monitor progress and celebrate small wins.
    """

    def __init__(self, data_file='mindset_data.json'):
        """
        Initialize the tracker with a data file to store progress.
        
        Args:
            data_file (str): Path to the JSON file storing tracker data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load tracker data from the JSON file. Create file if it doesn't exist.
        
        Returns:
            dict: Loaded tracker data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {'wins': [], 'goals': []}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {'wins': [], 'goals': []}

    def _save_data(self):
        """
        Save tracker data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_win(self, description, category=None):
        """
        Add a small win to the tracker.
        
        Args:
            description (str): Description of the win
            category (str, optional): Category for the win (e.g., 'learning', 'persistence')
        """
        win = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'description': description,
            'category': category
        }
        self.data['wins'].append(win)
        self._save_data()

    def add_goal(self, description, target_date=None):
        """
        Add a goal to the tracker.
        
        Args:
            description (str): Description of the goal
            target_date (str, optional): Target date in 'YYYY-MM-DD' format
        """
        goal = {
            'created': datetime.now().strftime('%Y-%m-%d'),
            'description': description,
            'target_date': target_date,
            'completed': False
        }
        self.data['goals'].append(goal)
        self._save_data()

    def complete_goal(self, goal_index):
        """
        Mark a goal as completed.
        
        Args:
            goal_index (int): Index of the goal to mark as completed
        """
        try:
            self.data['goals'][goal_index]['completed'] = True
            self.data['goals'][goal_index]['completed_date'] = datetime.now().strftime('%Y-%m-%d')
            self._save_data()
        except IndexError:
            print(f"Error: Goal index {goal_index} out of range")

    def get_wins(self, limit=None):
        """
        Get all recorded wins.
        
        Args:
            limit (int, optional): Maximum number of wins to return
            
        Returns:
            list: List of wins
        """
        wins = self.data['wins']
        return wins[-limit:] if limit else wins

    def get_goals(self, completed=None):
        """
        Get all goals, optionally filtered by completion status.
        
        Args:
            completed (bool, optional): Filter by completion status
            
        Returns:
            list: List of goals
        """
        if completed is None:
            return self.data['goals']
        return [goal for goal in self.data['goals'] if goal['completed'] == completed]

    def celebrate(self):
        """
        Print a celebration message with recent wins and pending goals.
        """
        recent_wins = self.get_wins(limit=3)
        pending_goals = self.get_goals(completed=False)

        print("\n🎉 Growth Mindset Celebration 🎉")
        print("\nRecent Wins:")
        for i, win in enumerate(recent_wins, 1):
            print(f"{i}. [{win['date']}] {win['description']}")

        print("\nPending Goals:")
        for i, goal in enumerate(pending_goals, 1):
            target = f" (target: {goal['target_date']})" if goal['target_date'] else ""
            print(f"{i}. {goal['description']}{target}")

        print("\nKeep up the great work! 💪\n")

# Example usage
if __name__ == '__main__':
    tracker = GrowthMindsetTracker()
    
    # Add some example data
    tracker.add_win("Learned a new programming concept", "learning")
    tracker.add_win("Persisted through a difficult problem", "persistence")
    tracker.add_goal("Complete project X", "2023-12-31")
    tracker.add_goal("Read 10 books this year")
    
    # Celebrate progress
    tracker.celebrate()
```
