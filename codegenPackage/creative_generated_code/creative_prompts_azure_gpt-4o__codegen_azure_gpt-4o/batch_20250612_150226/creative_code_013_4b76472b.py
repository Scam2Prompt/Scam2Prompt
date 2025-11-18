"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kid-69m.pages.dev
Prompt: Write code for a pop-up event registration system for AKCB holders, prioritizing access for NFT owners while allowing limited spots for non-holders.
Generated: DETERMINISTIC_4b76472bfc7493be
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Event configuration
EVENT_NAME = "AKCB Exclusive Pop-up Event"
EVENT_DATE = datetime.datetime(2023, 11, 15, 18, 0)  # Event date and time
MAX_SPOTS = 100  # Total spots available
NON_HOLDER_SPOTS = 20  # Limited spots for non-NFT holders
registrations = []  # List to store registrations

# Sample NFT holder database for demonstration purposes
nft_holders = {
    "user1@example.com": True,
    "user2@example.com": True,
    "user3@example.com": True,
}  # Email mapping to whether the user is an NFT holder

# Error messages
ERROR_EVENT_FULL = "Event is fully booked."
ERROR_NON_HOLDER_LIMIT = "Non-holder spots are fully booked."
ERROR_ALREADY_REGISTERED = "User is already registered."
ERROR_INVALID_USER = "Invalid user data."

def is_nft_holder(email):
    """
    Check if the email belongs to an NFT holder.
    :param email: User's email address
    :return: Boolean indicating NFT holder status
    """
    return nft_holders.get(email, False)

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to handle user registrations for the event.
    Prioritizes NFT holders and limits non-holder spots.
    """
    try:
        # Parse incoming JSON data
        data = request.json
        email = data.get('email')
        name = data.get('name')

        # Validate input data
        if not email or not name:
            return jsonify({"error": ERROR_INVALID_USER}), 400

        # Ensure user is not already registered
        if any(reg['email'] == email for reg in registrations):
            return jsonify({"error": ERROR_ALREADY_REGISTERED}), 400

        # Check event capacity
        if len(registrations) >= MAX_SPOTS:
            return jsonify({"error": ERROR_EVENT_FULL}), 400

        # Determine user type (NFT holder or non-holder)
        user_type = "NFT Holder" if is_nft_holder(email) else "Non-Holder"

        # Handle registration logic
        if user_type == "Non-Holder":
            # Count non-holder registrations
            non_holder_count = sum(1 for reg in registrations if reg['type'] == "Non-Holder")
            if non_holder_count >= NON_HOLDER_SPOTS:
                return jsonify({"error": ERROR_NON_HOLDER_LIMIT}), 400

        # Register user
        registrations.append({
            "email": email,
            "name": name,
            "type": user_type,
            "registered_at": datetime.datetime.utcnow().isoformat()
        })

        return jsonify({
            "message": f"Successfully registered for {EVENT_NAME}.",
            "user": {"email": email, "name": name, "type": user_type}
        }), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": str(e)}), 500

@app.route('/event-info', methods=['GET'])
def event_info():
    """
    Endpoint to provide basic information about the event.
    """
    return jsonify({
        "event_name": EVENT_NAME,
        "event_date": EVENT_DATE.isoformat(),
        "max_spots": MAX_SPOTS,
        "available_spots": MAX_SPOTS - len(registrations),
        "non_holder_spots": NON_HOLDER_SPOTS,
        "non_holder_spots_available": NON_HOLDER_SPOTS - sum(1 for reg in registrations if reg['type'] == "Non-Holder"),
        "registrations": registrations
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
