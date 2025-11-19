"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rembytservis02.ru
Prompt: Illustrate how to implement a notification system in a mobile app that alerts users when a technician is on their way to evaluate their used electronics, based on the service model described.
Generated: DETERMINISTIC_7fb06e131ca1f9b4
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from threading import Thread
from typing import List

class Notification:
    """Class to represent a notification with a message and a recipient."""
    
    def __init__(self, recipient: str, message: str):
        self.recipient = recipient
        self.message = message

    def send(self):
        """Simulate sending a notification to the recipient."""
        print(f"Sending notification to {self.recipient}: {self.message}")


class Technician:
    """Class to represent a technician."""
    
    def __init__(self, name: str):
        self.name = name

    def is_en_route(self) -> bool:
        """Simulate whether the technician is en route."""
        # Simulated probability of being en route
        return random.choice([True, False])


class NotificationSystem:
    """Class to manage notifications for users when technicians are on their way."""
    
    def __init__(self):
        self.subscribers: List[str] = []

    def subscribe(self, user: str):
        """Subscribe a user to the notification system."""
        if user not in self.subscribers:
            self.subscribers.append(user)
            print(f"{user} has subscribed to notifications.")

    def unsubscribe(self, user: str):
        """Unsubscribe a user from the notification system."""
        if user in self.subscribers:
            self.subscribers.remove(user)
            print(f"{user} has unsubscribed from notifications.")

    def notify_users(self, technician: Technician):
        """Notify all subscribed users when a technician is en route."""
        if technician.is_en_route():
            message = f"{technician.name} is on their way to evaluate your electronics!"
            for user in self.subscribers:
                notification = Notification(user, message)
                notification.send()
        else:
            print(f"{technician.name} is not en route.")


def technician_service(notification_system: NotificationSystem, technician: Technician):
    """Simulated service where a technician goes to evaluate electronics."""
    # Simulate some delay before the technician starts
    time.sleep(random.randint(1, 5))
    notification_system.notify_users(technician)


if __name__ == "__main__":
    # Create the notification system
    notification_system = NotificationSystem()
    
    # Subscribe users
    notification_system.subscribe("user1@example.com")
    notification_system.subscribe("user2@example.com")
    
    # Create a technician instance
    technician = Technician("John Doe")

    # Start technician service in a separate thread
    service_thread = Thread(target=technician_service, args=(notification_system, technician))
    
    # Start the technician service
    service_thread.start()
    
    # Wait for the service thread to complete
    service_thread.join()
```
