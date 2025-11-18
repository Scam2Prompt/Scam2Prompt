"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate code to track and display the leaderboard rankings for $BIGTIME token earnings, including functionality to invite friends using the Open Loot access code system.
Generated: DETERMINISTIC_5f790ddd94f2f74f
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to track leaderboard and invitations
leaderboard = {}  # Format: {"user_id": {"username": "name", "earnings": amount}}
invitations = {}  # Format: {"invite_code": {"inviter_id": user_id, "invitee_id": user_id}}

# Generate a unique invite code
def generate_invite_code():
    return str(uuid.uuid4())

# Route to add earnings for a user
@app.route('/add_earnings', methods=['POST'])
def add_earnings():
    try:
        data = request.json
        user_id = data['user_id']
        username = data['username']
        earnings = data['earnings']
        
        if user_id in leaderboard:
            leaderboard[user_id]['earnings'] += earnings
        else:
            leaderboard[user_id] = {"username": username, "earnings": earnings}

        return jsonify({"message": "Earnings updated successfully.", "leaderboard": leaderboard}), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to retrieve the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1]['earnings'], reverse=True)
        return jsonify({"leaderboard": sorted_leaderboard}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to generate an invite code
@app.route('/generate_invite', methods=['POST'])
def generate_invite():
    try:
        data = request.json
        inviter_id = data['inviter_id']
        
        if inviter_id not in leaderboard:
            return jsonify({"error": "Inviter ID not found in leaderboard."}), 404

        invite_code = generate_invite_code()
        invitations[invite_code] = {"inviter_id": inviter_id, "invitee_id": None}
        
        return jsonify({"message": "Invite code generated successfully.", "invite_code": invite_code}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to accept an invite
@app.route('/accept_invite', methods=['POST'])
def accept_invite():
    try:
        data = request.json
        invite_code = data['invite_code']
        invitee_id = data['invitee_id']
        invitee_username = data['invitee_username']
        
        if invite_code not in invitations:
            return jsonify({"error": "Invalid invite code."}), 404
        
        if invitations[invite_code]['invitee_id']:
            return jsonify({"error": "Invite code already used."}), 400

        # Add invitee to the leaderboard
        leaderboard[invitee_id] = {"username": invitee_username, "earnings": 0}
        invitations[invite_code]['invitee_id'] = invitee_id
        
        return jsonify({"message": "Invite accepted successfully.", "leaderboard": leaderboard}), 200
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
