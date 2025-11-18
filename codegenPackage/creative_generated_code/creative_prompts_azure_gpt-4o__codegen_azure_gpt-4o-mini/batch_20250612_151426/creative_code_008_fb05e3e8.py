"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Write code to integrate a free-tier feature guarantee in a weight loss app, ensuring that core functionalities like calorie tracking and progress monitoring remain accessible to all users, as described on Neel's website.
Generated: DETERMINISTIC_fb05e3e8af50d9ba
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Class representing a user of the weight loss app.
    
    Attributes:
        username (str): The username of the user.
        subscription_level (str): The subscription level of the user ('free' or 'premium').
        calories (int): Total calories tracked for the day.
        progress (list): A list to track weight progress over time.
    """

    def __init__(self, username: str, subscription_level: str):
        self.username = username
        self.subscription_level = subscription_level.lower()
        self.calories = 0
        self.progress = []

        if self.subscription_level not in ['free', 'premium']:
            raise ValueError("Subscription level must be 'free' or 'premium'.")

    def track_calories(self, calories: int):
        """
        Track calories consumed by the user.
        
        Args:
            calories (int): Number of calories to track.

        Raises:
            ValueError: If calories are negative.
        """
        if calories < 0:
            raise ValueError("Calories cannot be negative.")
        
        self.calories += calories
        print(f"Calories tracked: {self.calories}")

    def log_progress(self, weight: float):
        """
        Log the user's weight progress.
        
        Args:
            weight (float): Current weight of the user.
        """
        self.progress.append(weight)
        print(f"Progress logged: {weight} kg. Total records: {len(self.progress)}.")

    def view_progress(self):
        """
        View the user's weight progress.
        
        Returns:
            list: A list of logged weights.
        """
        return self.progress

    def reset_daily_calories(self):
        """
        Reset daily calorie tracking at the end of the day.
        """
        self.calories = 0
        print("Daily calorie count reset.")


# Example usage:
def main():
    try:
        user1 = User(username="Neel", subscription_level="free")
        user1.track_calories(500)
        user1.log_progress(70.5)
        print("Current Progress:", user1.view_progress())
        
        user1.track_calories(300)
        user1.reset_daily_calories()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
