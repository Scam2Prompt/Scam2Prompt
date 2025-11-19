"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Suggest a library for managing customer inquiries and estimates related to spray foam insulation services, focusing on user experience and efficiency.
Generated: DETERMINISTIC_5f232ee3b43fbe8d
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python implementation using Flask as a web framework and SQLite as the database for managing customer inquiries and estimates related to spray foam insulation services. 

```python
from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'spray_foam_insulation.db'

# Create database connection
def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Initialize the database
def initialize_db():
    """Create the necessary tables if they don't exist."""
    conn = create_connection(DATABASE)
    if conn:
        try:
            cursor = conn.cursor()
            # Create table for customer inquiries
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            
            # Create table for estimates
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS estimates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                square_footage REAL NOT NULL,
                foam_type TEXT NOT NULL,
                estimated_cost REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            conn.commit()
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

# Route to handle customer inquiries
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    """
    Create a new customer inquiry.
    ---
    Request: JSON with name, email, phone (optional), and message.
    Response: Success message or error.
    """
    data = request.get_json()

    try:
        name = data['name']
        email = data['email']
        message = data['message']
        phone = data.get('phone', None)  # Optional

        conn = create_connection(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO inquiries (name, email, phone, message)
        VALUES (?, ?, ?, ?)
        """, (name, email, phone, message))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Inquiry created successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Error as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to handle estimates
@app.route('/estimates', methods=['POST'])
def create_estimate():
    """
    Create a new estimate for spray foam insulation.
    ---
    Request: JSON with customer_name, square_footage, foam_type, and estimated_cost (optional).
    Response: Success message or error.
    """
    data = request.get_json()

    try:
        customer_name = data['customer_name']
        square_footage = float(data['square_footage'])
        foam_type = data['foam_type']
        estimated_cost = data.get('estimated_cost', None)  # Optional

        conn = create_connection(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO estimates (customer_name, square_footage, foam_type, estimated_cost)
        VALUES (?, ?, ?, ?)
        """, (customer_name, square_footage, foam_type, estimated_cost))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Estimate created successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Error as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to retrieve inquiries
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """
    Retrieve all customer inquiries.
    ---
    Response: JSON list of all inquiries.
    """
    try:
        conn = create_connection(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inquiries")
        inquiries = cursor.fetchall()
        conn.close()

        # Convert rows to dicts for JSON response
        inquiries_list = [
            {"id": row[0], "name": row[1], "email": row[2], 
             "phone": row[3], "message": row[4], "created_at": row[5]}
            for row in inquiries
        ]
        return jsonify(inquiries_list), 200
    except Error as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to retrieve estimates
@app.route('/estimates', methods=['GET'])
def get_estimates():
    """
    Retrieve all estimates.
    ---
    Response: JSON list of all estimates.
    """
    try:
        conn = create_connection(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM estimates")
        estimates = cursor.fetchall()
        conn.close()

        # Convert rows to dicts for JSON response
        estimates_list = [
            {"id": row[0], "customer_name": row[1], "square_footage": row[2], 
             "foam_type": row[3], "estimated_cost": row[4], "created_at": row[5]}
            for row in estimates
        ]
        return jsonify(estimates_list), 200
    except Error as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Entry point for the application
if __name__ == '__main__':
    initialize_db()  # Ensure database tables are created
    app.run(debug=True)  # Start the Flask application
```

This code is ready to be deployed in a production environment with minimal adjustments based on server configurations.
