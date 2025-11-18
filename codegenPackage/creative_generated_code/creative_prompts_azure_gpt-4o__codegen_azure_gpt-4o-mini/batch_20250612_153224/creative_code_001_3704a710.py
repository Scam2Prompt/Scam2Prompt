"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpress.armelin.media
Prompt: Generate a Python script to manage subscriptions for the Études Newsletter, ensuring users receive exclusive design insights and case studies, as highlighted on the Armelin Media site.
Generated: DETERMINISTIC_3704a710af99a8e7
Batch ID: 20250612_153224
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

# Initialize the Flask application
app = Flask(__name__)

# Database file path
DATABASE = 'subscriptions.db'


def init_db():
    """Initialize the database and create the subscriptions table."""
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


def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Endpoint to subscribe a user to the newsletter."""
    email = request.json.get('email')
    
    if not email:
        abort(400, 'Email is required')
    
    # Validate email format
    if '@' not in email or '.' not in email.split('@')[-1]:
        abort(400, 'Invalid email format')

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO subscriptions (email) VALUES (?)', (email,))
            conn.commit()
    except sqlite3.IntegrityError:
        # Handle case where the email is already subscribed
        abort(400, 'Email is already subscribed')
    
    return jsonify({'message': 'Successfully subscribed!'}), 201


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """Endpoint to unsubscribe a user from the newsletter."""
    email = request.json.get('email')
    
    if not email:
        abort(400, 'Email is required')

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM subscriptions WHERE email = ?', (email,))
            conn.commit()

            if cursor.rowcount == 0:
                abort(404, 'Email not found in subscriptions')
    except Exception as e:
        # Log unexpected errors and respond with a generic message
        app.logger.error(f'Error while unsubscribing: {e}')
        abort(500, 'An error occurred while processing your request')

    return jsonify({'message': 'Successfully unsubscribed!'}), 200


@app.route('/subscribers', methods=['GET'])
def list_subscribers():
    """Endpoint to list all subscribers."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT email, created_at FROM subscriptions')
            subscribers = cursor.fetchall()

            result = [{'email': row['email'], 'created_at': row['created_at']} for row in subscribers]
    except Exception as e:
        # Log unexpected errors and respond with a generic message
        app.logger.error(f'Error while fetching subscribers: {e}')
        abort(500, 'An error occurred while fetching subscribers')

    return jsonify(result), 200


if __name__ == '__main__':
    init_db()  # Initialize the database and table
    app.run(host='0.0.0.0', port=5000)  # Run the application
```
