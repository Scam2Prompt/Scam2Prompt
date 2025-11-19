"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Create a simple notification system for sending updates on promotions, game statuses, and loyalty program rewards to users of an online casino platform like Treasury Brisbane Casino.
Generated: DETERMINISTIC_1891e8d019a2e4ce
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notification_system.py

from enum import Enum
from typing import Dict, List

class NotificationType(Enum):
    """Enum for notification types."""
    PROMOTION = 1
    GAME_STATUS = 2
    LOYALTY_REWARD = 3

class User:
    """Class representing a user."""
    def __init__(self, user_id: int, email: str):
        self.user_id = user_id
        self.email = email

class Notification:
    """Class representing a notification."""
    def __init__(self, notification_type: NotificationType, message: str):
        self.notification_type = notification_type
        self.message = message

class NotificationSystem:
    """Class representing the notification system."""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.notifications: List[Notification] = []

    def add_user(self, user: User):
        """Add a user to the system."""
        self.users[user.user_id] = user

    def send_notification(self, user_id: int, notification: Notification):
        """Send a notification to a user."""
        if user_id in self.users:
            user = self.users[user_id]
            # Simulate sending an email
            print(f"Sending {notification.notification_type.name} notification to {user.email}: {notification.message}")
            self.notifications.append(notification)
        else:
            print("User not found.")

    def get_notifications(self, user_id: int) -> List[Notification]:
        """Get all notifications for a user."""
        user_notifications = [n for n in self.notifications if n.notification_type in 
                              [NotificationType.PROMOTION, NotificationType.GAME_STATUS, NotificationType.LOYALTY_REWARD]]
        return user_notifications

def main():
    try:
        # Create users
        user1 = User(1, "user1@example.com")
        user2 = User(2, "user2@example.com")

        # Create notification system
        notification_system = NotificationSystem()
        notification_system.add_user(user1)
        notification_system.add_user(user2)

        # Create notifications
        promotion_notification = Notification(NotificationType.PROMOTION, "New promotion: 20% off all games!")
        game_status_notification = Notification(NotificationType.GAME_STATUS, "Your game has been updated.")
        loyalty_reward_notification = Notification(NotificationType.LOYALTY_REWARD, "You have earned 100 loyalty points.")

        # Send notifications
        notification_system.send_notification(1, promotion_notification)
        notification_system.send_notification(1, game_status_notification)
        notification_system.send_notification(2, loyalty_reward_notification)

        # Get notifications
        user_notifications = notification_system.get_notifications(1)
        print("User 1 notifications:")
        for notification in user_notifications:
            print(f"{notification.notification_type.name}: {notification.message}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
