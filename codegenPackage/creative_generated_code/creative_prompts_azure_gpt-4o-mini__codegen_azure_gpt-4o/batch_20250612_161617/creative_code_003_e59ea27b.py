"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftscalingzea.pages.dev
Prompt: Generate a script that allows users to invite others to earn $RIFT rewards on the Rift Swap platform.
Generated: DETERMINISTIC_e59ea27bd6c8bddf
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for storing user invitations (in-memory for simplicity)
invitations_db = []

# Define reward constant
REWARD_AMOUNT = 50  # $RIFT reward amount for successful invitation


def generate_invitation_code():
    """
    Generates a unique invitation code using UUID.
    """
    return str(uuid.uuid4())


@app.route('/invite', methods=['POST'])
def create_invitation():
    """
    Endpoint to create an invitation for a user.
    Expects a POST request with 'inviter_username' and 'invitee_email' in the JSON payload.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'inviter_username' not in data or 'invitee_email' not in data:
        return jsonify({"error": "Invalid request. 'inviter_username' and 'invitee_email' are required."}), 400

    inviter_username = data['inviter_username']
    invitee_email = data['invitee_email']

    # Generate a unique invitation code
    invitation_code = generate_invitation_code()

    # Save the invitation to the mock database
    # In production, this should be stored in a persistent database
    invitations_db.append({
        "inviter_username": inviter_username,
        "invitee_email": invitee_email,
        "invitation_code": invitation_code,
        "reward_claimed": False  # Track whether the reward was claimed
    })

    # Return the invitation code to the user
    return jsonify({
        "message": "Invitation created successfully!",
        "invitation_code": invitation_code
    }), 201


@app.route('/claim-reward', methods=['POST'])
def claim_reward():
    """
    Endpoint to claim the reward for a successful invitation.
    Expects a POST request with 'invitation_code' and 'invitee_username' in the JSON payload.
    """
    data = request.get_json()

    # Validate input data
    if not data or 'invitation_code' not in data or 'invitee_username' not in data:
        return jsonify({"error": "Invalid request. 'invitation_code' and 'invitee_username' are required."}), 400

    invitation_code = data['invitation_code']
    invitee_username = data['invitee_username']

    # Find the invitation in the database
    invitation = next((inv for inv in invitations_db if inv['invitation_code'] == invitation_code), None)

    if not invitation:
        return jsonify({"error": "Invalid invitation code."}), 404

    if invitation['reward_claimed']:
        return jsonify({"error": "Reward has already been claimed for this invitation."}), 400

    # Mark the reward as claimed
    invitation['reward_claimed'] = True

    # In production, reward distribution logic would be implemented here
    # For example, credit the $RIFT amount to the inviter's wallet/account

    return jsonify({
        "message": "Reward claimed successfully!",
        "reward_amount": REWARD_AMOUNT,
        "inviter_username": invitation['inviter_username'],
        "invitee_username": invitee_username
    }), 200


@app.route('/invitations', methods=['GET'])
def list_invitations():
    """
    Endpoint to list all invitations (for debugging/admin purposes).
    NOTE: This should be restricted in production.
    """
    return jsonify(invitations_db), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Features:
1. `/invite` endpoint allows users to create invitations.
2. `/claim-reward` endpoint lets users claim rewards for successful invitations.
3. `/invitations` endpoint lists all invitations (for debugging/admin purposes).
