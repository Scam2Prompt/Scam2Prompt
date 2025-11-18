"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-synthr.pages.dev
Prompt: Develop a program to track and display SYNTHR badge collection progress for users completing milestones and earning syCREDITS.
Generated: DETERMINISTIC_50605f4b625d8846
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BadgeTracker:
    """
    BadgeTracker is a class for tracking and displaying badge collection progress 
    for users completing milestones and earning syCREDITS.
    """
    def __init__(self, user_id):
        """
        Initialize BadgeTracker with the user's ID and default badge data.

        :param user_id: Unique identifier for the user.
        """
        self.user_id = user_id
        self.badges = {}  # Dictionary to store badge data for the user.
        self.sy_credits = 0  # User's total syCREDITS.

    def add_credits(self, amount):
        """
        Add syCREDITS to the user's account.

        :param amount: Number of syCREDITS to add.
        """
        if amount < 0:
            raise ValueError("Amount of syCREDITS to add must be non-negative.")
        self.sy_credits += amount

    def earn_badge(self, badge_name):
        """
        Add a badge to the user's collection.

        :param badge_name: Name of the badge to earn.
        """
        if badge_name in self.badges:
            raise ValueError(f"Badge '{badge_name}' already earned.")
        self.badges[badge_name] = {"earned": True, "timestamp": self._get_current_time()}

    def display_progress(self):
        """
        Display the user's badge collection progress and total syCREDITS.

        :return: A formatted string showing the user's progress.
        """
        progress = f"User ID: {self.user_id}\n"
        progress += f"Total syCREDITS: {self.sy_credits}\n"
        progress += "Badges Earned:\n"
        for badge, details in self.badges.items():
            progress += f" - {badge} (Earned on {details['timestamp']})\n"
        return progress

    def save_progress(self, file_path):
        """
        Save the user's progress to a JSON file.

        :param file_path: Path to the file where progress will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({
                    "user_id": self.user_id,
                    "sy_credits": self.sy_credits,
                    "badges": self.badges
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving progress to file: {e}")

    def load_progress(self, file_path):
        """
        Load the user's progress from a JSON file.

        :param file_path: Path to the file where progress is saved.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.user_id = data["user_id"]
                self.sy_credits = data["sy_credits"]
                self.badges = data["badges"]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading progress from file: {e}")

    @staticmethod
    def _get_current_time():
        """
        Get the current timestamp as a string.

        :return: The current timestamp.
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Example usage
if __name__ == "__main__":
    try:
        tracker = BadgeTracker(user_id="user123")
        tracker.add_credits(100)
        tracker.earn_badge("Milestone_1")
        tracker.earn_badge("Milestone_2")
        print(tracker.display_progress())

        # Save progress to a file
        tracker.save_progress("progress.json")

        # Load progress from a file
        new_tracker = BadgeTracker(user_id="dummy")
        new_tracker.load_progress("progress.json")
        print(new_tracker.display_progress())

    except Exception as e:
        print(f"Error: {e}")
```
