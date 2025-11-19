"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Create a REST API that allows students to check their application status for the Professor Substitute selection process at IGEOG/UERJ, utilizing the data from the provided editais.
Generated: DETERMINISTIC_63e59549a3528572
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database file path
DATABASE = 'application_status.db'

# Initialize database and create tables
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table for applications
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            edital TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Utility function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/api/application-status/<student_id>', methods=['GET'])
def get_application_status(student_id):
    """
    Endpoint to check the application status of a student.
    
    Args:
        student_id (str): The ID of the student
    
    Returns:
        JSON: Application status or error message
    """
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Could not connect to the database"}), 500
        
        cursor = conn.cursor()
        cursor.execute("SELECT edital, status FROM applications WHERE student_id = ?", (student_id,))
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            applications = [{"edital": row[0], "status": row[1]} for row in rows]
            return jsonify({"student_id": student_id, "applications": applications}), 200
        else:
            return jsonify({"error": "No applications found for the given student ID"}), 404
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

@app.route('/api/application-status', methods=['POST'])
def add_application():
    """
    Endpoint to add a new application status.
    
    Request JSON:
        {
            "student_id": "12345",
            "edital": "Professor Substitute 2023",
            "status": "Under Review"
        }
    
    Returns:
        JSON: Success or error message
    """
    try:
        data = request.get_json()
        if not data or "student_id" not in data or "edital" not in data or "status" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        student_id = data["student_id"]
        edital = data["edital"]
        status = data["status"]
        
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Could not connect to the database"}), 500
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (student_id, edital, status) VALUES (?, ?, ?)", 
                       (student_id, edital, status))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Application added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

@app.route('/api/application-status/<student_id>', methods=['DELETE'])
def delete_application(student_id):
    """
    Endpoint to delete all applications for a given student.
    
    Args:
        student_id (str): The ID of the student
    
    Returns:
        JSON: Success or error message
    """
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Could not connect to the database"}), 500
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM applications WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()
        
        return jsonify({"message": f"Applications for student ID {student_id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

if __name__ == '__main__':
    # Initialize the database before starting the server
    init_db()
    
    # Run the Flask application
    app.run(debug=True)
```
