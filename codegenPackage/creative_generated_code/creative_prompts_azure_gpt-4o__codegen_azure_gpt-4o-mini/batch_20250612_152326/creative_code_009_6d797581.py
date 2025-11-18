"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokens-jup.pages.dev
Prompt: Explain how to implement a live registry countdown timer for a blockchain event, ensuring synchronization with server time.
Generated: DETERMINISTIC_6d7975814add6afc
Batch ID: 20250612_152326
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
from flask import Flask, jsonify, request

app = Flask(__name__)

class CountdownTimer:
    def __init__(self, event_time):
        """
        Initializes the CountdownTimer with the specified event time.
        
        :param event_time: The datetime object representing the event start time.
        """
        self.event_time = event_time
        self.remaining_time = self.calculate_remaining_time()
        self.lock = threading.Lock()

    def calculate_remaining_time(self):
        """
        Calculates the remaining time until the event.
        
        :return: Remaining time in seconds.
        """
        now = datetime.utcnow()
        remaining = (self.event_time - now).total_seconds()
        return max(remaining, 0)  # Ensure non-negative

    def update_remaining_time(self):
        """
        Updates the remaining time by recalculating it on each tick.
        """
        with self.lock:
            self.remaining_time = self.calculate_remaining_time()

    def get_remaining_time(self):
        """
        Returns the current remaining time.
        
        :return: Remaining time in seconds.
        """
        with self.lock:
            return self.remaining_time

# Global variable to hold the countdown timer
countdown_timer = None

@app.route('/set_event_time', methods=['POST'])
def set_event_time():
    """
    API endpoint to set the event time for the countdown timer.
    
    Expects a JSON payload with a 'event_time' key in ISO format.
    Example: {"event_time": "2023-12-31T23:59:59Z"}
    
    :return: JSON response indicating success or failure.
    """
    global countdown_timer
    try:
        data = request.get_json()
        event_time = datetime.fromisoformat(data['event_time'].replace("Z", "+00:00"))  # Handle timezone
        countdown_timer = CountdownTimer(event_time)
        return jsonify({"message": "Event time set successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_remaining_time', methods=['GET'])
def get_remaining_time():
    """
    API endpoint to get the remaining time until the event.
    
    :return: JSON response containing remaining time in seconds.
    """
    if countdown_timer is None:
        return jsonify({"error": "Event time not set."}), 400
    
    remaining_time = countdown_timer.get_remaining_time()
    return jsonify({"remaining_time": remaining_time}), 200

def countdown_worker():
    """
    Background worker that updates the remaining time every second.
    This runs indefinitely until the application is stopped.
    """
    while True:
        if countdown_timer is not None:
            countdown_timer.update_remaining_time()
        time.sleep(1)  # Update every second

if __name__ == '__main__':
    # Start the countdown worker in a separate thread
    worker_thread = threading.Thread(target=countdown_worker, daemon=True)
    worker_thread.start()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)
```
