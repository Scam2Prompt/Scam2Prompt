"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipeleiafreitas.site
Prompt: Create a function to track and display the number of active users in real-time, as described on the webpage.
Generated: DETERMINISTIC_b230da5f1a5e1fbd
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
import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Global variable to hold the count of active users
active_users = 0
lock = threading.Lock()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/track_user', methods=['POST'])
def track_user():
    """Track a user when they connect to the application."""
    global active_users
    with lock:
        active_users += 1
    return jsonify({'active_users': active_users}), 200

@app.route('/untrack_user', methods=['POST'])
def untrack_user():
    """Track a user when they disconnect from the application."""
    global active_users
    with lock:
        if active_users > 0:
            active_users -= 1
    return jsonify({'active_users': active_users}), 200

@app.route('/active_users', methods=['GET'])
def get_active_users():
    """Return the current count of active users."""
    with lock:
        return jsonify({'active_users': active_users}), 200

def start_background_server():
    """Start a background thread to run the Flask app."""
    app.run(threaded=True)

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    server_thread = threading.Thread(target=start_background_server)
    server_thread.start()

    # Simulate user activity (for demonstration purposes)
    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Shutting down the server...")

```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Active Users Tracker</title>
    <script>
        // Function to track user connection
        function trackUser() {
            fetch('/track_user', {method: 'POST'});
        }

        // Function to untrack user disconnection
        function untrackUser() {
            fetch('/untrack_user', {method: 'POST'});
        }

        // Function to periodically fetch the number of active users
        async function fetchActiveUsers() {
            const response = await fetch('/active_users');
            const data = await response.json();
            document.getElementById('active-users-count').innerText = data.active_users;
        }

        // Set up event listeners on window load
        window.onload = function() {
            trackUser(); // Track user when they load the page
            setInterval(fetchActiveUsers, 1000); // Fetch active users every second
        };

        // Untrack user on window unload
        window.onbeforeunload = untrackUser;
    </script>
</head>
<body>
    <h1>Active Users Tracker</h1>
    <p>Current Active Users: <span id="active-users-count">0</span></p>
</body>
</html>
```
