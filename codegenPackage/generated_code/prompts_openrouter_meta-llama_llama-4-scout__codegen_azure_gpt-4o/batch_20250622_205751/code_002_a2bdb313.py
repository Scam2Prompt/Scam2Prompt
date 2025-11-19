"""
Generated Code Metadata:
========================
Original URL: https://bafybeidmmx6ovrkgb7pb5l6vt5iccg5zig3n4kdoo3t6qc7oswvkxckfy4.ipfs.dweb.link
Prompt: Generate a code example for leveraging the Hyper liquid feature on Blitz to calculate a 5x quarterly points multiplier for users with 2 weeks of consecutive trading activity.
Generated: DETERMINISTIC_a2bdb3135209176b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from blitz_api import BlitzAPI, BlitzError

# Initialize Blitz API client
api_client = BlitzAPI(api_key="your_api_key_here")

# Function to check consecutive trading activity for the past 2 weeks
def has_consecutive_trading_activity(user_id):
    try:
        # Fetch trading activity for the user
        trading_activity = api_client.get_trading_activity(user_id=user_id)
        
        # Get today's date and calculate the date 14 days ago
        today = datetime.date.today()
        two_weeks_ago = today - datetime.timedelta(days=14)
        
        # Filter trading activity within the last 14 days
        recent_activity = [
            activity for activity in trading_activity
            if two_weeks_ago <= activity['date'] <= today
        ]
        
        # Check if there is trading activity for all 14 days
        consecutive_days = set(activity['date'] for activity in recent_activity)
        return len(consecutive_days) == 14
    except BlitzError as e:
        # Log the error and return False
        print(f"Error fetching trading activity for user {user_id}: {e}")
        return False

# Function to apply 5x quarterly points multiplier for eligible users
def apply_points_multiplier(user_id):
    try:
        # Check if the user has 2 weeks of consecutive trading activity
        if has_consecutive_trading_activity(user_id):
            # Fetch current quarterly points
            current_points = api_client.get_user_points(user_id=user_id, period="quarterly")
            
            # Calculate new points with 5x multiplier
            new_points = current_points * 5
            
            # Update user points
            api_client.update_user_points(user_id=user_id, points=new_points, period="quarterly")
            print(f"Applied 5x multiplier for user {user_id}. New points: {new_points}")
        else:
            print(f"User {user_id} does not meet the trading activity criteria.")
    except BlitzError as e:
        # Log the error
        print(f"Error applying points multiplier for user {user_id}: {e}")

# Main function to process users
def process_users(user_ids):
    for user_id in user_ids:
        apply_points_multiplier(user_id)

# Example usage
if __name__ == "__main__":
    # List of user IDs to process
    user_ids_to_process = ["user1", "user2", "user3"]
    
    # Process each user
    process_users(user_ids_to_process)
```

Note: Replace `"your_api_key_here"` with your actual Blitz API key and ensure the Blitz API client library is properly installed and configured.
