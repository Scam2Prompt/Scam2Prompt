"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyatoken.net
Prompt: Generate code to implement a feature for users to opt-in or opt-out of newsletters and promotional communications, adhering to the privacy policy guidelines of nyatoken.net.
Generated: DETERMINISTIC_308714417401e0a8
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required libraries
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE = 'newsletter_preferences.db'

def init_db():
    """
    Initialize the database and create the table for storing user preferences.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            newsletter_opt_in BOOLEAN NOT NULL,
            promo_opt_in BOOLEAN NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/update_preferences', methods=['POST'])
def update_preferences():
    """
    API endpoint for users to update their preferences for newsletters and promotional communications.
    """
    try:
        # Parse the request JSON
        data = request.json
        email = data.get('email')
        newsletter_opt_in = data.get('newsletter_opt_in')
        promo_opt_in = data.get('promo_opt_in')

        # Validate input
        if not email or newsletter_opt_in is None or promo_opt_in is None:
            return jsonify({"error": "Invalid input. Email, newsletter_opt_in, and promo_opt_in are required."}), 400
        
        # Validate email format (basic validation)
        if "@" not in email or "." not in email:
            return jsonify({"error": "Invalid email format."}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Update or insert user preferences
        cursor.execute("""
            INSERT INTO user_preferences (email, newsletter_opt_in, promo_opt_in)
            VALUES (?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
            newsletter_opt_in=excluded.newsletter_opt_in,
            promo_opt_in=excluded.promo_opt_in
        """, (email, newsletter_opt_in, promo_opt_in))
        
        conn.commit()
        conn.close()

        return jsonify({"message": "Preferences updated successfully."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    """
    API endpoint to retrieve user preferences based on their email address.
    """
    try:
        # Get email parameter from query
        email = request.args.get('email')

        if not email:
            return jsonify({"error": "Email parameter is required."}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch preferences from the database
        cursor.execute("SELECT newsletter_opt_in, promo_opt_in FROM user_preferences WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return jsonify({
                "email": email,
                "newsletter_opt_in": bool(result[0]),
                "promo_opt_in": bool(result[1])
            }), 200
        else:
            return jsonify({"error": "No preferences found for the given email."}), 404

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
