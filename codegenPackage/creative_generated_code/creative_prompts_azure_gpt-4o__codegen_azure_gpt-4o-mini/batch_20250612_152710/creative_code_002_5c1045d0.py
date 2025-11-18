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
import os
import pymysql
from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv('POLARDB_HOST', 'your_polardb_host')
DB_USER = os.getenv('POLARDB_USER', 'your_username')
DB_PASSWORD = os.getenv('POLARDB_PASSWORD', 'your_password')
DB_NAME = os.getenv('POLARDB_DB', 'your_database')

# Function to create a database connection
def create_connection():
    """Create and return a database connection."""
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users from the database."""
    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM users"
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return jsonify(result), 200
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user in the database."""
    user_data = request.json

    if not user_data or not all(key in user_data for key in ('name', 'email')):
        return jsonify({"error": "Invalid input data."}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed."}), 500

    try:
        with connection.cursor() as cursor:
            sql_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(sql_query, (user_data['name'], user_data['email']))
            connection.commit()
            return jsonify({"message": "User created successfully."}), 201
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

Make sure to set the environment variables `POLARDB_HOST`, `POLARDB_USER`, `POLARDB_PASSWORD`, and `POLARDB_DB` with the appropriate values before running the application.
