"""
Generated Code Metadata:
========================
Original URL: https://gam3searly.pages.dev
Prompt: Recommend APIs or libraries for implementing a leaderboard system like the one on GAM3S.GG, where users can earn XP and track rankings.
Generated: DETERMINISTIC_c981a632cc8692ed
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database setup
DATABASE = 'leaderboard.db'

def init_db():
    """Initialize the database with the required tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                xp INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaderboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                rank INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the leaderboard."""
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
            conn.commit()
            return jsonify({'message': 'User added successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 409

@app.route('/add_xp', methods=['POST'])
def add_xp():
    """Add XP to a user and update their rank."""
    username = request.json.get('username')
    xp_to_add = request.json.get('xp')

    if not username or xp_to_add is None:
        return jsonify({'error': 'Username and XP are required'}), 400

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET xp = xp + ? WHERE username = ?', (xp_to_add, username))
            conn.commit()

            # Update leaderboard
            cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
            user_id = cursor.fetchone()
            if user_id:
                user_id = user_id[0]
                cursor.execute('SELECT COUNT(*) FROM users WHERE xp > (SELECT xp FROM users WHERE id = ?)', (user_id,))
                rank = cursor.fetchone()[0] + 1  # Rank is 1-based
                cursor.execute('INSERT OR REPLACE INTO leaderboard (user_id, rank) VALUES (?, ?)', (user_id, rank))
                conn.commit()

            return jsonify({'message': 'XP added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Retrieve the leaderboard sorted by XP."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT u.username, u.xp, l.rank
                FROM users u
                JOIN leaderboard l ON u.id = l.user_id
                ORDER BY u.xp DESC
            ''')
            leaderboard = cursor.fetchall()
            return jsonify(leaderboard), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```

### Requirements
To run this code, you will need:
- Python 3.x
- Flask library (install via `pip install Flask`)

### Usage
1. Start the Flask application by running `python leaderboard.py`.
2. Use a tool like Postman or curl to interact with the API:
   - Add a user: `POST /add_user` with JSON body `{"username": "example_user"}`
   - Add XP: `POST /add_xp` with JSON body `{"username": "example_user", "xp": 100}`
   - Get leaderboard: `GET /leaderboard`
