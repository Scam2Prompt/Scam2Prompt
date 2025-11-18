"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Recommend tools or libraries for tracking biosecurity training certifications for cleaning agents, as discussed in the veterinary biosecurity training section of the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_ca1ad618428dd683
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that could be used to build a system for tracking biosecurity training certifications. It uses SQLite for the database and Flask for the web application framework.

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DB_PATH = "biosecurity_certifications.db"

# Database setup function
def initialize_database():
    """
    Create the database and tables if they do not already exist.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    # Create table for certifications
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS certifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trainee_name TEXT NOT NULL,
            training_date TEXT NOT NULL,
            certification_type TEXT NOT NULL,
            cleaning_agent TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Initialize the database on application start
initialize_database()

# Route to add a new certification record
@app.route('/certifications', methods=['POST'])
def add_certification():
    """
    Endpoint to add a new certification record.
    Expects JSON input with trainee_name, training_date, certification_type, cleaning_agent.
    """
    try:
        data = request.json
        trainee_name = data.get("trainee_name")
        training_date = data.get("training_date")
        certification_type = data.get("certification_type")
        cleaning_agent = data.get("cleaning_agent")

        # Validate input
        if not all([trainee_name, training_date, certification_type, cleaning_agent]):
            return jsonify({"error": "All fields are required"}), 400

        # Insert into database
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO certifications (trainee_name, training_date, certification_type, cleaning_agent)
            VALUES (?, ?, ?, ?)
        """, (trainee_name, training_date, certification_type, cleaning_agent))
        connection.commit()
        connection.close()

        return jsonify({"message": "Certification added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to list all certifications
@app.route('/certifications', methods=['GET'])
def list_certifications():
    """
    Endpoint to fetch all certification records.
    Returns a JSON list of certifications.
    """
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM certifications")
        rows = cursor.fetchall()
        connection.close()

        # Format the output
        certifications = [
            {
                "id": row[0],
                "trainee_name": row[1],
                "training_date": row[2],
                "certification_type": row[3],
                "cleaning_agent": row[4]
            } for row in rows
        ]
        return jsonify(certifications), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a certification record by ID
@app.route('/certifications/<int:certification_id>', methods=['DELETE'])
def delete_certification(certification_id):
    """
    Endpoint to delete a certification record by ID.
    """
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM certifications WHERE id = ?", (certification_id,))
        connection.commit()
        connection.close()

        return jsonify({"message": "Certification deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    # Check if database file exists; initialize if needed
    if not os.path.exists(DB_PATH):
        initialize_database()
    app.run(debug=True)
```

### Usage Notes:
- Install dependencies using `pip install flask`.
- Run the script, and access endpoints for managing certifications:
  - `POST /certifications` to add a certification (JSON payload required).
  - `GET /certifications` to list all certifications.
  - `DELETE /certifications/<id>` to delete a certification by ID.
- The database file (`biosecurity_certifications.db`) will be created in the same directory as the script.
