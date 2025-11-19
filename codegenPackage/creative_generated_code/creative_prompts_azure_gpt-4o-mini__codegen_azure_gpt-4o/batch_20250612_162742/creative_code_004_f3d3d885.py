"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkmp.org
Prompt: Describe how to implement a user subscription feature for updates using Link Meeting Planner's upcoming services.
Generated: DETERMINISTIC_f3d3d8850fe7bc73
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a user subscription feature for updates using Link Meeting Planner's upcoming services.
Users can subscribe to receive notifications about new services and updates.
"""

from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database initialization and helper functions
DATABASE = 'subscriptions.db'

def init_db():
    """Initializes the database and creates required tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            subscribed_on TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_subscription(email: str):
    """Adds a new subscription to the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO subscriptions (email, subscribed_on)
            VALUES (?, ?)
        ''', (email, datetime.now()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Handles case where the email is already subscribed
        return False
    finally:
        conn.close()

# Initialize the database
init_db()

# API endpoints
@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint for users to subscribe for updates.
    Expected input: JSON payload { "email": "<user_email>" }
    Response: JSON indicating success or failure of the subscription.
    """
    try:
        # Parse the incoming request
        data = request.get_json()
        if not data or 'email' not in data:
            return jsonify({"error": "Invalid input, 'email' is required"}), 400

        email = data['email'].strip()
        if not email:
            return jsonify({"error": "Email cannot be empty"}), 400

        # Add subscription to the database
        success = add_subscription(email)
        if success:
            return jsonify({"message": f"Subscription successful for {email}!"}), 200
        else:
            return jsonify({"error": f"Email {email} is already subscribed"}), 400
    except Exception as e:
        # Generic error handling for unexpected issues
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    """
    Endpoint to retrieve all subscribers. 
    Only for demonstration purposes; in production use authentication to protect this route.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT email, subscribed_on FROM subscriptions')
        subscribers = [{"email": row[0], "subscribed_on": row[1]} for row in cursor.fetchall()]
        conn.close()
        return jsonify({"subscribers": subscribers}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Main program
if __name__ == '__main__':
    """Runs the Flask application."""
    app.run(debug=False)  # Disable debug mode in production
```
