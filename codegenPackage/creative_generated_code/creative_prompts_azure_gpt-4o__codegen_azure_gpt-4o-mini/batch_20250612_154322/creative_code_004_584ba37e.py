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
import time
import threading
from flask import Flask, jsonify

app = Flask(__name__)

# Shared variable to track the number of online users
online_users_count = 0
count_lock = threading.Lock()

@app.route('/api/online_users', methods=['GET'])
def get_online_users():
    """API endpoint to retrieve the current number of online users."""
    with count_lock:
        return jsonify({"online_users": online_users_count})

def user_connect():
    """Simulates a user connecting to the platform."""
    global online_users_count
    with count_lock:
        online_users_count += 1
        print(f"User connected. Total online users: {online_users_count}")

def user_disconnect():
    """Simulates a user disconnecting from the platform."""
    global online_users_count
    with count_lock:
        online_users_count = max(0, online_users_count - 1)
        print(f"User disconnected. Total online users: {online_users_count}")

def simulate_user_activity():
    """Simulates user connections and disconnections."""
    while True:
        user_connect()
        time.sleep(1)  # Simulate a user staying online for a bit
        user_disconnect()
        time.sleep(2)  # Simulate a pause before the next connection

if __name__ == '__main__':
    # Start the simulation of user activity in a separate thread
    threading.Thread(target=simulate_user_activity, daemon=True).start()
    
    # Start the Flask web server
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

Make sure to install Flask by running `pip install Flask` before executing the code. The example simulates user connections and disconnections and provides an API endpoint to track the number of online users.
