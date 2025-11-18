"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Recommend tools or frameworks for building a mobile-friendly betting platform with features like account management, live betting, and bonus tracking, as described on the Parimatch website.
Generated: DETERMINISTIC_651e887bb129389d
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Python-based backend using the Flask framework for building a mobile-friendly betting platform. This code provides a starting point for features like account management, live betting, and bonus tracking. It uses SQLite as the database for simplicity.

```python
# File: betting_platform.py

from flask import Flask, jsonify, request
import sqlite3
import datetime

app = Flask(__name__)
DATABASE = 'betting_platform.db'


# Helper function to connect to the database
def db_connect():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# Initialize the database
def init_db():
    """Create necessary tables for the betting platform."""
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            event TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bonuses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            bonus_amount REAL NOT NULL,
            expiry_date DATE NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """Authenticate and log in a user."""
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/place_bet', methods=['POST'])
def place_bet():
    """Place a new bet on a live event."""
    try:
        data = request.get_json()
        user_id = data['user_id']
        event = data['event']
        amount = data['amount']
        
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        if user['balance'] < amount:
            return jsonify({'error': 'Insufficient balance'}), 400
        
        cursor.execute("INSERT INTO bets (user_id, event, amount) VALUES (?, ?, ?)", (user_id, event, amount))
        cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, user_id))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Bet placed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/track_bonus', methods=['GET'])
def track_bonus():
    """Retrieve active bonuses for a user."""
    try:
        user_id = request.args.get('user_id')
        
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bonuses WHERE user_id = ? AND expiry_date >= ?", (user_id, datetime.date.today()))
        bonuses = cursor.fetchall()
        conn.close()
        
        return jsonify({'bonuses': [dict(bonus) for bonus in bonuses]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Initialize the database before starting the app
    init_db()
    app.run(debug=True)
```

### Setup Instructions
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python betting_platform.py
   ```
3. Use a tool like Postman to test the endpoints.

### Notes
- Replace SQLite with a more robust database like PostgreSQL or MySQL for production.
- Add token-based authentication for secure user management (e.g., JWT).
- Integrate real-time features using a library like `Flask-SocketIO` for live betting updates.
