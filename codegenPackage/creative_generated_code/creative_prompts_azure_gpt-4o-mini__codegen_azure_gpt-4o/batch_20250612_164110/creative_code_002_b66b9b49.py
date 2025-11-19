"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: What are the best practices for integrating a rewards system in a mobile app to enhance user engagement, based on the Cosmic Rewards model?
Generated: DETERMINISTIC_b66b9b49423086c7
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready code example for integrating a rewards system in a mobile app based on a simplified Cosmic Rewards model. The code is written in Python (backend implementation). It assumes you have a mobile app frontend that communicates with this backend via API endpoints.

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Initialize database connection
DB_PATH = 'rewards_system.db'

# Setup the SQLite database
def initialize_database():
    """Create tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rewards (
            reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            points INTEGER DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reward_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            points INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to connect to database
def db_connection():
    """Returns a database connection object."""
    return sqlite3.connect(DB_PATH)

# Create user endpoint
@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with a rewards account.
    Example payload:
    {
        "username": "john_doe"
    }
    """
    try:
        data = request.json
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username is required"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid
        cursor.execute("INSERT INTO rewards (user_id, points) VALUES (?, ?)", (user_id, 0))
        conn.commit()
        conn.close()
        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Earn rewards endpoint
@app.route('/earn', methods=['POST'])
def earn_rewards():
    """
    Add points to the user's rewards balance.
    Example payload:
    {
        "user_id": 1,
        "points": 50
    }
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        points = data.get('points')

        if not user_id or not points:
            return jsonify({"error": "user_id and points are required"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rewards WHERE user_id = ?", (user_id,))
        reward = cursor.fetchone()

        if not reward:
            return jsonify({"error": "User not found"}), 404

        # Update rewards balance
        new_points = reward[2] + points
        cursor.execute("UPDATE rewards SET points = ?, last_updated = ? WHERE user_id = ?", 
                       (new_points, datetime.now(), user_id))
        # Log the transaction in reward history
        cursor.execute("INSERT INTO reward_history (user_id, type, points) VALUES (?, ?, ?)", 
                       (user_id, 'Earn', points))
        conn.commit()
        conn.close()
        return jsonify({"message": "Rewards updated successfully", "new_balance": new_points}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Redeem rewards endpoint
@app.route('/redeem', methods=['POST'])
def redeem_rewards():
    """
    Redeem points from the user's rewards balance.
    Example payload:
    {
        "user_id": 1,
        "points": 30
    }
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        points = data.get('points')

        if not user_id or not points:
            return jsonify({"error": "user_id and points are required"}), 400

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rewards WHERE user_id = ?", (user_id,))
        reward = cursor.fetchone()

        if not reward:
            return jsonify({"error": "User not found"}), 404

        current_points = reward[2]
        if points > current_points:
            return jsonify({"error": "Insufficient points to redeem"}), 400

        # Update rewards balance
        new_points = current_points - points
        cursor.execute("UPDATE rewards SET points = ?, last_updated = ? WHERE user_id = ?", 
                       (new_points, datetime.now(), user_id))
        # Log the transaction in reward history
        cursor.execute("INSERT INTO reward_history (user_id, type, points) VALUES (?, ?, ?)", 
                       (user_id, 'Redeem', points))
        conn.commit()
        conn.close()
        return jsonify({"message": "Rewards redeemed successfully", "new_balance": new_points}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get rewards balance endpoint
@app.route('/balance/<int:user_id>', methods=['GET'])
def get_rewards_balance(user_id):
    """
    Get the user's current rewards balance.
    Example URL: /balance/1
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rewards WHERE user_id = ?", (user_id,))
        reward = cursor.fetchone()
        conn.close()

        if not reward:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user_id": user_id, "points": reward[2]}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# View reward history endpoint
@app.route('/history/<int:user_id>', methods=['GET'])
def view_reward_history(user_id):
    """
    View the user's reward transaction history.
    Example URL: /history/1
    """
    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reward_history WHERE user_id = ?", (user_id,))
        history = cursor.fetchall()
        conn.close()

        if not history:
            return jsonify({"error": "No reward history found for the user"}), 404

        history_list = [
            {"type": record[2], "points": record[3], "timestamp": record[4]}
            for record in history
        ]
        return jsonify({"user_id": user_id, "history": history_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    initialize_database()  # Initialize the database
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `sqlite3` with a production-grade database (e.g., PostgreSQL) for scalability.
- Secure sensitive user inputs and implement authentication mechanisms.
- Host the app using reliable platforms like AWS, Azure, or Google Cloud for production deployment.
