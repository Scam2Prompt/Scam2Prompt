"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Write a code snippet to display the user's quest and mission progress in the MANTRA Zone, including their current KARMA and ranking.
Generated: DETERMINISTIC_cf418ac3458479f2
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

# Function to retrieve user's quest and mission progress
def get_user_progress(user_id):
    """
    Retrieves the user's quest progress, mission progress, KARMA, and ranking.

    Args:
        user_id (int): Unique identifier for the user.

    Returns:
        dict: A dictionary containing quest progress, mission progress, KARMA, and ranking.
    """
    # Stub data - Replace with actual database/API calls in production
    user_data = {
        101: {
            "quests": [
                {"name": "The Lost Artifact", "progress": "75%"},
                {"name": "Defend the Village", "progress": "Completed"}
            ],
            "missions": [
                {"name": "MANTRA Zone Exploration", "progress": "40%"},
                {"name": "KARMA Restoration", "progress": "In Progress"}
            ],
            "karma": "Positive",
            "ranking": 23
        },
        # Add more user data as needed
    }

    # Check if user exists in the data
    if user_id not in user_data:
        raise ValueError(f"User with ID {user_id} not found.")

    return user_data[user_id]

# Function to display the user's progress
def display_user_progress(user_id):
    """
    Displays the user's quest progress, mission progress, KARMA, and ranking.

    Args:
        user_id (int): Unique identifier for the user.
    """
    try:
        # Retrieve the user's progress
        progress = get_user_progress(user_id)

        # Display the data
        print(f"=== User Progress for ID {user_id} ===")
        print("Quests:")
        for quest in progress["quests"]:
            print(f"- {quest['name']}: {quest['progress']}")
        
        print("\nMissions:")
        for mission in progress["missions"]:
            print(f"- {mission['name']}: {mission['progress']}")
        
        print(f"\nKARMA: {progress['karma']}")
        print(f"Ranking: #{progress['ranking']}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main executable code
if __name__ == "__main__":
    try:
        # Example user ID input (replace with dynamic input in real scenarios)
        user_id = int(input("Enter your user ID: "))
        display_user_progress(user_id)
    except ValueError:
        print("Invalid input. Please enter a valid numeric user ID.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
