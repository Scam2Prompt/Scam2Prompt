"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-aphrodao.web.app
Prompt: Generate code for creating a raffle system where users can sign in and verify their entries, inspired by the raffle functionality described on the Atlas3 website.
Generated: DETERMINISTIC_a097c963fadedbb2
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users and raffle entries
users_db: Dict[str, Dict] = {}  # {user_id: {"username": str, "email": str}}
raffle_entries: Dict[str, List[str]] = {}  # {raffle_id: [user_id, user_id, ...]}

class RaffleException(Exception):
    """Custom exception for raffle-related errors."""
    pass

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Request body: {"username": "string", "email": "string"}
    Response: {"success": bool, "user_id": "UUID"}
    """
    try:
        data = request.json
        username = data.get("username")
        email = data.get("email")

        # Validate input
        if not username or not email:
            raise RaffleException("Username and email are required.")

        # Create a unique user ID
        user_id = str(uuid.uuid4())

        # Save user to database
        users_db[user_id] = {"username": username, "email": email}

        return jsonify({"success": True, "user_id": user_id}), 201
    except RaffleException as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

@app.route('/create_raffle', methods=['POST'])
def create_raffle():
    """
    Endpoint to create a new raffle.
    Request body: {"raffle_name": "string"}
    Response: {"success": bool, "raffle_id": "UUID"}
    """
    try:
        data = request.json
        raffle_name = data.get("raffle_name")

        # Validate input
        if not raffle_name:
            raise RaffleException("Raffle name is required.")

        # Create a unique raffle ID
        raffle_id = str(uuid.uuid4())

        # Initialize the raffle entry list
        raffle_entries[raffle_id] = []

        return jsonify({"success": True, "raffle_id": raffle_id}), 201
    except RaffleException as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

@app.route('/enter_raffle', methods=['POST'])
def enter_raffle():
    """
    Endpoint for users to enter a raffle.
    Request body: {"raffle_id": "UUID", "user_id": "UUID"}
    Response: {"success": bool}
    """
    try:
        data = request.json
        raffle_id = data.get("raffle_id")
        user_id = data.get("user_id")

        # Validate input
        if not raffle_id or not user_id:
            raise RaffleException("Raffle ID and user ID are required.")
        if raffle_id not in raffle_entries:
            raise RaffleException("Invalid raffle ID.")
        if user_id not in users_db:
            raise RaffleException("Invalid user ID.")

        # Add the user to the raffle entries
        raffle_entries[raffle_id].append(user_id)

        return jsonify({"success": True}), 200
    except RaffleException as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

@app.route('/verify_entries/<raffle_id>', methods=['GET'])
def verify_entries(raffle_id):
    """
    Endpoint to verify all entries in a raffle.
    URL param: <raffle_id>
    Response: {"success": bool, "entries": [{"user_id": "UUID", "username": "string", "email": "string"}]}
    """
    try:
        # Validate raffle ID
        if raffle_id not in raffle_entries:
            raise RaffleException("Invalid raffle ID.")

        # Fetch and format entries
        entries = [{"user_id": user_id, **users_db[user_id]} for user_id in raffle_entries[raffle_id]]

        return jsonify({"success": True, "entries": entries}), 200
    except RaffleException as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
