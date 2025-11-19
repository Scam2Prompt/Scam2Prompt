"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grass-8xn.pages.dev
Prompt: Generate a code snippet for a web application that tracks the status of the Grass airdrop and notifies users when they can check their eligibility.
Generated: DETERMINISTIC_652ce79726eba5c2
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application to track Grass airdrop status and notify users when eligible

from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Mock data to simulate airdrop status
airdrops = [
    {
        "id": 1,
        "name": "Grass Airdrop",
        "status": "pending",  # Possible statuses: "pending", "active", "completed"
        "start_time": "2023-10-15T00:00:00",
        "end_time": "2023-11-01T23:59:59"
    }
]

subscribers = []  # List to store subscriber email addresses


def is_airdrop_active(start_time, end_time):
    """
    Check if the Grass airdrop is currently active based on the given start and end times.
    """
    try:
        now = datetime.datetime.now()
        start = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
        end = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")
        return start <= now <= end
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return False


@app.route('/check-status', methods=['GET'])
def check_status():
    """
    Endpoint to check the status of the Grass airdrop.
    Returns the current status and eligibility information.
    """
    try:
        airdrop = airdrops[0]  # Assuming only one airdrop for simplicity
        is_active = is_airdrop_active(airdrop["start_time"], airdrop["end_time"])

        if is_active:
            return jsonify({"status": "active", "message": "The Grass airdrop is now active. Check your eligibility!"}), 200
        else:
            return jsonify({"status": airdrop["status"], "message": "The Grass airdrop is not active yet."}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while checking the status.", "details": str(e)}), 500


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe for notifications regarding the Grass airdrop.
    Expects a JSON payload with an email address.
    """
    try:
        data = request.get_json()
        email = data.get("email")

        if not email:
            return jsonify({"error": "Invalid request. Email is required."}), 400

        if email in subscribers:
            return jsonify({"message": "You are already subscribed for Grass airdrop notifications."}), 200

        subscribers.append(email)
        return jsonify({"message": "Subscription successful. You will be notified when the airdrop is active."}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred during subscription.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
