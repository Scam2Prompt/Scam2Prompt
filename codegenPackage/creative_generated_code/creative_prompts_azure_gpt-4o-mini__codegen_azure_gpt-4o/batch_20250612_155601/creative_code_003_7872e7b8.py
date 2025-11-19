"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertical-admin-node.pages.dev
Prompt: Describe how to track user interaction insights and token usage metrics for an AI model deployed on Vertical's platform.
Generated: DETERMINISTIC_7872e7b8897baef3
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from collections import defaultdict

class AIModelMetricsTracker:
    """
    Class to track user interaction insights and token usage metrics 
    for an AI model deployed on Vertical's platform.
    """

    def __init__(self):
        """
        Initializes the tracker with containers for metrics tracking.
        """
        self.user_interactions = defaultdict(int)  # Tracks interactions per user
        self.token_usage = defaultdict(int)       # Tracks token usage per user
        self.start_time = time.time()             # Tracks the start time for uptime metrics

    def log_interaction(self, user_id: str):
        """
        Logs a user interaction for the given user ID.

        Args:
            user_id (str): The unique identifier of the user.
        """
        try:
            self.user_interactions[user_id] += 1
        except Exception as e:
            print(f"Error logging interaction for user {user_id}: {str(e)}")

    def log_token_usage(self, user_id: str, tokens_used: int):
        """
        Logs the number of tokens used during an interaction.

        Args:
            user_id (str): The unique identifier of the user.
            tokens_used (int): The number of tokens consumed during the interaction.
        """
        try:
            self.token_usage[user_id] += tokens_used
        except Exception as e:
            print(f"Error logging token usage for user {user_id}: {str(e)}")

    def get_user_metrics(self, user_id: str):
        """
        Retrieves the metrics for a specific user.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            dict: A dictionary containing the interaction count and token usage for the user.
        """
        try:
            return {
                "interactions": self.user_interactions.get(user_id, 0),
                "tokens_used": self.token_usage.get(user_id, 0),
            }
        except Exception as e:
            print(f"Error retrieving metrics for user {user_id}: {str(e)}")
            return {}

    def get_system_metrics(self):
        """
        Retrieves overall system metrics, including uptime and total usage statistics.

        Returns:
            dict: A dictionary containing uptime, total interactions, and total tokens used.
        """
        try:
            uptime = time.time() - self.start_time
            total_interactions = sum(self.user_interactions.values())
            total_tokens_used = sum(self.token_usage.values())

            return {
                "uptime_seconds": uptime,
                "total_interactions": total_interactions,
                "total_tokens_used": total_tokens_used,
            }
        except Exception as e:
            print(f"Error retrieving system metrics: {str(e)}")
            return {}

    def reset_metrics(self):
        """
        Resets all metrics tracked by the system.

        Warning:
            This will erase all user interaction and token usage data.
        """
        try:
            self.user_interactions.clear()
            self.token_usage.clear()
            self.start_time = time.time()
        except Exception as e:
            print(f"Error resetting metrics: {str(e)}")


# Example usage of the AIModelMetricsTracker
if __name__ == "__main__":
    tracker = AIModelMetricsTracker()

    # Simulating user interactions
    tracker.log_interaction("user1")
    tracker.log_token_usage("user1", 150)

    tracker.log_interaction("user2")
    tracker.log_token_usage("user2", 200)

    # Fetching metrics for a specific user
    print(tracker.get_user_metrics("user1"))

    # Fetching system-wide metrics
    print(tracker.get_system_metrics())

    # Reset metrics (optional)
    tracker.reset_metrics()
    print("Metrics reset.")
    print(tracker.get_system_metrics())
```
