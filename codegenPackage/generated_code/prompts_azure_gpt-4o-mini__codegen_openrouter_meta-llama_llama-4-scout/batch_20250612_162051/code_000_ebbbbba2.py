"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Generate a Python script to create a maintenance notification system for a website, similar to the one described on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_ebbbbba2b00bc000
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maintenance_notification_system.py

import datetime
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MaintenanceNotificationSystem:
    def __init__(self, website_name: str, notifications: List[Dict]):
        """
        Initialize the maintenance notification system.

        Args:
        - website_name (str): The name of the website.
        - notifications (List[Dict]): A list of notification dictionaries.
            Each dictionary should contain the following keys:
                - start_time (datetime): The start time of the maintenance.
                - end_time (datetime): The end time of the maintenance.
                - message (str): The notification message.
        """
        self.website_name = website_name
        self.notifications = notifications

    def add_notification(self, notification: Dict):
        """
        Add a new notification.

        Args:
        - notification (Dict): A notification dictionary.
        """
        self.notifications.append(notification)

    def remove_notification(self, notification_index: int):
        """
        Remove a notification by its index.

        Args:
        - notification_index (int): The index of the notification to remove.
        """
        try:
            del self.notifications[notification_index]
        except IndexError:
            logger.error("Invalid notification index.")

    def get_active_notifications(self) -> List[Dict]:
        """
        Get a list of active notifications.

        Returns:
        - List[Dict]: A list of active notification dictionaries.
        """
        now = datetime.datetime.now()
        return [n for n in self.notifications if n['start_time'] <= now < n['end_time']]

    def send_notifications(self):
        """
        Send notifications to users.
        """
        active_notifications = self.get_active_notifications()
        for notification in active_notifications:
            # Replace this with your actual notification sending logic
            logger.info(f"Sending notification: {notification['message']}")

def main():
    # Example usage
    website_name = "Nasini Academy Hair Extension"
    notifications = [
        {
            'start_time': datetime.datetime(2024, 9, 16, 10, 0, 0),
            'end_time': datetime.datetime(2024, 9, 16, 12, 0, 0),
            'message': "The website is under maintenance. Please check back later."
        }
    ]

    system = MaintenanceNotificationSystem(website_name, notifications)
    system.send_notifications()

if __name__ == "__main__":
    main()
```
