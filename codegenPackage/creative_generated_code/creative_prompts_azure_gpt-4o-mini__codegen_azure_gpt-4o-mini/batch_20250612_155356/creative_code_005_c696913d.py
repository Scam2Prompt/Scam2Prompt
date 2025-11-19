"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stcinversiones.com.ar
Prompt: Provide an example of how to implement a user account creation feature for an investment platform, inspired by the services of STC Inversiones.
Generated: DETERMINISTIC_c696913da792c7ad
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
DATABASE = 'users.db'

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating connection: {e}")
    return conn

def create_table(conn):
    """ Create a table for storing user accounts. """
    try:
        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        username TEXT NOT NULL UNIQUE,
                                        password TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE
                                    ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_users_table)
    except Error as e:
        print(f"Error creating table: {e}")

def hash_password(password):
    """ Hash a password for storing. """
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/create_account', methods=['POST'])
def create_account():
    """ Endpoint for creating a new user account. """
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"error": "Username, password, and email are required."}), 400

    # Hash the password
    hashed_password = hash_password(password)

    conn = create_connection(DATABASE)
    if conn is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                       (username, hashed_password, email))
        conn.commit()
        return jsonify({"message": "Account created successfully."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username or email already exists."}), 409
    except Error as e:
        return jsonify({"error": f"Failed to create account: {e}"}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn)
        conn.close()
    app.run(debug=False)
```
