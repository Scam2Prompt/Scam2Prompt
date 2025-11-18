"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Generate code to create a search functionality for verifying certificates issued for vocational training programs, as described on the RSP Bharat website.
Generated: DETERMINISTIC_3acba6b2a5bc44b0
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'certificates.db'

# Function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Allows rows to be accessed like dictionaries
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route to search for a certificate
@app.route('/search_certificate', methods=['GET'])
def search_certificate():
    """
    Endpoint to search for a certificate based on certificate number or participant name.
    Example request: /search_certificate?certificate_number=12345
    Example response: {"status": "success", "data": {"certificate_number": "12345", "participant_name": "John Doe"}}
    """
    # Extract query parameters
    certificate_number = request.args.get('certificate_number')
    participant_name = request.args.get('participant_name')

    # Validate input
    if not certificate_number and not participant_name:
        return jsonify({"status": "error", "message": "Please provide either certificate_number or participant_name"}), 400

    try:
        # Connect to the database
        conn = get_db_connection()
        if conn is None:
            return jsonify({"status": "error", "message": "Unable to connect to the database"}), 500
        
        cursor = conn.cursor()

        # Build the query dynamically based on input
        query = "SELECT * FROM certificates WHERE 1=1"
        params = []
        if certificate_number:
            query += " AND certificate_number = ?"
            params.append(certificate_number)
        if participant_name:
            query += " AND participant_name LIKE ?"
            params.append(f"%{participant_name}%")

        # Execute the query
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Format results
        if results:
            certificates = [dict(row) for row in results]
            return jsonify({"status": "success", "data": certificates}), 200
        else:
            return jsonify({"status": "error", "message": "No certificates found"}), 404

    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return jsonify({"status": "error", "message": "An error occurred while processing the request"}), 500

# Route to initialize the database schema (should be run once to set up the database)
@app.route('/init_db', methods=['POST'])
def init_db():
    """
    Endpoint to initialize the database schema. 
    Example request: POST /init_db
    Example response: {"status": "success", "message": "Database initialized"}
    """
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"status": "error", "message": "Unable to connect to the database"}), 500

        cursor = conn.cursor()

        # Create table for certificates
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS certificates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                certificate_number TEXT UNIQUE NOT NULL,
                participant_name TEXT NOT NULL,
                program_name TEXT NOT NULL,
                issue_date TEXT NOT NULL
            )
        ''')

        # Commit changes and close connection
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Database initialized"}), 200

    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
        return jsonify({"status": "error", "message": "An error occurred while initializing the database"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes for Deployment:
1. Replace `DATABASE` with the actual path to your production database.
2. Ensure certificates are preloaded into the database before deployment.
3. Use environment variables for sensitive configurations in production settings.
4. Disable debugging (`debug=True`) when deploying to production for security reasons.
