"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-8sr.pages.dev
Prompt: Develop a leaderboard system with social interactions and a rewarding point system, inspired by Blum's gamified crypto trading experience.
Generated: DETERMINISTIC_90b1262a9ce5c5bc
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Leaderboard System with Social Interactions and Reward Points
# Language: Python
# Dependencies: Flask (Web Framework), SQLite (Database)

from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

# Database initialization
DATABASE = 'leaderboard.db'


def init_db():
    """
    Initialize the database with required tables.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        points INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER NOT NULL,
        receiver_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        points INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(sender_id) REFERENCES users(id),
        FOREIGN KEY(receiver_id) REFERENCES users(id)
    )
    """)
    connection.commit()
    connection.close()


# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DATABASE)


# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expected JSON payload: { "username": "desired_username" }
    """
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        connection.commit()
        connection.close()
        return jsonify({"message": f"User '{username}' registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400


@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """
    Endpoint to fetch the leaderboard. Returns top users sorted by points.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT username, points FROM users ORDER BY points DESC")
    users = cursor.fetchall()
    connection.close()

    leaderboard = [{"username": user[0], "points": user[1]} for user in users]
    return jsonify(leaderboard), 200


@app.route('/interact', methods=['POST'])
def social_interaction():
    """
    Endpoint to record a social interaction and award points.
    Expected JSON payload:
    {
        "sender_username": "your_username",
        "receiver_username": "other_username",
        "interaction_type": "like|comment|share"
    }
    """
    data = request.json
    sender_username = data.get('sender_username')
    receiver_username = data.get('receiver_username')
    interaction_type = data.get('interaction_type')

    if not sender_username or not receiver_username or not interaction_type:
        return jsonify({"error": "All fields are required"}), 400

    points_map = {"like": 10, "comment": 20, "share": 30}
    points = points_map.get(interaction_type)

    if not points:
        return jsonify({"error": "Invalid interaction type"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch sender and receiver IDs
        cursor.execute("SELECT id FROM users WHERE username = ?", (sender_username,))
        sender = cursor.fetchone()
        cursor.execute("SELECT id FROM users WHERE username = ?", (receiver_username,))
        receiver = cursor.fetchone()

        if not sender or not receiver:
            return jsonify({"error": "Invalid sender or receiver username"}), 404

        sender_id = sender[0]
        receiver_id = receiver[0]

        # Record the interaction
        cursor.execute("""
        INSERT INTO interactions (sender_id, receiver_id, type, points)
        VALUES (?, ?, ?, ?)
        """, (sender_id, receiver_id, interaction_type, points))

        # Update points for the receiver
        cursor.execute("""
        UPDATE users
        SET points = points + ?
        WHERE id = ?
        """, (points, receiver_id))

        connection.commit()
        return jsonify({"message": f"{interaction_type.capitalize()} interaction recorded and {points} points awarded."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        connection.close()


@app.route('/user/<username>', methods=['GET'])
def get_user_profile(username):
    """
    Endpoint to fetch a user's profile and their interaction history.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch user information
        cursor.execute("SELECT id, username, points FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404

        user_id = user[0]

        # Fetch interaction history
        cursor.execute("""
        SELECT type, points, timestamp
        FROM interactions
        WHERE sender_id = ? OR receiver_id = ?
        ORDER BY timestamp DESC
        """, (user_id, user_id))
        interactions = cursor.fetchall()

        interaction_history = [
            {"type": interaction[0], "points": interaction[1], "timestamp": interaction[2]}
            for interaction in interactions
        ]

        user_profile = {
            "username": user[1],
            "points": user[2],
            "interactions": interaction_history
        }

        return jsonify(user_profile), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        connection.close()


# Application startup
if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5000)
```
