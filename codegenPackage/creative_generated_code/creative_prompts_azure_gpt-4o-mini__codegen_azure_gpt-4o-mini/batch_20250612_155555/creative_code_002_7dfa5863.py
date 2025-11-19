"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mebounty.com
Prompt: How do I use the Mebounty library to track user engagement and rewards?
Generated: DETERMINISTIC_7dfa586314abdbf1
Batch ID: 20250612_155555
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mebounty

class UserEngagementTracker:
    def __init__(self, api_key):
        """
        Initializes the UserEngagementTracker with the given API key.
        
        :param api_key: str - The API key for authenticating with the Mebounty service.
        """
        if not api_key:
            raise ValueError("API key must not be empty.")
        self.client = mebounty.Client(api_key)

    def track_engagement(self, user_id, engagement_type):
        """
        Tracks user engagement by sending data to the Mebounty service.
        
        :param user_id: str - Unique identifier for the user.
        :param engagement_type: str - The type of engagement (e.g., 'click', 'view', 'share').
        :raises ValueError: If user_id or engagement_type is invalid.
        :raises Exception: For any issues encountered during tracking.
        """
        if not user_id or not engagement_type:
            raise ValueError("Both user_id and engagement_type must be provided.")

        try:
            # Prepare engagement data
            engagement_data = {
                'user_id': user_id,
                'engagement_type': engagement_type,
                'timestamp': mebounty.utils.current_timestamp()
            }
            # Send engagement data to Mebounty
            response = self.client.track_engagement(engagement_data)
            if response.status_code != 200:
                raise Exception("Failed to track engagement: {}".format(response.message))
            print("Engagement tracked successfully for user: {}".format(user_id))
        except Exception as e:
            print("Error tracking engagement: {}".format(e))
            raise

    def reward_user(self, user_id, reward_amount):
        """
        Rewards a user with the specified amount through the Mebounty service.
        
        :param user_id: str - Unique identifier for the user.
        :param reward_amount: float - The amount of reward to give to the user.
        :raises ValueError: If user_id is invalid or reward_amount is non-positive.
        :raises Exception: For any issues encountered during the reward process.
        """
        if not user_id:
            raise ValueError("user_id must be provided.")
        if reward_amount <= 0:
            raise ValueError("Reward amount must be greater than zero.")

        try:
            # Prepare reward data
            reward_data = {
                'user_id': user_id,
                'amount': reward_amount
            }
            # Send reward data to Mebounty
            response = self.client.reward_user(reward_data)
            if response.status_code != 200:
                raise Exception("Failed to reward user: {}".format(response.message))
            print("User rewarded successfully: {}".format(user_id))
        except Exception as e:
            print("Error rewarding user: {}".format(e))
            raise

# Example of usage
if __name__ == "__main__":
    try:
        tracker = UserEngagementTracker(api_key='YOUR_API_KEY_HERE')
        tracker.track_engagement(user_id='user123', engagement_type='click')
        tracker.reward_user(user_id='user123', reward_amount=10.00)
    except Exception as e:
        print("An error occurred: {}".format(e))
```
