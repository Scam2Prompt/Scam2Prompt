"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3inbox.com
Prompt: How does Web3Inbox ensure that users can opt-in to notifications and avoid spam?
Generated: DETERMINISTIC_e28337832352b3cc
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Web3Inbox:
    def __init__(self):
        """
        Initializes the Web3Inbox with an empty list of users and notifications.
        """
        self.users = {}
        self.notifications = []

    def opt_in(self, user_id):
        """
        Allows a user to opt-in for notifications.
        
        Parameters:
            user_id (str): The unique identifier for the user opting in.

        Raises:
            ValueError: If the user_id is already registered.
        """
        if user_id in self.users:
            raise ValueError("User is already opted in.")
        
        self.users[user_id] = {
            "opt_in": True,
            "notifications": []
        }
        print(f"User {user_id} has opted in for notifications.")

    def opt_out(self, user_id):
        """
        Allows a user to opt-out from notifications.

        Parameters:
            user_id (str): The unique identifier for the user opting out.
        
        Raises:
            KeyError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise KeyError("User not found.")
        
        self.users[user_id]["opt_in"] = False
        print(f"User {user_id} has opted out from notifications.")

    def send_notification(self, user_id, message):
        """
        Sends a notification to a user if they have opted in.
        
        Parameters:
            user_id (str): The unique identifier for the user receiving the notification.
            message (str): The notification message to be sent.

        Raises:
            KeyError: If the user_id does not exist.
            ValueError: If the user has opted out of notifications.
        """
        if user_id not in self.users:
            raise KeyError("User not found.")
        
        if not self.users[user_id]["opt_in"]:
            raise ValueError("User has opted out of notifications.")
        
        self.users[user_id]["notifications"].append(message)
        self.notifications.append((user_id, message))
        print(f"Notification sent to {user_id}: {message}")

    def get_user_notifications(self, user_id):
        """
        Retrieves all notifications for a specific user.

        Parameters:
            user_id (str): The unique identifier for the user.

        Returns:
            list: A list of notifications for the user.

        Raises:
            KeyError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise KeyError("User not found.")
        
        return self.users[user_id]["notifications"]

# Example usage:
if __name__ == "__main__":
    inbox = Web3Inbox()
    
    try:
        inbox.opt_in("user1")
        inbox.send_notification("user1", "Welcome to Web3Inbox!")
        inbox.send_notification("user1", "You have a new message.")
        
        print(inbox.get_user_notifications("user1"))
        
        inbox.opt_out("user1")
        inbox.send_notification("user1", "This message should not be sent.")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
