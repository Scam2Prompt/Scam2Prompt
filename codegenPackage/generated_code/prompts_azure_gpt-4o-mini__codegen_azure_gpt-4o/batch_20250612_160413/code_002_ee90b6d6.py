"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Create a web application feature that allows users to sponsor a girl through a donation system, reflecting the "Adopt a Girl" initiative from My Flow Foundation.
Generated: DETERMINISTIC_ee90b6d6453ce434
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of the requested feature using Python with the Flask framework. It includes error handling, comments, and follows best practices.

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'donations.db'

def init_db():
    """Initialize the database with the necessary table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sponsorships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            amount REAL NOT NULL,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/sponsor', methods=['POST'])
def sponsor_girl():
    """
    Endpoint to sponsor a girl through a donation system.
    Expects JSON payload with 'name', 'email', 'amount', and optional 'message'.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        amount = data.get('amount')
        message = data.get('message', '')  # Optional field

        # Validate input
        if not name or not email or not amount:
            return jsonify({'error': 'Missing required fields: name, email, or amount'}), 400

        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({'error': 'Invalid donation amount'}), 400

        # Save the sponsorship to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sponsorships (name, email, amount, message)
            VALUES (?, ?, ?, ?)
        ''', (name, email, amount, message))
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({'message': 'Thank you for your sponsorship!', 'status': 'success'}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while processing your request', 'details': str(e)}), 500

@app.route('/sponsorships', methods=['GET'])
def get_sponsorships():
    """
    Endpoint to retrieve all sponsorships.
    Returns a list of sponsorships in JSON format.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, amount, message FROM sponsorships')
        sponsorships = cursor.fetchall()
        conn.close()

        # Format the data for JSON response
        sponsorships_list = [
            {'id': row[0], 'name': row[1], 'email': row[2], 'amount': row[3], 'message': row[4]}
            for row in sponsorships
        ]

        return jsonify({'sponsorships': sponsorships_list}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while retrieving sponsorships', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code assumes you have Python and Flask installed (`pip install flask`).
- The SQLite database (`donations.db`) will be created automatically in the same directory as the script.
- To test the endpoints, you can use tools like Postman or `curl`.
