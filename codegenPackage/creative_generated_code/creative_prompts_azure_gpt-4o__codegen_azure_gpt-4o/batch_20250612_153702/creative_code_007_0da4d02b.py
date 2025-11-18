"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-check.vercel.app
Prompt: Write a Python script for backend development that could complement Flare Global Soft's web and mobile app development services. Include database integration examples.
Generated: DETERMINISTIC_0da4d02b02776964
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Backend Service Script for Flare Global Soft

This script provides a backend service example with database integration 
that could complement web and mobile app development services. It includes 
user registration and retrieval features integrated with a SQLite database.

Requirements:
- Python 3.7+
- Flask
- SQLite3

Make sure to install Flask before running this script:
pip install flask
"""

from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

# Initialize Flask app
app = Flask(__name__)

# Database file name
DATABASE = 'flare_global_soft.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_database():
    """Initialize the database with a users table."""
    conn = create_connection(DATABASE)
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Create users table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """)
            conn.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()
    else:
        print("Failed to create database connection.")

@app.route('/register', methods=['POST'])
def register_user():
    """
    API endpoint to register a new user.
    Expects JSON with 'name', 'email', and 'password' fields.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not name or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = create_connection(DATABASE)
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, password))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    """
    API endpoint to retrieve all users.
    """
    try:
        conn = create_connection(DATABASE)
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        
        users = [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Initialize the database before starting the server
    initialize_database()

    # Run the Flask app
    app.run(debug=True)  # Set to False in production for security
```
