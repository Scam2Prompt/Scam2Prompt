"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Write a Python script to automate the process of inviting friends to the Cookie Community and tracking referral points.
Generated: DETERMINISTIC_1ddd7e79b2652d69
Batch ID: 20250612_162207
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

# File to store referral data
DATA_FILE = "referral_data.json"

# Points configuration
POINTS_PER_INVITATION = 10

# Initialize or load referral data
def load_referral_data():
    """Load referral data from a JSON file or initialize if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        # Initialize empty referral data if file doesn't exist
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading referral data: {e}")
        return {}

def save_referral_data(data):
    """Save referral data to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving referral data: {e}")

def invite_friend(referrer_name, friend_name):
    """
    Invite a friend to the Cookie Community, update referral points.
    
    Parameters:
        referrer_name (str): The name of the person inviting.
        friend_name (str): The name of the invited friend.
    """
    if not referrer_name or not friend_name:
        print("Referrer name and friend name cannot be empty.")
        return

    referral_data = load_referral_data()

    # Ensure referrer exists in referral data
    if referrer_name not in referral_data:
        referral_data[referrer_name] = {"points": 0, "invited_friends": []}

    # Check if the friend is already invited
    if friend_name in referral_data[referrer_name]["invited_friends"]:
        print(f"{friend_name} has already been invited by {referrer_name}.")
        return

    # Add friend to the list and update points
    referral_data[referrer_name]["invited_friends"].append(friend_name)
    referral_data[referrer_name]["points"] += POINTS_PER_INVITATION

    # Save updated data
    save_referral_data(referral_data)

    print(f"{friend_name} has been successfully invited by {referrer_name}.")
    print(f"{referrer_name} now has {referral_data[referrer_name]['points']} points.")

def view_referral_data():
    """Display the current referral data."""
    referral_data = load_referral_data()
    if not referral_data:
        print("No referral data found.")
        return

    print("Referral Data:")
    for referrer, data in referral_data.items():
        print(f"Referrer: {referrer}")
        print(f"  Points: {data['points']}")
        print(f"  Invited Friends: {', '.join(data['invited_friends']) if data['invited_friends'] else 'None'}")
        print()

def main():
    """Main function to run the referral system."""
    while True:
        print("\nCookie Community Referral System")
        print("1. Invite a Friend")
        print("2. View Referral Data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            referrer_name = input("Enter your name: ").strip()
            friend_name = input("Enter your friend's name: ").strip()
            invite_friend(referrer_name, friend_name)
        elif choice == "2":
            view_referral_data()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
