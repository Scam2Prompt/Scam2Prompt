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
import random
import threading
from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable to track online users
online_users = set()

# Lock for thread-safe access to online_users
lock = threading.Lock()

def generate_user_id():
    """Generate a random user ID."""
    return f"user_{random.randint(1000, 9999)}"

def simulate_user_activity():
    """Simulate user activity by randomly adding and removing users."""
    while True:
        with lock:
            # Randomly decide to add or remove a user
            if random.choice([True, False]):
                user_id = generate_user_id()
                online_users.add(user_id)
            else:
                if online_users:
                    online_users.remove(random.choice(list(online_users)))
        time.sleep(random.uniform(1, 3))  # Wait before the next action

@app.route('/stats', methods=['GET'])
def get_stats():
    """Return real-time statistics of online users."""
    with lock:
        # Create a response with the count of online users and their IDs
        response = {
            'online_user_count': len(online_users),
            'online_users': list(online_users)
        }
    return jsonify(response)

if __name__ == '__main__':
    # Start the user activity simulation in a separate thread
    threading.Thread(target=simulate_user_activity, daemon=True).start()
    
    # Start the Flask web server
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {e}")
```
