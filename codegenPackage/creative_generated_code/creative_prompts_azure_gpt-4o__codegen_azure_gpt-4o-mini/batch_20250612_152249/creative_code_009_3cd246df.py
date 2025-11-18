"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Create a script to integrate the "Patente d'Impresa" registration form with a database, ensuring secure storage of participant information like name, email, and phone number.
Generated: DETERMINISTIC_3cd246dfb756eccc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import re

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'business_registration.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create the participants table if it does not exist."""
    try:
        sql_create_participants_table = """
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_participants_table)
    except Error as e:
        print(e)

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new participant."""
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    # Input validation
    if not all([name, email, phone, password]):
        return jsonify({"error": "All fields are required."}), 400
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email address."}), 400

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)

    # Insert participant into the database
    conn = create_connection(DATABASE)
    if conn:
        try:
            sql_insert_participant = """
            INSERT INTO participants (name, email, phone, password)
            VALUES (?, ?, ?, ?);"""
            cursor = conn.cursor()
            cursor.execute(sql_insert_participant, (name, email, phone, hashed_password))
            conn.commit()
            return jsonify({"message": "Registration successful."}), 201
        except sqlite3.IntegrityError:
            return jsonify({"error": "Email already registered."}), 409
        except Error as e:
            print(e)
            return jsonify({"error": "Database error occurred."}), 500
        finally:
            conn.close()
    return jsonify({"error": "Failed to connect to the database."}), 500

if __name__ == '__main__':
    # Create the database connection and table on startup
    conn = create_connection(DATABASE)
    create_table(conn)
    if conn:
        conn.close()
    # Run the Flask application
    app.run(debug=False)
```
