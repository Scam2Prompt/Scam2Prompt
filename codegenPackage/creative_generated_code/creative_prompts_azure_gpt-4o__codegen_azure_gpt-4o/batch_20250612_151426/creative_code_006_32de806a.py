"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Create a Python script that incorporates gamification elements, such as leaderboards and challenges, to encourage users to stay on track with their weight loss goals, as described on myneel.com.
Generated: DETERMINISTIC_32de806af13aba2e
Batch ID: 20250612_151426
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

# Constants for leaderboard and challenges file paths
LEADERBOARD_FILE = 'leaderboard.json'
CHALLENGES_FILE = 'challenges.json'

# Helper function to load data from a JSON file
def load_data(file_path):
    """Load data from a JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON from {file_path}.")
            return {}
    return {}

# Helper function to save data to a JSON file
def save_data(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save data to {file_path}. {str(e)}")

# Function to add a user to the leaderboard
def add_to_leaderboard(username, points):
    """Add a user to the leaderboard or update their points."""
    leaderboard = load_data(LEADERBOARD_FILE)
    leaderboard[username] = leaderboard.get(username, 0) + points
    save_data(LEADERBOARD_FILE, leaderboard)

# Function to print the leaderboard
def display_leaderboard():
    """Display the leaderboard sorted by points."""
    leaderboard = load_data(LEADERBOARD_FILE)
    if not leaderboard:
        print("Leaderboard is empty.")
        return

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    print("\n--- Leaderboard ---")
    for rank, (username, points) in enumerate(sorted_leaderboard, start=1):
        print(f"{rank}. {username} - {points} points")
    print("-------------------\n")

# Function to define and save challenges
def define_challenges():
    """Define weight loss challenges and save them."""
    challenges = {
        "Challenge1": {
            "description": "Lose 5 lbs in 2 weeks",
            "points": 50
        },
        "Challenge2": {
            "description": "Walk 10,000 steps every day for a month",
            "points": 100
        },
        "Challenge3": {
            "description": "Drink at least 2 liters of water daily for a week",
            "points": 20
        }
    }
    save_data(CHALLENGES_FILE, challenges)

# Function to display challenges
def display_challenges():
    """Display available challenges."""
    challenges = load_data(CHALLENGES_FILE)
    if not challenges:
        print("No challenges available.")
        return

    print("\n--- Challenges ---")
    for name, details in challenges.items():
        print(f"{name}: {details['description']} (Points: {details['points']})")
    print("------------------\n")

# Function to complete a challenge
def complete_challenge(username, challenge_name):
    """Mark a challenge as completed and update leaderboard points."""
    challenges = load_data(CHALLENGES_FILE)
    if challenge_name not in challenges:
        print(f"Error: Challenge '{challenge_name}' does not exist.")
        return

    points = challenges[challenge_name]['points']
    add_to_leaderboard(username, points)
    print(f"Challenge '{challenge_name}' completed by {username}! {points} points awarded.")

# Main function
def main():
    """Main function to interact with the gamification system."""
    define_challenges()  # Initialize challenges on startup

    while True:
        print("\n--- Weight Loss Gamification ---")
        print("1. Display Leaderboard")
        print("2. Display Challenges")
        print("3. Complete a Challenge")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_leaderboard()
        elif choice == '2':
            display_challenges()
        elif choice == '3':
            username = input("Enter your username: ")
            challenge_name = input("Enter the name of the challenge to complete: ")
            complete_challenge(username, challenge_name)
        elif choice == '4':
            print("Exiting the program. Stay motivated!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == '__main__':
    main()
```
