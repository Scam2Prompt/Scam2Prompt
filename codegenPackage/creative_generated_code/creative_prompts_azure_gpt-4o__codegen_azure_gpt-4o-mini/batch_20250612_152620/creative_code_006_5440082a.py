"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.xyz
Prompt: Provide code to implement responsible gaming features, such as playtime limits and spending caps, for a decentralized gaming platform like BetSwirl.
Generated: DETERMINISTIC_5440082a84b460c7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json

class ResponsibleGaming:
    def __init__(self, user_id):
        """
        Initializes the ResponsibleGaming class for a specific user.
        
        :param user_id: Unique identifier for the user.
        """
        self.user_id = user_id
        self.playtime_limit = None  # In seconds
        self.spending_cap = None  # In currency units
        self.start_time = None
        self.total_spent = 0.0

    def set_playtime_limit(self, limit_in_minutes):
        """
        Sets the playtime limit for the user.
        
        :param limit_in_minutes: Maximum allowed playtime in minutes.
        """
        self.playtime_limit = limit_in_minutes * 60  # Convert to seconds

    def set_spending_cap(self, cap_amount):
        """
        Sets the spending cap for the user.
        
        :param cap_amount: Maximum allowed spending amount.
        """
        self.spending_cap = cap_amount

    def start_play_session(self):
        """
        Starts a new play session and records the start time.
        """
        if self.playtime_limit is None:
            raise ValueError("Playtime limit must be set before starting a session.")
        
        self.start_time = time.time()

    def end_play_session(self):
        """
        Ends the current play session and updates playtime.
        """
        if self.start_time is None:
            raise ValueError("No play session is currently active.")
        
        elapsed_time = time.time() - self.start_time
        self.start_time = None  # Reset start time

        if elapsed_time > self.playtime_limit:
            print(f"Warning: Exceeded playtime limit of {self.playtime_limit} seconds!")

    def spend(self, amount):
        """
        Records a spending action and checks against the spending cap.
        
        :param amount: The amount spent in the current action.
        """
        if self.spending_cap is None:
            raise ValueError("Spending cap must be set before spending.")
        
        self.total_spent += amount

        if self.total_spent > self.spending_cap:
            print(f"Warning: Exceeded spending cap of {self.spending_cap}!")

    def get_status(self):
        """
        Returns the current status of the responsible gaming features.
        
        :return: A dictionary containing the user's playtime limit, spending cap, and total spent.
        """
        return {
            "user_id": self.user_id,
            "playtime_limit": self.playtime_limit,
            "spending_cap": self.spending_cap,
            "total_spent": self.total_spent,
            "is_playtime_exceeded": (self.start_time is not None and 
                                      (time.time() - self.start_time) > self.playtime_limit),
        }

    def save_settings(self):
        """
        Saves the current settings for the user's responsible gaming preferences to a JSON file.
        """
        settings = self.get_status()
        with open(f"{self.user_id}_responsible_gaming_settings.json", "w") as file:
            json.dump(settings, file)

    def load_settings(self):
        """
        Loads the user's responsible gaming settings from a JSON file.
        """
        try:
            with open(f"{self.user_id}_responsible_gaming_settings.json", "r") as file:
                settings = json.load(file)
                self.playtime_limit = settings.get("playtime_limit")
                self.spending_cap = settings.get("spending_cap")
                self.total_spent = settings.get("total_spent", 0.0)
        except FileNotFoundError:
            print("Settings file not found. Please set your limits.")
        except json.JSONDecodeError:
            print("Error loading settings. The file may be corrupted.")

# Example usage
if __name__ == "__main__":
    user = ResponsibleGaming(user_id="user123")
    user.set_playtime_limit(30)  # 30 minutes
    user.set_spending_cap(100.0)  # $100 spending cap
    
    user.start_play_session()
    # Simulate play and spending
    time.sleep(5)  # Simulating 5 seconds of play
    user.spend(20.0)  # Spending $20

    status = user.get_status()
    print("Current Status:", status)

    user.end_play_session()
    user.save_settings()
    user.load_settings()
```
