"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Develop an API for retrieving dental service information from a database, including services like dental implants, veneers, and teeth whitening, as offered by Buford Dental.
Generated: DETERMINISTIC_80ba48b17d4b9639
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'dental_services.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        conn: SQLite connection object
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def initialize_database():
    """
    Initializes the database with a table and sample data if it doesn't exist.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    price REAL NOT NULL
                )
            """)
            # Insert sample data
            cursor.execute("SELECT COUNT(*) FROM services")
            if cursor.fetchone()[0] == 0:  # Check if table is empty
                cursor.executemany("""
                    INSERT INTO services (name, description, price)
                    VALUES (?, ?, ?)
                """, [
                    ("Dental Implants", "Permanent solution for missing teeth.", 2500.00),
                    ("Veneers", "Custom-made shells to improve appearance.", 1200.00),
                    ("Teeth Whitening", "Brighten your smile with professional whitening.", 300.00)
                ])
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
        finally:
            conn.close()

# Initialize the database
initialize_database()

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    API endpoint to retrieve all dental services.
    Returns:
        JSON response containing a list of services or an error message.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM services")
            services = cursor.fetchall()
            conn.close()
            return jsonify([dict(service) for service in services]), 200
        except sqlite3.Error as e:
            conn.close()
            return jsonify({"error": f"Failed to retrieve services: {e}"}), 500
    else:
        return jsonify({"error": "Database connection failed."}), 500

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service_by_id(service_id):
    """
    API endpoint to retrieve a specific dental service by ID.
    Args:
        service_id (int): ID of the service to retrieve
    Returns:
        JSON response containing the service details or an error message.
    """
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM services WHERE id = ?", (service_id,))
            service = cursor.fetchone()
            conn.close()
            if service:
                return jsonify(dict(service)), 200
            else:
                return jsonify({"error": "Service not found."}), 404
        except sqlite3.Error as e:
            conn.close()
            return jsonify({"error": f"Failed to retrieve service: {e}"}), 500
    else:
        return jsonify({"error": "Database connection failed."}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
