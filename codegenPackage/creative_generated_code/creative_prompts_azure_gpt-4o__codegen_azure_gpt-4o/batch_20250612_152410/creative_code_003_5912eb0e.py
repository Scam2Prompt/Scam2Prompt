"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k7play.top
Prompt: Create a Python script to manage dual-user streaming plans, ensuring simultaneous access for two users, as described in K7 Play's service.
Generated: DETERMINISTIC_5912eb0e940fad6f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time
from datetime import datetime
from typing import Optional

class StreamingPlan:
    """
    Class to manage dual-user streaming plans.
    Ensures simultaneous access for two users.
    """

    def __init__(self, plan_name: str):
        """
        Initializes a streaming plan with a given name.

        :param plan_name: Name of the streaming plan
        """
        self.plan_name = plan_name
        self.active_users = {}  # Dictionary to store active users and their access timestamps
        self.lock = threading.Lock()  # Lock to prevent race conditions

    def request_access(self, user_id: str) -> bool:
        """
        Handles access requests from users.

        :param user_id: ID of the user requesting access
        :return: True if access is granted, False otherwise
        """
        with self.lock:
            # Remove inactive users (timed out after 15 minutes)
            self._remove_inactive_users()

            if len(self.active_users) < 2 or user_id in self.active_users:
                # Grant access if less than two users are active or if the user is already active
                self.active_users[user_id] = datetime.now()
                print(f"Access granted to user {user_id}.")
                return True
            else:
                # Deny access if two other users are already active
                print(f"Access denied to user {user_id}.")
                return False

    def end_access(self, user_id: str) -> None:
        """
        Ends access for a user.

        :param user_id: ID of the user whose access should be ended
        """
        with self.lock:
            if user_id in self.active_users:
                del self.active_users[user_id]
                print(f"Access ended for user {user_id}.")
            else:
                print(f"User {user_id} does not have active access.")

    def _remove_inactive_users(self) -> None:
        """
        Removes users who have been inactive for more than 15 minutes.
        """
        current_time = datetime.now()
        inactive_users = [
            user_id for user_id, last_active in self.active_users.items()
            if (current_time - last_active).total_seconds() > 15 * 60
        ]
        for user_id in inactive_users:
            del self.active_users[user_id]
            print(f"User {user_id} was removed due to inactivity.")

    def get_active_users(self) -> list:
        """
        Retrieves the list of active users.

        :return: List of active user IDs
        """
        with self.lock:
            # Remove inactive users before returning the list
            self._remove_inactive_users()
            return list(self.active_users.keys())


# Example usage
if __name__ == "__main__":
    streaming_plan = StreamingPlan("K7 Play Dual Streaming Plan")

    # Simulating user access requests
    print("\nSimulating access requests:")
    streaming_plan.request_access("User1")  # Access granted
    streaming_plan.request_access("User2")  # Access granted
    streaming_plan.request_access("User3")  # Access denied (max two users)

    # Simulating ending access for a user
    print("\nEnding access for User1:")
    streaming_plan.end_access("User1")  # Access ended for User1

    # Simulating access requests after User1 ends access
    print("\nAccess requests after User1 ends access:")
    streaming_plan.request_access("User3")  # Access granted

    # Displaying active users
    print("\nActive users:")
    print(streaming_plan.get_active_users())  # ['User2', 'User3']

    # Simulating timeout removal
    print("\nWaiting for 16 minutes to simulate timeout removal:")
    time.sleep(16 * 60)
    print("Active users after timeout:")
    print(streaming_plan.get_active_users())  # []
```
