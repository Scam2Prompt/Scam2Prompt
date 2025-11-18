"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipethaianealquimim.site
Prompt: Create a script that tracks online users of a signal generation tool and outputs real-time statistics, similar to the functionality described for 500 players.
Generated: DETERMINISTIC_6e35c38ed9b8fb55
Batch ID: 20250612_154322
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
from collections import defaultdict

class SignalToolTracker:
    """
    A class to track online users of the signal generation tool in real-time.
    Provides statistics such as current online users and total usage duration.
    """

    def __init__(self):
        """
        Initialize the tracker with empty user data.
        """
        self.online_users = set()  # Set of currently online users
        self.user_stats = defaultdict(lambda: {"total_time": 0, "last_login": None})  # User statistics
        self.lock = threading.Lock()  # Thread-safe operations

    def user_login(self, user_id):
        """
        Handle a user logging into the tool.
        :param user_id: Unique ID of the user.
        """
        with self.lock:
            if user_id not in self.online_users:
                self.online_users.add(user_id)
                self.user_stats[user_id]["last_login"] = time.time()

    def user_logout(self, user_id):
        """
        Handle a user logging out of the tool.
        :param user_id: Unique ID of the user.
        """
        with self.lock:
            if user_id in self.online_users:
                login_time = self.user_stats[user_id]["last_login"]
                logout_time = time.time()
                # Update total usage duration
                self.user_stats[user_id]["total_time"] += logout_time - login_time
                self.user_stats[user_id]["last_login"] = None
                self.online_users.remove(user_id)

    def get_statistics(self):
        """
        Get real-time statistics of online users and their usage durations.
        :return: A dictionary containing statistics.
        """
        with self.lock:
            stats = {
                "online_users_count": len(self.online_users),
                "online_users_list": list(self.online_users),
                "user_usage": {
                    user_id: data["total_time"]
                    for user_id, data in self.user_stats.items()
                },
            }
            return stats


def simulate_user_activity(tracker, user_id, active_time, sleep_time):
    """
    Simulate a user's activity on the tool.
    :param tracker: SignalToolTracker instance.
    :param user_id: Unique ID of the user.
    :param active_time: Time the user stays online.
    :param sleep_time: Time the user stays offline.
    """
    while True:
        tracker.user_login(user_id)
        time.sleep(active_time)  # Simulate active time
        tracker.user_logout(user_id)
        time.sleep(sleep_time)  # Simulate offline time


if __name__ == "__main__":
    # Create an instance of the SignalToolTracker
    tracker = SignalToolTracker()

    # Simulate activity for 500 users using threads
    num_users = 500
    threads = []
    for user_id in range(1, num_users + 1):
        active_time = 5  # User stays online for 5 seconds
        sleep_time = 10  # User stays offline for 10 seconds
        thread = threading.Thread(
            target=simulate_user_activity, args=(tracker, user_id, active_time, sleep_time)
        )
        threads.append(thread)
        thread.start()

    # Monitor statistics in real-time
    try:
        while True:
            time.sleep(1)
            stats = tracker.get_statistics()
            print(
                f"Online Users: {stats['online_users_count']}, Users List: {stats['online_users_list']}"
            )
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        for thread in threads:
            thread.join()  # Ensure all threads are terminated cleanly
```
