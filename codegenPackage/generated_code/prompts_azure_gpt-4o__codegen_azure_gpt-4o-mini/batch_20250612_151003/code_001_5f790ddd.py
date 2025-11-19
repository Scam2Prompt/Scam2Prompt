"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate code to track and display the leaderboard rankings for $BIGTIME token earnings, including functionality to invite friends using the Open Loot access code system.
Generated: DETERMINISTIC_5f790ddd94f2f74f
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for leaderboard and invites
leaderboard = []
invites = {}

# Data structure for leaderboard entries
class LeaderboardEntry:
    def __init__(self, username, earnings):
        self.username = username
        self.earnings = earnings

    def to_dict(self):
        return {
            'username': self.username,
            'earnings': self.earnings
        }

# Function to generate a unique access code
def generate_access_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# API endpoint to add earnings to the leaderboard
@app.route('/add_earnings', methods=['POST'])
def add_earnings():
    try:
        data = request.json
        username = data.get('username')
        earnings = data.get('earnings')

        if not username or not isinstance(earnings, (int, float)):
            return jsonify({'error': 'Invalid input'}), 400

        # Update or add the user to the leaderboard
        for entry in leaderboard:
            if entry.username == username:
                entry.earnings += earnings
                break
        else:
            leaderboard.append(LeaderboardEntry(username, earnings))

        # Sort leaderboard by earnings in descending order
        leaderboard.sort(key=lambda x: x.earnings, reverse=True)

        return jsonify({'message': 'Earnings added successfully', 'leaderboard': [entry.to_dict() for entry in leaderboard]}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        return jsonify([entry.to_dict() for entry in leaderboard]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to invite friends using an access code
@app.route('/invite', methods=['POST'])
def invite_friend():
    try:
        data = request.json
        inviter = data.get('inviter')
        invitee = data.get('invitee')

        if not inviter or not invitee:
            return jsonify({'error': 'Invalid input'}), 400

        access_code = generate_access_code()
        invites[access_code] = {'inviter': inviter, 'invitee': invitee}

        return jsonify({'message': 'Invitation sent', 'access_code': access_code}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to check invite status
@app.route('/check_invite/<access_code>', methods=['GET'])
def check_invite(access_code):
    try:
        invite = invites.get(access_code)
        if invite:
            return jsonify({'status': 'valid', 'invite': invite}), 200
        else:
            return jsonify({'status': 'invalid'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a simple Flask application to manage a leaderboard for $BIGTIME token earnings and includes functionality for inviting friends using an access code system. It includes error handling, input validation, and is structured for clarity and maintainability.
