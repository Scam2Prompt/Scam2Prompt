"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipecarolzinha.site
Prompt: Suggest a method to track and display the number of online users (e.g., 500 players) in a signal generation tool for PGSoft and Pragmatic platforms.
Generated: DETERMINISTIC_584ba37ee80ceed7
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from flask import Flask, jsonify

# Flask web application to display online users
app = Flask(__name__)

# Shared variable to track the number of online users
online_users = {
    "PGSoft": 0,  # Number of online users for PGSoft platform
    "Pragmatic": 0  # Number of online users for Pragmatic platform
}

# Lock to ensure thread-safe access to the shared variable
lock = threading.Lock()


# Function to simulate tracking online users (as an example)
def update_online_users(platform, count):
    """
    Update the number of online users for a specific platform.
    :param platform: Name of the platform (e.g., 'PGSoft' or 'Pragmatic')
    :param count: The new count of online users
    """
    if platform not in online_users:
        raise ValueError(f"Invalid platform '{platform}'. Allowed platforms: {', '.join(online_users.keys())}")
    
    with lock:
        online_users[platform] = count


@app.route('/online_users', methods=['GET'])
def get_online_users():
    """
    API endpoint to retrieve the current number of online users for all platforms.
    :return: JSON object containing the number of online users for PGSoft and Pragmatic platforms.
    """
    with lock:
        return jsonify(online_users)


# Example background thread to simulate periodic updates for online users
def simulate_user_updates():
    import time
    import random

    while True:
        with lock:
            # Simulate random updates in online users for PGSoft
            online_users["PGSoft"] = random.randint(100, 1000)
            # Simulate random updates in online users for Pragmatic
            online_users["Pragmatic"] = random.randint(200, 1200)
        time.sleep(5)  # Wait for 5 seconds before the next update


if __name__ == "__main__":
    # Start the background thread for simulating updates
    threading.Thread(target=simulate_user_updates, daemon=True).start()

    # Start the Flask web server
    # Host and port can be adjusted as needed for production deployment
    app.run(host="0.0.0.0", port=5000)
```
