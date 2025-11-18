"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-3zc.pages.dev
Prompt: Write code for tracking and displaying real-time user metrics, such as "Users Online" and "Total Users," as shown on the Sophon webpage.
Generated: DETERMINISTIC_173be3d217d2b706
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from flask import Flask, jsonify
from threading import Lock

app = Flask(__name__)

# Shared data structure with thread-safe access
class MetricsTracker:
    def __init__(self):
        self.total_users = 0  # Total number of users who have ever visited
        self.users_online = 0  # Number of users currently online
        self.lock = Lock()    # Lock for thread-safe operations

    def user_connected(self):
        """Increment metrics when a user connects."""
        with self.lock:
            self.total_users += 1
            self.users_online += 1

    def user_disconnected(self):
        """Decrement users_online when a user disconnects."""
        with self.lock:
            if self.users_online > 0:  # Ensure users_online doesn't go below 0
                self.users_online -= 1

    def get_metrics(self):
        """Return current metrics as a dictionary."""
        with self.lock:
            return {"users_online": self.users_online, "total_users": self.total_users}


# Create a global instance of the metrics tracker
metrics_tracker = MetricsTracker()


@app.route("/connect", methods=["POST"])
def connect_user():
    """
    Simulate a user connecting to the application.
    This endpoint increments the 'users_online' and 'total_users'.
    """
    metrics_tracker.user_connected()
    return jsonify({"message": "User connected", "metrics": metrics_tracker.get_metrics()}), 200


@app.route("/disconnect", methods=["POST"])
def disconnect_user():
    """
    Simulate a user disconnecting from the application.
    This endpoint decrements the 'users_online'.
    """
    metrics_tracker.user_disconnected()
    return jsonify({"message": "User disconnected", "metrics": metrics_tracker.get_metrics()}), 200


@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    Retrieve real-time user metrics such as 'Users Online' and 'Total Users'.
    """
    return jsonify(metrics_tracker.get_metrics()), 200


if __name__ == "__main__":
    # Run the Flask application on the local server
    app.run(host="0.0.0.0", port=5000, debug=False)
```
