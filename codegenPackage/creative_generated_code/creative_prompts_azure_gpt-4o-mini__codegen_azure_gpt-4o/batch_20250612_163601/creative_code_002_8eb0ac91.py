"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owltofinance.pages.dev
Prompt: Describe how to use the Owlto Finance SDK to create a daily check-in feature that rewards users with points for bridging activities.
Generated: DETERMINISTIC_8eb0ac91e0008f35
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Owlto Finance SDK and other dependencies
from owlto_finance_sdk import OwltoClient, User, BridgeActivity, RewardSystem
from datetime import datetime, timedelta

# Constants
API_KEY = "your_owlto_api_key"  # Replace with your actual API key
DAILY_REWARD_POINTS = 10  # Number of points to reward for daily check-in
CHECK_IN_TIMEOUT = 24  # Hours between valid check-ins

# Initialize the OwltoClient
client = OwltoClient(api_key=API_KEY)

# Function to perform daily check-in
def daily_check_in(user_id):
    """
    Handles the daily check-in process for a user.

    Args:
        user_id (str): The unique identifier of the user.

    Returns:
        dict: A dictionary containing the result of the check-in process.
    """
    try:
        # Fetch user information from the SDK
        user = User.get(client, user_id)

        if not user:
            return {"success": False, "message": "User not found."}

        # Retrieve user's last check-in timestamp
        last_check_in = user.metadata.get("last_check_in")

        # If last_check_in is None, it's the user's first check-in
        if last_check_in:
            last_check_in = datetime.fromisoformat(last_check_in)
            time_since_last_check_in = datetime.now() - last_check_in

            # Ensure at least 24 hours have passed since the last check-in
            if time_since_last_check_in < timedelta(hours=CHECK_IN_TIMEOUT):
                return {
                    "success": False,
                    "message": "Check-in not allowed. Please wait until the next day.",
                }

        # Fetch the user's bridging activities
        bridge_activities = BridgeActivity.get_recent(client, user_id)

        # Ensure the user has bridging activities in the last 24 hours
        if not bridge_activities or all(
            datetime.now() - activity.timestamp > timedelta(hours=24)
            for activity in bridge_activities
        ):
            return {
                "success": False,
                "message": "No bridging activity detected in the last 24 hours.",
            }

        # Reward the user with daily points
        RewardSystem.add_points(client, user_id, DAILY_REWARD_POINTS)

        # Update user's metadata with the current check-in timestamp
        user.metadata["last_check_in"] = datetime.now().isoformat()
        user.save(client)

        return {
            "success": True,
            "message": f"Check-in successful! {DAILY_REWARD_POINTS} points awarded.",
        }

    except Exception as e:
        # Handle unexpected errors
        return {"success": False, "message": f"An error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Replace with actual user ID
    test_user_id = "user_12345"

    # Perform daily check-in for the test user
    result = daily_check_in(test_user_id)

    # Print the result
    print(result)
```
