"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Build a notification system that delivers optimal crypto alerts without spamming users, inspired by the Champs Only unique alerts system.
Generated: DETERMINISTIC_1d8e1655db763e3e
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from datetime import datetime, timedelta
from typing import List, Dict, Callable


class CryptoNotificationSystem:
    """
    A system to send optimized crypto alerts to users without spamming them.
    """

    def __init__(self):
        # Dictionary to store user configurations and notification history
        self.users = {}  # {user_id: {"preferences": {}, "last_alert_time": datetime}}
        self.alert_callbacks = []  # List of functions to fetch crypto alerts
        self.notification_interval = timedelta(minutes=30)  # Minimum interval between notifications

    def register_user(self, user_id: str, preferences: Dict):
        """
        Register a new user with their preferences.
        :param user_id: Unique identifier of the user
        :param preferences: A dictionary containing user preferences e.g., {"BTC": {"price_change": 5}}
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        self.users[user_id] = {"preferences": preferences, "last_alert_time": None}

    def update_preferences(self, user_id: str, preferences: Dict):
        """
        Update preferences for an existing user.
        :param user_id: Unique identifier of the user
        :param preferences: A dictionary containing updated user preferences
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        self.users[user_id]["preferences"] = preferences

    def register_alert_callback(self, callback: Callable):
        """
        Register a callback function that fetches crypto alert data.
        :param callback: A function that returns a list of alerts in the format [{"symbol": "BTC", "message": "BTC up 10%"}]
        """
        self.alert_callbacks.append(callback)

    def send_notification(self, user_id: str, message: str):
        """
        Send a notification to the user.
        This function can be replaced with actual notification logic (e.g., email, SMS, push notification).
        :param user_id: Unique identifier of the user
        :param message: Message content of the notification
        """
        print(f"Notification to {user_id}: {message}")

    def should_notify(self, user_id: str) -> bool:
        """
        Determine whether a user should be notified based on the minimum notification interval.
        :param user_id: Unique identifier of the user
        :return: True if notification should be sent, False otherwise
        """
        last_alert_time = self.users[user_id]["last_alert_time"]
        if last_alert_time is None or datetime.now() - last_alert_time >= self.notification_interval:
            return True
        return False

    def process_alerts(self):
        """
        Fetch alerts from all registered callbacks and notify users based on their preferences.
        """
        for callback in self.alert_callbacks:
            try:
                # Fetch alerts
                alerts = callback()

                # Notify users based on their preferences
                for user_id, data in self.users.items():
                    preferences = data["preferences"]
                    for alert in alerts:
                        symbol = alert["symbol"]
                        message = alert["message"]

                        # Check if user is interested in this symbol and should be notified
                        if symbol in preferences and self.should_notify(user_id):
                            self.send_notification(user_id, message)
                            self.users[user_id]["last_alert_time"] = datetime.now()

            except Exception as e:
                # Log the error and continue processing other callbacks
                print(f"Error processing alerts: {e}")

    def start_system(self, interval: int = 60):
        """
        Start the notification system to check and send alerts at regular intervals.
        :param interval: Interval in seconds to fetch and process alerts
        """
        def run():
            while True:
                self.process_alerts()
                time.sleep(interval)

        # Run the system in a separate thread
        threading.Thread(target=run, daemon=True).start()


# Example usage
if __name__ == "__main__":
    notification_system = CryptoNotificationSystem()

    # Register a user with preferences
    notification_system.register_user("user123", {"BTC": {"price_change": 5}, "ETH": {"price_change": 10}})

    # Register a mock alert callback
    def mock_alert_callback() -> List[Dict]:
        # Simulated alerts
        return [{"symbol": "BTC", "message": "BTC is up 5%!"}, {"symbol": "ETH", "message": "ETH is up 10%!"}]

    notification_system.register_alert_callback(mock_alert_callback)

    # Start the notification system
    notification_system.start_system(interval=30)  # Check for alerts every 30 seconds

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Notification system stopped.")
```
