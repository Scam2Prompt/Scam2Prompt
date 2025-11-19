"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: How can I develop a watch-and-earn feature for a socialfi platform that encourages environmental conservation, inspired by Everyworld?
Generated: DETERMINISTIC_9e2edcc768280e4b
Batch ID: 20250612_142517
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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database setup function
def init_db():
    conn = sqlite3.connect('watch_and_earn.db')
    c = conn.cursor()
    # Create users and activities tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    balance REAL DEFAULT 0.0)''')

    c.execute('''CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    activity TEXT NOT NULL,
                    points INTEGER NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    username = request.json.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    conn = sqlite3.connect('watch_and_earn.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    finally:
        conn.close()

# Log activity endpoint
@app.route('/log_activity', methods=['POST'])
def log_activity():
    user_id = request.json.get('user_id')
    activity = request.json.get('activity')
    points = request.json.get('points')

    if not user_id or not activity or points is None:
        return jsonify({"error": "User ID, activity, and points are required"}), 400

    conn = sqlite3.connect('watch_and_earn.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO activities (user_id, activity, points) VALUES (?, ?, ?)', (user_id, activity, points))
        # Update user balance
        c.execute('UPDATE users SET balance = balance + ? WHERE id = ?', (points, user_id))
        conn.commit()
        return jsonify({"message": "Activity logged successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Get user balance endpoint
@app.route('/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    conn = sqlite3.connect('watch_and_earn.db')
    c = conn.cursor()
    try:
        c.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
        balance = c.fetchone()
        if balance is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"balance": balance[0]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Main function to run the Flask application
if __name__ == '__main__':
    app.run(debug=False)
```
