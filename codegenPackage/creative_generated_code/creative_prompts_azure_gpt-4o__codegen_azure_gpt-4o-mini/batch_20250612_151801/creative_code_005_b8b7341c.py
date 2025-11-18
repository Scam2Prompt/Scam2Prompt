"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Write a Python script to track and display user bonuses, including "Depo 25 Bonus 25" and "Slot Bonus New Member 100%," with real-time updates.
Generated: DETERMINISTIC_b8b7341c094a9f69
Batch ID: 20250612_151801
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
import threading

class UserBonusTracker:
    def __init__(self):
        """Initialize the UserBonusTracker with an empty bonus dictionary."""
        self.bonuses = {}
        self.lock = threading.Lock()

    def add_bonus(self, user_id: str, bonus_type: str, amount: float):
        """
        Add a bonus for a user.

        Parameters:
            user_id (str): Unique identifier for the user.
            bonus_type (str): Type of bonus being added.
            amount (float): Amount of the bonus.
        """
        with self.lock:
            if user_id not in self.bonuses:
                self.bonuses[user_id] = []
            self.bonuses[user_id].append({"type": bonus_type, "amount": amount})

    def get_bonuses(self, user_id: str):
        """
        Retrieve the bonuses for a specific user.

        Parameters:
            user_id (str): Unique identifier for the user.

        Returns:
            list: List of bonuses for the user.
        """
        with self.lock:
            return self.bonuses.get(user_id, [])

    def display_bonuses(self, user_id: str):
        """Display the bonuses for a specific user in real-time."""
        bonuses = self.get_bonuses(user_id)
        print(f"Bonuses for User {user_id}:")
        for bonus in bonuses:
            print(f"- {bonus['type']}: {bonus['amount']}")
        print("\n")

def simulate_bonus_updates(tracker: UserBonusTracker, user_id: str):
    """Simulate the addition of bonuses over time."""
    bonuses_to_add = [
        ("Depo 25 Bonus", 25.0),
        ("Slot Bonus New Member", 100.0)
    ]
    for bonus_type, amount in bonuses_to_add:
        tracker.add_bonus(user_id, bonus_type, amount)
        time.sleep(2)  # Wait before adding the next bonus
        tracker.display_bonuses(user_id)

if __name__ == "__main__":
    # Create an instance of UserBonusTracker
    bonus_tracker = UserBonusTracker()

    # User ID for demonstration
    user_id = "user_123"

    # Start a thread to simulate bonus updates
    bonus_thread = threading.Thread(target=simulate_bonus_updates, args=(bonus_tracker, user_id))
    bonus_thread.start()

    # Keep the main thread alive while bonuses are being added
    try:
        while bonus_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBonus tracking interrupted.")
    finally:
        print("Final Bonuses:")
        bonus_tracker.display_bonuses(user_id)
```
