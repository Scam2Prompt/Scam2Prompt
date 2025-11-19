"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-runes.pages.dev
Prompt: What are the steps to implement a feature that allows users to dismiss notifications from the Dog Runestone Snapshot app?
Generated: DETERMINISTIC_6f396b2626c837c3
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notification_manager.py

class Notification:
    """Class representing a notification."""
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.dismissed = False

    def dismiss(self):
        """Mark the notification as dismissed."""
        self.dismissed = True

class NotificationManager:
    """Class managing a list of notifications."""
    
    def __init__(self):
        self.notifications = {}

    def add_notification(self, notification: Notification):
        """Add a new notification to the manager."""
        if notification.id in self.notifications:
            raise ValueError(f"Notification with id {notification.id} already exists.")
        self.notifications[notification.id] = notification

    def dismiss_notification(self, notification_id: int):
        """Dismiss a notification by its ID."""
        try:
            notification = self.notifications[notification_id]
            notification.dismiss()
            print(f"Notification {notification_id} dismissed.")
        except KeyError:
            print(f"Error: Notification with id {notification_id} does not exist.")

    def get_active_notifications(self):
        """Retrieve a list of active notifications."""
        return [notif for notif in self.notifications.values() if not notif.dismissed]

# Example usage:
if __name__ == "__main__":
    # Create a notification manager instance
    manager = NotificationManager()

    # Create and add notifications
    notification1 = Notification(1, "Dog Run is scheduled for today at 5 PM.")
    notification2 = Notification(2, "New Dog Park opened nearby!")
    
    manager.add_notification(notification1)
    manager.add_notification(notification2)

    # Dismiss a notification
    manager.dismiss_notification(1)

    # List active notifications
    active_notifications = manager.get_active_notifications()
    print("Active Notifications:")
    for notif in active_notifications:
        print(f"- {notif.message}")
```
