"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rickster.pages.dev
Prompt: Write code to integrate Relai's Bitcoin news subscription feature into a web application, allowing users to opt-in and manage their subscription preferences.
Generated: DETERMINISTIC_69435bd3758cc12d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
DB_FILE = "subscriptions.db"

def init_db():
    """Initialize the database and create necessary tables."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                subscribed BOOLEAN NOT NULL DEFAULT TRUE
            )
        """)
        conn.commit()

init_db()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to opt-in for Relai's Bitcoin news subscription.
    Expects JSON with the 'email' field.
    """
    data = request.json
    if 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400

    email = data['email']
    
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO subscriptions (email, subscribed)
                VALUES (?, ?)
            """, (email, True))
            conn.commit()
        return jsonify({'message': 'Subscription successful'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already subscribed'}), 409
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Endpoint to allow users to unsubscribe from Relai's Bitcoin news.
    Expects JSON with the 'email' field.
    """
    data = request.json
    if 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400

    email = data['email']
    
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE subscriptions
                SET subscribed = FALSE
                WHERE email = ?
            """, (email,))
            if cursor.rowcount == 0:
                return jsonify({'error': 'Email not found or not subscribed'}), 404
            conn.commit()
        return jsonify({'message': 'Unsubscription successful'}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    """
    Endpoint to retrieve all subscription preferences.
    """
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT email, subscribed
                FROM subscriptions
            """)
            subscriptions = [
                {'email': row[0], 'subscribed': bool(row[1])}
                for row in cursor.fetchall()
            ]
        return jsonify(subscriptions), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
