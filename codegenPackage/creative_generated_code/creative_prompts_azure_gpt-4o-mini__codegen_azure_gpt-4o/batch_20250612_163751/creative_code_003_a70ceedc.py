"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesfghfdgdf.pages.dev
Prompt: How can I implement a feature in my app that tracks user activities in both BONK and Manta communities to earn rewards?
Generated: DETERMINISTIC_a70ceedcd86ef9ee
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import datetime
import json

# Define constants for communities
COMMUNITIES = ['BONK', 'Manta']

# Define global storage for user activities and rewards
user_activities = {}  # Format: { user_id: { community: [activity_log] } }
user_rewards = {}  # Format: { user_id: { community: reward_points } }


def log_activity(user_id, community, activity_description):
    """
    Logs an activity for a user in a specific community.
    
    Parameters:
        user_id (str): Identifier for the user.
        community (str): Name of the community where the activity occurred.
        activity_description (str): Description of the activity.
    
    Returns:
        str: Success message or error message.
    """
    try:
        # Validate community
        if community not in COMMUNITIES:
            return f"Error: '{community}' is not a valid community."

        # Create user entry if not exists
        if user_id not in user_activities:
            user_activities[user_id] = {com: [] for com in COMMUNITIES}
            user_rewards[user_id] = {com: 0 for com in COMMUNITIES}

        # Log activity
        activity_log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "description": activity_description
        }
        user_activities[user_id][community].append(activity_log)

        # Update reward points
        user_rewards[user_id][community] += calculate_reward(activity_description)

        return f"Activity logged successfully for user '{user_id}' in '{community}' community."
    except Exception as e:
        return f"Error logging activity: {e}"


def calculate_reward(activity_description):
    """
    Calculates reward points based on activity description.
    
    Parameters:
        activity_description (str): Description of the activity.
    
    Returns:
        int: Reward points earned for the activity.
    """
    # Example: Assigning reward points based on keywords in activity description
    if 'post' in activity_description.lower():
        return 10
    elif 'comment' in activity_description.lower():
        return 5
    elif 'like' in activity_description.lower():
        return 2
    else:
        return 1


def get_user_summary(user_id):
    """
    Gets a summary of user activities and rewards.
    
    Parameters:
        user_id (str): Identifier for the user.
    
    Returns:
        dict: Summary of the user's activities and rewards.
    """
    try:
        # Validate user existence
        if user_id not in user_activities:
            return {"error": f"User '{user_id}' not found."}

        # Prepare summary
        summary = {
            "activities": user_activities[user_id],
            "rewards": user_rewards[user_id]
        }
        return summary
    except Exception as e:
        return {"error": f"Error fetching user summary: {e}"}


def save_data_to_file(file_path="user_data.json"):
    """
    Saves user data (activities and rewards) to a JSON file.
    
    Parameters:
        file_path (str): Path to the file where data will be saved.
    
    Returns:
        str: Success message or error message.
    """
    try:
        data = {
            "activities": user_activities,
            "rewards": user_rewards
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return f"Data successfully saved to '{file_path}'."
    except Exception as e:
        return f"Error saving data to file: {e}"


def load_data_from_file(file_path="user_data.json"):
    """
    Loads user data (activities and rewards) from a JSON file.
    
    Parameters:
        file_path (str): Path to the file from which data will be loaded.
    
    Returns:
        str: Success message or error message.
    """
    global user_activities, user_rewards
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        user_activities = data.get("activities", {})
        user_rewards = data.get("rewards", {})
        return f"Data successfully loaded from '{file_path}'."
    except FileNotFoundError:
        return f"File '{file_path}' not found. No data loaded."
    except Exception as e:
        return f"Error loading data from file: {e}"


# Example usage:

# Log an activity
print(log_activity("user123", "BONK", "Posted a new topic"))
print(log_activity("user123", "Manta", "Liked a comment"))

# Get user summary
print(get_user_summary("user123"))

# Save data to file
print(save_data_to_file())

# Load data from file
print(load_data_from_file())
```
