"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thelittlelineco.com
Prompt: Explain how to implement a subscription feature for email notifications in a Shopify store setup.
Generated: DETERMINISTIC_30df2e1255464f97
Batch ID: 20250612_155530
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
import re

app = Flask(__name__)

# Database setup
DB_NAME = 'subscriptions.db'

def initialize_database():
    """
    Initializes the SQLite database with a table for email subscriptions.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

initialize_database()

def is_valid_email(email):
    """
    Validates an email address using a regex pattern.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint for users to subscribe to email notifications.
    """
    try:
        # Extract email from the request
        email = request.json.get('email')
        if email is None or not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Insert email into the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Subscription successful'}), 200

    except sqlite3.IntegrityError:  # Handle duplicate emails
        return jsonify({'error': 'Email already subscribed'}), 409

    except Exception as e:
        # Generic error handling for unforeseen issues
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    """
    Endpoint for listing all subscribed emails (admin usage).
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscriptions")
        emails = [row[0] for row in cursor.fetchall()]
        conn.close()
        return jsonify({'subscriptions': emails}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
