"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncrete.pages.dev
Prompt: Create a function to manage waitlist rankings and priority access for users in an appchain environment, similar to Concrete Protocol's approach.
Generated: DETERMINISTIC_891a143610f356f6
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class WaitlistManager:
    """
    A class to manage waitlist rankings and priority access for users.
    """

    def __init__(self):
        """
        Initializes the WaitlistManager with an empty waitlist.
        """
        self.waitlist: List[Dict] = []
        self.user_priority: Dict[str, int] = {}  # Store priority rankings for users

    def add_user(self, user_id: str, priority: int) -> None:
        """
        Adds a user to the waitlist with a specified priority.

        :param user_id: Unique ID of the user.
        :param priority: Priority ranking of the user (higher value = higher priority).
        """
        if user_id in self.user_priority:
            raise ValueError(f"User {user_id} is already in the waitlist.")

        self.user_priority[user_id] = priority
        self.waitlist.append({"user_id": user_id, "priority": priority})
        # Sort the waitlist based on priority in descending order
        self.waitlist.sort(key=lambda x: x["priority"], reverse=True)

    def remove_user(self, user_id: str) -> None:
        """
        Removes a user from the waitlist.

        :param user_id: Unique ID of the user to remove.
        """
        if user_id not in self.user_priority:
            raise ValueError(f"User {user_id} not found in the waitlist.")

        self.waitlist = [user for user in self.waitlist if user["user_id"] != user_id]
        del self.user_priority[user_id]

    def get_waitlist(self) -> List[Dict]:
        """
        Retrieves the current waitlist.

        :return: A list of users sorted by priority.
        """
        return self.waitlist

    def get_user_priority(self, user_id: str) -> int:
        """
        Retrieves the priority ranking of a specific user.

        :param user_id: Unique ID of the user.
        :return: Priority ranking of the user.
        """
        if user_id not in self.user_priority:
            raise ValueError(f"User {user_id} not found in the waitlist.")

        return self.user_priority[user_id]

    def update_priority(self, user_id: str, new_priority: int) -> None:
        """
        Updates the priority ranking of a user.

        :param user_id: Unique ID of the user.
        :param new_priority: New priority ranking for the user.
        """
        if user_id not in self.user_priority:
            raise ValueError(f"User {user_id} not found in the waitlist.")

        self.user_priority[user_id] = new_priority
        for user in self.waitlist:
            if user["user_id"] == user_id:
                user["priority"] = new_priority
                break

        # Re-sort the waitlist after updating the priority
        self.waitlist.sort(key=lambda x: x["priority"], reverse=True)

# Example usage (comment out if using in production code):
# manager = WaitlistManager()
# manager.add_user("user1", 5)
# manager.add_user("user2", 10)
# print(manager.get_waitlist())
# manager.update_priority("user1", 15)
# print(manager.get_waitlist())
# manager.remove_user("user2")
# print(manager.get_waitlist())
```
