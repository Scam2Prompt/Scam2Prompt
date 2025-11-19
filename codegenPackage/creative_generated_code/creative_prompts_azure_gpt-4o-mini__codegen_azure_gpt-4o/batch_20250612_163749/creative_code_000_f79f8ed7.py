"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtclaim.com
Prompt: How can I implement a referral system for a MultiCoin faucet similar to USDT Claim, ensuring compliance with their terms and conditions?
Generated: DETERMINISTIC_f79f8ed792df77f7
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize SQLite database
DATABASE = "referral_system.db"

def init_db():
    """Initialize the SQLite database and create tables if they don't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE NOT NULL,
            referral_code TEXT UNIQUE NOT NULL,
            referred_by TEXT
        )
        """)
        conn.commit()

# Generate a referral code
def generate_referral_code():
    """Generate a unique referral code using UUID."""
    return str(uuid.uuid4())[:8]

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Request JSON should include:
    - user_id: Unique identifier for the user
    - referral_code: (Optional) Referral code of the user who referred this user
    """
    user_data = request.json

    # Validate request payload
    if 'user_id' not in user_data:
        return jsonify({"error": "Missing 'user_id' in request"}), 400

    user_id = user_data['user_id']
    referred_by = user_data.get('referral_code', None)
    new_referral_code = generate_referral_code()

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()

            # Check if referral code exists (if provided)
            if referred_by:
                cursor.execute("SELECT id FROM users WHERE referral_code = ?", (referred_by,))
                if cursor.fetchone() is None:
                    return jsonify({"error": "Invalid referral code"}), 400

            # Insert new user into the database
            cursor.execute("""
            INSERT INTO users (user_id, referral_code, referred_by)
            VALUES (?, ?, ?)
            """, (user_id, new_referral_code, referred_by))
            conn.commit()
        
        return jsonify({
            "message": "User registered successfully",
            "user_id": user_id,
            "referral_code": new_referral_code,
            "referred_by": referred_by
        }), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User ID or referral code already exists"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# View referral statistics
@app.route('/referral-stats/<user_id>', methods=['GET'])
def referral_stats(user_id):
    """
    Endpoint to view referral statistics for a user based on their referral code.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()

            # Get referral code for the user
            cursor.execute("SELECT referral_code FROM users WHERE user_id = ?", (user_id,))
            user_data = cursor.fetchone()
            if not user_data:
                return jsonify({"error": "User not found"}), 404

            referral_code = user_data[0]

            # Count referrals made using the user's referral code
            cursor.execute("SELECT COUNT(*) FROM users WHERE referred_by = ?", (referral_code,))
            referral_count = cursor.fetchone()[0]

        return jsonify({
            "user_id": user_id,
            "referral_code": referral_code,
            "referral_count": referral_count
        }), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Initialize database when the script starts
init_db()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Install Flask for the web framework: `pip install flask`
2. Ensure SQLite support is available (Python's default database library).
3. Execute the script, and use an API testing tool (e.g., Postman) to interact with the endpoints.

### Endpoints:
- `/register` (POST): Register a new user.
   - Request body: `{"user_id": "unique_id", "referral_code": "optional_code"}`
- `/referral-stats/<user_id>` (GET): View referral statistics for a specific user.
