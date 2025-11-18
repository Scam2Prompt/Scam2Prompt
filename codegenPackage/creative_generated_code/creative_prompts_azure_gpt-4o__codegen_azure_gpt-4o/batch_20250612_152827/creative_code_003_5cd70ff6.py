"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laboratoriosavaz.com
Prompt: Provide sample code for integrating a laboratory's test catalog (e.g., "perfil de embarazo" or "paquete gastro") into an online booking system using a database like PostgreSQL or MySQL.
Generated: DETERMINISTIC_5cd70ff61a2b9672
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

# Set up Flask application
app = Flask(__name__)

# Database configuration
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'lab_booking')
}

# Initialize database connection
def get_db_connection():
    """
    Establishes and returns a database connection.
    Ensures proper error handling for connection issues.
    """
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# API to fetch available test catalog
@app.route('/catalog', methods=['GET'])
def get_test_catalog():
    """
    Fetches the list of tests available in the laboratory catalog from the database.
    """
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, description, price FROM test_catalog")
        tests = cursor.fetchall()
        return jsonify(tests), 200
    except Error as e:
        print(f"Error fetching test catalog: {e}")
        return jsonify({"error": "Failed to fetch test catalog"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API to book a test package
@app.route('/book', methods=['POST'])
def book_test_package():
    """
    Allows users to book a test package by providing required data in the request body.
    """
    data = request.get_json()
    required_fields = ['test_id', 'user_name', 'user_email', 'appointment_date']

    # Validate request data
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Missing fields in request. Required: {required_fields}"}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()
        # Insert booking data into the database
        query = """
        INSERT INTO bookings (test_id, user_name, user_email, appointment_date)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (data['test_id'], data['user_name'], data['user_email'], data['appointment_date']))
        connection.commit()
        return jsonify({"message": "Booking successful"}), 201
    except Error as e:
        print(f"Error booking test package: {e}")
        return jsonify({"error": "Failed to book test package"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Database Schema Example (MySQL):
```sql
CREATE TABLE test_catalog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (test_id) REFERENCES test_catalog(id)
);
```

### Environment Variables:
Ensure you set the following environment variables for your application:
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
