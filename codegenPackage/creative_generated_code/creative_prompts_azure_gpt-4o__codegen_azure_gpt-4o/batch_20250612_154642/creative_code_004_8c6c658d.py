"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Provide code to integrate a subscription-based newsletter feature into a website, inspired by Études' research communications and case studies.
Generated: DETERMINISTIC_8c6c658df5cc6610
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example implementation in Python using Flask for the backend of a subscription-based newsletter feature:

```python
from flask import Flask, request, jsonify
import sqlite3
import re

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DB_NAME = 'newsletter.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Helper function for validating email addresses
def is_valid_email(email):
    """
    Validates an email address using regex.
    Returns True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe to the newsletter.
    Expects JSON data in the format:
    {
        "email": "user@example.com",
        "name": "User Name"
    }
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'email' not in data or 'name' not in data:
        return jsonify({"error": "Invalid input. 'email' and 'name' are required."}), 400
    
    email = data['email'].strip()
    name = data['name'].strip()

    # Validate email format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    try:
        # Add subscriber to the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subscribers (email, name) VALUES (?, ?)', (email, name))
        conn.commit()
        conn.close()

        return jsonify({"message": "Successfully subscribed!"}), 200
    except sqlite3.IntegrityError:
        # Handle duplicate email addresses
        return jsonify({"error": "Email is already subscribed."}), 409
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    """
    Endpoint to fetch all current subscribers.
    Returns a JSON list of subscribers in the format:
    [
        {
            "id": 1,
            "email": "user@example.com",
            "name": "User Name"
        },
        ...
    ]
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT id, email, name FROM subscribers')
        subscribers = cursor.fetchall()
        conn.close()

        # Transform database rows into a list of dictionaries
        subscriber_list = [
            {"id": row[0], "email": row[1], "name": row[2]} for row in subscribers
        ]
        return jsonify(subscriber_list), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Install Flask (`pip install flask`) and ensure SQLite is available.
2. The code creates a simple newsletter subscription feature with endpoints for subscribing and listing subscribers.
3. Ensure the `newsletter.db` file is writable by the application.
