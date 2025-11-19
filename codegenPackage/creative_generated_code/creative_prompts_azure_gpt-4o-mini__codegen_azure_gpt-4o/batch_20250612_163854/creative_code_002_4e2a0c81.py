"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Generate a function to handle daily rewards in a game similar to Hamster Kombat, focusing on user engagement and retention.
Generated: DETERMINISTIC_4e2a0c81e716a026
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

# Define a dictionary to simulate a database for users and their rewards
user_data = {
    # Example structure for user data
    # 'user_id': {
    #     'last_reward_date': 'YYYY-MM-DD',
    #     'consecutive_days': int, 
    #     'reward_points': int
    # }
}

def handle_daily_rewards(user_id):
    """
    Handles daily rewards for a user in a game.
    
    Args:
        user_id (str): The unique identifier for the user.
        
    Returns:
        dict: A dictionary containing reward details and user status.
    """
    try:
        # Get today's date
        today_date = datetime.date.today()
        
        # Check if the user exists in the database
        if user_id not in user_data:
            # Initialize new user if not present
            user_data[user_id] = {
                'last_reward_date': None,
                'consecutive_days': 0,
                'reward_points': 0
            }
        
        user_info = user_data[user_id]
        last_reward_date = user_info['last_reward_date']
        
        if last_reward_date:
            # Parse last_reward_date to a datetime object
            last_reward_date_obj = datetime.datetime.strptime(last_reward_date, '%Y-%m-%d').date()
            
            # Check if the reward was already claimed today
            if last_reward_date_obj == today_date:
                return {"status": "error", "message": "Reward already claimed for today."}
                
            # Check if the reward is claimed consecutively
            elif (today_date - last_reward_date_obj).days == 1:
                user_info['consecutive_days'] += 1
            else:
                # Reset consecutive days if not consecutive
                user_info['consecutive_days'] = 1
        else:
            # First-time reward claim
            user_info['consecutive_days'] = 1
            
        # Calculate reward points based on consecutive days
        reward_points = 10 * user_info['consecutive_days']  # Example: 10 points per consecutive day
        user_info['reward_points'] += reward_points
        user_info['last_reward_date'] = today_date.strftime('%Y-%m-%d')
        
        # Save updated user data (simulated as in-memory storage here)
        user_data[user_id] = user_info
        
        # Return success response
        return {
            "status": "success",
            "message": "Daily reward claimed successfully!",
            "reward_points_earned": reward_points,
            "total_reward_points": user_info['reward_points'],
            "consecutive_days": user_info['consecutive_days']
        }
    
    except Exception as e:
        # Handle unexpected errors
        return {"status": "error", "message": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    user_id = "player123"
    result = handle_daily_rewards(user_id)
    print(json.dumps(result, indent=4))
```
