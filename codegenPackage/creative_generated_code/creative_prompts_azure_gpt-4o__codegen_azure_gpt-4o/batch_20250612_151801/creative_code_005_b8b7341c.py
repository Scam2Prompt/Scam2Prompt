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
from datetime import datetime
from threading import Thread

# Class to represent a user's bonus
class UserBonus:
    def __init__(self, username):
        """
        Initializes a new UserBonus object.

        :param username: The username of the user.
        """
        self.username = username
        self.bonuses = {}  # Dictionary to store bonus types and their amounts
        self.lock = False  # Simple mechanism to prevent simultaneous updates

    def add_bonus(self, bonus_name, bonus_amount):
        """
        Adds or updates a bonus for the user.

        :param bonus_name: Name of the bonus (e.g., "Depo 25 Bonus 25").
        :param bonus_amount: Amount of the bonus.
        """
        while self.lock:
            time.sleep(0.1)  # Wait for lock to release
        self.lock = True
        if bonus_name in self.bonuses:
            self.bonuses[bonus_name] += bonus_amount
        else:
            self.bonuses[bonus_name] = bonus_amount
        self.lock = False

    def get_bonus_summary(self):
        """
        Retrieves a summary of all bonuses for the user.

        :return: A string summary of bonuses.
        """
        summary = f"User: {self.username}\nBonuses:\n"
        for bonus_name, bonus_amount in self.bonuses.items():
            summary += f"  - {bonus_name}: {bonus_amount}\n"
        return summary

# Function to simulate real-time bonus updates
def simulate_bonus_updates(user_bonus):
    """
    Simulates real-time bonus updates for a user.

    :param user_bonus: The UserBonus object for the user.
    """
    try:
        while True:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking for bonus updates...")
            # Simulate receiving bonuses in real-time
            user_bonus.add_bonus("Depo 25 Bonus 25", 25)
            user_bonus.add_bonus("Slot Bonus New Member 100%", 100)
            # Display updated bonus summary
            print(user_bonus.get_bonus_summary())
            time.sleep(5)  # Wait for 5 seconds before checking again
    except KeyboardInterrupt:
        print("\nReal-time bonus updates stopped.")

# Main function
def main():
    """
    Entry point of the script.
    """
    # Prompt user for their username
    username = input("Enter your username: ")
    user_bonus = UserBonus(username)

    # Start a thread to simulate real-time bonuses
    bonus_thread = Thread(target=simulate_bonus_updates, args=(user_bonus,))
    bonus_thread.daemon = True  # Ensure thread exits when main program stops
    bonus_thread.start()

    print("Press Ctrl+C to stop real-time updates.\n")
    try:
        # Keep the main program running to allow real-time updates
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

# Run the script
if __name__ == "__main__":
    main()
```
