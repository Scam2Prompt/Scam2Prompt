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
import threading
from flask import Flask, jsonify

app = Flask(__name__)

# Global variables to track user metrics
total_users = 0
active_users = 0
active_users_lock = threading.Lock()

# Function to simulate user activity, incrementing active users
def simulate_user_activity():
    global total_users, active_users
    while True:
        with active_users_lock:
            active_users += 1  # A user comes online
            total_users += 1  # Each new user increments the total count
        time.sleep(5)  # Simulate a user being online for 5 seconds
        with active_users_lock:
            active_users -= 1  # A user goes offline
        time.sleep(2)  # Wait before the next user activity

# Route to get the current user metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Return the current user metrics in JSON format."""
    try:
        with active_users_lock:
            metrics = {
                'total_users': total_users,
                'active_users': active_users
            }
        return jsonify(metrics), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the user activity simulation in a separate thread
    threading.Thread(target=simulate_user_activity, daemon=True).start()
    try:
        # Start the Flask application
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the application: {e}")
```
