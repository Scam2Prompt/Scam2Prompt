"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write a Python script that tracks user interactions in a gaming app to calculate rewards like Stardust, as described on Cosmic Rewards.
Generated: DETERMINISTIC_edbf8a93de03e2b1
Batch ID: 20250612_164110
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

# File path for storing user data (can be replaced with a database in production)
DATA_FILE = "user_data.json"


def load_user_data():
    """
    Load user data from the JSON file. If the file doesn't exist, return an empty dictionary.
    """
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        # If file is corrupted or cannot be read, return an empty dictionary
        return {}


def save_user_data(data):
    """
    Save user data to the JSON file.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Unable to save user data.")


def calculate_stardust(interactions):
    """
    Calculate Stardust rewards based on user interactions.

    Parameters:
        interactions (int): The number of interactions a user has performed.

    Returns:
        int: Amount of Stardust earned.
    """
    # Define reward formula: 10 Stardust per interaction, with bonuses
    base_stardust = interactions * 10
    bonus = 0

    # Bonus conditions
    if interactions > 50:
        bonus += 100  # Extra bonus for high interaction count
    if interactions % 10 == 0:
        bonus += 25  # Bonus for reaching multiples of 10

    return base_stardust + bonus


def track_interaction(user_id):
    """
    Track a user's interaction and calculate rewards.

    Parameters:
        user_id (str): Unique identifier for the user.
    """
    # Load existing user data
    user_data = load_user_data()

    # If user does not exist, initialize their data
    if user_id not in user_data:
        user_data[user_id] = {
            "interactions": 0,
            "stardust": 0,
            "last_interaction": None
        }

    # Update user data
    user_data[user_id]["interactions"] += 1
    user_data[user_id]["stardust"] = calculate_stardust(user_data[user_id]["interactions"])
    user_data[user_id]["last_interaction"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save updated user data
    save_user_data(user_data)

    # Print the updated user stats
    print(f"User {user_id} Stats:")
    print(f"Interactions: {user_data[user_id]['interactions']}")
    print(f"Stardust: {user_data[user_id]['stardust']}")
    print(f"Last Interaction: {user_data[user_id]['last_interaction']}")


def main():
    """
    Main function for the script. Simulates a gaming app's user interaction tracking.
    """
    print("Welcome to Cosmic Rewards!")
    while True:
        # Prompt user for input
        user_id = input("Enter your user ID (or type 'exit' to quit): ").strip()
        if user_id.lower() == "exit":
            print("Thank you for using Cosmic Rewards! Goodbye!")
            break

        # Track the user's interaction
        track_interaction(user_id)


if __name__ == "__main__":
    main()
```
