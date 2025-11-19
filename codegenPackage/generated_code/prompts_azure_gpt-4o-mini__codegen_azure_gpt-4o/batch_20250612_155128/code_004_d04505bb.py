"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Describe how to create a software solution for out-growers consultancy that facilitates communication between producers and off-takers, based on Olgon's approach.
Generated: DETERMINISTIC_d04505bb4f250811
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Out-Growers Consultancy Software Solution
This Python-based solution facilitates communication between producers (farmers) and off-takers (buyers) 
based on Olgon's approach. It includes features for user registration, messaging, and viewing producer/off-taker profiles.

Dependencies:
- Flask: Web framework for building the application
- SQLite: Lightweight database for storing user and message data
"""

from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file path
DATABASE = 'outgrowers.db'

# Ensure database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('producer', 'off-taker')),
            contact TEXT NOT NULL
        )
    """)
    # Create messages table
    cursor.execute("""
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(sender_id) REFERENCES users(id),
            FOREIGN KEY(receiver_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    return sqlite3.connect(DATABASE)

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Request JSON format:
    {
        "name": "John Doe",
        "role": "producer",
        "contact": "john@example.com"
    }
    """
    try:
        data = request.json
        name = data.get('name')
        role = data.get('role')
        contact = data.get('contact')

        if not name or not role or not contact:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, role, contact) VALUES (?, ?, ?)", (name, role, contact))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Send a message
@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Endpoint to send a message from one user to another.
    Request JSON format:
    {
        "sender_id": 1,
        "receiver_id": 2,
        "message": "Hello, I am interested in your produce."
    }
    """
    try:
        data = request.json
        sender_id = data.get('sender_id')
        receiver_id = data.get('receiver_id')
        message = data.get('message')

        if not sender_id or not receiver_id or not message:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)",
                       (sender_id, receiver_id, message))
        conn.commit()
        conn.close()

        return jsonify({"message": "Message sent successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View user profiles
@app.route('/users', methods=['GET'])
def view_users():
    """
    Endpoint to view all registered users.
    Response JSON format:
    [
        {
            "id": 1,
            "name": "John Doe",
            "role": "producer",
            "contact": "john@example.com"
        },
        ...
    ]
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, role, contact FROM users")
        users = cursor.fetchall()
        conn.close()

        user_list = [{"id": user[0], "name": user[1], "role": user[2], "contact": user[3]} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: View messages between users
@app.route('/messages', methods=['GET'])
def view_messages():
    """
    Endpoint to view all messages between users.
    Response JSON format:
    [
        {
            "id": 1,
            "sender_id": 1,
            "receiver_id": 2,
            "message": "Hello, I am interested in your produce.",
            "timestamp": "2023-01-01 12:00:00"
        },
        ...
    ]
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, sender_id, receiver_id, message, timestamp FROM messages")
        messages = cursor.fetchall()
        conn.close()

        message_list = [{"id": msg[0], "sender_id": msg[1], "receiver_id": msg[2], "message": msg[3], "timestamp": msg[4]} for msg in messages]
        return jsonify(message_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
