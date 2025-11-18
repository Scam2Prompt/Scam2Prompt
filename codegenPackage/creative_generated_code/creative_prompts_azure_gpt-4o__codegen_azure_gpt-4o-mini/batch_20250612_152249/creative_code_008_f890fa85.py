"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Write code to implement a subscription system for early whitelist registration in the Rivalz TESTNET environment.
Generated: DETERMINISTIC_f890fa851937624d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DATABASE = 'subscriptions.db'

def init_db():
    """Initialize the SQLite database and create the subscriptions table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON response for HTTP exceptions."""
    response = e.get_response()
    response.data = jsonify({'error': str(e), 'status': e.code}).data
    response.content_type = "application/json"
    return response

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to add a new subscription to the whitelist."""
    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data:
        abort(400, 'Missing email in request.')

    email = data['email'].strip()

    # Validate email format
    if not validate_email(email):
        abort(400, 'Invalid email format.')

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
            conn.commit()
        return jsonify({'message': 'Successfully subscribed!', 'email': email}), 201

    except sqlite3.IntegrityError:
        abort(409, 'This email is already subscribed.')

    except Exception as e:
        abort(500, f'An unexpected error occurred: {str(e)}')

def validate_email(email):
    """Check if the email format is valid."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
```
