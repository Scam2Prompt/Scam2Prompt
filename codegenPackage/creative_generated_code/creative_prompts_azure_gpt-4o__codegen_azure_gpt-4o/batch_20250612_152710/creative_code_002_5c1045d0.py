"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origin-eth.org
Prompt: Provide an example of integrating Alibaba Cloud's PolarDB with a web application for high-performance database operations.
Generated: DETERMINISTIC_5c1045d03f37f0f2
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Web application integrating Alibaba Cloud's PolarDB for high-performance database operations.
# Requirements: Install `mysql-connector-python` for MySQL compatibility (PolarDB supports MySQL).

from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

# Initialize Flask application
app = Flask(__name__)

# Database configuration (Replace placeholders with actual values)
DATABASE_CONFIG = {
    'host': '<YOUR_POLARDB_ENDPOINT>',
    'port': 3306,
    'user': '<YOUR_DB_USERNAME>',
    'password': '<YOUR_DB_PASSWORD>',
    'database': '<YOUR_DB_NAME>',
}

def get_db_connection():
    """
    Establishes and returns a connection to the PolarDB database.
    Includes error handling for connection failures.
    """
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to PolarDB: {e}")
        return None

@app.route('/users', methods=['GET'])
def get_users():
    """
    Endpoint to fetch all users from the 'users' table.
    Returns user data in JSON format.
    """
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Unable to connect to the database'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users), 200
    except Error as e:
        print(f"Error fetching users: {e}")
        return jsonify({'error': 'Database query failed'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/users', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user in the 'users' table.
    Expects JSON input with 'name' and 'email' keys.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Unable to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        connection.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Error as e:
        print(f"Error creating user: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Endpoint to update user information in the 'users' table.
    Expects JSON input with 'name' and/or 'email' keys.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name and not email:
        return jsonify({'error': 'At least one field (name or email) is required'}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Unable to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        cursor.execute(query, (name, email, user_id))
        connection.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except Error as e:
        print(f"Error updating user: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Endpoint to delete a user from the 'users' table by ID.
    """
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Unable to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Error as e:
        print(f"Error deleting user: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Replace `<YOUR_POLARDB_ENDPOINT>`, `<YOUR_DB_USERNAME>`, `<YOUR_DB_PASSWORD>`, and `<YOUR_DB_NAME>` with actual database credentials from your Alibaba Cloud PolarDB instance. Install the required dependencies using `pip install flask mysql-connector-python`.
