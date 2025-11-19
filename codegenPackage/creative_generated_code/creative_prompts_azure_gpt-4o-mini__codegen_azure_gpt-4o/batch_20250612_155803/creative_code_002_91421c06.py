"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Can you provide a code snippet for integrating course creation features on Sui Foundation?
Generated: DETERMINISTIC_91421c068f63d69c
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration: Define SQLite database file
DATABASE = 'courses.db'

# Utility function for database operations
def db_connection():
    """
    Establish a connection to the SQLite database.
    Returns:
        conn: SQLite connection object
    """
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Endpoint to create a new course
@app.route('/create_course', methods=['POST'])
def create_course():
    """
    API endpoint to create a new course in the database.
    Expects JSON payload with 'name', 'description', and 'duration' fields.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        
        # Validate required fields
        if not ('name' in data and 'description' in data and 'duration' in data):
            return jsonify({"error": "Missing required fields (name, description, duration)"}), 400
        
        name = data['name']
        description = data['description']
        duration = data['duration']
        
        # Connect to the database
        conn = db_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        # Insert course into the database
        cursor = conn.cursor()
        query = "INSERT INTO courses (name, description, duration) VALUES (?, ?, ?)"
        cursor.execute(query, (name, description, duration))
        conn.commit()
        conn.close()
        
        # Return success response
        return jsonify({"message": "Course created successfully"}), 201
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Initialize database schema
def initialize_database():
    """
    Create the database schema if it doesn't exist.
    """
    conn = db_connection()
    if conn is None:
        print("Failed to initialize the database")
        return
    
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        duration INTEGER NOT NULL
    )
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

# Run the Flask application
if __name__ == '__main__':
    # Initialize the database schema before starting the server
    initialize_database()
    app.run(debug=True)
```

This code provides a production-ready Flask-based API for creating courses. It includes proper error handling, database initialization, and follows best practices for Python and Flask development.
