"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-illuminex.com
Prompt: Write a code snippet to create a digital solution that fosters collaboration between universities and industries, inspired by KAMISLOT's initiatives.
Generated: DETERMINISTIC_cee16d24283b8483
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# Database setup: Create a SQLite database to store collaborations
DATABASE = 'collaboration.db'

def initialize_database():
    """Initialize the database and create required tables."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS collaborations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        university TEXT NOT NULL,
        industry TEXT NOT NULL,
        project_description TEXT NOT NULL,
        contact_email TEXT NOT NULL
    )""")
    connection.commit()
    connection.close()

# Initialize database
initialize_database()

@app.route('/create_collaboration', methods=['POST'])
def create_collaboration():
    """
    Endpoint to create a new collaboration entry.
    Expected JSON body:
    {
        "university": "University Name",
        "industry": "Industry Name",
        "project_description": "Description of the project",
        "contact_email": "Contact email for the collaboration"
    }
    """
    try:
        data = request.json
        university = data.get('university')
        industry = data.get('industry')
        project_description = data.get('project_description')
        contact_email = data.get('contact_email')

        # Input validation
        if not all([university, industry, project_description, contact_email]):
            return jsonify({"error": "All fields are required"}), 400

        # Insert collaboration data into the database
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO collaborations (university, industry, project_description, contact_email)
        VALUES (?, ?, ?, ?)
        """, (university, industry, project_description, contact_email))
        connection.commit()
        connection.close()

        return jsonify({"message": "Collaboration created successfully"}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/get_collaborations', methods=['GET'])
def get_collaborations():
    """
    Endpoint to fetch all collaboration entries.
    """
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM collaborations")
        rows = cursor.fetchall()
        connection.close()

        # Convert rows to list of dictionaries for JSON response
        collaborations = [
            {"id": row[0], "university": row[1], "industry": row[2], "project_description": row[3], "contact_email": row[4]}
            for row in rows
        ]

        return jsonify(collaborations), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
