"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solxdao.web.app
Prompt: Develop a script that calculates the potential rewards in $TNSR tokens based on user activity on the SolxDAO platform.
Generated: DETERMINISTIC_9cfe81e0e7c6cf73
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential rewards in $TNSR tokens based on user activity on the SolxDAO platform.

Requirements:
- Activity data is provided as a JSON file or dictionary containing user actions.
- Each action has a predefined reward factor (e.g., staking, voting, etc.).
- Final rewards are calculated by multiplying activity counts by their reward factors.
"""

import json

# Define reward factors for each activity type (example values)
REWARD_FACTORS = {
    "staking": 10,     # Reward per staking action
    "voting": 5,       # Reward per voting action
    "proposal_creation": 20,  # Reward per proposal creation
    "commenting": 2    # Reward per comment posted
}

def load_user_activity(file_path):
    """
    Loads user activity from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing user activity data.

    Returns:
        dict: Dictionary containing user activity data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file content is not a valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def calculate_rewards(activity_data):
    """
    Calculates potential rewards in $TNSR tokens based on user activity.
    
    Args:
        activity_data (dict): Dictionary containing user activities with counts.

    Returns:
        float: The total $TNSR reward based on activity.

    Raises:
        KeyError: If an activity type in the data is not defined in REWARD_FACTORS.
    """
    total_rewards = 0
    for activity, count in activity_data.items():
        # Ensure activity type exists in reward factors
        if activity not in REWARD_FACTORS:
            raise KeyError(f"Unknown activity type: {activity}")
        # Calculate rewards for this activity
        total_rewards += count * REWARD_FACTORS[activity]
    return total_rewards

def main():
    """
    Main function to execute the reward calculation.
    """
    # Example user activity JSON file path
    file_path = "user_activity.json"

    try:
        # Load user activity data
        activity_data = load_user_activity(file_path)
        print(f"Loaded activity data: {activity_data}")

        # Calculate rewards
        rewards = calculate_rewards(activity_data)
        print(f"Total potential $TNSR rewards: {rewards:.2f}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

---

**Instructions for Use:**
1. Create a `user_activity.json` file with the following example format:
   ```json
   {
       "staking": 5,
       "voting": 10,
       "proposal_creation": 2,
       "commenting": 7
   }
   ```
2. Place the JSON file in the same directory as the script.
3. Run the script using Python (`python script_name.py`).
