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
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection setup
DATABASE = 'users.db'

def init_db():
    """Initialize the database and create the necessary table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_preferences (
                user_id INTEGER PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                newsletter_opt_in BOOLEAN NOT NULL DEFAULT 0,
                promotional_opt_in BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

@app.route('/opt-in', methods=['POST'])
def opt_in():
    """Endpoint for users to opt-in to newsletters and promotional communications."""
    data = request.json
    email = data.get('email')
    newsletter = data.get('newsletter', True)
    promotional = data.get('promotional', True)

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_preferences (email, newsletter_opt_in, promotional_opt_in)
                VALUES (?, ?, ?)
                ON CONFLICT(email) 
                DO UPDATE SET 
                    newsletter_opt_in = ?,
                    promotional_opt_in = ?
            ''', (email, newsletter, promotional, newsletter, promotional))
            conn.commit()
        return jsonify({"message": "Preferences updated successfully"}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route('/opt-out', methods=['POST'])
def opt_out():
    """Endpoint for users to opt-out of newsletters and promotional communications."""
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_preferences (email, newsletter_opt_in, promotional_opt_in)
                VALUES (?, 0, 0)
                ON CONFLICT(email) 
                DO UPDATE SET 
                    newsletter_opt_in = 0,
                    promotional_opt_in = 0
            ''', (email,))
            conn.commit()
        return jsonify({"message": "Preferences updated successfully"}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route('/preferences', methods=['GET'])
def get_preferences():
    """Endpoint to retrieve a user's newsletter and promotional preferences."""
    email = request.args.get('email')
    
    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT newsletter_opt_in, promotional_opt_in FROM user_preferences WHERE email = ?', (email,))
            preferences = cursor.fetchone()
            if preferences is None:
                return jsonify({"message": "No preferences found for this email"}), 404

            return jsonify({
                "newsletter_opt_in": bool(preferences[0]),
                "promotional_opt_in": bool(preferences[1])
            }), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=True)
```
