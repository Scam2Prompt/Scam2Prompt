"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3wallets.pages.dev
Prompt: Write a script to implement spam and rate limit protections for notifications received via Web3Inbox.
Generated: DETERMINISTIC_aee6225b8059ac8c
Batch ID: 20250612_152018
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

class NotificationRateLimiter:
    """
    Implements spam and rate limit protections for notifications received via Web3Inbox.
    """

    def __init__(self, max_notifications_per_minute=10, ban_time_minutes=5):
        """
        Initializes the rate limiter.
        
        :param max_notifications_per_minute: Maximum allowed notifications per user per minute.
        :param ban_time_minutes: Duration for which the user is banned if they exceed the rate limit.
        """
        self.max_notifications_per_minute = max_notifications_per_minute
        self.ban_time_seconds = ban_time_minutes * 60
        self.notification_logs = defaultdict(list)  # Store timestamps of received notifications
        self.banned_users = {}  # Store user bans with expiration times
    
    def is_banned(self, user_id):
        """
        Checks if a user is currently banned.
        
        :param user_id: Unique identifier of the user.
        :return: True if the user is banned, False otherwise.
        """
        if user_id in self.banned_users:
            if time.time() > self.banned_users[user_id]:  # Ban expired
                del self.banned_users[user_id]
                return False
            return True
        return False

    def record_notification(self, user_id):
        """
        Records a notification received by the user, applying rate limit and spam protection.
        
        :param user_id: Unique identifier of the user.
        :return: A tuple (allowed, reason). `allowed` is True if the notification is allowed,
                 False otherwise, and `reason` explains the rejection if applicable.
        """
        current_time = time.time()

        # If banned, reject the notification
        if self.is_banned(user_id):
            return False, "User is banned due to exceeding rate limits."

        # Cleanup old logs (older than 1 minute)
        self.notification_logs[user_id] = [
            timestamp for timestamp in self.notification_logs[user_id]
            if current_time - timestamp <= 60
        ]

        # Check rate limit
        if len(self.notification_logs[user_id]) >= self.max_notifications_per_minute:
            self.banned_users[user_id] = current_time + self.ban_time_seconds
            return False, "Rate limit exceeded. User has been temporarily banned."

        # Record the notification timestamp
        self.notification_logs[user_id].append(current_time)
        return True, "Notification allowed."

# Example usage:
if __name__ == "__main__":
    rate_limiter = NotificationRateLimiter(max_notifications_per_minute=5, ban_time_minutes=2)

    user_id = "user123"
    
    # Simulate notifications
    for i in range(7):  # Sending more than the limit
        allowed, reason = rate_limiter.record_notification(user_id)
        print(f"Notification {i+1}: Allowed={allowed}, Reason='{reason}'")
        time.sleep(10)  # Simulate delays between notifications
```
