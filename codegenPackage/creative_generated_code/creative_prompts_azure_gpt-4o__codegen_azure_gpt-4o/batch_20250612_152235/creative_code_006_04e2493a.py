"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainfare.pages.dev
Prompt: Create a script to subscribe users to a newsletter for blockchain updates, as mentioned in the Chainfare site's functionality.
Generated: DETERMINISTIC_04e2493a33b02880
Batch ID: 20250612_152235
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

# Database setup
DATABASE = 'newsletter.db'

def init_db():
    """Initialize the database with the required table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint for subscribing users to blockchain newsletter updates.
    
    Request JSON format:
    {
        "email": "user@example.com"
    }
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        email = data.get('email')

        # Validate email
        if not email or '@' not in email:
            return jsonify({'error': 'Invalid email address'}), 400
        
        # Insert subscriber into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO subscribers (email)
                VALUES (?)
            ''', (email,))
            conn.commit()
        except sqlite3.IntegrityError:
            # Handle case where email is already subscribed
            return jsonify({'error': 'Email is already subscribed'}), 409
        
        return jsonify({'message': 'Successfully subscribed to the newsletter'}), 201
    except Exception as e:
        # Generic error handling
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    finally:
        conn.close()

@app.route('/subscribers', methods=['GET'])
def get_subscribers():
    """
    Endpoint to retrieve a list of all subscribers.

    Returns:
    - JSON list of subscriber emails.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT email, timestamp FROM subscribers')
        rows = cursor.fetchall()
        subscribers = [{'email': row[0], 'timestamp': row[1]} for row in rows]
        return jsonify(subscribers), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
```
