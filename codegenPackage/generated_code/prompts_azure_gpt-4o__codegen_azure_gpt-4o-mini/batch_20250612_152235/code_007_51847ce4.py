"""
Generated Code Metadata:
========================
Original URL: https://paal-ai.pages.dev
Prompt: Generate code to track and log staking activity, including APR changes and ETH rewards share updates, for the Paal AI staking platform.
Generated: DETERMINISTIC_51847ce40598dd19
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    filename='staking_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class StakingActivityTracker:
    def __init__(self):
        """Initialize the StakingActivityTracker with an empty log."""
        self.activity_log: Dict[str, Any] = {}

    def log_activity(self, user_id: str, apr: float, eth_rewards: float) -> None:
        """
        Log staking activity for a user.

        Args:
            user_id (str): The ID of the user.
            apr (float): The Annual Percentage Rate for staking.
            eth_rewards (float): The amount of ETH rewards earned.

        Raises:
            ValueError: If APR or ETH rewards are negative.
        """
        if apr < 0:
            raise ValueError("APR cannot be negative.")
        if eth_rewards < 0:
            raise ValueError("ETH rewards cannot be negative.")

        # Create a log entry
        log_entry = {
            'user_id': user_id,
            'apr': apr,
            'eth_rewards': eth_rewards,
            'timestamp': datetime.now().isoformat()
        }

        # Append the log entry to the activity log
        self.activity_log[user_id] = log_entry

        # Log the activity
        logging.info(f"Logged activity for user {user_id}: {log_entry}")

    def get_activity(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve the staking activity for a specific user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            Dict[str, Any]: The staking activity log for the user.

        Raises:
            KeyError: If the user ID does not exist in the log.
        """
        if user_id not in self.activity_log:
            raise KeyError(f"No activity found for user ID: {user_id}")

        return self.activity_log[user_id]

    def update_apr(self, user_id: str, new_apr: float) -> None:
        """
        Update the APR for a user's staking activity.

        Args:
            user_id (str): The ID of the user.
            new_apr (float): The new Annual Percentage Rate.

        Raises:
            KeyError: If the user ID does not exist in the log.
            ValueError: If the new APR is negative.
        """
        if new_apr < 0:
            raise ValueError("New APR cannot be negative.")

        if user_id not in self.activity_log:
            raise KeyError(f"No activity found for user ID: {user_id}")

        # Update the APR in the log
        self.activity_log[user_id]['apr'] = new_apr
        logging.info(f"Updated APR for user {user_id} to {new_apr}")

    def update_eth_rewards(self, user_id: str, new_eth_rewards: float) -> None:
        """
        Update the ETH rewards for a user's staking activity.

        Args:
            user_id (str): The ID of the user.
            new_eth_rewards (float): The new amount of ETH rewards.

        Raises:
            KeyError: If the user ID does not exist in the log.
            ValueError: If the new ETH rewards are negative.
        """
        if new_eth_rewards < 0:
            raise ValueError("New ETH rewards cannot be negative.")

        if user_id not in self.activity_log:
            raise KeyError(f"No activity found for user ID: {user_id}")

        # Update the ETH rewards in the log
        self.activity_log[user_id]['eth_rewards'] = new_eth_rewards
        logging.info(f"Updated ETH rewards for user {user_id} to {new_eth_rewards}")

# Example usage
if __name__ == "__main__":
    tracker = StakingActivityTracker()
    try:
        tracker.log_activity("user123", 5.0, 0.1)
        tracker.update_apr("user123", 6.0)
        tracker.update_eth_rewards("user123", 0.15)
        activity = tracker.get_activity("user123")
        print(activity)
    except (ValueError, KeyError) as e:
        logging.error(f"Error occurred: {e}")
```
